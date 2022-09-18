/**
 * Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
 *
 * In the American keyboard:
 *
 * the first row consists of the characters "qwertyuiop",
 * the second row consists of the characters "asdfghjkl", and
 * the third row consists of the characters "zxcvbnm".
 */
var findWords = function(words) {
    const keyboardRows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

    return words.filter((word) => {
        const split = word.toLowerCase().split('')
        const rowIndex = keyboardRows.findIndex((row) => (row.includes(split[0])))
        
        return !split.some((letter) => (rowIndex !== keyboardRows.findIndex((row) => (row.includes(letter)))))
    })
};

findWords(["Hello","Alaska","Dad","Peace"])
