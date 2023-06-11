# SIGNPY

A convenient notification tool between python classes.

<br>
<br>

## CONTENTS

This package contains just 3 elements:

* **Signal**: *class*

  the core object of this package, which allows to handle different source of signalling events

<br>

* **connect**: *decorator*

  a decorator to be used to link a target function to an existing signal

<br>

* **emit**: *decorator*

  a decorator which allow the emission of a signal after the execution of a function

<br>
<br>

## EXAMPLES

```python
from signpy import *

connection = 0

# check the standard connection mechanism
def rise_connection(connection: int):
        connection += 1
        print(f"connection = {connection}")

def reset_connection(connection: int):
        connection = 0
        print(f"connection = {connection}")

signal = Signal()
signal.connect(rise_connection)
signal2 = Signal(reset_connection)
print(signal.emit(connection))
print(signal2.emit(connection))

# check the connect decorator
signal3 = Signal()

@connect(signal3)
def connected_fun():
  print("inside connected_fun")

print(signal3.emit())

# check the emit decorator

@emit(signal3)
def emitting_fun(num: int = 2):
  print(f"num={num}")

print(emitting_fun())
```
