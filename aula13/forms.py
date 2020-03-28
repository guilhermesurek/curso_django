from django import forms
from .models import UploadFile

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class UploadFileModelForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = "__all__"