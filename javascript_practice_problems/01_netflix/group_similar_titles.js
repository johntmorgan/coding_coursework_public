// O(n * k) time
// O(n * k) space

function groupTitles(strs) {
  var res = {}
  for (var s of strs) {
    var count = new Array(26).fill(0);
    for (var c of s) {
      index = c.charCodeAt(0) - 'a'.charCodeAt(0)
      count[index] += 1
    }
    var key = count;
    if (key in res) {
      res[key].push(s)
    } else {
      res[key] = [s]
    }
  }
  var result = [];
  for (var key in res) {
    result.push(res[key]);
  }
  return result;
}

var titles = ["duel","dule","speed","spede","deul","cars"]
var gt = groupTitles(titles)
var query = "spede"

for (var [_, g] of Object.entries(gt)) {
    if (g.includes(query)){
        console.log(g)
    }
}