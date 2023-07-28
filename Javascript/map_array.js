// understanding map - use map to create new array multiplied by 3 using map

const myArray = [1, 2,3,4,5]

const multiplyByThree = myArray.map((elem, i, arr) => {
    return elem * 3
})

console.log(multiplyByThree);