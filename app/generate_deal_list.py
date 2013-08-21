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
    os.chdir(CURRENT_DIR)
    with open('all_deals', 'wb') as f:
        cPickle.dump(well_reviewed_deals, f)

if __name__ == "__main__":
    main()
