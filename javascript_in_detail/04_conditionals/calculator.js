// left_operand = left_operand; // Left operand is assigned here
// right_operand = right_operand; // Right operand is assigned here
// operator = operator; // This is the String representation of operator
// if (operator === '+') {
//     var ans = left_operand + right_operand;
// } else if (operator === "-") {
//     var ans = left_operand - right_operand;
// } else if (operator === "*") {
//     var ans = left_operand * right_operand;
// } else if (operator === "/") {
//     var ans = left_operand / right_operand;
// } else {
//     var ans = NaN
// }

// Ternary version

left_operand = 2; // left operand
right_operand = 3; // right operand
operator = '*'; // target operator
let ans = NaN;
let all_oprators= ['+','-','*','/'];
ans = operator === '+' ? left_operand + right_operand
    : operator === '-' ? left_operand - right_operand
    : operator === '*' ? left_operand * right_operand
    : operator === '/' ? left_operand / right_operand
    : NaN

console.log(`ans value is ${ans}`);