/* Problem Description:
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
*/
function generateRow(N) {
    let valuesToReplace, nextRow, replacedValue;
    function iteration(N, prevRow, counter) {
        if (N > 1) {
            nextRow = '';
            if (counter < 6) {
                valuesToReplace = prevRow.match(new RegExp('[0, 1]', 'g'));
                valuesToReplace.forEach(function(value) {
                    replacedValue = value === '0' ? '01' : '10';
                    nextRow += replacedValue;
                });
            } else if (counter >= 6) {
                valuesToReplace = prevRow.match(new RegExp('(0110100110010110)|(1001011001101001)', 'g'));
                valuesToReplace.forEach(function(value) {
                    replacedValue = value === '0110100110010110' ? '01101001100101101001011001101001' : '10010110011010010110100110010110';
                    nextRow += replacedValue;
                });
            }   
            return iteration(N-1, nextRow, counter + 1);        
        } else {
            return prevRow;
        }
    }
    let firstRow = '0';
    return iteration(N, firstRow, 1);
}
console.log(generateRow(1));
console.log(generateRow(2));
console.log(generateRow(3));
console.log(generateRow(4));
console.log(generateRow(5));
console.log(generateRow(6));
console.log(generateRow(7));
console.log(generateRow(8));
console.log(generateRow(9));
console.log(generateRow(10));
// 0110 1001 pattern
// 0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110
// 1001 0110 0110 1001 0110 1001 1001 0110 0110 1001 1001 0110 1001 0110 0110 1001
// 1001 0110 0110 1001 0110 1001 1001 0110 0110 1001 1001 0110 1001 0110 0110 1001 0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110

// 0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110
// 1001 0110 0110 1001 0110 1001 1001 0110 0110 1001 1001 0110 1001 0110 0110 1001 
// 1001 0110 0110 1001 0110 1001 1001 0110 0110 1001 1001 0110 1001 0110 0110 1001
// 0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110 
// 1001 0110 0110 1001 0110 1001 1001 0110 0110 1001 1001 0110 1001 0110 0110 1001
// 0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110
// 0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110
// 1001 0110 0110 1001 0110 1001 1001 0110 0110 1001 1001 0110 1001 0110 0110 1001
function KthSymmbolInGrammar(N, K) {
    let row = generateRow(N);
    let kthSymbol = row.charAt(K-1);
    console.log(parseInt(kthSymbol));
    return parseInt(kthSymbol);
}
KthSymmbolInGrammar(2, 1);