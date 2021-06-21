# 单词模式匹配
def wordMatch(p, input):
  word = input.split("")
  if len(word) != len(p):
    return False
  hash = {}
  used = {}
  for i in range(len(p)):
    if p[i] in hash:
      if hash[p[i]] != word[i]:
        return False

    else:
      if word[i] in used:
        return False
    hash[p[i]] = word[i]
    used[word[i]] = True
  return True


if __name__ == '__name__':
  exp = 'abba'
  inp = input("enter a string:")
  if wordMatch(exp, inp):
    print("匹配成功！")
  else:
    print("匹配失败！")