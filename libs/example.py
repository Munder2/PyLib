# Example of a package
class _Latch:
  def __init__(self):
    self.__state = False
  def __call__(self, a, b):
    self.__state = b or(not a and self.__state)
    return self.__state
latch = _Latch()
