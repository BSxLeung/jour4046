# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
from static import *

try:
    os.chdir(os.path.join(os.getcwd(), '..\\..\..\..\Desktop\JOUR LAB\flaskapp'))
    print(os.getcwd())
except:
    pass

app = Flask(__name__)

link = "https://api.airtable.com/v0/appSIXcmOX4r4NuzY/"

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
# app.config['SECRET_KEY'] = "lkkajdghdadkglajkgah"


# @login_manager.user_loader
# def load_user(user_id):
#     return User(user_id)


# class User(UserMixin):
#     def __init__(self, id):
#         self.id = id


# root
@app.route('/')
# @login_required
def home():
    user = {"name": "Benix"}
    return render_template('myhome.html', title="Benix's Page", user=user)

# show all the user
@app.route("/list_users")
# @login_required
def table():
    params = (
    )
    dataset = REST(action="retriveall", link=link +
                   "flasktable").exec(params=params)
    # print(dataset)
    return render_template('table.html', entries=dataset, title="Benix's Table Page")

# show user form
@app.route("/user")
# @login_required
def user():
    message = 'Please enter user information.'
    return render_template('userform.html', message=message)

# action: add user -> return home page
@app.route("/adduser", methods=['POST'])
# @login_required
def adduser():
    fname = request.form['fname']
    lname = request.form['lname']
    student_id = request.form['student_id']
    date_of_birth = request.form['date_of_birth']
    pwd = request.form['pwd']
    pwd = pwd.encode('UTF-8')
    # Hash a password for the first time, with a randomly-generated salt
    hashed = bcrypt.hashpw(pwd, bcrypt.gensalt())
    pwd = hashed.decode('UTF-8')
    mydict = {
        "fname": fname,
        "lname": lname,
        "student_id": student_id,
        "date_of_birth": date_of_birth,
        'pwd': pwd
    }
    data = {"fields": mydict}
    message = dataset = REST(action="add", link=link +
                             "flasktable").exec(dataset=data)
    return render_template('myhome.html', message=message)

# action: get user -> update user -> return home page
@app.route("/updateuser", methods=['POST'])
# @login_required
def updateuser():

    data = request.form
    record_id = data['record_id']
    fields = REST(action="retriveone", link=link +
                  "flasktable").exec(record_id=record_id)
    fields["fname"] = data['fname']
    fields["lname"] = data['lname']
    fields["student_id"] = data['student_id']
    fields["date_of_birth"] = data['date_of_birth']
    del fields["record_id"]
    del fields["full_name"]
    data = {
        "records": [
            {
                "id": record_id,
                "fields": fields
            }
        ]
    }
    message = REST(action="update", link=link+"flasktable").exec(dataset=data)
    return render_template('myhome.html', message=message)

# action: delete user -> return home page
@app.route("/deleteuser", methods=['POST'])
# @login_required
def deleteuser():
    data = request.form
    record_id = data['record_id']
    message = fields = REST(action="delete", link=link +
                            "flasktable").exec(record_id=record_id)
    return render_template('myhome.html', message=message)

# assignment_three
@app.route("/assignment_three", methods=['GET'])
# @login_required
def assignment_three():
    return render_template('assignment_three.html')

# assignment_four
@app.route("/assignment_four", methods=['GET'])
# @login_required
def assignment_four():
    return render_template('assignment_four.html')


# footer
@app.route("/footer", methods=['GET'])
# @login_required
def footer():
    return render_template('layout/footer.html')


# header
@app.route("/navbar")
# @login_required
def header():
    return render_template('layout/navbar.html')


# @app.route("/process", methods=['POST'])
# def process():
#     student_id = request.form['student_id']
#     password = request.form['password']
#     password = password.encode('UTF-8')
#     hashed = ''
#     user = ''
#     # filter = 'IF(AND({UserName}="'+username+'",{Pwd}="'+password+'"), 1, 0)'
#     filter = 'IF(({student_id}="'+student_id+'"), 1, 0)'

#     params = (
#         ('view', 'Grid view'),
#         ('filterByFormula', filter),
#     )

#     dataset = []
#     r = requests.session()
#     r = REST(action="retriveall", link=link+"flasktable").exec(params=params)

#     dict = r.json()

#     for i in dict['records']:
#         dict = i['fields']
#         dataset.append(dict)
#     for item in dataset:
#         user = item.get('student_id')
#         if user != None:
#             hashed = item.get('Pwd')
#             fname = item.get('fname')
#             hashed = hashed.encode('UTF-8')
#         else:
#             message = 'wrong password!'
#             return render_template('login.html', message=message)

#     if student_id == user and bcrypt.checkpw(password, hashed):
#         login_user(User(1))
#         message = "Your login has been granted."
#         return render_template('myhome.html', message=message)
#     message = 'wrong password!'
#     return render_template('login.html', message=message)


# @app.errorhandler(500)
# def internal_error(error):
#     message = 'wrong password!'
#     return render_template('login.html', message=message), 500


# @app.route('/logout/')
# @login_required
# def logout():
#     logout_user()
#     message = 'Thanks for logging out.'
#     return render_template('login.html', message=message)
# @app.route("/login")
# def login():
#     message = 'Please login in first.'
#     return render_template('login.html', message=message)
# entry point
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9003, app)
