# 两数之和
def threeSum(nums, target):

  m = {}  # 存储将列表元素和其下标 构建的键值对
  for i in range(len(nums)):
    m[nums[i]] = i

  l = []
  for a in range(len(nums)):
    for b in range(len(nums)):
      c = target - (nums[a] + nums[b])
      if (a != b) and c in nums and (a != m[c]) and (b != m[c]):
        l.append(sorted([nums[a], nums[b], c]))
  #    return(list(list(t) for t in(set([tuple(t) for t in l]))))
  return ([list(t) for t in (set([tuple(t) for t in l]))])


nums = [-1, 0, 1, 2, -1, -4]
target = 0
print(threeSum(nums, target))