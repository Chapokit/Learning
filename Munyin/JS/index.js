// array

let fruits = ["apple", "orange", "banana"];
/*
fruits[1] = "coconut";
fruits.push("juice");
fruits.pop();
fruits.unshift("mango");
fruits.shift();


console.log(fruits);

let numOfFruits = fruits.length;
let index = fruits.indexOf("apple"); // will return -1 if doesnt exist

console.log(numOfFruits);
console.log(index); 


for(let i = 0; i < fruits.length; i++){
    console.log(fruits[i]);
}
for (let i = fruits.length - 1; i >= 0 ; i--) {
    console.log(fruits[i]);
}

*/

fruits.sort().reverse(); //alphabetical

for(let fruit of fruits){
    console.log(fruit);
}