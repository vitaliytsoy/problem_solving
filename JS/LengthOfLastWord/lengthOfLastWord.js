/* Problem Description:

*/
let lengthOfLastWord = (s) => {
    const splitted = s.trim().split(' ');
    return splitted[splitted.length - 1].length;
}
lengthOfLastWord("Hello ");
