# C Programming Practice Bank — Increment (`++`) & Decrement (`--`) Operators
**Scope:** Variables → Operators → Control Statements → Loops → Functions → Arrays
**Total problems:** 105 | Organized by topic and difficulty (Basic → Intermediate → Advanced)

> These are practice/output-prediction/debugging questions only — no solutions included, so you can attempt each one yourself first.

---

## Section 1: Core Concept — Pre vs Post (Basic)

1. What is the difference between `++a` and `a++`? Write two snippets that prove the difference through output.
2. Predict the output: `int a = 5; printf("%d %d", a++, a);`
3. Predict the output: `int a = 5; printf("%d %d", ++a, a);`
4. What will `int a = 5, b; b = a++;` store in `b` and `a`?
5. What will `int a = 5, b; b = ++a;` store in `b` and `a`?
6. Predict output: `int x = 10; x--; --x; printf("%d", x);`
7. Predict output: `int x = 10; printf("%d", x--); printf("%d", x);`
8. Write a program that shows pre-increment and post-increment give the same final value of the variable, but different values when *used in an expression*.
9. What is the value of `a` after `int a = 1; a = a++;`? Explain why this is undefined/compiler-dependent behavior.
10. Predict output: `char c = 'A'; c++; printf("%c", c);`
11. Predict output: `char c = 'z'; c--; printf("%c", c);`
12. What happens when you apply `++` or `--` to a `float`/`double` variable? Predict: `float f = 2.5; f++; printf("%.2f", f);`

---

## Section 2: Increment/Decrement Inside Expressions (Basic–Intermediate)

13. Predict output: `int a = 5; int b = a++ + ++a; printf("%d %d", a, b);`
14. Predict output: `int a = 5; int b = ++a + a++; printf("%d %d", a, b);`
15. Predict output: `int a = 5; int b = a++ + a++; printf("%d %d", a, b);`
16. Predict output: `int a = 5; int b = ++a + ++a; printf("%d %d", a, b);`
17. Why is `a++ + ++a` considered undefined behavior in C? Explain using sequence points.
18. Predict output: `int i = 1; printf("%d %d %d", i++, i++, i++);` — why can real compilers disagree here?
19. Predict output: `int x = 5; int y = x++ * 2; printf("%d %d", x, y);`
20. Predict output: `int x = 5; int y = ++x * 2; printf("%d %d", x, y);`
21. Predict output: `int a = 2, b = 3; int c = a++ + b--; printf("%d %d %d", a, b, c);`
22. Predict output: `int a = 5; if (a++ == 5) printf("yes"); else printf("no"); printf(" %d", a);`
23. Predict output: `int a = 5; if (++a == 5) printf("yes"); else printf("no"); printf(" %d", a);`
24. Write an expression using only one variable `a` and increment/decrement operators such that the result is always `0`, regardless of `a`'s starting value (explain why).

---

## Section 3: Operator Precedence & Combined Operators (Intermediate)

25. Predict output: `int a = 5; a = a++ + 1; printf("%d", a);`
26. Predict output: `int a = 5; int b = -a++; printf("%d %d", a, b);`
27. Predict output: `int a = 5; int b = -(-a--); printf("%d %d", a, b);`
28. Predict output: `int a = 5, b = 10; a += b--; printf("%d %d", a, b);`
29. Predict output: `int a = 5; printf("%d", a++ == 5 && a++ == 6);` then print `a`.
30. Predict output involving short-circuit evaluation: `int a = 0; if (a-- && a++) printf("A"); else printf("B"); printf("%d", a);`
31. Predict output: `int a = 5; printf("%d", a-- > 0 || a++ > 0); printf(" %d", a);`
32. Explain the difference in evaluation order risk between `a++ + b++` and `a += 1; b += 1;`.
33. Predict output: `int a = 3; int result = (a++, ++a, a--); printf("%d %d", a, result);` (comma operator).
34. Write code demonstrating how the ternary operator interacts with post-increment: `int a = 5; int b = (a > 0) ? a++ : --a; printf("%d %d", a, b);`

---

## Section 4: Boundary, Overflow & Type Behavior (Intermediate–Advanced)

35. Predict output: `unsigned char c = 255; c++; printf("%d", c);` — explain the wraparound.
36. Predict output: `unsigned char c = 0; c--; printf("%d", c);` — explain underflow.
37. Predict output: `int a = 2147483647; a++; printf("%d", a);` (signed int overflow — explain UB vs typical behavior).
38. Predict output: `short s = 32767; s++; printf("%d", s);`
39. Predict output: `unsigned int u = 0; u--; printf("%u", u);`
40. Compare: what is the difference in behavior/UB status between signed integer overflow and unsigned integer overflow in increment operations?
41. Predict output: `char ch = 127; ch++; printf("%d", ch);` (assume signed char, 8-bit).
42. Write code to detect (without triggering UB) whether incrementing a given signed `int` would overflow, before doing it.

---

## Section 5: Loops — `for` (Basic–Intermediate)

