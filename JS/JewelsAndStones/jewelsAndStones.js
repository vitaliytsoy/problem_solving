/* Description:

You're given strings J representing the types of stones 
that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all 
characters in J and S are letters. Letters are case
sensitive, so "a" is considered a different type of stone from "A".

*/


const J = "aAs";
const S = "aAAbbbb"

function jewelsAndStones(J, S){
    let counter = 0;
    for(let letter of J) {
        if (S.match(new RegExp(letter,'g'))) {
            counter += S.match(new RegExp(letter,'g')).length;
        }
    }
return counter;
}
jewelsAndStones(J, S);
  