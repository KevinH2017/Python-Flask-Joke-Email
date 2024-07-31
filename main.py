from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
import dadjokes

app = Flask(__name__)

# Sets configuration for app
app.config.update(dict(
    SECRET_KEY = os.urandom(12),
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{app.root_path}/instance/email.db",
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = 587,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = os.getenv("EMAIL_ADDRESS"),
    MAIL_PASSWORD = os.getenv("PASSWORD"),
    MAIL_USE_TLS = True
))

mail = Mail(app)

def send_email(rec_email):
    """Sends email as txt and html files"""
    joke = dadjokes.joke()                                  # Gets a joke from dadjokes.py

    msg = Message("Here Have A Joke!",
                    sender=app.config["MAIL_USERNAME"], 
                    recipients=[rec_email])                 # Make sure to send recipients as a list


    msg.body = render_template("joke.txt")                  # text file to contain the body
    msg.html = render_template("joke.html", joke=joke)      # html file to contain the elements, html has priority over body

    mail.send(msg)                                          # Sends msg to recipient email


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/success', methods=["POST"])  
def verify():  
    """Sends email with verify link"""
    email = request.form["email"]
    send_email(email)

    return render_template('success.html')
 
if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True, port=5001)        # Only runs on local 127.0.0.1 network
        # app.run(host="0.0.0.0")         # Opens webpage to entire network (Uses host IPv4 address)