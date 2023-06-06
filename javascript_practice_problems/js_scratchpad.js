var obj = {"a": 1, "b": 2, "c": 3}

for (key in obj) {
  console.log(key)
  console.log(obj[key])
}

if (obj[4] == null) {
  console.log("missing")
}

Object.entries(obj).forEach(x => console.log(x));
Object.keys(obj).forEach(x => console.log(x));
Object.values(obj).forEach(x => console.log(x));

var arr = [1, 2, 3]

for (index in arr) {
  console.log(index);
  console.log(arr[index])
}

arr.forEach(x => console.log(x + 1));
arr.forEach(x => {console.log(x + 1)});

arr.push(4);
console.log(arr);
arr.pop(4);
console.log(arr);
arr.shift()
console.log(arr);
arr.unshift(4)
console.log(arr);