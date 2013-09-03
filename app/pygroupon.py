import httplib
import json

DEFAULT_FIELDS = {
    "callback": '_',
    'limit': '4000',
    'offset': '0',
    'division_id': 'new-york',
    'facets': 'category%7Ccategory2',
    'relevance_context': 'web_local',
    'show_facets': 'Local',
    'filters': 'category%3Afood-and-drink',
    'lat': '40.7143528',
    'lng': '-74.0059731',
    'locale': 'en',
    'secure_assets': 'true',
    'force_http_success': 'true',
    '_': '1371507745085',
    'client_id': None
}

class Groupon(object):
    """wraps groupon http api for quick use with python
    by default it will search for all current restaurant deals
    in the NYC area"""

    def __init__(self, client_id):
        self._fields = DEFAULT_FIELDS
        self._fields['client_id'] = client_id
        self._base_url = "http://api.groupon.com/v2/deals/search"

    def generate_query_url(self):
        """takes a base url and set of fields and returns implied url"""
        field_string = '&'.join([k + '=' + v for (k,v) in self._fields.items()])
        return '%s?%s' % (self._base_url, field_string)

    def fetch(self):
        """queries groupon api and returns json object with results"""
        request_string = self.generate_query_url()
        connection = httplib.HTTPConnection('api.groupon.com', 80)
        connection.request('GET', request_string)
        response = connection.getresponse()

        #strip beginning and end characters to expose just the json from the request
        return json.loads(response.read()[2:-1])
