/* 
Problem Description:

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
*/

let reverseOnlyLetters = (strToReverse) => {
    let splittedString = strToReverse.match(new RegExp('([^\\d\\W]+|[\\d\\W])', 'g')).reverse
    splittedString.forEach(element => {
        if(elemtn)
        console.log(element);
    });
}
reverseOnlyLetters('Test1ng-Leet=code-Q!');