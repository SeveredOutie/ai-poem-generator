import requests
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Helper function to get a random word
def get_random_word(part_of_speech="n"):
    url = f"https://random-word-api.herokuapp.com/word?number=1&partOfSpeech={part_of_speech}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]  # Returns the first word from the list
    else:
        return None  # If the API fails

# Logic for generating the poem
def generate_poem_logic(name):
    adjective1 = get_random_word("adjective")  # Fetch a random adjective
    adjective2 = get_random_word("adjective")  # Fetch another random adjective
    noun1 = get_random_word("noun")  # Fetch a random noun
    noun2 = get_random_word("noun")  # Fetch another random noun

    if None in [adjective1, adjective2, noun1, noun2]:  # In case the API fails
        return "Error: Unable to generate words."

    # Generate a simple poem using the random words
    poem = f"The {adjective1} {noun1} and the {adjective2} {noun2},\n" \
           f"Where {name} finds peace, under the moon's soft glow."

    return poem

@app.route('/generate', methods=['POST'])
def generate_poem():
    data = request.get_json()  # Get the data from the request
    name = data.get('name')  # Extract the name from the JSON payload

    if name:
        poem = generate_poem_logic(name)  # Call the poem generation logic
        return jsonify({'poem': poem})  # Return the poem as JSON response
    else:
        return jsonify({'error': 'No name provided'}), 400  # Handle errors

if __name__ == "__main__":
    app.run(debug=True)
