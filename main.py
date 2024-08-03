from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os, dadjokes, random

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY = os.urandom(12),
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = 587,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = os.getenv("EMAIL_ADDRESS"),
    MAIL_PASSWORD = os.getenv("PASSWORD"),
    MAIL_USE_TLS = True
))

mail = Mail(app)


def rand_images():
    """returns a random absolute URL of an image"""
    image_list = ["https://images.pexels.com/photos/2337789/pexels-photo-2337789.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "https://images.pexels.com/photos/1115680/pexels-photo-1115680.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "https://images.pexels.com/photos/1183434/pexels-photo-1183434.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "https://i.kym-cdn.com/entries/icons/original/000/014/959/Screenshot_116.png",
            "https://cdn.pixabay.com/photo/2014/03/24/13/43/cat-294120_960_720.png"
            ]
    
    image = random.choice(image_list)

    return image


def send_email(rec_email):
    """Sends email as txt and html files"""
    joke = dadjokes.joke()                                  # Gets a joke from dadjokes.py
    img_tag = rand_images()                                 # Gets a random image from rand_images()

    msg = Message("Here Have A Joke!",
                    sender=app.config["MAIL_USERNAME"], 
                    recipients=[rec_email])                 # Make sure to have recipients in a list


    # text file to contain the body, 
    # will display if html file is unable to load
    msg.body = render_template("joke.txt")                                      
    
    # html file to contain the elements and variables
    msg.html = render_template("joke.html", joke=joke, img_tag=img_tag)         

    mail.send(msg)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/success', methods=["POST"])  
def verify():  
    """Sends email with pun and image"""
    email = request.form["email"]
    send_email(email)

    return render_template('success.html')
 

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True, port=5001)        # Only runs on local 127.0.0.1 network
        # app.run(host="0.0.0.0")         # Opens webpage to entire network (Uses host IPv4 address)