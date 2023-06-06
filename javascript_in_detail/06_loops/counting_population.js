var raw_arr = [[null, {population: 5, temp: 3}], [{population: 6, temp: 2}, {population: 8, temp: 11}]];
var ans = 0;
console.log(raw_arr);
for (i = 0; i < raw_arr.length; i++) {
  for (j = 0; j < raw_arr[i].length; j++) {
    location = raw_arr[i][j]
    if (location !== null && location.temp <= 10.0) {
      ans += location.population
    }
  }
}
console.log(ans);