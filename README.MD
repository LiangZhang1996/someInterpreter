# Rquirements:
    python3

# Functions used:

-  `load(fname)`
  --input the filename 'fname', print the rules and return
    the head and atoms of this rules.

- `is_valid_kb(head)`
  --determine the KB if is valid or not throung the head.

- `tell(atoms, meomory)`
  -- inputs the atoms and meomory of the interpeter,
    compare them to see if already known.

- `infer_all(head_meomory, head_atoms_meomory, meomory, Nmeomory)`
    `head_meomory`: save head of a KB
    `head_atoms_meomory`: save atoms of a KB the same as head
    `meomory`: save the tell input
    `Nmeomory`: save the known and inferred atoms
    Just use as the assignments showed.

- `myInterpreter()`
  -- the interpreter of our work
    It use commands: load, tell, infer_all
    Use an infinite loop, recongnize commands and run them.

# How to use
1. run the main.py and then come into the interpreter
2. load example.txt which contains rules
3. tell new atoms
4. infer these atoms