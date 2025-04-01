import random
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Helper function to fetch a random word from Datamuse API
def get_random_word(adjective):
    url = f"https://api.datamuse.com/words?rel_jjb={adjective}&max=1000"
    response = requests.get(url)
    words = response.json()
    if words:
        return random.choice(words)['word']
    return "random"

# Helper function to get a rhyming word using the Datamuse API
def get_rhyming_word(word):
    url = f"https://api.datamuse.com/words?rel_rhy={word}&max=10"
    response = requests.get(url)
    words = response.json()
    if words:
        return random.choice(words)['word']
    return word  # fallback to the original word if no rhymes are found

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_poem():
    name = request.form['name']

    # Generate random adjectives and nouns
    adj1 = get_random_word("adj")
    adj2 = get_random_word("adj")
    noun1 = get_rhyming_word(name) or get_random_word("n")
    noun2 = get_rhyming_word(name) or get_random_word("n")

    # Format poem
    poem = f"""
    {name}
    {adj1} and {adj2}
    {adj1} like {noun1}
    Breathing {name} into the world around
    {name}
    A world of {noun1} and {noun2}
    """

    return jsonify({"poem": poem})

if __name__ == '__main__':
    app.run(debug=True)
