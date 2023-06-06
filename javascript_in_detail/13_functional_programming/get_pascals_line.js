function getPascalsLine(x) {
  if (x === 0) {
    return [1];
  } else {
    var prior_line = getPascalsLine(x - 1);
    var arr = []
    for (var i = 0; i < x + 1; i ++) {
      if (i > 0) {
        var left = prior_line[i - 1];
      } else {
        var left = 0;
      }
      if (i < prior_line.length) {
        var right = prior_line[i];
      } else {
        var right = 0;
      }
      arr.push(left + right)
    }
    return arr
  }
}

console.log(getPascalsLine(4));


// compositon approach

const compose = (...fns) => x => fns.reduceRight((y, f) => f(y), x);

function getPascalsLine(x) {
    function createNextLine(previousLine){
        var line = [1]; // initialise by 1 in start
        for (let i = 0; i < previousLine.length - 1; i++) {
            line.push(previousLine[i] + previousLine[i + 1]);
        }
        line.push(1); // add ending 1 value
        return line; // return line
    }
    var firstLine = [1]; // index 0
    var functions = []; // empty array of functions
    for(var i = 0; i < x; i++){
        functions.push(createNextLine);
    }
    var answer = compose(...functions)(firstLine);
    return answer;
}