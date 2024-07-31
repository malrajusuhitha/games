document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('button').addEventListener('click', submitGuess);
    document.querySelector('button:nth-of-type(2)').addEventListener('click', startNewGame);
    startNewGame(); // Ensure game starts correctly
});

function updateHearts() {
    const heartsElement = document.getElementById('hearts');
    heartsElement.innerHTML = '❤️'.repeat(attempts);
}

function submitGuess() {
    const letter = document.getElementById('letter').value.toLowerCase();
    if (letter) {
        fetch('/guess', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ letter: letter })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }
            document.getElementById('word').textContent = `Word: ${data.display_word}`;
            document.getElementById('clue').textContent = `📝 Clue: ${data.clue}`;
            document.querySelector('.score').textContent = `Score: ${data.score}`;
            document.getElementById('letter').value = ''; // Clear input

            attempts = data.attempts;
            updateHearts();

            if (data.message) {
                alert(data.message);
                startNewGame(); // Start a new game after the current one ends
            }
        });
    }
}

function startNewGame() {
    fetch('/new_game')
        .then(response => response.json())
        .then(data => {
            document.getElementById('word').textContent = `Word: ${data.display_word}`;
            document.getElementById('clue').textContent = `📝 Clue: ${data.clue}`;
            document.querySelector('.score').textContent = `Score: ${data.score}`;
            document.getElementById('letter').value = ''; // Clear input
            attempts = data.attempts;
            updateHearts();
        });
}
