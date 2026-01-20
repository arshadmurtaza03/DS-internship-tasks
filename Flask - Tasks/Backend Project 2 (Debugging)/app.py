from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    # Check if the user has submitted the form
    if request.method == "POST":
        # Get the note from the form data
        note = request.form.get("note")
        
        # Only add the note if it's not empty
        if note:
            notes.append(note)

    # Render the homepage with the list of notes
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)