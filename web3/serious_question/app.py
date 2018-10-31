from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bike():
  if request.method == "GET":
    return render_template("bike_rental.html")
  elif request.method == "POST":
    form = request.form
    model = form["model"]
    fee = form["fee"]
    image = form["image"]
    year = form["year"]

    print(model, fee, image, year)
    return "Gotcha"


if __name__ == '__main__':
  app.run(debug=True)