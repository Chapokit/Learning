// spread operator ...

/*
let numbers = [1,2,3,4,5];
let maximum = Math.max(...numbers); // spreading arrays
let mininum = Math.min(...numbers);

console.log(numbers);

console.log(maximum);
console.log(mininum);

let username = "Bro Code";
let letters = [...username].join("-");

console.log(letters);*/

let fruits = ["apple", "orange", "banana"];
let vegetables = ["Carrots", "celery", "potatoes"];
let foods = [...fruits, ...vegetables, "eggs", "milk"];

console.log(foods);