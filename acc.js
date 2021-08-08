const userData = [
    {
        firstName = "Ariel",
        lastName = "Dumphy",
        userName = "cdumphy1",
        email = "example@gmail.com",
        pronoun = "She/her",
        phone = 998-238-492,
        avatar = "https://cdn.pixabay.com/photo/2016/11/08/15/21/user-1808597_960_720.png"
    }
]

function getInfo(user){
    return `
    <div class="rec">
    <div class="left>
    <h3>${user.firstName}</h3>
    <img src="${user.avatar}">
    </div>
    </div>
    `

}

document.getElementById("acc").innerHTML = "Hi"


