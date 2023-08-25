from django.template.loader import render_to_string


def send_activation_notification(user):
    subject = render_to_string(
        'email/activation_letter_subject.txt',
    )
    body_text = render_to_string(
        'email/activation_letter_body.txt',
    )
    user.email_user(subject, body_text)
