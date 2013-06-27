from flask import Flask, render_template
# import deal_list
import cPickle
#from flask import session, config, g

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# with open('all_deals') as f:
#     deals = cPickle.load(f)

@app.route('/')
def show_deals():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()