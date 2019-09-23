arr = [9, 3, 1, 3, 9, 2]
arrNew = []

for (let i = 0; i < arr.length-1; i++) {
    for (let j = 1; j < arr.length; j++) {
        if (arr[i] == arr[j]) {
            
            console.log("se repite el", arr[j])
        }
        
    }
    
}