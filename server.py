from flask import Flask

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return "Hi There"

if __name__ == "__main__":
    app.run(debug=True)