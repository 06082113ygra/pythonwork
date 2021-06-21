# 猜数字
def getHint(secret, guess):

  secret_dict = {}
  guess_dict = {}

  A = 0
  B = 0
  for i in range(len(secret)):
    if secret[i] == guess[i]:  # 查找A的数量
      A += 1
    else:
      if secret[i] in secret_dict:
        secret_dict[secret[i]] += 1
      else:
        secret_dict[secret[i]] = 1
      if guess[i] in guess_dict:
        guess_dict[guess[i]] += 1
      else:
        guess_dict[guess[i]] = 1
  # 记录好了数量，接下来根据两个数组中的数的最小值来判断B的数量
  for digit in secret_dict:
    if digit in guess_dict:
      B += min(secret_dict[digit], guess_dict[digit])
  return str(A) + 'A' + str(B) + 'B'