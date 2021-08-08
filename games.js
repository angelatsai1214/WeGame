const gameData = [
    {
        game_modes: ["Single player"], 
        genres: ["Indie", "Adventure"], 
        name: "Nuclear", 
        company: "RGDX",
        themes: ["Action"], 
        player_perspective: ["Split Screen"],
        iamge: "https://media.comicbook.com/2017/12/pubg-xbox-one-vs-xbox-one-x-1066041-1280x0.jpg"
    }, 
    {
        game_modes: ["Single player", "Multiplayer"], 
        genres: ["Fighting"], 
        name: "SOME game", 
        company: "LionLin",
        themes: ["Thriller", "Kids"], 
        player_perspective: ["First Person"],
        image: "https://wallpaperaccess.com/full/2621589.jpg"
    },
    {
        game_modes: ["Single player", "Multiplayer"], 
        genres: ["Shooter", "Strategy"], 
        name: "Goater", 
        company: "Superion",
        themes: ["Action", "Survival"], 
        player_perspective: ["First Person"],
        image: "https://wallpaperaccess.com/full/2621589.jpg"
    },
    {
        game_modes: ["Single player", "Multiplayer"], 
        genres: ["Platform", "Role-playing (RPG)"], 
        name: "HiStoryVR", 
        themes: ["Historical", "Non-fiction"], 
        player_perspective: ["VR"],
        game_description: "Lorem ipsum dolor sit amet consectetur adipisicing elit.",
        company: "Bezene",
        image: "https://wallpaperaccess.com/full/2621589.jpg"
    },
    {
        game_modes: ["Massively Multiplayer Online (MMO)", "Multiplayer"],
        genres: ["Tactical", "Shooter"],
        name: "Not your average mmo",
        themes: ["Survival", "Mystery", "Open world"],
        player_perspective: ["First Person", "Third Person"],
        game_description: "Lorem ipsum dolor sit amet consectetur adipisicing elit.",
        company:"AYMOY",
        image: "https://upload.wikimedia.org/wikipedia/commons/6/6c/Black_photo.jpg"
    },
    {
        game_modes: ["Virtual Reality"],
        genres: ["Puzzle"],
        name: "Can You Solve It?",
        themes: ["Educational", "Mystery"],
        player_perspective: ["First Person"],
        game_description: "Lorem ipsum dolor sit amet consectetur adipisicing elit.",
        company:"MeGames Productions",
        image:"https://upload.wikimedia.org/wikipedia/commons/6/6c/Black_photo.jpg"},
    {
        game_modes: ["Co-operative", "Multiplayer"],
        genres: ["Racing"],
        name: "Race It!",
        themes: ["Thriller"],
        player_perspective: ["Side View"],
        game_description: "Lorem ipsum dolor sit amet consectetur adipisicing elit.",
        company:"MeGames Productions",
        image:"https://upload.wikimedia.org/wikipedia/commons/6/6c/Black_photo.jpg"
    }
]

function gameTemplate(game){
    return `
    <div class="rec">
        <h3><strong>${game.name}</strong> from ${game.company}</h3>
        <img src="game.image">
        <h4>Game Mode: ${game.game_modes}</h4>
        <h4>Player Perspective: ${game.player_perspective}</h4>
        <h4>Generes/Themes: ${game.genres}/ ${game.themes}</h4>
        <h4>${game_description}
    </div>
    `
}

document.getElementById("rec").innerHTML = `
    <h2>Your Game Recommendations</h2>    
    ${gameData.map(gameTemplate).join('')}
`
