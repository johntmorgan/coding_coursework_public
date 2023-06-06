console.log(Math.random());


const Grid = require('./grid').gridClass;
// Create MazeSolver class below
class MazeSolver extends Grid{
    constructor(arr){
        super(arr); // initialize the grid
    }
    canTraverse(x,y){
        // check bounds
        if (x < 0 || y < 0)
            return false;
        else if (x >= this.grid.length)
            return false;
        else if (y >= this.grid[x].length)
            return false;
        // check if 0 or not
        else if(this.grid[x][y]===0)
            return false;
        else
            return true; // all passsed
    }
    getNeighbours(x,y){
        // return array of neighbours
        var neighbours = [];
        // up
        if(this.canTraverse(x-1, y))
            neighbours.push([x-1,y]);
        // down
        if(this.canTraverse(x+1, y))
            neighbours.push([x+1,y]);
        // left
        if(this.canTraverse(x, y-1))
            neighbours.push([x,y-1]);
        // right
        if(this.canTraverse(x, y+1))
            neighbours.push([x,y+1]);
        return neighbours;
    }

    checkVisited(x,y,visited){
        // traverse array for visited
        // console.log(x,y,visited)
        for(var i= 0; i< visited.length; i++){
          if(visited[i][0]=== x && visited[i][1]===y){
                return true;
            }
        }
        return false;
    }
    solve(x1,y1, x2, y2){
        var stack = [];
        var visited = [];
        if (this.canTraverse(x1, y1))
            stack.push([x1, y1]);
        while (stack.length > 0) {
            console.log(stack);
            var curr = stack.pop();
            var x = curr[0];
            var y = curr[1];
            if (x === x2 && y === y2)
                return true;
            if (!this.checkVisited(x, y, visited)) {
                visited.push([x, y]);
                var neighbours = this.getNeighbours(x, y);
                for (var i = 0; i < neighbours.length; i++) {
                    var nx = neighbours[i][0]
                    var ny = neighbours[i][1]
                    if (!this.checkVisited(nx, ny, visited)) {
                        stack.push(neighbours[i]);
                    }
                }
            }
        }
        return false;
    }
}