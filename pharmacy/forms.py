from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from models import Department


def validate_license_number(license_number):
    if len(license_number) != 8:
        raise ValidationError("License number must be 8 characters long.")
    elif not license_number[:3].isalpha() or not license_number[:3].isupper():
        raise ValidationError("First 3 characters must be uppercase letters.")
    elif not license_number[3:].isdigit():
        raise ValidationError("Last 5 characters must be digits.")
    return license_number


class DepartmentCreationForm(UserCreationForm):
    license_number = forms.CharField(validators=[validate_license_number])

    class Meta(UserCreationForm.Meta):
        model = Department
        fields = UserCreationForm.Meta.fields + (
            "name_pharmacy",
            "license_number",
            "address",
            "phone",
            "time_work",
            "first_name",
            "last_name"
        )


class DepartmentLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(validators=[validate_license_number])

    class Meta:
        model = Department
        fields = ("license_number",)


class DepartmentAddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("address",)


class DepartmentPhoneUpdateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("phone",)


class DepartmentTimeWorkUpdateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("time_work",)


class DepartmentNameUpdateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("first_name", "last_name")
