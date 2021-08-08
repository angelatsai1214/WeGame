const gameData = [
    {
        name: "Solver",
        company:"MeGames Productions",
        image:"https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg",
        score: "92%",
        time: "43 hours",
        
    },
    {
        name: "SOME", 
        company: "LionLin",
        image: "https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg",
        score: "90%",
        time: "107 hours"
    }
]

function gameTemplate(game){
    return `
    <div class="rec">
        <div class="left">
            <h3 class="namename"><strong>${game.name}</strong> from ${game.company}</h3>
            <img src="${game.image}" class="cs">
        </div>
        <div class="right">
            <h4 class="cri"><strong>Average Score from Gamers:</strong> ${game.score}</h4>
            <h4 class="cri"><strong>Play Time:</strong> ${game.time}</h4>
            <h4 class="cri"><strong>Bonuses Earned:</strong> ${game.player_perspective}</h4>
            <input type="button" class="cta" value="View Reviews">
            <input type="button" class="cta" value="Play Game">
        </div>
    </div>
    `
}

document.getElementById("his").innerHTML = `  
    ${gameData.map(gameTemplate).join('')}
`

