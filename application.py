from app import app, application

if __name__=='__main__':
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])
