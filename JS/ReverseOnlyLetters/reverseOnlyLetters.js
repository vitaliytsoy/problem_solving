/* 
Problem Description:

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
*/

let reverseOnlyLetters = (strToReverse) => {
    if(strToReverse.length <= 0) {
        return '';
    }
    let splittedString = strToReverse.match(new RegExp('([^(?!_)\\d\\W]+|[\\d\\W_])', 'g'));
    let onlyLetters = strToReverse.match(new RegExp('(?!_)[^\\d\\W]', 'g'));
    if(onlyLetters) {
        onlyLetters = onlyLetters.join('').split('').reverse();
    }

    let reversedString = [];
    splittedString.forEach(item => {
        if(item.length > 1) {
            reversedString.push(onlyLetters.slice(0, item.length).join(''));
            onlyLetters.splice(0, item.length)
        } else { 
            if(RegExp('[a-zA-Z]', 'g').test(item)) {
                reversedString.push(onlyLetters.slice(0, 1).join(''));
                onlyLetters.splice(0, 1);
            } else {
                reversedString.push(item);
            }
        }
    });
    return reversedString.join('');
}
reverseOnlyLetters("5b6y_e");