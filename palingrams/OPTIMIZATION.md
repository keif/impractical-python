# Palingrams Optimization

## Overview

Comparison of our implementations against the original from [Impractical Python Projects](https://github.com/rlvaugh/Impractical_Python_Projects/tree/master/Chapter_2) by Lee Vaughan.

- `main.py` - Our refactored version of the original
- `main_optimized.py` - Our optimized implementation

## Optimizations Applied

1. **Precomputed reversed words** - Built a dict of reversed words upfront instead of calling `[::-1]` per iteration
2. **Cached slices** - `rev_suffix` and `rev_prefix` computed once per inner loop iteration
3. **Range starts at 1** - Skips redundant `i == 0` checks
4. **Set for results** - Eliminates duplicate palingrams

## Profiling Results

```
Original:    0.206s total, find_palingrams: 0.198s, 1028 results
Optimized:   0.201s total, find_palingrams: 0.184s, 614 results
```

| Metric | Original | Optimized | Change |
|--------|----------|-----------|--------|
| Total time | 0.206s | 0.201s | -2.4% |
| `find_palingrams` | 0.198s | 0.184s | -7% |
| Function calls | 62,452 | 61,625 | -1.3% |
| Results | 1,028 | 614 | -40% duplicates removed |

## Analysis

The optimizations provide modest gains (~7% in the core function) because:

- The dictionary (~60k words) isn't large enough for dramatic improvement
- Python's string slicing is already efficient
- The `len()` calls (60,389) dominate execution time

The most significant outcome is **duplicate elimination** - the original produced 414 duplicate palingram pairs that the set-based approach removes.

## Baseline Comparison

`cprofile_test_orig.py` profiles just the `find_palingrams()` function in isolation (no sorting or printing) to compare against the original book's implementation:

```
find_palingrams only: 0.194s total, 0.190s in function
```

| Test | Scope | Total | `find_palingrams` |
|------|-------|-------|-------------------|
| `cprofile_test_orig.py` | Function only | 0.194s | 0.190s |
| `cprofile_test.py` | Full main() | 0.206s | 0.198s |
| `cprofile_optimized_test.py` | Full main() | 0.201s | 0.184s |

The ~0.008s difference between the function-only and full main() tests accounts for sorting and printing 1,028 results.

## Recursive Approach

`palingram_recursion.py` implements the algorithm using recursion instead of iteration. However, Python's default recursion limit (~1000) is quickly exceeded when processing a dictionary of ~60k words.

```
RecursionError: maximum recursion depth exceeded
```

While `sys.setrecursionlimit()` can increase this limit, the iterative approach is more practical for large datasets. The recursive version serves as an educational example of converting loops to recursion.

## Running the Profiler

```bash
python palingrams/cprofile_test_orig.py      # function only (baseline)
python palingrams/cprofile_test.py           # our refactored version
python palingrams/cprofile_optimized_test.py # optimized
```
