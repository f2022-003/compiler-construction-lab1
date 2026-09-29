# Lab-410 — Task 1: Compiler vs Interpreter (Time Comparison)

**Course:** Compiler Construction Lab (Lab-410), Fall 2026 · **CLO1**
**Student:** Usman hassan · **Enrollment No:** f2022-003

Compares how long a compiled language (C++) and an interpreted language (Python)
take to produce output for the same task.

## Programs

| Program | C++ file | Python file | Description |
|---------|----------|-------------|-------------|
| A — Sum loop | `sumA.cpp` | `sumA.py` | Sum of 0 … 99,999,999 |
| B — Recursion | `fibB.cpp` | `fibB.py` | Naive recursive Fibonacci, fib(35) |
| C — Conditionals | `primesC.cpp` | `primesC.py` | Count primes below 200,000 (trial division) |
| D — Sorting | `sortD.cpp` | `sortD.py` | Bubble sort of 5,000 random ints (seed 42) |

## How to reproduce

```bash
# C++ — measure compilation and execution separately
time g++ sumA.cpp -o sumA      # compilation time
time ./sumA                    # execution time

# Python — single step, no compilation
time python3 sumA.py           # total time
```

Repeat for `fibB`, `primesC`, `sortD`. Record the `real` value from `time`.

## Results (measured on Linux, g++ 13.3, Python 3.12)

| Program | g++ compile time (real) | C++ execution time (real) | C++ total | Python total (real) |
|---|---|---|---|---|
| A — Sum loop | 0.652s | 0.105s | **0.757s** | **9.887s** |
| B — Recursion | 0.350s | 0.086s | **0.436s** | **1.691s** |
| C — Conditionals | 0.394s | 0.027s | **0.421s** | **1.083s** |
| D — Sorting | 0.544s | 0.216s | **0.760s** | **2.457s** |

Outputs verified identical across languages: A → `4999999950000000`,
B → `9227465`, C → `17984`, D → sorted min/max pair.

## Reflection (short answers)

1. **Was C++'s total time always higher or lower than Python's? Consistent across all four?**
   C++'s total was lower in every program — consistent across all four.
   Python was ~2.6× slower (C) to ~13× slower (A) than C++'s total.

2. **Did compilation time change much between programs?**
   No — it stayed in a narrow band (0.350s–0.652s). Compile time tracks source
   size and headers included (`<iostream>`, `<vector>`), not the runtime
   workload, and all four sources are small.

3. **Running the same program 100 times — which saves more total time?**
   C++, by far. Compilation is paid once; each extra run costs only execution
   time. E.g. program A: C++ ≈ 0.652 + 100×0.105 ≈ 11.2s vs
   Python ≈ 100×9.887 ≈ 989s — the per-run gap (~94×) compounds every run.

4. **When to prefer compiled vs interpreted?**
   Compiled (C++): performance-critical or repeatedly executed code — heavy
   computation, production systems. Interpreted (Python): one-off scripts,
   prototyping, and cases where development speed beats runtime speed, since
   there is no compile step in the edit–run cycle.

## Files

- `*.cpp` / `*.py` — the eight program sources
- `Lab410_Task1_Report_f2022-003.docx` — the lab submission document
  (name, enrollment no., results table, reflection answers)
