import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

SMTPS_PORT = 587
LAST_ELEMENT = -1


class EmailManager:
    def __init__(self, smtp_host, imap_host, login, password):
        self.smtp_host = smtp_host
        self.imap_host = imap_host
        self.login = login
        self.password = password

    def send(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        transport = smtplib.SMTP(self.smtp_host, SMTPS_PORT)
        try:
            # identify ourselves to smtp gmail client
            transport.ehlo()
            # secure our email with tls encryption
            transport.starttls()
            # re-identify ourselves as an encrypted connection
            transport.ehlo()

            transport.login(self.login, self.password)
            transport.sendmail(
                self.login,
                transport,
                msg.as_string())
        finally:
            transport.quit()

    @staticmethod
    def _search(transport, terms):
        _, messages = transport.uid('search', None, terms)
        if not messages[0]:  # Ошибка в коде?
            raise ValueError(
                'There are no letters with current header')
        return messages

    @staticmethod
    def _fetch_first_by_uid(transport, uid):
        _, message = transport.uid('fetch', uid, '(RFC822)')
        message_body = message[0][1]
        return email.message_from_string(message_body)

    def read(self, header=None, inbox_name='inbox'):
        search_term = '(HEADER Subject "%s")' % header if header else 'ALL'
        transport = imaplib.IMAP4_SSL(self.imap_host)

        try:
            transport.login(self.login, self.password)
            transport.list()
            transport.select(inbox_name)
            messages = self._search(transport, search_term)
            latest_uid = messages[0].split()[LAST_ELEMENT]
            email_message = self._fetch_first_by_uid(
                transport, latest_uid)
        finally:
            transport.logout()

        return email_message
