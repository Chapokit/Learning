// string slicing
/*
const fullName = "Munyin Sam";

let firstName = fullName.slice(0,6);
let lastName = fullName.slice(7,11);
let lastName2 =  fullName.slice(7);

let firstChar = fullName.slice(0,1);
let lastChar = fullName.slice(-3);

console.log(firstName);
console.log(lastName2);
console.log(firstChar);
console.log(lastChar);


let firstName = fullName.slice(0, fullName.indexOf(" "));
let lastName = fullName.slice(fullName.indexOf(" ") + 1);

console.log(firstName);
console.log(lastName);

*/

const email = "kelvinsam2233@gmail.com";

let username = email.slice(0, email.indexOf("@"));
let extension = email.slice(email.indexOf("@") + 1);

console.log(username);
console.log(extension);