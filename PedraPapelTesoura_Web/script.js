let userScore = 0;
let cpuScore = 0;

const choices = ['rock', 'paper', 'scissors'];

const userScoreEl = document.getElementById('user-score');
const cpuScoreEl = document.getElementById('cpu-score');
const statusEl = document.getElementById('game-status');
const userImg = document.getElementById('user-img');
const cpuImg = document.getElementById('cpu-img');
const userDisplay = document.getElementById('user-choice-display');
const cpuDisplay = document.getElementById('cpu-choice-display');

function playGame(userChoice) {
    // Disable buttons during animation
    const buttons = document.querySelectorAll('.choice-btn');
    buttons.forEach(btn => btn.disabled = true);

    statusEl.textContent = "JO...";
    
    // Clear styles
    userDisplay.classList.remove('active', 'winner-animate');
    cpuDisplay.classList.remove('active', 'winner-animate');
    
    setTimeout(() => {
        statusEl.textContent = "KEN...";
        setTimeout(() => {
            statusEl.textContent = "PO!!!";
            processResult(userChoice);
            buttons.forEach(btn => btn.disabled = false);
        }, 600);
    }, 600);
}

function processResult(userChoice) {
    const cpuChoice = choices[Math.floor(Math.random() * 3)];
    
    // Update displays
    userImg.src = `${userChoice}.png`;
    cpuImg.src = `${cpuChoice}.png`;
    userDisplay.classList.add('active');
    cpuDisplay.classList.add('active');

    if (userChoice === cpuChoice) {
        statusEl.textContent = "EMPATE!";
        statusEl.style.color = "white";
    } else if (
        (userChoice === 'rock' && cpuChoice === 'scissors') ||
        (userChoice === 'paper' && cpuChoice === 'rock') ||
        (userChoice === 'scissors' && cpuChoice === 'paper')
    ) {
        userScore++;
        userScoreEl.textContent = userScore;
        statusEl.textContent = "VOCÊ VENCEU! 🎉";
        statusEl.style.color = "var(--win-color)";
        userDisplay.classList.add('winner-animate');
    } else {
        cpuScore++;
        cpuScoreEl.textContent = cpuScore;
        statusEl.textContent = "VOCÊ PERDEU! 😢";
        statusEl.style.color = "var(--loss-color)";
        cpuDisplay.classList.add('winner-animate');
    }
}

function resetGame() {
    userScore = 0;
    cpuScore = 0;
    userScoreEl.textContent = '0';
    cpuScoreEl.textContent = '0';
    statusEl.textContent = "E o placar volta a zero!";
    statusEl.style.color = "white";
    userDisplay.classList.remove('active', 'winner-animate');
    cpuDisplay.classList.remove('active', 'winner-animate');
}
