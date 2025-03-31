from flask import Flask, render_template, request, jsonify
import random
import pronouncing

app = Flask(__name__)

# Get a random word from a predefined list of common words
COMMON_WORDS = [
    "happy", "sad", "bright", "dark", "lovely", "angry", "beautiful", "cloud", "mountain", "ocean",
    "sky", "heart", "dream", "river", "rain", "snow", "flower", "bird", "star", "night", "day"
]

# Function to get a rhyming word for the name
def get_rhyming_word(word):
    rhyme_list = pronouncing.rhymes(word)
    if rhyme_list:
        return random.choice(rhyme_list)
    return None  # If no rhyme is found, return None

# Function to get a random word from COMMON_WORDS
def get_random_word(word_type):
    if word_type == "a":  # Adjective
        return random.choice([word for word in COMMON_WORDS if word not in ["bird", "cloud", "river", "star"]])
    elif word_type == "n":  # Noun
        return random.choice([word for word in COMMON_WORDS if word not in ["happy", "bright", "dark", "lovely", "sad"]])
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_poem():
    name = request.form['name']
    
    # Generate random words to fill the blanks
    adj1 = get_random_word("a")
    adj2 = get_random_word("a")
    adj_rhyme = get_rhyming_word(name) or get_random_word("a")
    noun_rhyme = get_rhyming_word(name) or get_random_word("n")
    noun1 = get_random_word("n")
    noun2 = get_random_word("n")

    # Create the poem based on the name and random words
    poem = f"""
    {name}
    {adj1} and {adj2} like {adj_rhyme}
    {adj1} like {noun_rhyme}
    Breathing {name} into the world around
    {name}
    A world of {noun1} and {noun2}
    """
    
    return jsonify({'poem': poem})

if __name__ == '__main__':
    app.run(debug=True)
