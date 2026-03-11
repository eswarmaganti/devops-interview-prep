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
  
if __name__ == "__main__":
  for val in Squares(1, 10):
    print(val)