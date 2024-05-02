// while loop

//let username = "";
/*
do{
    username = window.prompt(`Enter your name`);
} while (username === "" || username === null)

console.log(`Hello ${username}`);
*/
let loggedIn = false;

let username;
let password;

do{
    username = window.prompt("Enter your username");
    password = window.prompt("Enter your password");

    if(username === "user" && password === "mypass"){
        loggedIn = true;
        console.log("You are logged in!")
    }
    else{
        console.log("What do")
    }
} while (!loggedIn)