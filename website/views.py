from flask import Blueprint,render_template


views=Blueprint('views',__name__)
@views.route('/')
def home():
    
    return render_template("home.html")
def info1():
    return render_template("info1.html")


