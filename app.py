from flask import Flask, request, jsonify, render_template
import requests
import random

app = Flask(__name__)

# Function to get a random AI-generated word
def get_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        if response.status_code == 200:
            return response.json()[0]  # Extract the word from the API response
        else:
            return "mystical"  # Default word if API fails
    except Exception as e:
        print("Error fetching random word:", e)
        return "mystical"

# Function to generate a poem with a random AI-generated word
def generate_poem_logic(name):
    adjective = get_random_word()
    poem = f"""
    Oh {name}, so {adjective} and bright,  
    Dancing like stars in the velvet night.  
    Your soul, a whisper, a delicate art,  
    A melody sung from the depths of the heart.  
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
