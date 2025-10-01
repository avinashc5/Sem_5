CS355: Programming Paradigms Lab (Autumn 2025)

Lab 3A: Basics of OO Design

⸻

Q1. (A) Define an abstract class Employee with:
	•	Fields: name, salary.
	•	Abstract method double calculateBonus().
	•	toString() that prints employee details.

(B) Create subclasses:
	•	Manager (bonus = 20% of salary).
	•	Developer (bonus = 10% of salary).
	•	Intern (bonus = fixed ₹500).

	// Create objects of these classes and make them interact in a EmployeeDemo class.

Q2. Write a PayrollSystem class that:
	•	Stores a List<Employee> as a field.
	•	Iterates through and prints salaries, bonuses, and total compensation polymorphically (in a method printPayRoll called in main).
	•	Demonstrates abstraction barriers by being easily extendable to new employee types.

	// Continue with EmployeeDemo being the main class.

Q3. Suppose we add a new subclass Contractor with fields: hourlyRate and hoursWorked.
	•	Show how PayrollSystem requires no change in its iteration code.
	•	Use your code to tell the TA why this is a strong argument for OO design.

	// Have the main class be called PayrollDemo.

Q4. Create an interface Payable with a method `double getPayment()` (invent an implementation).
(A) Now decide:
	•	Should Employee implement Payable?
	•	Should Contractor implement Payable too?
Justify your design choice:

(B) What are the pros and cons of making both implement the same interface?

(C) Does this choice improve extensibility and uniformity in your payroll system?

	// Continue with PayrollDemo being the main class.
