# Palingrams Optimization

## Overview

Comparison of `main.py` (original) vs `main_optimized.py` with profiling results.

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

## Running the Profiler

```bash
python palingrams/cprofile_test.py           # original
python palingrams/cprofile_optimized_test.py # optimized
```
