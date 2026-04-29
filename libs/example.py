# Example of a package
ans = False
def latch(a, b):
  global ans
  ans = (not(a) or ans) or b
  return ans
