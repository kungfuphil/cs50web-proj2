"""Project 2: Flack"""
import os

from flask import Flask, render_template, session, request, url_for, redirect
from flask_socketio import SocketIO, emit
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
Session(app)


@app.route("/")
def index():
    """
    1. Check to see if the user exists. If not then have the user type in a display name.
    """
    print("Inside index()")
    if "display_name" not in session:
        return render_template("create_account.html")

    return f"Hello, {session['display_name']}"

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    "Creates a new account"

    if request.method == "GET":
        return render_template("create_account.html")
    else:
        display_name = request.form.get("displayName")
        session["display_name"] = display_name
        return redirect(url_for("index"))

if __name__ == "__main__":
    socketio.run(app, debug=True)

"""Requirements

Channel Creation: Any user should be able to create a new channel, so long as its name doesn’t conflict with the name of an existing channel.
Channel List: Users should be able to see a list of all current channels, and selecting one should allow the user to view the channel. We leave it to you to decide how to display such a list.
Messages View: Once a channel is selected, the user should see any messages that have already been sent in that channel, up to a maximum of 100 messages. Your app should only store the 100 most recent messages per channel in server-side memory.
Sending Messages: Once in a channel, users should be able to send text messages to others the channel. When a user sends a message, their display name and the timestamp of the message should be associated with the message. All users in the channel should then see the new message (with display name and timestamp) appear on their channel page. Sending and receiving messages should NOT require reloading the page.
Remembering the Channel: If a user is on a channel page, closes the web browser window, and goes back to your web application, your application should remember what channel the user was on previously and take the user back to that channel.
Personal Touch: Add at least one additional feature to your chat application of your choosing! Feel free to be creative, but if you’re looking for ideas, possibilities include: supporting deleting one’s own messages, supporting use attachments (file uploads) as messages, or supporting private messaging between two users.
In README.md, include a short writeup describing your project, what’s contained in each file, and (optionally) any other additional information the staff should know about your project. Also, include a description of your personal touch and what you chose to add to the project.
If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!
Beyond these requirements, the design, look, and feel of the website are up to you! You’re also welcome to add additional features to your website, so long as you meet the requirements laid out in the above specification!

Hints
You shouldn’t need to use a database for this assignment. However, you should feel free to store any data you need in memory in your Flask application, as via using one or more global variables defined in application.py.
You will likely find that local storage will prove helpful for storing data client-side that will be saved across browser sessions."""