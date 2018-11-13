/* Problem Description:

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
*/
function decToBin(number) {
    return (number >>> 0).toString(2);
}

let hammingDistance = (x, y) => {
    let xBin = decToBin(x);
    let yBin = decToBin(y);
    let addZerosToX = xBin.length >= yBin.length ? false : true;
    const zerosToAdd = Math.max(yBin.length, xBin.length) - Math.min(yBin.length, xBin.length);
    if (addZerosToX) {
        xBin = '0'.repeat(zerosToAdd) + xBin;
    } else {
        yBin = '0'.repeat(zerosToAdd) + yBin;        
    }
    let counter = 0;
    let distance = 0;
    while (counter <= xBin.length) {
        if (yBin.charAt(counter - 1) !== xBin.charAt(counter - 1)) {
            distance++;
        }
        counter++;
    }
    return distance;
}
hammingDistance(4, 14);




