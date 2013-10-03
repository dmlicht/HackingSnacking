import search_script
import unicodedata
import pygroupon
import cPickle
import os
from deal import Deal
try:
    from keys import KEYS
    os.environ["GROUPON_CLIENT_ID"] = KEYS["GROUPON_CLIENT_ID"]
except:
    pass

CURRENT_DIR = '/Users/David/Learning/HackerSchool/hacking-snacking/'
PICKLE_FILENAME = 'all_deals'
FILTER_CUTOFF = 4.0

def convert_to_ascii(unicode_string):
    """returns the ascii version of string with characters valued over 128 stripped"""
    return unicodedata.normalize("NFKD", unicode_string).encode("ascii", "ignore")

def main():
    groupon = pygroupon.Groupon(os.environ["GROUPON_CLIENT_ID"])
    groupon_json = groupon.get_deals()
    well_reviewed_deals = []
    for deal_json in groupon_json['deals']:
        merchant = deal_json['merchant']
        name = deal_json['merchant']['name']
        ascii_name = convert_to_ascii(name)
        ratings = [d for d in merchant.get('ratings', []) if d.get('linkText', None) == 'Yelp']
        if len(ratings) == 1:
            ratings = ratings[0]
        else:
            ratings = {}
        #groupon_yelp_url = ratings.get('url', None)
        score = float(ratings.get('rating', 0))
        if score < FILTER_CUTOFF:
            continue
        yelp_json = search_script.get_rating(ascii_name)
        if yelp_json is None:   #do not add with no yelp data
            continue
        #yelp_url = yelp_json.get('url', None)
        #if groupon_yelp_url != yelp_url:
        #    print 'no match'
        #    print 'groupon: ', groupon_yelp_url
        #    print 'yelp: ', yelp_url
        #    continue
        deal = Deal.from_json(yelp_json, deal_json)
        #if score >= FILTER_CUTOFF:
        if deal.yelp_score >= FILTER_CUTOFF:
            print 'added: ', name
            well_reviewed_deals.append(deal)
    os.chdir(CURRENT_DIR)
    with open('all_deals', 'wb') as f:
        cPickle.dump(well_reviewed_deals, f)

if __name__ == "__main__":
    main()
