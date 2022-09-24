# oppia/context_processors.py
import datetime
import oppia

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from oppia.models import Points, Award, BadgeMethod

from reports.signals import dashboard_accessed
from reports.menu import menu_reports

from settings import constants
from settings.models import SettingProperties


def get_points(request):
    if not request.user.is_authenticated:
        return {'points': 0, 'badges': 0}
    else:
        points = Points.get_userscore(request.user)
        if points is None:
            points = 0
        badges = Award.get_userawards(request.user)
        if badges is None:
            badges = 0
    return {'points': points, 'badges': badges}


# Sonarcloud raises a code smell that the request param here is redundant,
# however, Django requires it
def get_version(request):
    version = "v" + str(oppia.VERSION[0]) + "." \
                + str(oppia.VERSION[1]) + "." \
                + str(oppia.VERSION[2]) + "-" \
                + str(oppia.VERSION[3]) + "." \
                + str(oppia.VERSION[4]) + "-" \
                + str(oppia.VERSION[5])
    return {'version': version}


# Sonarcloud raises a code smell that the request param here is redundant,
# however, Django requires it
def get_settings(request):
    self_register = SettingProperties.get_bool(
                                constants.OPPIA_ALLOW_SELF_REGISTRATION,
                                settings.OPPIA_ALLOW_SELF_REGISTRATION)

    show_gravatars = SettingProperties.get_bool(
                                constants.OPPIA_SHOW_GRAVATARS,
                                settings.OPPIA_SHOW_GRAVATARS)

    ga_enabled = SettingProperties.get_bool(
                                constants.OPPIA_GOOGLE_ANALYTICS_ENABLED,
                                settings.OPPIA_GOOGLE_ANALYTICS_ENABLED)

    ga_code = SettingProperties.get_string(
                                constants.OPPIA_GOOGLE_ANALYTICS_CODE,
                                settings.OPPIA_GOOGLE_ANALYTICS_CODE)

    ga_domain = SettingProperties.get_string(
                                constants.OPPIA_GOOGLE_ANALYTICS_DOMAIN,
                                settings.OPPIA_GOOGLE_ANALYTICS_DOMAIN)

    try:
        badge_award_method = BadgeMethod.objects.get(
            badge__ref="coursecompleted")
        badge_award_method_percent = SettingProperties.get_int(
            constants.OPPIA_BADGES_PERCENT_COMPLETED, 100)
    except BadgeMethod.DoesNotExist:
        badge_award_method = "undefined"
        badge_award_method_percent = 100

    cron_warning = False
    last_cron = SettingProperties.get_string(
        constants.OPPIA_CRON_LAST_RUN, None)
    last_summary_cron = SettingProperties.get_string(
        constants.OPPIA_SUMMARY_CRON_LAST_RUN, None)
    cron_warning_threshold = SettingProperties.get_int(
        constants.OPPIA_CRON_WARNING_HOURS, 168)

    TIME_ZONE_FIX = '+00:00'
    # fix for bad timezone dates
    if last_cron and TIME_ZONE_FIX not in last_cron:
        last_cron += TIME_ZONE_FIX

    if last_summary_cron and TIME_ZONE_FIX not in last_summary_cron:
        last_summary_cron += TIME_ZONE_FIX

    if last_cron is None or last_summary_cron is None:
        cron_warning = True
    else:
        start_date = datetime.datetime.now() - datetime.timedelta(
            hours=cron_warning_threshold)
        last_cron_date = datetime.datetime.strptime(
            last_cron, constants.CRON_DATETIME_FORMAT)
        if last_cron_date < start_date:
            cron_warning = True

        last_summary_cron_date = datetime.datetime.strptime(
            last_summary_cron, constants.CRON_DATETIME_FORMAT)
        if last_summary_cron_date < start_date:
            cron_warning = True

    cron_warning_message = _("Cron tasks have not been run for over %d hours" % cron_warning_threshold)
    server_registered = SettingProperties.get_bool(
            constants.OPPIA_SERVER_REGISTERED, False)

    email_certificates = SettingProperties.get_bool(
            constants.OPPIA_EMAIL_CERTIFICATES, False)

    return {
        'OPPIA_ALLOW_SELF_REGISTRATION': self_register,
        'OPPIA_GOOGLE_ANALYTICS_ENABLED': ga_enabled,
        'OPPIA_GOOGLE_ANALYTICS_CODE': ga_code,
        'OPPIA_GOOGLE_ANALYTICS_DOMAIN': ga_domain,
        'OPPIA_SHOW_GRAVATARS': show_gravatars,
        'OPPIA_REPORTS': menu_reports(),
        'DEBUG': settings.DEBUG,
        'CRON_WARNING': cron_warning,
        'CRON_WARNING_MESSAGE': cron_warning_message,
        'COURSE_COMPLETE_BADGE_CRITERIA': badge_award_method,
        'COURSE_COMPLETE_BADGE_CRITERIA_PERCENT': badge_award_method_percent,
        'SERVER_REGISTERED': server_registered,
        'OPPIA_EMAIL_CERTIFICATES': email_certificates}


def add_dashboard_access_log(request):
    if request.POST:
        dashboard_accessed.send(sender=None,
                                request=request,
                                data=request.POST)
    else:
        dashboard_accessed.send(sender=None, request=request)

    return {'dashboard_access_added': True}
