console.log("hello");

// function recurSplitLine (arr, line, width){
//   if (line.length == 0 || line[0].length > width) {
//     arr.push(line);
//   } else {
//     arr[0].push(line[0]);
//     recurSplitLine(arr, line.slice(1), width - line[0].length)
//   }
// }

// function splitLine(line, width){
//   var arr = [[]];
//   recurSplitLine(arr, line, width)

//   return arr;
// }

// var line = ['He', 'who', 'controls', 'it'];
// var width = 13
// var arr = splitLine(line, width);
// console.log(arr);

var enHyp = {
  "creative" : ["cr","ea","ti","ve"],
  "controls" : ["co","nt","ro","ls"],
  "achieve" : ["ach","ie","ve"],
  "future" : ["fu","tu","re"],
  "present" : ["pre","se","nt"],
  "motivated" : ["mot","iv","at","ed"],
  "desire" : ["de","si","re"],
  "others" : ["ot","he","rs"],
}
var dict = enHyp;
var width = 15;
var line = ['He', 'who', 'controls,', 'it'];