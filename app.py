from flask import Flask, render_template, jsonify
from deal_list import Deal
import cPickle
import json
#from flask import session, config, g

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

with open('all_deals') as f:
    deals= cPickle.load(f)

deal_jsons = {deal.name: json.dumps(deal.__dict__) for deal in deals}

# num_non_matching = 0
# for deal in deals:
#     if not deal.name_matches():
#         num_non_matching += 1
# print num_non_matching + "out of" + len(deals) + "dont match"

# print dir(d[0])

@app.route('/')
def show_deals():
    return render_template('index.html', deals=deals)

@app.route('/_deal_data')
def _deal_data():
    return jsonify(deal_jsons) 

if __name__ == '__main__':
    app.run(port=5002)
