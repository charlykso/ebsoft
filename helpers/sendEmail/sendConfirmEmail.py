import random
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives

from ebsoft import settings

def send_email_to_user(firstname, lastname, pdf_path):
        
    subject=f'Resume for {firstname} {lastname}',
    message='This is the email body.',
    from_email='eventify141@gmail.com',
    to=['umehlilian45@gmail.com'],
    reply_to=['eventify141@gmail.com'],
    try:
        # Create an EmailMultiAlternatives object.
        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [to],
        )

        # Attach PDF file
        email.attach(f'CV_{lastname}_{firstname}.pdf', pdf_path, "application/pdf")

        # Send the email.
        sent_count = email.send(fail_silently=True)
        return sent_count 
    except Exception as e:
        error_message = str(e)
        print(error_message)
        sent_count = 0
        return sent_count

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