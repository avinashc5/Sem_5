CS355: Programming Paradigms Lab (Autumn 2025)

Lab 2A: Higher Order Functions

⸻

Q1. Define a recursive procedure lcm that takes two positive numbers as arguments and returns their least common multiple. (Hint: use the relation lcm(a, b) = (* a b) / (gcd a b)).

Q2. Suppose we represent points in 2D as pairs (x . y).
(A) Define a procedure (slope p1 p2) that computes the slope of the line between points p1 and p2.
(B) Extend the abstraction so that slopes are always returned in lowest terms as rationals.

Q3. Extend the Church numerals defined in class with the following procedures:
(A) A procedure church-min that returns the smaller of two numerals.
(B) Verify if church-min behaves as expected by converting the results to integers using a procedure church->int.
(C) A procedure int->church that converts positive integers to Church numerals.

Q4. Design a small pipeline (a single top-level function called `process`) that takes a list of integers and produces the product of all squares of odd numbers less than 20.

Example: `(process '(3 8 11 25 4 7)) --> product of (9 121 49) = 53361.`

Q5. Higher-order functions often let us write concise "domain-specific languages". Identify one non-numerical domain (e.g., working with strings, trees, or files) where map, filter, or fold would yield a clean solution. Briefly sketch an example (pseudocode is fine).