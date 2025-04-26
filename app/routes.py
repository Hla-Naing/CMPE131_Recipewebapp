from app import myapp_obj

@myapp_obj.route("/")
def home():
    return render_template('home.html')
#displays option to log in at top and list of recipes

@myapp_obj.route("/login")
def login():
    return render_template('login.html')
#allows for entry of username, email and password

@myapp_obj.route("/register")
def register():
    return render_template('register.html')
#same format as login page but for first time user

@myapp_obj.route("/recipe/<username>/<int:recipeid>")
def recipe():
    return render_template('viewrecipe.html')
#allows you to view one specific recipe, (later on) rate, save, comment

@myapp_obj.route("/recipe/new")
def newrecipe():
    return render_template('createrecipe.html')
#opens empty recipe to fill in ingredients, directions, etc

@myapp_obj.route("/recipe/<username>/<int:recipeid>/edit")
def editrecipe():
    return render_template('editrecipe.html')
#opens user's recipe to edit ingredients, directions, etc

@myapp_obj.route("/profile/<username>")
def viewprofile():
    return render_template('viewprofile.html')
#allows you to view a user's profile and their list of recipes

@myapp_obj.route("/profile/edit")
def editprofile():
    return render_template('editprofile.html')
#opens current user's DISPLAYED profile data to be changed

@myapp_obj.route("/account")
def account():
    return render_template('account.html')
#opens current user's username, email and password to view or edit
