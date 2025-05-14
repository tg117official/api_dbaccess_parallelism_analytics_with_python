
def increment_salary(salary):
    if salary > 19999 :
        return salary*1.20
    else :
        return salary*1.40

ic_salary = increment_salary(salary=15000)
print(ic_salary)