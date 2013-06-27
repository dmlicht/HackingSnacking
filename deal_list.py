import search_script
import unicodedata
import pygroupon
import cPickle
# from pprint import pprint
from keys import keys

GROUPON_BASE_DEAL_URL = 'http://www.groupon.com/deals/'
FILTER_CUTOFF = 4.0

class Deal(object):

    @classmethod
    def from_json(cls, yelp_json, deal_json, deal_site="Groupon"):
        """takes yelp and deal site json data and creates deal object from it
        currently only handles groupon"""
        if deal_site != "Groupon":
            raise Exception
        else:
            name = deal_json['merchant']['name']
            yelp_score = yelp_json["rating"]
            # name = yelp_json["name"] 
            yelp_url = yelp_json["url"]
            num_reviews = yelp_json["review_count"]
            loc = yelp_json["location"]
            deal_url = GROUPON_BASE_DEAL_URL + deal_json['id']
            return cls(name, yelp_score, yelp_url, num_reviews, deal_url, loc, yelp_json, deal_json)

    def __init__(self, name, yelp_score, yelp_url, num_reviews, deal_url, address, yelp_json=None, deal_json=None):
        self.name = name
        self.yelp_score = yelp_score
        self.yelp_url = yelp_url
        self.num_reviews = num_reviews
        self.deal_url = deal_url
        self.address = address
        self.yelp_json = yelp_json
        self.deal_json = deal_json

    def name_matches(self):
        """returns true if name from deals site matches name on yelp"""
        return self.name == self.yelp_json['name']


def convert_to_ascii(unicode_string):
    """returns the ascii version of string with characters valued over 128 stripped"""
    return unicodedata.normalize("NFKD", unicode_string).encode("ascii", "ignore")

def main():
    groupon = pygroupon.Groupon(keys["GROUPON_CLIENT_ID"])
    groupon_json = groupon.fetch()
    well_reviewed_deals = []
    for deal_json in groupon_json['deals']:
        name = deal_json['merchant']['name']
        ascii_name = convert_to_ascii(name)
        yelp_json = search_script.get_rating(ascii_name)
        if yelp_json is None:   #do not add with no yelp data
            continue
        deal = Deal.from_json(yelp_json, deal_json)
        if deal.yelp_score >= FILTER_CUTOFF:
            well_reviewed_deals.append(deal)
    with open('all_deals', 'w') as f:
        cPickle.dump(well_reviewed_deals, f)

if __name__ == "__main__":
    main()