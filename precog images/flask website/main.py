from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

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
        	name=request.form['name']
        	#print(name)
        
        if form.validate():
        # Save the comment here.
            flash('Hello ' + str(name))
            print("1")
        else:
            flash(' Error: Check URL... ')
        
        return render_template('home.html', form=form)

if __name__ == "__main__":
    app.run()