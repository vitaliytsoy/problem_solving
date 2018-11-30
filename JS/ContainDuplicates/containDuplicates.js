/* Problem Description:
Check if arra

*/
const isContainingDuplicates = (nums) => { 
    for(let i = 0; i < nums.length; i++) {
        if (i !== nums.lastIndexOf(nums[i])) return true;
    }
    return false;
}
console.log(isContainingDuplicates([1,2,3,4,1]));
console.log(isContainingDuplicates([1,2,3,4]));
console.log(isContainingDuplicates([1,1,3,3]));
console.log(isContainingDuplicates([1]));
console.log(isContainingDuplicates(['0100', '1100', '0101', '0100']));
