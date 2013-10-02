import json
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
            categories = cls.clean_categories(yelp_json["categories"])
            deal_url = GROUPON_BASE_DEAL_URL + deal_json['id']
            return cls(name, yelp_score, yelp_url, num_reviews, deal_url, loc, categories, image_url, yelp_json, deal_json)

    @staticmethod
    def clean_categories(categories):
        """takes yelp formatted categories and returns simple list
        containing first element of each inner list"""
        return [cat[0] for cat in categories]

    def __init__(self, name, yelp_score, yelp_url, num_reviews, deal_url, address, categories, image_url=None, yelp_json=None, deal_json=None):
        self.name = name
        self.yelp_score = yelp_score
        self.yelp_url = yelp_url
        self.num_reviews = num_reviews
        self.deal_url = deal_url
        self.address = address
        self.categories = categories
        self.image_url = image_url
        self.yelp_json = yelp_json
        self.deal_json = deal_json

    def name_matches(self):
        """returns true if name from deals site matches name on yelp"""
        return self.name == self.yelp_json['name']
