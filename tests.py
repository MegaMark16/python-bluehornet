import urllib2, urllib
from django.test import TestCase
from django.conf import settings
from bluehornet.api import BlueHornetAPI

class APITests(TestCase):

    def test_check_email_address(self):
        api = BlueHornetAPI(settings.BLUE_HORNET_API_KEY,
                            settings.BLUE_HORNET_API_SECRET)
        response = api.check_email('megamark16@gmail.com','bob@example.com')
        self.assertEquals('1', response['methodResponse']['item'][0]['responseData']['valid'])
        self.assertEquals('0', response['methodResponse']['item'][1]['responseData']['valid'])

    def test_add_subscriber(self):
        api = BlueHornetAPI(settings.BLUE_HORNET_API_KEY,
                            settings.BLUE_HORNET_API_SECRET)
        response = api.add_subscriber(email='test@example.com',
                                      firstname='Test',
                                      lastname='Subscriber')
        self.assertEquals('1', response['methodResponse']['item'][0]['responseData']['valid'])


    def test_retrieve_active(self):
        api = BlueHornetAPI(settings.BLUE_HORNET_API_KEY,
                            settings.BLUE_HORNET_API_SECRET)
        response = api.retrieve_active(extended='1')
        self.assertEquals('1', response['methodResponse']['item'][0]['responseData']['valid'])
        self.assertEquals('0', response['methodResponse']['item'][1]['responseData']['valid'])

