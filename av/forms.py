# oppia/av/forms.py

import hashlib

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from django import forms
from django.conf import settings
from django.core.files.uploadedfile import TemporaryUploadedFile, \
                                           InMemoryUploadedFile, \
                                           SimpleUploadedFile
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from av.models import UploadedMedia


class UploadMediaForm(forms.Form):
    media_file = forms.FileField(
                help_text=_(u'Media file types accepted: %s' %
                            ', '.join(settings.OPPIA_MEDIA_FILE_TYPES)),
                required=True,
                error_messages={'required': _(u'Please select a media file \
                                             to upload')},
                )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UploadMediaForm, self).__init__(* args, ** kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
                'media_file',
                Div(
                   Submit('submit',
                          _(u'Upload'),
                          css_class='btn btn-default'),
                   css_class='col-lg-offset-2 col-lg-4',
                ),
            )

    def clean(self):
        cleaned_data = super(UploadMediaForm, self).clean()
        media_file = cleaned_data.get("media_file")

        if media_file is not None \
                and media_file.content_type  \
                not in settings.OPPIA_MEDIA_FILE_TYPES:
            raise forms.ValidationError(
                _(u"You may only upload a media file \
                  which is one of the following types: %s" % ', '
                  .join(settings.OPPIA_MEDIA_FILE_TYPES)))

        '''
        check this file hasn't already been uploaded
        the media_file might either by a TemporaryUploadedFile or an
        InMemoryUploadedFile - so need to handle generation of the md5
        differently in each case
        '''

        if isinstance(media_file, TemporaryUploadedFile):
            md5 = hashlib.md5(open(media_file.temporary_file_path(),
                                   'rb').read()).hexdigest()
        elif isinstance(media_file, InMemoryUploadedFile) \
                or isinstance(media_file, SimpleUploadedFile):
            md5 = hashlib.md5(media_file.read()).hexdigest()
        else:
            raise forms.ValidationError(_(u"File failed to upload correctly"))

        media = UploadedMedia.objects.filter(md5=md5)
        if media.count() > 0:
            raise forms.ValidationError({
                'media_file':
                    mark_safe(
                        _(u"This media file has already been uploaded. \
                          <a href='%s'>View the original upload</a>."
                          % media.first().file.url)),
                })
        return cleaned_data
