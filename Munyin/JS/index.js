// function

function happyBirthday(username, age){
    console.log(`hbd ${username} ${age}`);
}

function isEven(number){

    return number % 2 === 0 ? true : false;
}

function isValidEmial(email){

    /*
    if(email.includes("@")){
        return true;
    }
    else{
        return false;
    }*/

    return email.includes("@") ? true : false;
}

happyBirthday("Munyin",18);
console.log(isEven(10));
console.log(isValidEmial("kelbvdsfs@"))