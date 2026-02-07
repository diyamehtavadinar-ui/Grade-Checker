from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def grade_checker():
    result = ""

    if request.method == "POST":
        try:
            a = int(request.form["marks"])

            if 100 >= a >= 90:
                result = "A+ Outstanding 🌟"
            elif 90>a >= 80:
                result = "A Excellent"
            elif  80>a >= 70:
                result = "B+ Very Good"
            elif  70>a >= 60:
                result = "B Good"
            elif  60>a >= 50:
                result = "C Average"
            elif  50>a >= 40:
                result = "D Pass"
            elif  0 <= a < 40:
                result = "F Fail"
            else:
                result = "Invalid input"

        except:
            result = "Please enter a valid number"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

