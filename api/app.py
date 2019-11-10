from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/login",methods=["POST","GET"])
def home():
    if request.method == "POST":
        print((request.form['nm']))
        return redirect(url_for('about',name = request.form['nm']))
    elif request.method == "GET":
        return render_template("login.html")

    #render_template("login.html")
def about(name):
    return f"<h1>'Welcome to About Page' {name} <h1>"
app.add_url_rule('/about/<name>','about',about)

if __name__=="__main__":
    app.run(debug=True)