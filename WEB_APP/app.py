from flask import Flask, render_template

# Create flask app
app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
