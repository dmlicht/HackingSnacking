from flask import Flask, render_template
from deal_list import Deal
import cPickle
#from flask import session, config, g

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

with open('all_deals') as f:
    deals= cPickle.load(f)

# num_non_matching = 0
# for deal in deals:
#     if not deal.name_matches():
#         num_non_matching += 1
# print num_non_matching + "out of" + len(deals) + "dont match"

# print dir(d[0])
@app.route('/')
def show_deals():
    return render_template('index.html', deals=deals)

if __name__ == '__main__':
    app.run()