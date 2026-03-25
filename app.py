import os
from flask import Flask, render_template

base_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, "templates"),
    static_folder=os.path.join(base_dir, "static"),
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/academy")
def academy():
    return render_template("academy.html")

@app.route("/ai-agent-services")
def agents():
    return render_template("agents.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
