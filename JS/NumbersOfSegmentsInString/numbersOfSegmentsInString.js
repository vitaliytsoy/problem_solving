/*
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:
Input: "Hello, my name is John"
Output: 5
*/

const numbersOfSegmentsInString = (s) => {
    const splittedS = s.split(' ');
    console.log(splittedS);
    let counter = 0;
    for(let i = 0; i < splittedS.length; i++) {
        if (splittedS[i]) {
            counter++;
        }
    }
    return counter;
};

console.log(numbersOfSegmentsInString('     dd   '));