from flask import Flask, render_template, request, jsonify
import nltk
from nltk.corpus import cmudict

nltk.download('cmudict')
prondict = cmudict.dict()

def get_rhyming_word(word):
    word = word.lower()
    if word in prondict:
        phonemes = prondict[word][0][-2:]  # Get the last two phonemes
        rhyming_words = [w for w in prondict if prondict[w][0][-2:] == phonemes]
        return random.choice(rhyming_words) if rhyming_words else None
    return None
import random
from nltk.corpus import wordnet
import nltk

# Ensure NLTK data is downloaded
nltk.download('wordnet')

app = Flask(__name__)

def get_rhyming_word(word):
    """Fetch a rhyming word for the given input. Returns None if no rhymes are found."""
   rhyme_list = get_rhyming_word(word)  
    return random.choice(rhyme_list) if rhyme_list else None  # Return None if no rhymes are available

def get_random_word(pos):
    """Fetches a poetic word from WordNet for the given part of speech (adj/noun)."""
    words = []
    for synset in wordnet.all_synsets(pos):  # Filter by part of speech
        for lemma in synset.lemmas():
            word = lemma.name().replace("_", " ")  # Replace underscores in compound words
            words.append(word)

    return random.choice(words) if words else "light"  # Default to "light" if nothing is found

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_poem():
    name = request.json.get('name')

    # Get words dynamically
    adj1 = get_random_word("a")  # Adjective
    adj2 = get_random_word("a")  # Adjective
    adj3 = get_random_word("a")  # Adjective
    
    noun1 = get_rhyming_word(name) or get_random_word("n")  # Rhyme if possible, else noun
    noun2 = get_random_word("n")  # Noun
    noun3 = get_rhyming_word(name) or get_random_word("n")  # Rhyme if possible, else noun

    # Format the poem
    poem = f"""{name}
{adj1} and {adj2}
{adj3} like {noun1}
breathing {name} into the world around
{name}
a world of {noun2} and {noun3}"""

    return jsonify({"poem": poem})

if __name__ == '__main__':
    app.run(debug=True)
