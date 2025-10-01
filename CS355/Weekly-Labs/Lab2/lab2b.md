CS355: Programming Paradigms Lab (Autumn 2025)

Lab 2B: Higher Order Functions

⸻

Q1. Define a recursive procedure `gcd` that takes two positive numbers as arguments and returns their greatest common divisor. You can use Euclid’s algorithm, which states that the gcd of two numbers a and b is the same as the gcd of b and r, where r is the remainder when a is divided by b.

Q2. Reckon that the implementation of rational numbers that we used in the class does not reduce a rational number to its lowest terms. For example, after multiplying 2/3 and 3/4, our implementation would give 6/12 instead of 1/2.

* (A) Use the gcd procedure from Q1 to give reduced rational numbers as the outcomes of our rational-number operations.
* (B) Notice that you can apply the reduction logic either in make-rat, or in the numer and denom procedures. Explain to your TA which is better.

Q3. Take the Church Numerals defined in the class (available on Moodle) and extend them with the following procedures:

* (A) A procedure `sub-church` that allows you to subtract one Church numeral from another.
* (B) A procedure `church-<=` that takes two Church numerals `m` and `n` and tells if `m` is less than or equal to `n`.
* (C) A procedure `church->int` that converts a Church numeral to the corresponding Scheme integer.

Q4. Design a small pipeline (a single top-level function) that takes a list of integer pairs `(num denom)`:

1) Converts each pair to a normalized rational.  
2) Filters out rationals greater than 1.  
3) Multiplies the remaining rationals into a single rational result.  

Provide the result for:
  '((1 . 3) (4 . 2) (2 . 5) (3 . 7) (9 . 10))

Q5. Identify a real-world scenario (outside the world of plain numbers) where higher order functions would lead to a very clean program design. Additional PC if you can identify a fairly large program that you yourself wrote as part of some other course assignment or project.