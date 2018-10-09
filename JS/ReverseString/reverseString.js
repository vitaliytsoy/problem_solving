/* 
Problem Description:
Write a function that takes a string as input and returns the string reversed.
*/

let reverseString = (strToReverse) => {
    let reversedStr = '';
    for(let i = strToReverse.length; i >= 0; i--) {
        reversedStr += strToReverse.charAt(i)
    }
    return reversedStr;
}
reverseString('Hello World!!!');
