from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize global variables for the game state
current_word = ''
display_word = ''
guessed_letters = []
attempts = 6
score = 0

def get_clue(word):
    clues = {
        "avatar": "Hero: Sam Worthington, Director: James Cameron.",
        "jalsa": "Hero: Pawan Kalyan, Director: Trivikram Srinivas.",
        "geetha govindam": "Hero: Vijay Devarakonda, Director: Parasuram Petla.",
        "sye": "Hero: Nithin, Director: S. S. Rajamouli.",
        "titanic": "Hero: Leonardo DiCaprio, Director: James Cameron.",
        "jumanji": "Hero: Dwayne Johnson, Director: Jake Kasdan.",
        "maari": "Hero: Dhanush, Director: Balaji Mohan.",
        "vakeel saab": "Hero: Pawan Kalyan, Director: Venu Sriram.",
        "jathi ratnalu": "Hero: Naveen Polishetty, Director: KV Anudeep.",
        "raja rani": "Hero: Arya, Director: Atlee.",
        "rrr": "Hero: N. T. Rama Rao Jr., Ram Charan, Director: S. S. Rajamouli.",
        "pushpa": "Hero: Allu Arjun, Director: Sukumar.",
        "mahanati": "Heroine: Keerthy Suresh, Director: Nag Ashwin.",
        "eega": "Hero: Nani, Director: S. S. Rajamouli.",
        "kgf": "Hero: Yash, Director: Prashanth Neel.",
        "fidaa": "Hero: Varun Tej, Director: Sekhar Kammula.",
        "magadheera": "Hero: Ram Charan, Director: S. S. Rajamouli.",
        "baahubali": "Hero: Prabhas, Director: S. S. Rajamouli.",
        "gundamma katha": "Hero: Akkineni Nageswara Rao, Director: Kamalakar Rao.",
        "mayabazar": "Hero: NTR, Director: Kadiri Venkata Reddy."

    }
    return clues.get(word, "No clue available.")

def choose_word():
    words = ["avatar", "jalsa", "geetha govindam", "sye", "titanic", "jumanji", "maari",
             "vakeel saab", "jathi ratnalu", "raja rani", "rrr", "pushpa",
             "mahanati", "eega", "kgf", "fidaa", "magadheera", "baahubali",
             "gundamma katha", "mayabazar"]
    return random.choice(words)

def initialize_game():
    global current_word, display_word, guessed_letters, attempts, score
    current_word = choose_word()
    display_word = ' '.join(['_' if char != ' ' else ' ' for char in current_word])
    guessed_letters = []
    attempts = 6
    score = 0

@app.route('/')
def index():
    initialize_game()
    return render_template('index.html', clue=get_clue(current_word), display_word=display_word, score=score)

@app.route('/guess', methods=['POST'])
def guess():
    global display_word, guessed_letters, attempts, score

    data = request.json
    letter = data.get('letter', '').lower()

    if len(letter) != 1 or not letter.isalpha():
        return jsonify({'error': 'Invalid input'}), 400

    if letter in guessed_letters:
        return jsonify({'error': 'Letter already guessed'}), 400

    guessed_letters.append(letter)

    if letter in current_word:
        display_word = ''.join([char if char in guessed_letters or char == ' ' else '_' for char in current_word])
        score += 10
    else:
        attempts -= 1
        score -= 5

    if '_' not in display_word:
        return jsonify({'display_word': display_word, 'clue': get_clue(current_word), 'score': score,
                        'message': 'Congratulations! You guessed the word!', 'attempts': attempts})

    if attempts == 0:
        return jsonify({'display_word': display_word, 'clue': get_clue(current_word), 'score': score,
                        'message': f'Sorry, you ran out of attempts. The word was: {current_word}', 'attempts': attempts})

    return jsonify({'display_word': display_word, 'clue': get_clue(current_word), 'score': score, 'attempts': attempts})

@app.route('/new_game')
def new_game():
    initialize_game()
    return jsonify({'clue': get_clue(current_word), 'display_word': display_word, 'score': score, 'attempts': attempts})

if __name__ == '__main__':
    app.run(debug=True)
