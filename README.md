# Button Coding Challenge Documentation
## Rakesh Chatrath
### 2.13.2017
---
### To run:
```sh
# Button/

python button_coding_challenge.py
```
---
The challenge given was to flatten an arbitrarily-deep nested array-like
structure and remove any null values. The language of choice used was Python.

### How it works
This program utilizes recursion to flatten the list. It's advantages are that
it's relatively simplistic in usage and is an O(n) algorithm. However, compared
to strict iteration, it has more overhead due to the added method calls. Likewise,
it returns a copy of an array, which for larger arrays passed through, could impose
memory constraints.

All things said, the program works as follows:
* It steps through the array value by value and checks if it's a list
  - If it's not a list, it yields that value and continues the iteration.
  - If the value is a list, we call `flatten` on the value, and proceed to
    iterate over the sublist value by value, yielding non-list values
    until we hit another list.

In practice we see the following results for speed:
* Arrays of size 100 (arbitrary number of nests) averaged over 100 trials: 0.000498ms
* Arrays of size 1000 (arbitrary number of nests) averaged over 100 trials: 0.000501ms
* Arrays of size 10000 (arbitrary number of nests) averaged over 100 trials: 0.00214ms

As we can see the speed of the algorithm seems to hold up even with large arrays. 
