# Reddit flair detection

Hello, I am Himanshu Garg, a B. tech undergrad @ IIIT-D, majors in CSE.

Here, i am presenting a simple website which can take URL of any submission of Reddit/India and
suggest us the best suited Flair for the post using NLP. The website has been hosted on heroku for ease of use.

URL of the website - https://flairofreddit.herokuapp.com

# HOW to use ?

Website main page looks something like the below image.

<img width="1440" alt="home page of the website" src="https://user-images.githubusercontent.com/43913398/61592756-fc9c9180-abf4-11e9-8090-03d457c58d94.png">


1. In the URL box, Just enter the Submission URL, of which you want the most appropriate flair.
2. Tap on submit button.

<Strong> Voila!!! </Strong>  You will have the most appropriated FLAIR (tag) displayed in the Blue box.

<Strong> NOTE : </Strong> If it displays the message "check URL..." --> means the entered URL is <Strong> NOT </Strong> correct.


# Technology Stack ...

1. PYTHON is the man programming language that this web app is built on. All the NLP related word and backend of the website (FLASK) is based on python.

2. A little Cascading style sheets (CSS) and bootstrap has been used for the frontend.

# How to install it on your PC's

Just follow the below steps in order to run this web app offline on your computer.

1. Clone the repository on the system.
2. Open the terminal and go to the destination of the cloned file.
3. Type "cd website" in the terminal.
4. Enter "virtualenv venv"
5. Enter "source venv/bin/activate"
6. Enter "pip install -r requirements.txt"
7. Run "python app.py" from your terminal.

Here you go, the application is running on your terminal. <br>
Just open the displayed URL (on terminal) on your web browser.
