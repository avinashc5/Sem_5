CS355: Programming Paradigms Lab (Autumn 2025)

Lab 4B: Programming with Streams

⸻

Q1. Copy and paste the definitions of various stream-related procedures from Moodle. Extend the listing to include `stream-ref`, `stream-enumerate-interval`, `stream-filter` and `stream-map`. Also have a version with the list higher order procedures. Write a few programs (such as the second prime number in a large range) and convince yourself that the stream version runs (much) faster than the list version.

Q2. In many applications using streams, we may end up forcing the same promise many times. The solution is to build promises so that the first time they are forced, they store the value that is computed by evaluating them (i.e., the result is memoized within the thunk object representing the promise). Re-implement your definition of delay such that it returns a memoizable promise. Test by checking that the Scheme programs you wrote in Q1 produce the same output as before.

Q3. Write a procedure `take` that extracts the first `n` elements of a stream as a list. Now use `stream-map` to generate an infinite stream of the squares of natural numbers. Write a procedure `take-n-squares` that uses `take` to get the first `n` squares of natural numbers.

> (take-n-squares 5)
(1 4 9 16 25)

Q4. Define a procedure `merge-streams` that takes two increasing streams and merges them (removing duplicates). Define two streams, one to generate all the multiples of 3 and another to generate all the multiples of 5, and then merge both the streams using `merge-streams`.