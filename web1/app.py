# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")  # "/" - homepage
# def homepage():
#     return "Welcome to C4E Web homepage, enjoy"

# @app.route("/hoa")
# def hello_hoa():
#     return "Hello everyone"

# @app.route("/praise/an")
# def praise_an():
#     return "Happy birthday An beo'"

# @app.route("/praise/<name>")
# def praise(name):
#     return name + " is awesome"

# @app.route("/add/<a>/<b>")        # @app.route("/add/<int:a>/<int:b>")
# def add(a,b):
#     s = int(a) + int(b)
#     return str(s)

# @app.route("/question")
# def show_question():
#     return render_template("question.html")


# if __name__ == "__main__":
#     app.run(debug=True)