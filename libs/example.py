from pl import export

ans = False
def latch(a, b):
  ans = (not(a) or ans) or b
  return ans

export()
