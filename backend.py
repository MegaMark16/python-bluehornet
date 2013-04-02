"""
Django email backend for sending mail through BlueHornet
"""
import smtplib
import socket
import threading

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.utils import DNS_NAME
from django.core.mail.message import sanitize_address
from bluehornet.api import BlueHornetAPI


class BlueHornetBackend(BaseEmailBackend):
    """
    A wrapper that manages the api connection.
    """
    def __init__(self, host=None, port=None, username=None, password=None,
                 fail_silently=False, **kwargs):
        super(BlueHronetBackend, self).__init__(fail_silently=fail_silently)
        self.host = host or settings.EMAIL_HOST
        self.port = port or settings.EMAIL_PORT
        self.username = username or settings.EMAIL_HOST_USER
        self.password = password or settings.EMAIL_HOST_PASSWORD
        self.connection = None
        self._lock = threading.RLock()

    def send_messages(self, email_messages):
        """
        Sends one or more EmailMessage objects and returns the number of email
        messages sent.
        """
        if not email_messages:
            return
        self._lock.acquire()
        try:
            api = BlueHornetAPI(self.host, self.port, self.username,
                    self.password)
            num_sent = 0
            for message in email_messages:
                sent = api.send(message)
                if sent:
                    num_sent += 1
        finally:
            self._lock.release()
        return num_sent
