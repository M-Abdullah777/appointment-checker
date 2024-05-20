import os
import yagmail

# Example credentials (replace with actual credentials)
EMAIL = 'tayyabasheikh009@gmail.com'
PASS = 'gplx qjli gawz tdam'
TO = 'abdullahjabbar.965@gmail.com','amnakanwal963@gmail.com'

def send_mail(subject, contents):
    yag = yagmail.SMTP(EMAIL, PASS)
    yag.send(
        to=TO,
        subject=subject,
        contents=contents,
    )

if __name__ == '__main__':
    send_mail( 'Test Email', 'Test Content')
