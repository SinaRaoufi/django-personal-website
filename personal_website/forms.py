from django import forms
from django.core import validators


class ConatactMeForm(forms.Form):
    fullname = forms.CharField(max_length=25,
                               widget=forms.TextInput(attrs={"class": "input input__icon form-control",
                                                             "id": "nameContact",
                                                             "name": "nameContact",
                                                             "placeholder": "نام و نام خانوادگی",
                                                                            "required": "required",
                                                                            "autocomplete": "on",
                                                                            "oninvalid": "setCustomValidity('لطفا نام و نام خانوادگی خود را وارد کنید')",
                                                                            "onkeyup": "setCustomValidity('')"}),
                               validators=[
                                   validators.MinLengthValidator(
                                       3, 'نام وارد شده نامعتبر است'),
                                   validators.MaxLengthValidator(
                                       30, 'نام وارد شده نامعتبر است')]
                               )
    email = forms.EmailField(widget=forms.TextInput(attrs={"type": "email",
                                                           "class": "input input__icon form-control",
                                                           "id": "emailContact",
                                                           "name": "emailContact",
                                                           "placeholder": "آدرس ایمیل",
                                                           "required": "required",
                                                           "autocomplete": "on",
                                                           "oninvalid": "setCustomValidity('ایمیل مورد نظر را وارد کنید')",
                                                           "onkeyup": "setCustomValidity('')"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "textarea form-control",
                                                           "id": "messageContact",
                                                           "name": "messageContact",
                                                           "placeholder": "پیام شما",
                                                           "rows": "7",
                                                           "required": "required",
                                                           "oninvalid": "setCustomValidity('فیلد مورد نظر را پر کنید')",
                                                           "onkeyup": "setCustomValidity('')"}))
