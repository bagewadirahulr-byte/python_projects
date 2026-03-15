# odd or even
import random
random_int = random.randint(1, 10)
if random_int % 2 != 0:
    print("odd number is : ", random_int)
else:
    print("even number is : ", random_int)