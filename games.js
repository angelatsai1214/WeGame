const gameData = [
    {
        game_modes: ["Single player"], 
        genres: ["Indie", "Adventure"], 
        name: "Nuclear", 
        company: "RGDX",
        themes: ["Action"], 
        player_perspective: ["Split Screen"],
        game_description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et aliqua.",
        image: "https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg",
        rank: "#1",
        score: "98%"
    }, 
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
        game_modes: ["Single player", "Multiplayer"], 
        genres: ["Shooter", "Strategy"], 
        name: "Goater", 
        company: "Superion",
        themes: ["Action", "Survival"], 
        player_perspective: ["First Person"],
        game_description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et aliqua.",
        image: "https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg",
        rank: "#3",
        score: "95%"
    },
    {
        game_modes: ["Single player", "Multiplayer"], 
        genres: ["Role-playing (RPG)"], 
        name: "HiStoryVR", 
        themes: ["Historical", "Non-fiction"], 
        player_perspective: ["VR"],
        game_description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et aliqua.",
        company: "Bezene",
        image: "https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg",
        rank: "#4",
        score: "94%"
    },
    {
        game_modes: ["Massively Multiplayer Online (MMO)"],
        genres: ["Tactical", "Shooter"],
        name: "MMOMundo",
        themes: ["Survival", "Mystery"],
        player_perspective: ["First Person", "Third Person"],
        game_description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et aliqua.",
        company:"AYMOY",
        image: "https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg",
        rank: "#5",
        score: "92%"
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
    },
    {
        game_modes: ["Single player", "Multiplayer"], 
        genres: ["Fighting"], 
        name: "SOME", 
        company: "LionLin",
        themes: ["Thriller", "Kids"], 
        player_perspective: ["First Person"],
        game_description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et aliqua.",
        image: "https://img.freepik.com/free-vector/neon-style-coming-soon-glowing-background-design_1017-25516.jpg?size=626&ext=jpg",
        rank: "#7",
        score: "90%"
    }
]

function gameTemplate(game){
    return `
    <div class="rec">
        <div class="left">
            <h3 class="namename">${game.rank} <strong>${game.name}</strong> from ${game.company}</h3>
            <img src="${game.image}" class="cs">
        </div>
        <div class="right">
            <h4 class="cri"><strong>Average Score from Gamers:</strong> ${game.score}</h4>
            <h4 class="cri"><strong>Game Mode:</strong> ${game.game_modes}</h4>
            <h4 class="cri"><strong>Player Perspective:</strong> ${game.player_perspective}</h4>
            <h4 class="cri"><strong>Generes/Themes: </strong>${game.genres}/ ${game.themes}</h4>
            <h3 class="cri">${game.game_description}</h3>
            <input type="button" class="cta" value="View Reviews">
            <input type="button" class="cta" value="Play Game">
        </div>
    </div>
    `
}

document.getElementById("exp").innerHTML = `  
    ${gameData.map(gameTemplate).join('')}
`

