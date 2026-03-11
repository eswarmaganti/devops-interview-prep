def squares(start: int, end: int):
  for i in range(start, end):
    yield i * i

print(squares(1,10))
print(list(squares(1,10)))