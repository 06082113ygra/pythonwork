# 爬山问题，迭代
class Solution:
  def climbStairs(self, n):
    a, b = 1, 2
    for i in range(1, n):
      a, b = b, a + b
      return a

