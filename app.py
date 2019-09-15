from flask import Flask, render_template, request, session
app = Flask(__name__)
@app.route("/<string:name>")
def customHello(name):
    return ""


@app.route("/")
def index():
    return render_template("index.html", headline="Hellooooooo")


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/notes", methods=["GET,POST"])
def notes():
    if session.get("notess") == []:
        note = request.form.get("note")
        session["notes"].append(note)

    if request.method == "POST":
        note = request.form.get("notezzz")
        session["notes"].append(note)

    return render_template("route.html", notes=session["notes"])
