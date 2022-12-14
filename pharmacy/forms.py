from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from pharmacy.models import Department, Medicine


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


class MedicineForm(forms.ModelForm):
    departments = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Medicine
        fields = "__all__"


class DepartmentSearchForm(forms.Form):
    name_pharmacy = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by name pharmacy "
        }
        )
    )


class MedicineSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name "})
    )


class ManufacturerSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name "})
    )
