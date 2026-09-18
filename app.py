from flask import Flask, render_template, request

app = Flask(__name__)

movies = {
    "action": [
        "Avengers",
        "Iron Man",
        "The Dark Knight"
    ],
    "comedy": [
        "Mr. Bean",
        "The Mask",
        "Home Alone"
    ],
    "science": [
        "Interstellar",
        "The Martian",
        "Gravity"
    ]
}

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":
        category = request.form["category"]
        recommendations = movies.get(category, [])

    return render_template(
        "index.html",
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)
