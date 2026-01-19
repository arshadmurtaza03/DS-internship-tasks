from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Initialize variables 
    matches = []
    error = None
    regex_input = ""
    test_string = ""

    # Check if the user hit the 'Submit' button
    if request.method == 'POST':
        regex_input = request.form.get('regex')
        test_string = request.form.get('test_string')

        #if both fields have text
        if regex_input and test_string:
            try:
                # Use re.findall to get all matching strings
                matches = re.findall(regex_input, test_string)
            except re.error:
                # Catch errors 
                error = "Invalid Regex Pattern! Please check your syntax."

    return render_template('index.html', 
                           matches=matches, 
                           error=error, 
                           regex_input=regex_input, 
                           test_string=test_string)

if __name__ == '__main__':
    app.run(debug=True)