import random
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from email.mime.text import MIMEText

from ebsoft import settings

def send_email_to_user(data, pdf_file):
    name = data['fullname'].replace(" ", "_")
    subject = '{} Application  From'.format(data['fullname'])
    to = 'umehlilian45@gmail.com',
    context = {
        'fullname': data['fullname'],
        'email': data['email'],
        'phone_number': data['phone_number'],
        'current_location': data['current_location'],
        'current_company': data['current_company'],
        'notice_period': data['notice_period'],
        'salary_expectation': data['salary_expectation'],
        'gender': data['gender'],
        'referral_source': data['referral_source'],
        'years_of_experience': data['years_of_experience'],
        'linkedin_profile': data['linkedin_profile'],
        'github_profile': data['github_profile'],
        'portfolio': data['portfolio']
    }
    template = get_template('email_template.html')
    html_content = template.render(context)
    try:
        
        with pdf_file.open(mode='rb') as f:  # Open in binary read mode
            pdf_content = f.read()

        # Create an EmailMultiAlternatives object.
        email = EmailMessage(subject.upper(), html_content, settings.EMAIL_HOST_USER, to)
        # email = EmailMultiAlternatives(subject, message, settings.EMAIL_HOST_USER, to)
        email.content_subtype = "html"

        # email.attach(MIMEText(html_content, 'text/html'))
        # email.attach_alternative(html_content, "text/html")
        # Attach PDF file
        email.attach(f'CV_{name}.pdf', pdf_content, "application/pdf")

        # email.attach(f'Application_{name}.html', html_content, "text/html")

        # Send the email.
        sent_count = email.send(fail_silently=False)
        return sent_count 
    except Exception as e:
        error_message = str(e)
        print(f"Error sending email: {error_message}")
        return 0

def generate_random_code():
    """Generates a random 6-letter string that combines letters and digits."""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    all_chars = letters + digits
    random_string = ""
    for i in range(6):
        random_char = random.choice(all_chars)
        random_string += random_char
    return random_string

# create a function to send email to user using a html template

def send_confirm_email(user_email, subject, message):

        try:
            message = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user_email],
            )

            # message.attach('qr_code.png', code, "image/png")

            sent_count = message.send(fail_silently=False)
            return sent_count
        except Exception as e:
            error_message = str(e)
            print(error_message)
            sent_count = 0
            return sent_count
