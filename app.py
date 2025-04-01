from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Function to generate a random adjective
def get_random_adjective():
    adjectives = ["gentle", "soft", "mighty", "brave", "kind", "brilliant"]
    return random.choice(adjectives)

# Function to generate a random noun
def get_random_noun():
    nouns = ["star", "cloud", "mountain", "river", "sky", "ocean"]
    return random.choice(nouns)

@app.route('/')
def home():
    return render_template('index.html')  # This renders the HTML file

@app.route('/generate', methods=['POST'])
def generate_poem():
    data = request.get_json()  # Get the JSON sent from the frontend
    name = data.get('name', '')  # Get the name, default to empty string if not provided

    # Check if the name is missing
    if not name:
        return jsonify({"error": "Name is required"}), 400  # Return an error message with 400 status code

    # Generate a poem with random words
    adj1 = get_random_adjective()
    adj2 = get_random_adjective()
    noun1 = get_random_noun()
    noun2 = get_random_noun()

    poem = f"""
    {name}
    {adj1} and {adj2} like {name}
    {adj1} like {noun1}
    Breathing {name} into the world around
    {name}
    A world of {noun1} and {noun2}
    """

    return jsonify({"poem": poem})

if __name__ == '__main__':
    app.run(debug=True)
