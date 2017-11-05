from flask import request
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
User = {}
Recipes = {}


@app.route("/")
def main():
    return render_template("homePage.html")


@app.route("/Signup", methods=['GET', 'POST'])
def Signup():
    if request.method == 'POST':

        email = request.form['email']
        name = request.form['fname']
        password = request.form['psw']

        if email and password:
            User[email] = password
            return redirect(url_for('login'))
    return render_template("Signup.html")


@app.route("/login",  methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] not in User.keys() or request.form['psw'] not in User.values():
            error = 'incorrect username or password'
        else:
            return redirect(url_for('addcategory'))
    return render_template("Signin.html", error=error)


@app.route("/addcategory", methods=['GET', 'POST'])
def addcategory():
    if request.method == 'Post':
        title = request.form['Title']
        item1 = request.form['item1']
        item2 = request.form['item2']
        item3 = request.form['item3']
        item4 = request.form['item4']
        if title and item1:
            Recipes['title'] = title
            Recipes['item1'] = item1
            Recipes['item2'] = item2
            Recipes['item3'] = item3
            Recipes['item4'] = item4
            return redirect(url_for('recipes'))

    return render_template("category.html")


@app.route("/recipes")
def recipes():
    return render_template('view_recipes.html', title=Recipes['title'], item1=Recipes['item1'],
                           item2=Recipes['item2'], item3=Recipes['item3'], item4=Recipes['item4'])


if __name__ == "__main__":
    app.run(debug=True)
