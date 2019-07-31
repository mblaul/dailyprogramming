// Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

/**
 * Function to remove dups from a sorted array
 *
 * @param {Array} arrayWithDups
 * @returns {Number}
 */

function removeDups(arrayWithDups) {
  for (let index = 0; index < arrayWithDups.length - 1; index++) {
    if (arrayWithDups[index - 1] === arrayWithDups[index]) {
      arrayWithDups.splice(index - 1, 1);
    }
    if (arrayWithDups[index] === arrayWithDups[index + 1]) {
      arrayWithDups.splice(index + 1, 1);
    }
  }

  console.log(arrayWithDups);
  return arrayWithDups.length;
}

// Test cases

const testCases = [[1, 1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]];

testCases.forEach(testCase => console.log(removeDups(testCase)));
