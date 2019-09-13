
var aux=1
var n=4

if (n<0) {
    console.error("n debe ser mayor a 0!")
} else {
    if (n<=10) {
        if (n==0 || n==1) {
            console.log("El factorial de:", n, " es: 1")
            
        } else {
            for (let index = 1; index < n; index++) {
                aux=aux*index

                
            }
            console.log("El factorial de:", n, " es: ", aux)
        }
    } else {
        console.error("n no es menor a 10!")
    }
}