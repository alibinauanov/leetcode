/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    let maxConsOne = 0;
    let l = 0;
    let zeroCount = 0;
    for (let r = 0; r < nums.length; r++) {
        if (nums[r] == 0) {
            zeroCount++;
        }
        
        while (zeroCount > k) {
            if (nums[l] === 0) {
                zeroCount--;
            }
            l++;
        }

        maxConsOne = Math.max(maxConsOne, r - l + 1);
    }
    return maxConsOne;
};