43. Write a `for` loop that prints 1 to 10 using post-increment in the update expression.
44. Write a `for` loop that prints 10 to 1 using post-decrement.
45. Predict output: `for (int i = 0; i < 5; i++) printf("%d ", i);` vs `for (int i = 0; i < 5; ++i) printf("%d ", i);` — is there any observable difference here? Why or why not?
46. Write a `for` loop that increments `i` by 2 each time from 0 to 20 (even numbers).
47. Write a `for` loop with **two** loop variables, one incrementing and one decrementing simultaneously, e.g., print pairs `(i, j)` where `i` goes 0→9 and `j` goes 9→0.
48. Predict output: `for (int i = 0, j = 10; i < j; i++, j--) printf("%d-%d ", i, j);`
49. Debug this loop (find the bug): 
    ```c
    for (int i = 0; i <= 10; i++);
        printf("%d ", i);
    ```
50. Debug this infinite loop:
    ```c
    for (int i = 10; i > 0; i++)
        printf("%d ", i);
    ```
51. Write a `for` loop that skips printing every 3rd number (using increment logic and modulo), from 1 to 30.
52. What's the difference between `i++` and `++i` when used purely as the *update expression* of a `for` loop (not in any other expression)? Justify with reasoning, not just "no difference."

---

## Section 6: Loops — `while` and `do-while` (Basic–Intermediate)

53. Write a `while` loop that counts down from a user-given number to 0 using `--`.
54. Write a `do-while` loop that always executes at least once, incrementing a counter, and prints numbers till it reaches 5.
55. Predict output: 
    ```c
    int i = 5;
    while (i--) printf("%d ", i);
    ```
56. Predict output:
    ```c
    int i = 5;
    while (--i) printf("%d ", i);
    ```
57. Explain the output difference between Q55 and Q56 in terms of when the decrement happens vs when it's tested.
58. Debug this code (find the logic error causing wrong loop count):
    ```c
    int i = 1;
    while (i < 10) {
        printf("%d ", i);
    }
    ```
59. Write a `do-while` loop to reverse the digits of a number using increment/decrement logic for digit counting.
60. Predict how many times this loop runs and what it prints: `int n = 0; do { printf("%d ", n); n++; } while (n < 0);`

---

## Section 7: Increment/Decrement with Conditionals (Intermediate)

61. Write a program that uses `if-else` with post-increment to count how many numbers from 1–100 are divisible by 7, incrementing a counter conditionally.
62. Predict output: 
    ```c
    int a = 5, count = 0;
    if (a-- > 0) count++;
    if (a-- > 0) count++;
    if (a-- > 0) count++;
    printf("%d %d", a, count);
    ```
63. Write a `switch` statement where `case` values are determined using a variable that gets incremented before the switch runs.
64. Predict output: 
    ```c
    int x = 3;
    switch (x++) {
        case 3: printf("three"); break;
        case 4: printf("four"); break;
    }
    printf(" %d", x);
    ```
65. Write nested `if` statements that decrement a "lives" counter and print a "Game Over" message when it reaches 0, simulating a simple counter-based game state.

---

## Section 8: Nested Loops & Patterns (Intermediate–Advanced)

66. Print a right-angled triangle pattern of stars using nested loops, where the inner loop bound depends on an incrementing outer loop variable.
67. Print an inverted triangle pattern using decrementing loop bounds.
68. Print a pyramid pattern (centered triangle) using a combination of incrementing space-counters and star-counters.
69. Print a diamond pattern combining increasing then decreasing row widths.
70. Print a number pattern where each row increments (e.g., `1`, `1 2`, `1 2 3`, ...).
71. Print a number pattern where each row's numbers decrement (e.g., `3 2 1`, `2 1`, `1`).
72. Write nested loops to print a multiplication table (1 to 10) using only increment operators for both row and column control.
73. Debug this nested-loop pattern code where the pattern comes out misaligned:
    ```c
    for (int i = 1; i <= 5; i++) {
        for (int j = 5; j >= i; j--)
            printf(" ");
        for (int k = 1; k <= i; k++)
            printf("*");
        printf("\n");
    }
    ```
74. Predict how many total `*` characters get printed by a nested loop where outer `i` goes 1→n (increment) and inner `j` goes 1→i (increment). Write the formula and verify with code for n = 5.

---

## Section 9: Functions & Call Semantics (Intermediate–Advanced)

75. Predict output:
    ```c
    void increment(int x) { x++; }
    int main() {
        int a = 5;
        increment(a);
        printf("%d", a);
    }
    ```
    Explain why the value of `a` does NOT change (call by value).
76. Rewrite Q75's function using a pointer parameter so that calling it actually increments `a` in `main`.
77. Predict output:
    ```c
    int counter = 0;
    void inc() { counter++; }
    int main() {
        inc(); inc(); inc();
        printf("%d", counter);
    }
    ```
    (global variable behavior)
