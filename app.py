import pyrebase
import json
import pandas as pd
from mlscript import calculate_depression_type
from gradings import grading
from flask import Flask, session, render_template, request, redirect
app = Flask(__name__, template_folder='templates')
app.secret_key = 'your_secret_key'
config = {
		'apiKey': "AIzaSyClvISIw6z9UJ6CxCynV2xT2ndCcz1b_wE",
		'authDomain': "depressiondetector-3df8b.firebaseapp.com",
		'projectId': "depressiondetector-3df8b",
		'storageBucket': "depressiondetector-3df8b.appspot.com",
		'messagingSenderId': "109601623434",
		'appId': "1:109601623434:web:edf06075a007b8c23dcc73",
		'measurementId': "G-WHCEWV954P",
		'databaseURL': "https://depressiondetector-3df8b-default-rtdb.firebaseio.com/"
	}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
app.secret_key = 'mysecretkey'


person = {"is_logged_in": False, "name": "", "email": "", "uid": ""}
#info = auth.get_account_info(user['userid'])
#print(info)

# auth.send_email_verification(user['idToken'])
# auth.send_password_reset_email(email)

@app.route('/resetPass', methods = ['POST', 'GET'])
def index1():
        if 'user' in session:
            return render_template("profiling.html")
        if request.method == 'POST':
             if 'reset' in request.form:
                  email = request.form.get('email')
                  try:   
                    auth.send_password_reset_email(email)
                    return 'Password reset email sent successfully'
                  except:
                       return 'error occured'
        return render_template('resetpassword.html')

@app.route('/', methods=['POST', 'GET'])
def index():
    if 'user' in session:
        return render_template("profiling.html")
    
    if request.method == 'POST':
        if 'login' in request.form:
            email = request.form.get('email')
            password = request.form.get("password")
            
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                session['user'] = email
                return redirect('/')
            except Exception as e:
                error_message = 'Failed to login: {}'.format(str(e))
                return render_template('index.html', error_message=error_message)

        elif 'signup' in request.form:
            result = request.form           #Get the data submitted
            email = result["email"]
            password = result["pass"]
            name = result["name"]
            print(email,password,name)
            try:
                #Try creating the user account using the provided data
                auth.create_user_with_email_and_password(email, password)
                print("successful")
                #Login the user
                user = auth.sign_in_with_email_and_password(email, password)
                #Add data to global person
                global person
                person["is_logged_in"] = True
                person["email"] = user["email"]
                person["uid"] = user["localId"]
                person["name"] = name
                #Append data to the firebase realtime database
                usr_data = {"Email": email, "Name": name, "ID": password}
                db.child("Users").push(usr_data)
                #Go to welcome page
                return redirect('/welcome')
            except Exception as e:
                print(e)
                return redirect('/')
        
    return render_template('index.html')


@app.route("/welcome", methods = ["GET", "POST"])
def welcome():   
    if request.method == "POST":
        age = request.form.get('age')
        gender = request.form.get('gender')
        occupation = request.form.get('occupation')
        additionalFields = request.form.get('additionalFields')
        
        if not age or not gender or not occupation:
            return 'Form fields are required.'
        
        available_age_groups = ['13-18', '19-25', '26-35']
        available_genders = ['male', 'female', 'others']
        available_occupations = ['student', 'working', 'unemployed']
        if age not in available_age_groups or gender not in available_genders or occupation not in available_occupations:
            return 'Invalid form fields.'
        if occupation == 'student':
            study_location = request.form.get('studyLocation')
            file = 'causeassessment' + study_location + '.html'
            return render_template(file)

        elif occupation == 'working':
            employment_type = request.form.get('employmentType')
            file = employment_type + '.html'
            return render_template(file)
        elif occupation == 'unemployed':
            return render_template('causeunemployed.html')
        
        # Process the form data further
        
        # print(age, gender, occupation, study_location, employment_type, unemployment_duration, additionalFields)
            
        return redirect('/')
    else:
           return redirect('/')

@app.route("/cause", methods=["GET", "POST"])
def cause():
    if request.method == "POST":
        q1 = float(request.form.get('question1'))
        q2 = float(request.form.get('question2'))
        q3 = float(request.form.get('question3'))
        q4 = float(request.form.get('question4'))
        q5 = float(request.form.get('question5'))
        q6 = float(request.form.get('question6'))
        data_dict1 = {
            'Physical Illness': q1,
            'Psychological stressors': q2,
            'Personality': q3,
            'Lost of interest': q4,
            'Gender': q5,
            'Change in energy levels': q6
        }
        print(data_dict1)
        session['data_dict1'] = data_dict1
        data_json = json.dumps(data_dict1)
        print('hello')
        return render_template("effectstudent.html", data_json=data_json)
        
    return 'error'
    
@app.route("/result", methods=["GET", "POST"])
def result():
     if request.method =="POST":
        q7 = float(request.form.get('question7'))
        q8 = float(request.form.get('question8'))
        q9 = float(request.form.get('question9'))
        q10 = float(request.form.get('question10'))
        q11 = float(request.form.get('question11'))
        q12 = float(request.form.get('question12'))   
        data_dict2 = {
            'Genetic': q7,
            'Feeling of worthlessness': q8,
            'Sleeping sickness': q9,
            'Hallucinations': q10,
            'Seasonal changes': q11,
            'Harmonal changes': q12
        }
        data_dict1 = session.get('data_dict1', {})

        final_dict = {**data_dict1, **data_dict2}
        df = pd.DataFrame([final_dict])
        df = df.apply(calculate_depression_type, axis=1)
        pd.set_option('display.max_rows', None)  # To show all rows
        pd.set_option('display.max_columns', None)
        print(final_dict)
        print(df)
        a = float(df.iat[0,10])
        b = float(df.iat[0,11])
        c = float(df.iat[0,12])
        d = float(df.iat[0,13])
        type = df.iat[0,14]
        prediction_data = pd.DataFrame({'Seasonal changes': [a],
                                    'Harmonal changes': [b],
                                    'Score': [c],
                                    'Score2': [d]})
        result = grading(prediction_data)
        res = round(result[0])
        if res==0:
            resulttxt= 'No chances of Depression'
        elif res ==1:
             resulttxt = 'Grade A - `Mild Depression`'
        elif res==2:
             resulttxt ='Grade B - `Moderate Depression, Pyschologist consultancy recommended`'
        elif res==3:
             resulttxt ='Grade C -`Severe Depression, Clinical/Professional diagnoses recommended`'

        print(result)
        print(res)
        print(a,b,c,d,sep=" ")

        return render_template("result.html", depression_type=resulttxt, depression_grade=type)
     else:
          return redirect("/cause")

@app.route('/logout')
def logout():
	session.pop('user')
	return redirect('/')

def hello_world():    
	return render_template('index.html')

@app.route('/login')
def hellop():
	return "hello"

if __name__ == '__main__':

	app.run()