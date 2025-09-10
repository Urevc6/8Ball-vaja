from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/8ball", methods = ["POST"])
def ball():
    tmp = dict(request.form)
    vpr= tmp.get("vprašanje")
    moz=["Da", "Ne", "Mogoče", "Vprašaj kasneje"] 
    r=random.choice(moz)
    if "ljubezen" in vpr:
        r="Kupi raje GPU"
    elif "vikend" in vpr:
        r="TikTok all day"
    elif "denar" in vpr:
        r="Burek only"
    elif "profesor" in vpr:
        r="F speedrun"
    elif "!" in vpr:
        r="Ne kriči"
    return render_template("index.html", rezultat = r)

app.run(debug= True)