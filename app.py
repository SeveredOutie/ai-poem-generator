from flask import Flask, request, jsonify, render_template
import requests
import random

app = Flask(__name__)

# Function to get a random AI-generated word
import requests

def get_random_word(word_type):
    try:
        response = requests.get(f"https://random-word-api.herokuapp.com/word?number=1")
        if response.status_code == 200:
            return response.json()[0]
        else:
            return f"[{word_type}]"
    except:
        return f"[{word_type}]"

# Function to generate a poem with a random AI-generated word
def generate_poem_logic(name):
    adjective1 = get_random_word("adjective")
    adjective2 = get_random_word("adjective")
    verb = get_random_word("verb")
    plural_noun = get_random_word("noun")

    poem = f"""
    {name}, so {adjective1} and {adjective2},  
    I see {verb} from my view.  
    {name}, what ever shall you do?  
    Dream about {plural_noun} for tonight.
    """
    return poem

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate_poem():
    data = request.get_json()
    name = data.get("name", "Dreamer")  # Default name if none is provided
    poem = generate_poem_logic(name)
    return jsonify({"poem": poem})

if __name__ == "__main__":
    app.run(debug=True)
