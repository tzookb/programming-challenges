var removeDuplicates = function(nums) {
    let i = 0
    let j = 0
    while (j < nums.length) {
      if (nums[i] != nums[j]) {
        i++
        nums[i] = nums[j]
      }
      j++
    }
    return i+1
};


const arr = [1,1,1,1,1,2,2,2,3]
const r = removeDuplicates(arr)
console.log(arr)
console.log(r)