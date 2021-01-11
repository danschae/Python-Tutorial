def get_fibonacci_sequence(n):
  """ Return the `n`th Fibonacci number for position `n`. """
  if 0 <= n <= 1:
   return n

  n_minus1, n_minus2 = 1, 0

  for f in range(n - 1):
   result = n_minus2 + n_minus1
   n_minus2 = n_minus1
   n_minus1 = result
  
  return result

print(get_fibonacci_sequence(5))

