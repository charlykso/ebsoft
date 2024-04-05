import random
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives

from ebsoft import settings

def send_email_to_user(firstname, lastname, pdf_file):
    subject = 'Resume for {} {}'.format(firstname, lastname)
    message ='This is the email body.',
    to ='umehlilian45@gmail.com',
    print(subject)
    print(to[0])
    print(message[0])
    try:
        with pdf_file.open(mode='rb') as f:  # Open in binary read mode
            pdf_content = f.read()
        
        # Create an EmailMultiAlternatives object.
        email = EmailMessage(subject, message[0], settings.EMAIL_HOST_USER, [to[0]])

        # Attach PDF file
        email.attach(f'CV_{lastname}_{firstname}.pdf', pdf_content, "application/pdf")

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