from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    engagement_model = forms.CharField(max_length=100)
