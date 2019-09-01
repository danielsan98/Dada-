const abs = function(num){
    const absoluto = 0
    if (num < 0) {
        absoluto = num * -1
    } else {
        absoluto = num
    }

    return absoluto
}

try {
    assert(abs(-7), 7)
    console.log('abuelita de batman')
} catch (error) {
    console.log('chale :(')
    console.error(error);
}
console.log(abs(5)) //5
console.log(abs(-1)) //1