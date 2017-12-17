# python3.6.3 挑战1

import sys
if len(sys.argv) != 2:
    print('params error')
    exit()
try:
    salary = int(sys.argv[1])
except ValueError:
    print("please enter number!")
    exit()
START_MONEY = 3500
should_count = salary  - START_MONEY
if should_count <= 1500:
    payable = should_count * 0.03 - 0
elif 1500 < should_count <= 4500:
    payable = should_count * 0.1 - 105
elif 4500 < should_count <= 9000:
    payable = should_count * 0.2 - 555
elif 9000 < should_count <= 35000:
    payable = should_count * 0.25 - 1005
elif 35000 < should_count <= 55000:
    payable = should_count * 0.3 - 2755
elif 55000 < should_count <= 80000:
    payable = should_count * 0.35 - 5505
else:
    payable = should_count * 0.45 - 13505
payable = format(payable, ".2f")
print(payable)
