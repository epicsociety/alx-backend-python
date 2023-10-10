# Type hints cheat sheet

## This document is a quick cheat sheet showing how to use type annotations for various common types in Python.

# Variables

Technically many of the type annotations shown below are redundant, since mypy can usually infer the type of a variable from its value. See Type inference and type annotations for more details.

- # This is how you declare the type of a variable

```age: int = 1

# You don't need to initialize a variable to annotate it
a: int  # Ok (no value at runtime until assigned)

# Doing so can be useful in conditional branches
child: bool
if age < 18:
    child = True
else:
    child = False
```

## Useful built-in types

- For most types, just use the name of the type in the annotation
- Note that mypy can usually infer the type of a variable from its value,
- so technically these annotations are redundant

```
x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"
```

- # For collections on Python 3.9+, the type of the collection item is in brackets

```
x: list[int] = [1]
x: set[int] = {6, 7}
```

- ## For mappings, we need the types of both keys and values

```
x: dict[str, float] = {"field": 2.0}  # Python 3.9+
```

- ## For tuples of fixed size, we specify the types of all the elements

```
x: tuple[int, str, float] = (3, "yes", 7.5)  # Python 3.9+
```

- ## For tuples of variable size, we use one type and ellipsis

```
x: tuple[int, ...] = (1, 2, 3)  # Python 3.9+
```

- # On Python 3.8 and earlier, the name of the collection type is capitalized, and the type is imported from the 'typing' module

```
from typing import List, Set, Dict, Tuple
x: List[int] = [1]
x: Set[int] = {6, 7}
x: Dict[str, float] = {"field": 2.0}
x: Tuple[int, str, float] = (3, "yes", 7.5)
x: Tuple[int, ...] = (1, 2, 3)
```

``` from typing import Union, Optional ```

## On Python 3.10+, use the | operator when something could be one of a few types

x: list[int | str] = [3, 5, "test", "fun"] # Python 3.10+

- On earlier versions, use Union

x: list[Union[int, str]] = [3, 5, "test", "fun"]

- Use Optional[X] for a value that could be None

- Optional[X] is the same as X | None or Union[X, None]

x: Optional[str] = "something" if some_condition() else None
if x is not None: # Mypy understands x won't be None here because of the if-statement
print(x.upper())

