## Iterators in Python
Iterators are objects that enable the traversal through a sequence of values one item at a time.
An Iterator is an object that implement the iterator protocol, which consists of two methods
- `__iter__()`: Returns the iterator object itself
- `__next__()`: Returns the next value in the sequence and raised a `StopIteration` exception when no more items are available

```python
class Squares:
  def __init__(self, start: int, end: int):
    self.start = start
    self.end = end

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.start >= self.end:
      raise StopIteration
    curr = self.start * self.start
    self.start += 1
    return curr

```

## Generators in Python
Generators are special type of function that provides a convenient, built-in way to implement the iterator protocol. Instead of using `return` to give a single value and terminate, generators use the `yield` keyword to pause the execution, return value, and save their internal state.
The function then resumes from where it left off on next call

All Generators are iterators but all Iterators are not generators

```python
def squares(start: int, end: int):
  for i in range(start, end):
    yield i * i

print(squares(1,10))
print(list(squares(1,10)))
```

## Decorators in Python
Decorators are a powerful and elegant way to modify or extend the behavior of function or classes without altering their original source code.

*A decorator essentially a function that takes another function as an argument, adds some functionality, and returns a new function.*


```python
import time


def timer(func):
  def wrapper(*args, **kwargs):
    print(f"Started {func.__name__} Execution")
    start_time = time.perf_counter()
    # execute the passed function
    value = func(*args,**kwargs)

    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Finished {func.__name__} in {run_time} secs")
    return value
  return wrapper

@timer
def perform_operation():
  print("Operation Started")
  time.sleep(10)
  print("Operation Completed")


if __name__ == "__main__":
  perform_operation()
```
