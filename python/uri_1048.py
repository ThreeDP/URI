def money_earned(percent):
    return salary * (percent / 100)

salary = float(input())

if salary >= 0 and salary <= 400:
    percent = 15
    earned = money_earned(percent)
elif salary > 400 and salary <= 800:
    percent = 12
    earned = money_earned(percent)
elif salary > 800 and salary <= 1200:
    percent = 10
    earned = money_earned(percent)
elif salary > 1200 and salary <= 2000:
    percent = 7
    earned = money_earned(percent)
else:
    percent = 4
    earned = money_earned(percent)

print("Novo salario: {:.2f}".format(salary + earned))
print("Reajuste ganho: {:.2f}".format(earned))
print("Em percentual: {} %".format(percent))
