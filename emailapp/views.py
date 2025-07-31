from django.core.mail import send_mail
from django.http import HttpResponse

def send_email_view(request):
    subject = 'Hello from Django'
    message = 'This is a test email sent using Django SMTP Gmail.'
    from_email = None  # Will use DEFAULT_FROM_EMAIL from settings.py
    recipient_list = ['oladraxler18@gmail.com']  # ✅ Change this to your email

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse("✅ Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"❌ Failed to send email: {e}")
