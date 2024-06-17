#!/usr/bin/node

//utilizing process.arv to check first command line argument
cmdArgs = process.argv.slice(2);
let firstArg = undefined;

for (let arg of cmdArgs){
    firstArg = arg;
    break;
}
if (firstArg === undefined){
    console.log("No argument");
}else{
    console.log(firstArg)
}
