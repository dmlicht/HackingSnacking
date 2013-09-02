from flask import Flask, render_template, jsonify
from app import app
from app.generate_deal_list import Deal
import cPickle
import json
#from flask import session, config, g

with open('all_deals') as f:
    deals = cPickle.load(f)

deal_jsons = {deal.name: json.dumps(deal.__dict__) for deal in deals}

# num_non_matching = 0
# for deal in deals:
#     if not deal.name_matches():
#         num_non_matching += 1
# print num_non_matching + "out of" + len(deals) + "dont match"

# print dir(d[0])

@app.route('/')
def show_deals():
    return render_template('index.html')

@app.route('/_deal_data')
def _deal_data():
    return jsonify(deal_jsons) 

if __name__ == '__main__':
    app.run(port = 5002)
