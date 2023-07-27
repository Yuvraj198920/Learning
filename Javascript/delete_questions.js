// Question on delete property of objects

const func = (function (a) {
    console.log(delete a);
    // above console.log will return false
    return a;
})(5);

console.log(func)