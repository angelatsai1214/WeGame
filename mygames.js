const gameData = [
    {
        game_modes: ["Co-operative", "Multiplayer"],
        genres: ["Racing"],
        name: "Race It!",
        themes: ["Thriller"],
        player_perspective: ["Side View"],
        game_description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et aliqua.",
        company:"MeGames Productions",
        image:"https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg",
        rank: "#2",
        score: "97%"
    },
    {
        game_modes: ["Virtual Reality"],
        genres: ["Puzzle"],
        name: "Solver",
        themes: ["Educational", "Mystery"],
        player_perspective: ["First Person"],
        game_description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et aliqua.",
        company:"MeGames Productions",
        image:"https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg",
        rank: "#6",
        score: "92%"
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
            <h4 class="cri"><strong>Rank:</strong> ${game.rank}</h4>
            <h4 class="cri"><strong>Player Perspective:</strong> ${game.player_perspective}</h4>
            <h4 class="cri"><strong>Generes/Themes: </strong>${game.genres}/ ${game.themes}</h4>
            <h3 class="cri">${game.game_description}</h3>
            <input type="button" class="cta" value="View Reviews">
            <input type="button" class="cta" value="Play Game">
        </div>
    </div>
    `
}

document.getElementById("mi").innerHTML = `  
    ${gameData.map(gameTemplate).join('')}
`

