from flask import Flask,render_template,request,flash,redirect,url_for,session
from models import User,Category,Recipe
from functools import wraps

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

def login_required(func):
    """ Decorator function to ensure some routes are only accessed by logged in users """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """ Modified descriprition of the decorated function """
        if not session.get('email'):
            flash('Login to continue', 'warning')
            return redirect(url_for('sign_in', next=request.url))
        return func(*args, **kwargs)
    return decorated_function

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

@app.route('/update_category/<title>', methods=['GET', 'POST'])
@login_required
def update_category(title):
    """ Handles request to update a category """
    session['category_title'] = title
    if request.method == 'POST':
        return_value = USERS[session['email']].edit_category(session['category_title'],
                                                          request.form['title'])
        if return_value == True:
            flash("category updated")
        return redirect(url_for('category'))
    return render_template('updatecategory.html')

@app.route('/delete_category/<title>',methods=['GET', 'POST'])
@login_required
def delete_category(title):
    """ Handles request to delete a category"""
    return_value = USERS[session['email']].delete_category(title)
    if return_value == True:
        flash("category deleted")
    return redirect(url_for('category'))

@app.route('/view_recipes/<category_title>', methods=['GET', 'POST'])
@login_required
def view_recipes(category_title):
    """ Handles displaying recipes """
    session['current_category_title'] = category_title
    return render_template('recipes.html', cat="category_title", recipes=USERS[session['email']].categories[category_title].recipes)

@app.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    """ Handles new recipe creation requests """
    if request.method == 'POST':
        return_value = USERS[session['email']].categories[session['current_category_title']].add_recipe(
            request.form['title'],request.form["description"])
        if return_value == True:
            flash("recipe added successfully")
        return redirect(url_for('view_recipes', category_title=session['current_category_title']))
    return render_template('recipes.html', recipes=USERS[session['email']].category[session['current_category_title']].recipess)

# @app.route('/update_recipe/<description>',methods=['GET', 'POST'])
# @login_required
# def update_recipe(description):
#     """ Handles request to update a recipe """
#     session['description'] = description
#     if request.method == 'POST':
#         description_result = (USERS[session['email']].categories[session['current_category_title']].
#                       update_description(session['description'], request.form['description']))
#         status_result = (USERS[session['email']].categories[session['current_category_title']].
#                          update_status(session['description'], request.form['status']))
#         if des_result == True or status_result == True:
#             flash('Recipe updated')
#         return redirect(url_for('view_recipes', category_title=session['current_category_title']))
#     return render_template('recipeupdate.html', recipe=USERS[session['username']]
#                            .category[session['current_category_title']].recipes[description],
#                            recipes=USERS[session['username']].
#                            categories[session['current_category_title']].recipes)
# @app.route('/logout')
# @login_required
# def logout():
#     """ logs out users """
#     session.pop('email')
#     flash('You have logged out')
#     return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug= True)
