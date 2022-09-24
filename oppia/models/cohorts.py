
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from oppia.models import Course, Award


class Cohort(models.Model):
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    criteria_based = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
        verbose_name = _('Cohort')
        verbose_name_plural = _('Cohorts')

    def __str__(self):
        return self.description

    def no_student_members(self):
        return Participant.objects.filter(cohort=self, role=Participant.STUDENT).count()

    def no_teacher_members(self):
        return Participant.objects.filter(cohort=self, role=Participant.TEACHER).count()

    def get_courses(self):
        courses = Course.objects.filter(coursecohort__cohort=self).order_by('title')
        return courses

    def get_leaderboard(self, count=0):
        users = User.objects \
            .filter(participant__cohort=self,
                    participant__role=Participant.STUDENT,
                    points__course__coursecohort__cohort=self) \
            .annotate(total=Sum('points__points')) \
            .order_by('-total')

        if count != 0:
            users = users[:count]

        for u in users:
            u.badges = Award.objects \
                .filter(user=u,
                        awardcourse__course__coursecohort__cohort=self) \
                .count()
            if u.total is None:
                u.total = 0
        return users

    # Update cohort participants based on the cohort criteria
    def update_participants(self):
        students = 0
        teachers = 0

        if self.criteria_based:
            if CohortCritera.objects.filter(cohort=self, role=Participant.STUDENT).count() > 0:
                students = self.update_participants_by_role(Participant.STUDENT)
            if CohortCritera.objects.filter(cohort=self, role=Participant.TEACHER).count() > 0:
                teachers = self.update_participants_by_role(Participant.TEACHER)
        return students, teachers

    def refresh_participants(self):
        students = 0
        teachers = 0
        if self.criteria_based:
            # We only refresh a role if it has at least one filtering criteria
            if CohortCritera.objects.filter(cohort=self, role=Participant.STUDENT).count() > 0:
                Participant.objects.filter(cohort=self, role=Participant.STUDENT).delete()
                students = self.update_participants_by_role(Participant.STUDENT)

            if CohortCritera.objects.filter(cohort=self, role=Participant.TEACHER).count() > 0:
                Participant.objects.filter(cohort=self, role=Participant.TEACHER).delete()
                teachers = self.update_participants_by_role(Participant.TEACHER)

        return students, teachers

    def update_participants_by_role(self, role):
        # Imported locally to avoid circular imports
        from profile.models import CustomField
        from profile.utils import get_customfields_filter

        role_criteria = CohortCritera.objects.filter(cohort=self, role=role)

        participants = []
        # as Django's filter() function is accumulative, we can concatenate them as an AND expression
        for criteria in role_criteria:
            customfield = CustomField.objects.filter(id=criteria.user_profile_field).first()
            if not customfield:
                continue
            value = criteria.user_profile_value
            participants = (participants if participants else User.objects).filter(get_customfields_filter(value, customfield))

        for participant in participants:
            if not Participant.objects.filter(cohort=self, user=participant, role=role).exists():
                Participant.objects.create(cohort=self, user=participant, role=role)

        return len(participants)


class CourseCohort(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("course", "cohort")


class Participant(models.Model):
    TEACHER = 'teacher'
    STUDENT = 'student'
    ROLE_TYPES = (
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    )
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_TYPES)

    class Meta:
        verbose_name = _('Participant')
        verbose_name_plural = _('Participants')

    # Return a list of cohorts a user belongs to (either as student or teacher)
    @staticmethod
    def get_user_cohorts(user):
        return list(set(Participant.objects.filter(user=user).values_list('cohort', flat=True)))

class CohortCritera(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Participant.ROLE_TYPES, default=Participant.STUDENT)
    user_profile_field = models.CharField(max_length=150, blank=False, null=False)
    user_profile_value = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = _('Cohort criteria')
