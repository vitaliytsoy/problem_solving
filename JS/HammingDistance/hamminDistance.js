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
    let counter = 0;
    let distance = 0;
    while (counter <= Math.max(yBin.length, xBin.length)) {
        counter++;
    }
    return distance;
    if (yBin.charAt(13)) {
        console.log("YAYA");
    } else {
        console.log("NONO");
    }
}
hammingDistance(1, 4);




