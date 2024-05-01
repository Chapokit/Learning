// String Method

let Username = "Munyin";

/*

console.log(Username.charAt(0))
console.log(Username.indexOf("n"))
console.log(Username.lastIndexOf("n"))
console.log(Username.length)


let Name = "     munyin      ";
Name = Name.trim(); //cut whitespace
Name = Name.toUpperCase();
Name = Name.toLowerCase();
Name = Name.repeat(3);

let result = Name.startsWith(" ");
let result2 = Name.endsWith(" ");

if(result){
    console.log("Your username cant begin with white space")
}
else{
    console.log(Name);
}
console.log(result);
console.log(Name);
splitName = "mun yin";

let result3 = splitName.includes(" ");
if(result3){
    console.log("Cant have a split");
}
*/

let phoneNumber = "123-455-4214";

phoneNumber = phoneNumber.replaceAll("-","");

console.log(phoneNumber);

phoneNumber = phoneNumber.padStart(15, "0"); //until it's 15 char long
phoneNumber = phoneNumber.padEnd(15, "0");
console.log(phoneNumber);

