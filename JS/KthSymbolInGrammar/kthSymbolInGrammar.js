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
    function iteration(N, prevRow) {
        if (N > 1 ) {
            let valuesToReplace = prevRow.match(new RegExp('[0, 1]', 'g'));
            let nextRow = '';
            valuesToReplace.forEach(function(value) {
                let replacedValue = value === '0' ? '01' : '10';
                nextRow += replacedValue;
            });
            return iteration(N-1, nextRow);
        } else {
            return prevRow
        }
    }
    let firstRow = '0';
    return iteration(N, firstRow);
}


function KthSymmbolInGrammar(N, K) {
    let row = generateRow(N);
    let kthSymbol = row.charAt(K-1);
    console.log(parseInt(kthSymbol));
    return parseInt(kthSymbol);
}
KthSymmbolInGrammar(2, 1);