from flask import Flask,render_template,request,flash,redirect,url_for,session
from models import User,Category,Recipe

app = Flask(__name__)
app.secret_key = 'SECRET'
USERS={}
def register(name, email, password, confirm_password):
    """ This function handles user registration"""
    if name and email and password and confirm_password:
        if password == confirm_password:
            USERS[email] = User(name, email, password)
            return True
        return False   
    return False

def login(email, password):
    """ Handles user login """
    if email and password:
        if USERS.get(email):
            if USERS[email].password == password:
                return True
            return False
        return False  
    return False

@app.route('/')
def main():
    """ Handles the home route """
    # if session.get('email'):
    #     return redirect(url_for('category'))
    # else:
    return render_template('homePage.html')

@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
    """ Handles the sign_in route """
    if request.method == 'POST':
        return_value = login(request.form['email'], request.form['password'])
        if return_value == True:
            session['email'] = request.form['email']
            return redirect(url_for('category'))
            flash ('log in successful', 'warning')
        return redirect(url_for('sign_in'))
        flash ('incorrect username or password', 'warning')
    return render_template('Signin.html')

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
    """ Handles the sign_up route """
    if request.method == 'POST':
        return_value = register(request.form['name'], request.form['email'], request.form['password']
                          , request.form['confirm_password'])
        if return_value == True:
            flash("Sign up successful")
            return redirect(url_for('sign_in'))
    return render_template('Signup.html')

# # def login_required(func):
# #     """ Decorator function to ensure some routes are only accessed by logged in users """
# #     @wraps(func)
# #     def decorated_function(*args, **kwargs):
# #         """ Modified descriprition of the decorated function """
# #         if not session.get('username'):
# #             flash('Login to continue', 'warning')
# #             return redirect(url_for('sign_in', next=request.url))
# #         return func(*args, **kwargs)
# #     return decorated_function

@app.route('/category', methods=['GET', 'POST'])
def category():
    """ Handles displaying categories """
    return render_template('category.html', categories=USERS[session['email']].categories)

@app.route('/create_category', methods=['GET', 'POST'])
# @login_required
def create_category():
    """ Handles new category creation requests """
    if request.method == 'POST':
        # USERS[session['email']] means a logged in user object
        return_value = USERS[session['email']].add_category(request.form['title'])
        if return_value == True:
            flash("category added")
        else:
            flash("category not added")
        return redirect(url_for('category'))
    return render_template('category.html')


if __name__ == '__main__':
    app.run(debug= True)
