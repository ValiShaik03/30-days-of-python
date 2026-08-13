#Exercise 2
import math_ops
print(math_ops.add(12,8))
print(math_ops.sub(3,9))

# Exercise 3
from math_ops import add
print(add(10,7))

#Exercise 4
import math_ops as mu
print(mu.add(10,8))
print(mu.sub(12,6))

#Exercise 5
import math
print(math.sqrt(25))
print(math.pi)

import random
print(random.randint(1,10))
# Exercise 9
from project.utils.string_utils import to_upper
print(to_upper("vali"))

import project.utils.string_utils as su
print(su.to_upper("vali"))
print(su.to_lower("VALI"))

# Exercise 10
import project.utils

# Exercise 11
from project.utils import to_upper
print(to_upper("vali"))

# Exercise 12
from calculator_pkg import adding,subtr
print(adding(12,4))
print(subtr(6,4))