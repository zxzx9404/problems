/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    const combinedArr = [...nums1, ...nums2]
    combinedArr.sort((a, b) => a - b);
    const center = Math.floor(combinedArr.length / 2)
    if (combinedArr.length % 2 == 1) {
        return combinedArr[center]
    } else {
        return (combinedArr[center] + combinedArr[center-1]) / 2
    }
};
