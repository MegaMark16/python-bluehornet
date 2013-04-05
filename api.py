import urllib2, urllib
import xon

class BlueHornetAPI(object):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.last_request = None

    def method_call(self, method_calls):
        api_dict = {
            'api': {
                'authentication': {
                    'api_key': self.api_key,
                    'shared_secret': self.api_secret,
                },
            'data': method_calls,
            },
        }
        request_xml = xon.dumps(api_dict)
        self.last_request = request_xml
        params = urllib.urlencode({'data': request_xml,})
        headers = {"Content-type": "application/x-www-form-urlencoded",
                "Accept": "text/plain"}
        url = 'https://echo.bluehornet.com/api/xmlrpc/index.php'
        request = urllib2.Request(url, params, headers)
        response = urllib2.urlopen(request)
        response_xml = response.read()
        return xon.loads(response_xml)

    def get_method_dict(self, method_name, **kwargs):
        return_dict = {
            'methodCall': {
                'methodName': method_name,
            },
        }
        return_dict['methodCall'].update(kwargs)
        return return_dict

    def send_mail(self, subject, message, from_email, recipient_list,
                  fail_silently=False):
        pass

    def set_subscriber(self, email, **kwargs):
        method_call = self.get_method_dict('legacy.manage_subscriber',
                                           email=email,
                                           **kwargs)
        return self.method_call([method_call])

    def retrieve_active(self, extended='1', basic='1', **kwargs):
        method_call = self.get_method_dict('legacy.retrieve_active',
                                           **kwargs)
        return self.method_call([method_call])

    def check_email(self, *addresses):
        method_calls = []
        for address in addresses:
            method_dict = self.get_method_dict('utilities.checkemail',
                                               email=address,
                                               mx_check='1')
            method_calls.append(method_dict)
        return self.method_call(method_calls)



