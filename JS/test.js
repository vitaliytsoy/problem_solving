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
// console.log(sum(1)(2)(3)(-6)(0)());

const isPrime = (num) => {
    if (num === 1 ) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if(num%i === 0) return false;
    }
    return true;
}

// console.log(isPrime(1));
// console.log(isPrime(5));
// console.log(isPrime(6));


const factorial = (num) => {
    return num ? num * factorial(num-1) : 1;
}
// console.log(factorial(5)); 


const fibonacci = (num) => {
    let firstNum = 0;
    let secondNum = 1;
    if (num == 1) return 0;
    if (num == 2 ) return 1;
    let result;
    for (let i = 3; i <= num; i++) {
        result = firstNum + secondNum;
        firstNum = secondNum;
        secondNum = result;
    }
    return result;
}
// console.log(fibonacci(1));
// console.log(fibonacci(3));


const isSorted = (array) => {
    let isSortedVar = array.reduce((isStillSorted, current, index, array) => {
        if (isStillSorted) {
            if (current >= array[index-1] || index === 0) {
                return true;                
            }
            else {
                return false;
            }
        } 
        return false;
    }, true);
    console.log(isSortedVar);
}

isSorted([-Infinity, 0, 3, 3]);


const filter = (array, isPassingFilter) => {
    let result = [];
    for (let i = 0; i < array.length; i++) {
        if (isPassingFilter(array[i])) {
            result.push(array[i]);
        }
    }
    return result;
}

console.log(filter([1,2,3,4,5,6,7], n => n % 2 == 0 ));


