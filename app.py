from flask import Flask, render_template, url_for, redirect
#render template: kita dapat menyediakan template html di dalam project flask

app = Flask (__name__)
app.config["SECRET_KEY"] = "SetSecretKey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/redirect-about")
def coba_redirect_about():
    return redirect(url_for('about'))

@app.route("/redirect-contact")
def coba_redirect_contact():
    return redirect(url_for('contact'))

if __name__ == "__main__":
    app.run(debug=True)