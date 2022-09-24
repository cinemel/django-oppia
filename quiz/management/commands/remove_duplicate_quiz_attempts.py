# coding: utf-8

"""
Management command to remove any duplicate quiz attempts (based on instance_id)
"""

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db.models import Count, Max
from django.utils.translation import gettext_lazy as _

from quiz.models import QuizAttempt


class Command(BaseCommand):
    help = _(u"Removes any duplicate quiz attempts based on instance_id")

    def handle(self, *args, **options):
        """
        Remove quizattempts with no UUID
        """
        result = QuizAttempt.objects.filter(instance_id=None).delete()
        if result[0] != 0:
            self.stdout.write(
                _(u"\n\n%d quiz attempts removed that had no instance_id\n"
                  % result[0]))

        """
        Remove proper duplicate quizattempts - using max id
        """
        quiz_attempts = QuizAttempt.objects.all() \
            .values('instance_id') \
            .annotate(dcount=Count('instance_id')) \
            .filter(dcount__gte=2)

        for index, quiz_attempt in enumerate(quiz_attempts):
            self.stdout.write("%d/%d" % (index, quiz_attempts.count()))
            exclude = QuizAttempt.objects \
                .filter(instance_id=quiz_attempt['instance_id']) \
                .aggregate(max_id=Max('id'))
            deleted = QuizAttempt.objects \
                .filter(instance_id=quiz_attempt['instance_id']) \
                .exclude(id=exclude['max_id']) \
                .delete()
            self.stdout.write(_(u"%(count)d duplicate quiz attempt(s) removed for \
                               instance_id %(instance)s based on max id"
                                % {'count': deleted[0],
                                   'instance': quiz_attempt['instance_id']}))

        """
        Remember to run summary cron from start
        """
        if result[0] + quiz_attempts.count() > 0:
            self.stdout.write(_(u"Since duplicates have been found and \
                               removed, you should now run `update_summaries` \
                               to ensure the dashboard graphs are accurate."))
            accept = input(_(u"Would you like to run `update_summaries` \
                                 now? [Yes/No]"))
            if accept == 'y':
                call_command('update_summaries', fromstart=True)
