import random

# Add clues for each word with hero/heroine names and director names
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

def display_hangman(attempts):
    stages = [
        '''
           --------
           |      |
           |
           |
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        '''
    ]
    return stages[attempts]

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

def main():
    print("🎉 Welcome to the Exciting Hangman Game! 🎉")
    print("🎉 The Movie Mania - Test your Movie Knowledge Here! 🎉")
    player_name = input("🌟 What's your name? ")
    print(f"Hello, {player_name}! Get ready for a thrilling challenge.")

    while True:
        print("\n")
        rounds = input("How many rounds do you want to play? (1/3/5): ")
        if rounds not in ["1", "3", "5"]:
            print("⚠️ Please enter a valid number of rounds.")
            continue
        rounds = int(rounds)

        total_score = 0

        for round_num in range(1, rounds + 1):
            print(f"\n🔥 Round {round_num} / {rounds} 🔥")
            word = choose_word()
            clue = get_clue(word)
            guessed_letters = []
            attempts = 6
            score = 100

            display_word = "".join([letter if letter in guessed_letters or letter == ' ' else '_' for letter in word])

            print("📝 Clue: ", clue)
            print(display_hangman(6 - attempts))
            print("Word:", display_word)

            while attempts > 0:
                guess = input("🔮 Guess a letter: ").lower()

                if len(guess) != 1 or not guess.isalpha():
                    print("⚠️ Please enter a valid single letter.")
                    continue

                if guess in guessed_letters:
                    print("⛔ You've already guessed that letter.")
                    continue

                guessed_letters.append(guess)

                if guess in word:
                    print("🎊 Correct! You're on fire!🔥")
                    # Increment the score for correct guess
                    score += 10
                else:
                    print("❌ Incorrect! Keep going, you can do it!")
                    attempts -= 1

                display_word = "".join([letter if letter in guessed_letters or letter == ' ' else '_' for letter in word])

                print(display_hangman(6 - attempts))
                print("Word:", display_word)

                if '_' not in display_word:
                    print(f"🌟 Congratulations, {player_name}! You've cracked the word:", word)
                    # Add the remaining attempts to the score
                    score += attempts * 10
                    total_score += score  # Add score for the round
                    print("Score:", score)
                    break

            if attempts == 0:
                total_score += score  # Add score even if attempts run out
                print(display_hangman(6 - attempts))
                print("😞 Sorry, you've run out of attempts. The word was:", word)
                print(f"Round {round_num} Score: {score}")

        print("\n🏆 Game Over! Score Report 🏆")
        print(f"Total Rounds Played: {rounds}")
        print(f"Total Score: {total_score}")

        if not play_again():
            print(f"🙌 Thank you for playing, {player_name}! You did great. See you next time!")
            break

if __name__ == "__main__":
    main()
