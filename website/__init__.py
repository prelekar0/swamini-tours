from flask import Flask,render_template


def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    

    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    @app.route('/home')
    def home():
       
        return render_template('home.html')
    return app

   