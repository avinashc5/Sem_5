CS355: Programming Paradigms Lab (Autumn 2025)

Lab 4A: Programming with Streams

⸻

Q1. Copy and paste the definitions of various stream-related procedures from Moodle. Extend the listing to include `stream-ref`, `stream-enumerate-interval`, `stream-filter` and `stream-map`. Also have a version with the list higher order procedures. Write a few programs (such as the second prime number in a large range) and convince yourself that the stream version runs (much) faster than the list version.

Q2. Define a procedure `random-stream` that generates an infinite stream of random integers in the range [0, 99].
	•	Use (random 100) for generating each random number.
	•	Test by extracting the first 10 elements (either using a procedure `take` or multiple applications of `stream-ref`).

Q3. Define a procedure `interleave-streams` that takes two streams and produces a new stream where elements alternate between the two. For example:
```scheme
(interleave-streams (list->stream '(1 2 3 ...)) (list->stream '(a b c ...)))
; -> 1 a 2 b 3 c ...
```
Test it by interleaving natural numbers and Fibonacci numbers.

Q4. Define a procedure `sliding-window` that takes two arguments:
	•	a stream s; and
	•	a window size n,
and returns a new stream of lists, each containing the next n elements from the original stream. Example:
```scheme
(define (naturals-from n)
  (cons-stream n (naturals-from (+ n 1))))
(define naturals (naturals-from 1))

(take (sliding-window naturals 3) 5)
; => ((1 2 3) (2 3 4) (3 4 5) (4 5 6) (5 6 7))
```
