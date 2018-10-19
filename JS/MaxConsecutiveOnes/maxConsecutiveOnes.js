/* Problem Description:
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
*/
let findMaxConsecutiveOnes = (nums) => {
    let match = nums.join('').match(new RegExp('1+', 'g'));
    if (!match) return 0;
    return match.reduce((prev, current) => {
        return prev < current.length ? current.length : prev;
    }, 1);
}
findMaxConsecutiveOnes([1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0]);

