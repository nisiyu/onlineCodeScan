from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, error_messages={'required': 'Your Name is Required'})
    file = forms.FileField()