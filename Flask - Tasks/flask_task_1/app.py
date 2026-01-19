from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    user_name = request.args.get('name')
    
    if user_name:
        # Convert to upper case and display
        return f"<h1>Your name in uppercase: {user_name.upper()}</h1>"
    else:
        # Instructions if no name is provided
        return "Please add your name to the URL like this: <b>/?name=yourname</b>"
    

# This counts the letters in the name
@app.route('/count')
def count_letters():
    user_name = request.args.get('name')
    
    if user_name:
        length = len(user_name)
        return f"<h1>The name '{user_name}' has {length} letters.</h1>"
    return "Please add <b>?name=yourname</b> to the URL"

if __name__ == '__main__':
    app.run(debug=True)