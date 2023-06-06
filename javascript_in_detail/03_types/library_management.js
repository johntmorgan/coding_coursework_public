var id = '456';
var available = 'false';
var count = '0';
var name = 'Game of Thrones';
var author = 'George RR Martin';

var id = new Number(id).valueOf(); // id Stringv
var available = new Boolean(available === 'true').valueOf(); // available String saying 'true' / 'false'
var count = new Number(count).valueOf(); // count String
var name = name; // name String
var author = author; // author String
ans = {
    'id': id,
    'available': available,
    'count': count,
    'name': name,
    'author': author,
}; // assign final answer to ans variable
console.log(ans);