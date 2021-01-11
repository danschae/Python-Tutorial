def sum_eo(n, t):
  answer = 0
  if t != "e" and t != "o" :
    return -1
  elif t == "e":
    for x in range(n):
      if x % 2 == 0:
        answer += x
  elif t == "o":
    for x in range(n):
      if x % 2 != 0:
        answer += x
  return answer


print(sum_eo(10, "e"))