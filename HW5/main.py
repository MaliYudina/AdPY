from .original import EmailManager

# it may also be Yandex or Mail.Ru
SMTP_HOST = 'smtp.gmail.com'
IMAP_HOST = 'imap.gmail.com'

LOGIN = 'login@gmail.com'
PASSWORD = 'qwerty'
SUBJECT = 'Subject'
MESSAGE = 'Message'
RCPTTO = ['vasya@email.com', 'petya@email.com']
HEADER = None


def _main():
    email = EmailManager(
        smtp_host=SMTP_HOST,
        imap_host=IMAP_HOST,
        login=LOGIN,
        password=PASSWORD)
    email.send(
        message=MESSAGE,
        recipients=RCPTTO,
        subject=SUBJECT)
    return email.read(HEADER)


if __name__ == '__main__':
    _main()
