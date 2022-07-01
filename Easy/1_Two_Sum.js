/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let visited = new Map();
    for(let i=0; i<nums.length; i++) {
        diff = target - nums[i];
        if (visited.has(diff)) {
            return [i, visited.get(diff)];
        }
        visited.set(nums[i], i);
    }
}
