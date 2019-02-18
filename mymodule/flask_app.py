from flask import Flask, render_template, request, redirect
import mymodule.twitter_map
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("front_look.html")

@app.route("/register", methods=["POST"])
def register():
    account = request.form.get("account")
    mymodule.twitter_map.main(account)
    return render_template("Map_{}.html".format(account))


if __name__ == "__main__":
    app.run(debug=True)


