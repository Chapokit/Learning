/*
let time = 9;
let isStudent = false/true

if(time < 12){
    console.log("Good morning!");
}
else{
    console.log("Good afternoon");
}
*/

const myText = document.getElementById("myText");
const mySubmit = document.getElementById("mySubmit");
const resultElement = document.getElementById("result");

let age;


mySubmit.onclick = function(){

    age = myText.value;
    age = Number(age);
    if (age >= 16) {

        resultElement.textContent = `You can drive`;

        if (hasLicense) {
            resultElement.textContent = `You have a license`;
        }
        else {
 
            resultElement.textContent = `You dont`;
        }
    }
    else if (age < 0) {

        resultElement.textContent = `wtf`;
    }
    else if (age == 0) {
        resultElement.textContent = `nabo`;
    }
    else {
        resultElement.textContent = `no`;
    }
}


let hasLicense = false;


