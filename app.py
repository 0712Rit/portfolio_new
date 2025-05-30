
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/experience')
def experience():
    return render_template("experience.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/certifications')
def certifications():
    return render_template("certifications.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
