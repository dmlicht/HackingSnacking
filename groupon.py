import search_script
import unicodedata
import pygroupon
from keys import keys

BASE_DEAL_URL = 'http://www.groupon.com/deals/'

def convert_to_ascii(unicode_string):
    """returns the ascii version of string with characters valued over 128 stripped"""
    return unicodedata.normalize("NFKD", unicode_string).encode("ascii", "ignore")

def main():
    groupon = pygroupon.Groupon(keys["GROUPON_CLIENT_ID"])
    response_json = groupon.fetch()
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
