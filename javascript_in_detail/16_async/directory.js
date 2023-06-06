// copied solution, did not get - need wayyy more practice with promises & async
// Under time pressure atm, oh well

const fs = require('fs'); // import fs module
// promise creating function for any file read
function readFile(filename){ // function to return promise
  return new Promise((resolve,reject) => {
    fs.readFile(filename,'utf8', (err, data) => {
      if(err){ // check for error
        resolve([filename, false]); // file read unsuccessful
      } else{
        resolve([filename, true]); // file read successful
      }
    });
  });
}

async function finder(filenames){
  let promiseList = []; // list all promises
  // populate promiseList with promises for each filename
  filenames.forEach(x => {promiseList.push(readFile(x));});
  data = await Promise.all(promiseList); // wait to resolve all promises
  return data;
}
var ans = finder(['index.js', 'content.txt','funny.txt']);
ans.then(val => {console.log(val)});