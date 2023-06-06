var generate = function(length, width, pieces)
{
    var board = []
    for (var i = 0; i < length; i++) {
        var row = new Array(width).fill(" ");
        board.push(row);
    }
    for (var i = 0; i < pieces.length; i++) {
        var piece = pieces[i];
        console.log(piece);
        if (piece.row >= 0 && piece.row < length && piece.col >= 0 && piece.col < width) {
            board[piece.row][piece.col] = piece.value;
        }
    }
    return board
}

var pieces = [ { row: 0, col: 0, value: 'X' },
  { row: 0, col: 1, value: 'O' },
  { row: 0, col: 2, value: 'O' },
  { row: 1, col: 0, value: 'X' },
  { row: 1, col: 1, value: 'X' },
  { row: 1, col: 2, value: 'O' },
  { row: 2, col: 0, value: 'X' },
  { row: 2, col: 1, value: 'O' },
  { row: 2, col: 2, value: 'O' } ]
var board = generate(3, 3, pieces);
console.log(board);

var pieces2 = [ { row: 0, col: 0, value: 'S' },
  { row: 0, col: 1, value: 'T' },
  { row: 0, col: 2, value: 'O' },
  { row: 1, col: 0, value: 'P' },
  { row: 1, col: 1, value: 'B' },
  { row: 1, col: 2, value: 'O' },
  { row: -2, col: 0, value: 'X' },
  { row: 2, col: 1, value: 'O' },
  { row: 2, col: 2, value: 'O' },
  { row: 2, col: 20, value: 'X' } ]
var board = generate(3, 4, pieces2);
console.log(board);

// pieces.forEach(piece => board[piece.row][piece.col] = piece.value);

// var generate = function(length, width, pieces)
// {
//     console.log(pieces)
// }