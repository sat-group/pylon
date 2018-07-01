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

# How to get all implications for each variable?

```
java -jar up.jar <cnf-file:string>
```

Example:
```
java -jar up.jar pairwise-n5.cnf
```
The above command will print the following output:

```
1,-2,1
1,-3,1
1,-4,1
1,-5,1
2,-1,1
2,-3,1
2,-4,1
2,-5,1
3,-1,1
3,-2,1
3,-4,1
3,-5,1
4,-1,1
4,-2,1
4,-3,1
4,-5,1
5,-1,1
5,-2,1
5,-3,1
5,-4,1
```

This shows that if x1=true then this implies that x2=false,x3=false,x4=false,x5=false.

We can check that the pairwise encoding maintains arc consistency via unit propagating since for all x_i (1 <= i <= 5) we have that x_i => not x_j (1 <= j <= 5 and i != j).

You can also see that the pairwise encoding has the shortest propagation distance since once you set x1=true, it can derive x2=false, x3=false, x4=false, x5=false with an average shortest distance of 1!

Another example:
```
java -jar up.jar sequential-n5.cnf
```

The above command will print the following output:
```
6,-1,1
7,-2,1
7,-6,1
7,-1,2
8,-3,1
8,-7,1
8,-2,2
8,-6,2
8,-1,3
9,-4,1
9,-8,1
9,-3,2
9,-7,2
9,-2,3
9,-6,3
9,-1,4
1,6,1
1,7,2
1,-2,2
1,8,3
1,-3,3
1,9,4
1,-4,4
1,-5,5
2,7,1
2,-6,1
2,8,2
2,-3,2
2,-1,2
2,9,3
2,-4,3
2,-5,4
3,8,1
3,-7,1
3,9,2
3,-4,2
3,-2,2
3,-6,2
3,-5,3
3,-1,3
4,9,1
4,-8,1
4,-5,2
4,-3,2
4,-7,2
4,-2,3
4,-6,3
4,-1,4
5,-9,1
5,-4,2
5,-8,2
5,-3,3
5,-7,3
5,-2,4
5,-6,4
5,-1,5
6,7,1
6,-2,1
6,8,2
6,-3,2
6,9,3
6,-4,3
6,-5,4
7,8,1
7,-3,1
7,9,2
7,-4,2
7,-5,3
8,9,1
8,-4,1
8,-5,2
9,-5,1
```
Here we can see that even though the sequential encoding maintains arc-consistency, it does so with a larger propagation distance.
