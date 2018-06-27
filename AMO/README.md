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

# How to get all implications for each variable that are 1 distance away (direct implication in the graph)?

```
java -jar up.jar <filename:string> <fixpoint:{0,1}>
```

To get all implications at one step away run the following command:

Example:
```
java -jar up.jar pairwise-n5.cnf 0
```
The above command will print the following output:

```
1,-2
1,-3
1,-4
1,-5
2,-1
2,-3
2,-4
2,-5
3,-1
3,-2
3,-4
3,-5
4,-1
4,-2
4,-3
4,-5
5,-1
5,-2
5,-3
5,-4
```

This shows that if x1=true then this implies that x2=false,x3=false,x4=false,x5=false.

We can check that the pairwise encoding maintains arc consistency via unit propagating since for all x_i (1 <= i <= 5) we have that x_i => not x_j (1 <= j <= 5 and i != j).

# How to get all implications for each variable at any distance, i.e. until fix point?

To get all implications until fix point run the following command:

Example:
```
java -jar up.jar pairwise-n5.cnf 1
```

For this example, we have the same output since the pairwise encoding can achieve arc consistency in one step.
