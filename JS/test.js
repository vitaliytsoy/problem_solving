// For test code 
const sum = (num) => {
    let currentSum = num;
    const nextSum = (innerNum) => {
        if (innerNum | innerNum === 0) {
            currentSum += innerNum;
            return nextSum;
        } else {
            return currentSum;
        }
    } 
    return nextSum;
}
console.log(sum(1)(2)(3)(-6)(0)());


// console.log(newCounter.increment());



