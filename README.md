## Turing's machine simulator

Simple simulator of Turing's machine in Python3.

### Input format
Input format:

`start state`

`accepting state 1` `accepting state 2`...


`current state` `character` -> `destination state` `character to write` `direction to move, can be < or >`

Take a look at `palindrome` or `addition` files for reference.

### How to run
To run:
```
python3 turing.py <filename> <input>
```
e.g.

```
python3 turing.py palingrom "100001"
```

### Interpreting results
I don't really plan on adding any error handling.
If you'll get ACCEPTED message at the end of the run then it means the machine accepts your input.
If you get an error along the way, it means the input is not accepted.
