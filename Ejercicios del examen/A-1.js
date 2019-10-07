/*
encontrar el numero faltante en una lista de arreglos del 0 al 9
*/

const total = 45
const arr = [2,1,9,3,8,7,4,6,0]
const missing = false
let aux = 0  //suma del arr

let i = 0
for (i = 0; i < arr.length; i++) {
    aux += arr[i];
    
}


if (total == aux && arr.length==10) {
    console.log("No falta ninguno")
} else {
    console.log("Falta el numero: ", total-aux)
}