import httplib
import json
import search_script
import unicodedata
from keys import keys

BASE_DEAL_URL = 'http://www.groupon.com/deals/'

def convert_to_ascii(unicode_string):
    """returns the ascii version of string with characters valued over 128 stripped"""
    return unicodedata.normalize("NFKD", unicode_string).encode("ascii", "ignore")

def generate_query_url(base, fields):
    """takes a base url and set of fields and returns implied url"""
    field_string = '&'.join([k + '=' + v for (k,v) in fields.items()])
    return '%s?%s' % (base, field_string)

def main():
    base_url = "http://api.groupon.com/v2/deals/search"
    query_url_fields = {
        "callback": '_',
        'limit': '4000',
        'offset': '0',
        'division_id': 'new-york',
        'facets': 'category%7Ccategory2',
        'relevance_context': 'web_local',
        'show_facets': 'Local',
        'filters': 'category%3Arestaurants-and-bars',
        'lat': '40.7143528',
        'lng': '-74.0059731',
        'locale': 'en',
        'secure_assets': 'true',
        'force_http_success': 'true',
        '_': '1371507745085',
        'client_id': keys["GROUPON_CLIENT_ID"]
    }

    request_string = generate_query_url(base_url, query_url_fields)
    groupon_connection = httplib.HTTPConnection('api.groupon.com', 80)
    groupon_connection.request('GET', request_string)
    response = groupon_connection.getresponse()

    #strip beginning and end characters to expose just the json from the request
    response_json = json.loads(response.read()[2:-1])

    for deal in response_json['deals']:
        name = deal['merchant']['name']
        ascii_name = convert_to_ascii(name)
        # print ascii_name

        yelp_score, name, yelp_url, num_reviews, loc = search_script.get_rating(ascii_name)
        if yelp_score >= 4.0:
            print name
            print str(yelp_score) + " with " + str(num_reviews) + " reviews from yelp!"
            print "DEAL: " + BASE_DEAL_URL + deal['id']
            print "Read more on yelp: " + yelp_url
            print loc["address"]
            print

    print len(response_json['deals'])

if __name__ == "__main__":
    main()
