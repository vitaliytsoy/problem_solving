/* Description:

Reverse bits of a given 32 bits unsigned integer.
*/

function reverseBits(n){
    n = n.toString(2);
    if (n.length < 32) {
        n = n.padStart(32, '0');
    }
    return parseInt(n.split('').reverse().join(''), 2);
}
reverseBits(43261596);
  