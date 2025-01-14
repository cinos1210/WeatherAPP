from flask import Flask, render_template

app =Flask("Website")

@app.route("/home")
def home():
    return render_template("test.html")

@app.route("/About/")
def about():
    return render_template("about.html")

app.run(debug=True)