## geometric_lib: Library of geometric shapes


- Hash: b5b0fae — L-04: Update docs for calculate.py
- Hash: d76db2a — L-04: Add calculate.py
- Hash: 51c40eb — L-04: Doc updated for triangle
- Hash: d080c78 — L-04: Triangle added
- Hash: d078c8d — L-03: Docs added
- Hash: 8ba9aeb — L-03: Circle and square added
General description:

`geometric_lib` is a Python library designed to calculate the area and perimeter of various geometric shapes.
 The library provides a simple and user-friendly interface for working with basic shapes: circle and square
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

Description of functions:

1. `circle.area(r)`:

 Description: Calculates the area of a circle by a given radius.
 Parameters:
 `r` (float): The radius of the circle.
 Returns:
The area of the circle (float).
 Example of a call:
``python
 >>> circle.area(5)
 78.53981633974483
 ```

2. `circle.perimeter(r)`:

 Description: Calculates the perimeter of a circle by a given radius.
 Parameters:
 `r` (float): The radius of the circle.
 Returns:
The perimeter of the circle (float).
 Example of a call:
``python
 >>> circle.perimeter(5)
 31.41592653589793
 ```

3. `square.area(a)`:

 Description: Calculates the area of a square on a given side.
