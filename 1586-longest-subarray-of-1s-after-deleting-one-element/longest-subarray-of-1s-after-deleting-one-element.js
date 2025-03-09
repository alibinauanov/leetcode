/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let longest = 0;
    let l = 0;
    let deleteOne = 0;
    for (let r = 0; r < nums.length; r++) {
        if (nums[r] == 0) {
            deleteOne++;
        }

        while (deleteOne > 1) {
            if (nums[l] === 0) {
                deleteOne--;
            }
            l++;
        }

        longest = Math.max(longest, r - l);
    }
    return longest;
};