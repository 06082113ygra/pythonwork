# 硬币找零
def get_min_coins(coin_combinations, amount_rem):
  coin_list = []

  sorted_coin_combinations = sorted(coin_combinations, reverse=True)   #将面值从大到小进行排序

  for coin_val in sorted_coin_combinations:
    coin_count = int(amount_rem / coin_val)    # 计算每个面值的个数（换成零钱时）
    coin_list += [coin_val] * coin_count       # 将零钱放入到输出列表

    amount_rem -= coin_val * coin_count         # 找零之后，剩下的钱
    if amount_rem <= 0:
      break
  if amount_rem != 0:
    print("无法找零！")
  else:
    return coin_list

if __name__ == '__main__':
  n = (int)(input("请输入面值个数："))
  coin_combinations = [0.5, 1, 0.2, 0.1, 1]
  for i in range(n):
    coin_combinations.append((int)(input("面值：")))
  money = (int)(input("需要找的零钱："))
  print(get_min_coins(coin_combinations, money))
