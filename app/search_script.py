import os
import json
#minimum value for returned result

def get_rating(name):
    """returns name, yelp rating, and yelp page url of given business
    if business cannot be found it returns rating 0, name, empty string for url, 0 reviews and empty string for addr"""

    #calls script provided by yelp to access API. 
    #Consumer credentials hardcoded. This seems like it could be bad practice
    command = 'python search.py --consumer_key="sPXjoKQ5TGRuP8O0VWW_0Q" --consumer_secret="28TsVhiznWyd9BdBiQGOsxKzSSY" --token="zJ6rk5-5Uk0ObRxI-fB7c9vqq7e1iiPb" --token_secret="uCzsZqjbUmOdMoiyyJ55-anlH9U" --term="' + name + '" --location="New York, NY" --limit=2'

    #popen is similar to os.system but returns result string instead of printing to stout
    results = os.popen(command).read()

    #parse output. first 3 lines equate to request data and empty line. 4th line is result json
    if len(results) < 10:
        return None
        continue
    url_line, signed_url, _, json_data = str.split(results, '\n', 3)

    json_obj = json.loads(json_data)
    businesses = json_obj.get("businesses", 0)
    if businesses:
        return businesses[0]

        # first = businesses[0]
        # return first["rating"], first["name"], first["url"], first["review_count"], first["location"]
    else:
        return None
        # return 0, name, "", 0, ""
