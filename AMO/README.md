# How to create a given encoding with n variables?

Example:
```
python amo.py Pairwise 10

```
Will print the pairwise encoding for x_1 + ... + x_10 <= 1.

# How to check if an encoding is correct?

Example:
```
python amo-checker.py Pairwise
```

Will run the encoding using n={2..20} and check if the current encoding obeys the specification x_1 + ... + x_n <= 1.

# Which at-most-one encodings are currently available?

The following encodings are available in amo.py:
- Pairwise
- Sequential
