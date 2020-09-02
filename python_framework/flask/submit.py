from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("input.html")

@app.route("/post",methods=["POST"])
def post():
    if(request.method == "GET"):
        return render_template("input.html")
    else:
	    value = request.form["input"]
	    msg = f"Welcome {value}!"
	    return msg

if __name__ == "__main__":
	app.run()