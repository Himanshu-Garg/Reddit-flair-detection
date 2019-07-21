from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import praw
import pickle
import pandas as pd 

reddit = praw.Reddit(client_id='8COttBbmIJSb3w',
                     client_secret='-zZqO_s0SQ-kfgyk3Dt9Y8JUXAM',
                     username='himanshu_garg_',
                     password='qwertyqwerty',
                     user_agent='himanshu_garg_')

# loading model and vectorizer
loaded_model = pickle.load(open('model/SGDC.pickle','rb'))
vectorizer = pickle.load(open('model/SGDC_vector.pickle','rb'))



# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    
    @app.route("/", methods=['GET', 'POST'])
    def home():
        form = ReusableForm(request.form)
        
        print(form.errors)
        if request.method == 'POST':
            name=str(request.form['name'])
            #print(name)
            try:
                subreddit = reddit.submission(url=name) 
                #print(subreddit.title)  
                
                flair = loaded_model.predict(vectorizer.transform([subreddit.title]))

                flash(flair[0])       
            except:
            	flash(' check URL... ')
        
        return render_template('home.html', form=form)

if __name__ == "__main__":
    app.run()
