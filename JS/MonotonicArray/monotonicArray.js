/* Problem Description:

*/
let isMonotonicArray = (array) => {
    let isIncremental = true;
    let isDecremental = true;
    for(let i = 0; i < array.length; i++) {
        if (array[i] > array[i+1]) {
            isIncremental = false;
        } 
        if (array[i] < array[i+1]) {
            isDecremental = false;
        } 
    }
    return !!(isIncremental | isDecremental);
}
isMonotonicArray([1, 2, 2, 3, 5])

