from flask import flask
app =Flask(_name_)
@app.route("/")
def hello():
return "Hello"
if __name__ == "__main__":
app.run(host="0.0.0.0",port=5000)
