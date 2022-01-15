// Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
// If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different
//  if one pair includes at least one array index which the other doesn't, even if they include the same values.

function numberOfWays(arr, k) {
  // Write your code here
  let count = 0;
  for (let i = 0; i <= arr.length - 1; i++) {
    for (let j = i + 1; j <= arr.length - 1; j++) {
      console.log(arr[i], arr[j]);
      if (arr[i] + arr[j] == k) {
        count += 1;
      }
    }
  }
  return count;
}
