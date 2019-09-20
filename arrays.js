const ages = [5, 7, 9, 52, 43, 23, 26, 69, 27, 40, 16, 18]

for (let i = 0; i < ages.length; i++) {
    if (ages[i] >= 18) {
        console.log(ages[i], ':)')
        
    } else if(ages[i] < 18 && ages[i] != 16){
        console.log(ages[i], ':(')  

    }

    if (ages[i] == 16) {
        console.log(ages[i], 'Legalicen')
    }

    
}