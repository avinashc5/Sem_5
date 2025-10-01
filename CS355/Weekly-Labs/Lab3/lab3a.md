CS355: Programming Paradigms Lab (Autumn 2025)

Lab 3A: Basics of OO Design

⸻

Q1. (A) Create an abstract class Shape with:
	•	an abstract method double area().
	•	an abstract method double perimeter().
(B)	Implement concrete subclasses:
	•	Circle (fields: radius).
	•	Rectangle (fields: width, height).
(C)	Write a ShapeDemo program that stores multiple shapes (of both kinds) in a List<Shape> and prints their areas and perimeters using a loop. Annotate the methods that override their parent versions with the annotation "@Override" before their definition, and find out why is that useful. (Hint: Like HashSet is an implementation of Set, Java provides ArrayList and LinkedList implementations of a List.)

Q2. Add a subclass Square that extends Rectangle, with the constructor correctly initializing the length and the width.
	•	Discuss whether Rectangle <-- Square is a good design choice.
	•	There is a principle called "Liskov Substitution Principle" that says a property satisfied by a parent should also be satisfied by its descendants. Demonstrate a violation of this principle by showing code where substituting a Square for a Rectangle causes confusion.

Q3. (A)	Add a method draw() in Shape.
(B)	Implement draw() for each shape by printing text-based graphics (e.g., “Drawing Circle of radius …”). If you have enthu and you have finished everything else, find some drawing library online and extend this part for a PC.
(C)	Write a program that calls draw() on a List<Shape> with mixed shapes.

Q4. Currently, each shape calculates its own area and perimeter. Suppose you wanted to add a new operation, say scale(double factor), that scales the shape.
	•	Implement scale() for each class.
	•	Then reflect: if instead of scaling, you had to add a new operation (say, “serialize to JSON”), what would be easier — adding it as a method in every subclass, or doing something else? Use your creativity, and ask the TA for hint if needed.
