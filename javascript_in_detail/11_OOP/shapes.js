class Shape {
  constructor(_name) {
    var _name = _name;

    this.getName = () => {
      return _name;
    }
  }
}

class Rectangle extends Shape {
  constructor(_name, side1, side2) {
    super(_name);
    this.side1 = side1;
    this.side2 = side2;
  }

  getArea() {
    return this.side1 * this.side2;
  }

  isSquare() {
    return this.side1 === this.side2;
  }
}

var shape = new Shape("hello");
console.log(shape.getName());