78. Write a recursive function `countdown(int n)` that prints numbers from `n` down to `1` using decrement logic within recursive calls (no loop allowed).
79. Write a recursive function `countup(int n, int limit)` that prints numbers increasing from `n` to `limit`.
80. Predict output:
    ```c
    int f(int *x) {
        (*x)++;
        return (*x)++;
    }
    int main() {
        int a = 5;
        int b = f(&a);
        printf("%d %d", a, b);
    }
    ```
81. Write a function `int fact(int n)` (factorial) using a `for` loop with post-increment, and trace through `fact(5)` by hand before coding.
82. Explain a scenario where passing `i++` as a function argument multiple times in the same statement (e.g., `foo(i++, i++);`) is dangerous/undefined, and how to avoid it.

---

## Section 10: Arrays — Traversal & Basic Manipulation (Intermediate)

83. Write a program to print all elements of an array using a `for` loop with `i++` as the index update.
84. Write a program to print all elements of an array in reverse using a `for` loop with `i--`.
85. Write a program that uses two indices — one starting at 0 incrementing, one starting at `n-1` decrementing — to check if an array is a palindrome.
86. Write a program to find the sum of all array elements using an incrementing loop counter.
87. Write a program to find the largest element in an array, incrementing an index while comparing with a "max so far" variable.
88. Write a program to count how many elements in an array are even, using a counter variable incremented conditionally inside the loop.
89. Write a program to reverse an array *in place* by swapping elements from both ends, moving one index forward (`++`) and one backward (`--`) until they meet/cross.
90. Predict output of this array traversal bug:
    ```c
    int arr[5] = {1,2,3,4,5};
    for (int i = 0; i <= 5; i++)
        printf("%d ", arr[i]);
    ```
    Explain the off-by-one bug and why it's dangerous (undefined behavior / out-of-bounds access).
91. Write a program that shifts every element of an array one position to the left, using incrementing indices, and fills the last position with 0.
92. Write a program that shifts every element of an array one position to the right using decrementing indices (why must you go backward here, not forward?).
93. Write a program to remove duplicate elements from a sorted array in place, using two pointers/indices — one incrementing for reading, one incrementing conditionally for writing.
94. Write a program to merge two sorted arrays into a third array using three separate indices, each incrementing independently.

---

## Section 11: Arrays — Search, Frequency & Counting (Intermediate–Advanced)

95. Write a linear search function that increments an index until it finds the target or reaches the end of the array; return the found index or -1.
96. Write a program to count the frequency of each element in an array (values 0–9) using a frequency/count array and incrementing the relevant slot.
97. Write a program to find the second-largest element in an array in a single pass, incrementing the index and updating two "largest so far" trackers.
98. Write a program that counts how many times the array elements strictly increase from one index to the next (i.e., `arr[i+1] > arr[i]`), incrementing a counter each time this condition is true.
99. Write a program to find the first non-repeating element in an array using a frequency array and incrementing counters.
100. Debug this frequency-counting code (find the bug):
    ```c
    int freq[10] = {0};
    for (int i = 0; i < n; i++) {
        freq[arr[i]]++;
    }
    for (int i = 0; i <= 10; i++)
        printf("%d occurs %d times\n", i, freq[i]);
    ```

---

## Section 12: Advanced / Tricky Combined Challenges

101. Predict the final array contents:
    ```c
    int arr[5] = {1,2,3,4,5};
    int i = 0;
    while (i < 5) {
        arr[i++]++;
    }
    // print arr
    ```
102. Predict output:
    ```c
    int arr[5] = {10,20,30,40,50};
    int i = 0, j = 4;
    while (i < j) {
        arr[i++] += arr[j--];
    }
    // print arr
    ```
    Trace through this carefully — does `i` and `j` update before or after the addition? What's the final array?
103. Predict output (index self-modification trap):
    ```c
    int arr[5] = {0,1,2,3,4};
    int i = 0;
    while (i < 5) {
        arr[i] = arr[i++] + 1;
    }
    // print arr — is this well-defined? explain
    ```
104. Write a program that uses only increment/decrement operators (no `+`, `-`, `+=`, `-=` on the loop/index variables) to compute the sum of the first `n` natural numbers, and separately their factorial, both via loops.
105. **Capstone problem:** Given an array of integers, write a program that in a single pass (one `for` loop, index incrementing) simultaneously: (a) counts even numbers, (b) counts odd numbers, (c) finds the max, (d) finds the min, and (e) computes the sum — using only one loop counter that increments once per iteration. Explain why this is more efficient than five separate loops.

---

### How to use this bank
- **Sections 1–4**: pure conceptual/output-prediction — do these on paper first, then verify by compiling.
- **Sections 5–8**: loop-control practice — focus on *when* the increment/decrement actually happens relative to the loop condition check.
- **Sections 9**: understand call-by-value vs pointer-based modification before moving to arrays.
- **Sections 10–12**: array problems — these are the ones most likely to appear in your practice sets, since array + index manipulation is where `++`/`--` bugs (off-by-one, out-of-bounds) most commonly happen.

Good luck — attempt each one yourself before checking a compiler or asking for help on a specific one.
