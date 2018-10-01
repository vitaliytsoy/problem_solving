/* Problem Description:
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
*/
function ToLowerCase(str) {
    let transformedString = '';
    for(let letter of str) {
        let asciiLetter = letter.charCodeAt(0);
        let lowerCaseLetter = '';
        if (asciiLetter >= 65 && asciiLetter <= 90) {
            asciiLetter = asciiLetter + 32
        }
        lowerCaseLetter = String.fromCharCode(asciiLetter);
        transformedString = transformedString + lowerCaseLetter;
    }
    console.log(transformedString);
    return transformedString;
}
ToLowerCase('HELLO');