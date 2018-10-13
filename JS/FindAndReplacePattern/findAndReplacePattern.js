/* Problem Description:
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
*/

let findUnifiedPattern = (word) => {
    let dictionary = {}
    let unifiedPattern = [];
    let patternCounter = 0;
    for(let letter of word) {
        if (!dictionary.hasOwnProperty(letter)) {
            dictionary[letter] = patternCounter;
            patternCounter++;
            unifiedPattern.push(dictionary[letter]);
        } else {
            unifiedPattern.push(dictionary[letter]);
        }
    }
    return unifiedPattern.join('');
}

let findAndReplacePattern = (words, pattern) => {
    let unifiedPattern = findUnifiedPattern(pattern);
    return words.filter(word => {
        let wordPattern = findUnifiedPattern(word);
        if (unifiedPattern === wordPattern) {
            return true;
        }
        return false;
    });
}
findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb");