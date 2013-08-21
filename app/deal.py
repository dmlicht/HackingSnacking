GROUPON_BASE_DEAL_URL = 'http://www.groupon.com/deals/'

class Deal(object):
    @classmethod
    def from_json(cls, yelp_json, deal_json, deal_site="Groupon"):
        """takes yelp and deal site json data and creates deal object from it
        currently only handles groupon"""
        if deal_site != "Groupon":
            raise Exception
        else:
            name = deal_json['merchant']['name']
            image_url = deal_json['grid4ImageUrl']
            yelp_score = yelp_json["rating"]
            # name = yelp_json["name"] 
            yelp_url = yelp_json["url"]
            num_reviews = yelp_json["review_count"]
            #categories = yelp_json['categories']
            loc = yelp_json["location"]
            deal_url = GROUPON_BASE_DEAL_URL + deal_json['id']
            return cls(name, yelp_score, yelp_url, num_reviews, deal_url, loc, image_url, yelp_json, deal_json)

    def __init__(self, name, yelp_score, yelp_url, num_reviews, deal_url, address, image_url=None, yelp_json=None, deal_json=None):
        self.name = name
        self.yelp_score = yelp_score
        self.yelp_url = yelp_url
        self.num_reviews = num_reviews
        self.deal_url = deal_url
        self.address = address
        self.image_url = image_url
        self.yelp_json = yelp_json
        self.deal_json = deal_json

    def name_matches(self):
        """returns true if name from deals site matches name on yelp"""
        return self.name == self.yelp_json['name']
