from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.utils.translation import gettext as _

from profile.models import CustomField, UserProfile, UserProfileCustomField
from profile.forms import helpers


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30,
                               min_length=4,
                               error_messages={
                                   'required':
                                   _(u'Please enter a username.')})
    email = forms.CharField(error_messages={
                                'invalid':
                                _(u'Please enter a valid e-mail address.'),
                                'required':
                                _(u'Please enter your e-mail address.')},
                            required=False)
    password = forms.CharField(widget=forms.PasswordInput,
                               error_messages={
                                   'required':
                                   _(u'Please enter a password.'),
                                   'min_length':
                                   _(u'Your password should be at least 6 \
                                   characters long.')},
                               min_length=6,
                               required=True)
    password_again = forms.CharField(widget=forms.PasswordInput,
                                     min_length=6,
                                     error_messages={
                                         'required':
                                         _(u'Please enter your password ' +
                                           u'again.'),
                                         'min_length':
                                         _(u'Your password again should be at \
                                         least 6 characters long.')},
                                     required=True)
    first_name = forms.CharField(max_length=100,
                                 error_messages={
                                     'required':
                                     _(u'Please enter your first name.'),
                                     'min_length':
                                     _(u'Your first name should be at least 2 \
                                     characters long.')},
                                 min_length=2,
                                 required=True)
    last_name = forms.CharField(max_length=100,
                                error_messages={
                                    'required':
                                    _(u'Please enter your last name.'),
                                    'min_length':
                                    _(u'Your last name should be at least 2 \
                                    characters long.')},
                                min_length=2,
                                required=True)
    job_title = forms.CharField(max_length=100, required=False)
    organisation = forms.CharField(max_length=100, required=False)
    phone_number = forms.CharField(max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(* args, ** kwargs)

        helpers.custom_fields(self)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
            'username',
            'email',
            'password',
            'password_again',
            'first_name',
            'last_name',
            'job_title',
            'organisation',
            'phone_number')

        custom_fields = CustomField.objects.all().order_by('order')
        for custom_field in custom_fields:
            self.helper.layout.append(custom_field.id)

        self.helper.layout.append(Div(
                Submit('submit', _(u'Register'), css_class='btn btn-default'),
                css_class='col-lg-offset-2 col-lg-4',
            ),
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email', '')
        password = cleaned_data.get('password')
        password_again = cleaned_data.get('password_again')
        username = cleaned_data.get('username')

        # check the username not already used
        num_rows = User.objects.filter(username=username).count()
        if num_rows != 0:
            raise forms.ValidationError(
                _(u"Username has already been registered, " +
                  u"please select another."))

        # check the email address not already used
        if email != '' and User.objects.filter(email=email).exists():
            raise forms.ValidationError(_(u"Email has already been " +
                                          u"registered"))

        if email != '':
            validate_email(email)

        # check the password are the same
        if password and password_again and password != password_again:
            raise forms.ValidationError(_(u"Passwords do not match."))

        # Always return the full collection of cleaned data.
        return cleaned_data

    def save(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # create UserProfile record
        UserProfile.objects.create(
            user=user,
            job_title=self.cleaned_data.get("job_title"),
            organisation=self.cleaned_data.get("organisation"),
            phone_number=self.cleaned_data.get("phone_number")
        )

        # save any custom fields
        custom_fields = CustomField.objects.all()
        for custom_field in custom_fields:
            if custom_field.type == 'int':
                profile_field = UserProfileCustomField(
                    key_name=custom_field,
                    user=user,
                    value_int=self.cleaned_data.get(custom_field.id))
            elif custom_field.type == 'bool':
                profile_field = UserProfileCustomField(
                    key_name=custom_field,
                    user=user,
                    value_bool=self.cleaned_data.get(custom_field.id))
            else:
                profile_field = UserProfileCustomField(
                    key_name=custom_field,
                    user=user,
                    value_str=self.cleaned_data.get(custom_field.id))

            if (self.cleaned_data.get(custom_field.id) is not None
                and self.cleaned_data.get(custom_field.id) != '') \
                    or custom_field.required is True:
                profile_field.save()
