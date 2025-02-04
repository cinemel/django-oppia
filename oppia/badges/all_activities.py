import datetime

from django.contrib.auth.models import User
from django.utils import timezone

from oppia.badges.base_badge import BaseBadge
from oppia.models import Tracker, Activity


class BadgeAllActivities(BaseBadge):

    def process(self, course, badge, hours):
        digests = Activity.objects.filter(section__course=course) \
                          .values_list('digest',
                                       flat=True).distinct()
        digests = list(digests)
        total_activities = len(digests)

        # get all the users who've added tracker for this course in last
        # 'hours'
        if hours == 0:
            users = User.objects.filter(tracker__course=course)
        else:
            since = timezone.now() - datetime.timedelta(hours=int(hours))
            users = User.objects.filter(tracker__course=course,
                                        tracker__submitted_date__gte=since)

        # exclude the users that already own this course award
        users = users.exclude(award__awardcourse__course=course).distinct()

        for user in users:
            user_completed = Tracker.objects.filter(user=user,
                                                    course=course,
                                                    completed=True,
                                                    digest__in=digests) \
                                    .values('digest').distinct().count()
            if user_completed >= total_activities:
                self.award_badge(course, user, badge)
