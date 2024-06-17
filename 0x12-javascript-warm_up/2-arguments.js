#!/usr/bin/node
//utilizing process.arv to check the array of  command line argument
argsLength = process.argv.length - 2;

if (argsLength == 0){
    console.log("No argument");
}else if (argsLength == 1){
    console.log("Argument found");
}else{
    console.log("Arguments found")
}
