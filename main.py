from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")
    
@app.route("/tds")
def salvador():
    return "Hello, TDS"
    
if __name__ == "__main__":
    app.run(debug=True)