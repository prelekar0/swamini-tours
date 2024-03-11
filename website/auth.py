from flask import Blueprint, render_template, flash, request

auth=Blueprint('auth',__name__)

@auth.route('/Login',methods=['GET', 'POST'])
def login():
    data=request.form
    print(data)
    return render_template("login.html")
    flash('Account Login!',category='success')

@auth.route('/About_Us')
def About_Us():
    data=request.form
    print(data)
    return render_template("about_us.html")

@auth.route('/Home' )
def home():
   return render_template("home.html")

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    
    if request.method=='POST':
        email=request.form.get('email')
        first_name=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        if len(email)<4:
         flash("Email must be greater than 4 characters.",category='error')
        elif len(first_name)<2:
            flash("First name must be greater than 2 characters.",category='error')
        elif password1!=password2:
             flash("Password don\'t match.",category='error')
        elif len(password1)<7:
             flash("Password must be at least 6 characters.",category='Error')
        else:
            flash("Account Created!",category='Success') 
    return render_template("sign_up.html")

@auth.route('/info1')
def info1():
    return render_template("/info1.html")

@auth.route('/info2')
def info2():
    return render_template("/info2.html")

@auth.route('/info3')
def info3():
    return render_template("/info3.html")

@auth.route('/info4')
def info4():
    return render_template("/info4.html")

@auth.route('/info5')
def info5():
    return render_template("/info5.html")

@auth.route('/info6')
def info6():
    return render_template("/info6.html")

@auth.route('/info7')
def info7():
    return render_template("/info7.html")

@auth.route('/info8')
def info8():
    return render_template("/info8.html")

@auth.route('/info9')
def info9():
    return render_template("/info9.html")

@auth.route('/info10')
def info10():
    return render_template("/info10.html")

@auth.route('/info11')
def info11():
    return render_template("/info11.html")

@auth.route('/Form',methods=['GET', 'POST'])
def form():
    data=request.form
    print(data)
    return render_template("Form.html")

@auth.route('/index',methods=['GET', 'POST'])
def index():
    data=request.form
    print(data)
    return render_template("/index.html")