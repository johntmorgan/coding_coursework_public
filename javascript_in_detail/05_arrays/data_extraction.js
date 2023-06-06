raw_arr = [[200, 50, 300, 5], [10, 25, 7, 100], [25, 20, 70, 45], [500, 170, 11, 35]]; // original data array
row = 1; // row index
s = 0; // column start
e = 2; // column end
if (row >= 0 && row < raw_arr.length) {
  var arr_row = raw_arr[row];
  if (s >= 0 && e < arr_row.length && s <= e) {
    ans = arr_row.slice(s, e + 1);
  } else {
    ans = undefined;
  }
} else {
  ans = undefined;
}
console.log(raw_arr[1])
console.log(ans)
