const gameData = [
    {
        name: "Race It!",
        company:"MeGames Productions",
        image:"https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg",
        rank: "#2",
        score: "97%",
        users: 14,
        bugs:2
    },
    {
        name: "Solver",
        company:"MeGames Productions",
        image:"https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg",
        rank: "#6",
        score: "92%",
        users: 14,
        bugs:8
    }
]

function gameTemplate(game){
    return `
    <div class="rec">
        <div class="left">
            <h3 class="namename"><strong>${game.name}</strong></h3>
            <img src="${game.image}" class="cs">
        </div>
        <div class="right">
            <h4 class="cri"><strong>Average Score from Gamers:</strong> ${game.score}</h4>
            <h4 class="cri"><strong>User Count:</strong> ${game.users}</h4>
            <h4 class="cri"><strong>Ranking:</strong> ${game.rank}</h4>
            <h4 class="cri"><strong>Bug Reports:</strong> ${game.bugs}</h4>
            <input type="button" class="cta" value="View All Reviews">
        </div>
    </div>
    `
}

document.getElementById("mi").innerHTML = `  
    ${gameData.map(gameTemplate).join('')}
`

