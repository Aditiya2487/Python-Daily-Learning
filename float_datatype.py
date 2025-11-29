from decimal import Decimal
import math
a=0.1
b=0.2
sum=a+b
print("The sum of",a,"and",b,"is:",sum)
print(sum==0.3)
print(round(sum, 2) == 0.3)
# Using Decimal for precise floating-point arithmetic
a = Decimal("0.1")
b = Decimal("0.2")
sum = a + b
print("The sum of",a,"and",b,"using Decimal is:",sum)
print(sum == Decimal("0.3"))

# Using math.isclose for comparison
a = 0.1
b = 0.2
sum = a + b
print(math.isclose(sum, 0.3))  # True