from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={"class": "input input__icon form-control",
                                           "id": "nameContact",
                                           "name": "nameContact",
                                           "placeholder": "نام و نام خانوادگی",
                                           "required": "required",
                                           "autocomplete": "on",
                                           "oninvalid": "setCustomValidity('فیلد مورد نظر را پر کنید')",
                                           "onkeyup": "setCustomValidity('')"}),
            'email': forms.TextInput(attrs={"type": "email",
                                            "class": "input input__icon form-control",
                                            "id": "emailContact",
                                            "name": "emailContact",
                                            "placeholder": "آدرس ایمیل",
                                            "required": "required",
                                            "autocomplete": "on",
                                            "oninvalid": "setCustomValidity('ایمیل مورد نظر را وارد کنید')",
                                            "onkeyup": "setCustomValidity('')"}),
            'body': forms.Textarea(attrs={"id": "commentForm",
                                          "class": "textarea textarea--white form-control",
                                          "required": "required",
                                          "placeholder": "  ارسال نظر ...",
                                          "rows": "1"})
        }
