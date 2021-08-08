const gameData = [
    {
        game_modes: ["Single player"], 
        genres: ["Indie", "Adventure"], 
        name: "Nuclear", 
        company: "RGDX",
        themes: ["Action"], 
        player_perspective: ["Split Screen"],
        game_description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ",
        image: "https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg"
    }, 
    {
        game_modes: ["Single player", "Multiplayer"], 
        genres: ["Shooter", "Strategy"], 
        name: "Goater", 
        company: "Superion",
        themes: ["Action", "Survival"], 
        player_perspective: ["First Person"],
        game_description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ",
        image: "https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg"
    },
    {
        game_modes: ["Massively Multiplayer Online (MMO)"],
        genres: ["Tactical", "Shooter"],
        name: "MMOMundo",
        themes: ["Survival", "Mystery"],
        player_perspective: ["First Person", "Third Person"],
        game_description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ",
        company:"AYMOY",
        image: "https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg"
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
            <h4 class="cri"><strong>Game Mode:</strong> ${game.game_modes}</h4>
            <h4 class="cri"><strong>Player Perspective:</strong> ${game.player_perspective}</h4>
            <h4 class="cri"><strong>Generes/Themes: </strong>${game.genres}/ ${game.themes}</h4>
            <h3 class="cri">${game.game_description}</h3>
        </div>
    </div>
    `
}

document.getElementById("rec").innerHTML = `  
    ${gameData.map(gameTemplate).join('')}
`

