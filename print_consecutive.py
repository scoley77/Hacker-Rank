import math
import random

n = random.randint(1, 101)

string = ''
i = 1
while i <= n:
  string += f"{''.join(str(i))}"
  i += 1
print(string)