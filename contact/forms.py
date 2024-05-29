from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    engagement_model = forms.CharField(max_length=100)


class UserAplicationForm(forms.Form):
    fullname = forms.CharField(max_length=160)
    phone_number = forms.CharField(max_length=100)
    email = forms.EmailField()
    current_location = forms.CharField(max_length=160)
    current_company = forms.CharField(max_length=160)
    notice_period = forms.CharField(max_length=100)
    salary_expectation = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
    referral_source = forms.CharField(max_length=200)
    years_of_experience = forms.CharField(max_length=50)
    linkedin_profile = forms.URLField(max_length=500)
    github_profile = forms.URLField(max_length=500)
    portfolio = forms.URLField(max_length=500)
    pdf_path = forms.FileField()
    cv = forms.BooleanField(required=False)
