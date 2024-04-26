// const = a variable that can't be changed

let pi = 3.14565432;
let radius;
let circumference;

radius = window.prompt(`Enter the radius of a circle`);
radius = Number(radius);

circumference = 2 * pi * radius;

console.log(circumference);