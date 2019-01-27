name =input("Name:")
age =int (input("Age:"))
job =input("Job:")
salary =input("Salary:")
if salary.isdigit(): #长的像不像数字
    salary=int(salary)
# else:
#     exit("must input salary")
msg ='''
    - - - - - - - - info of %s- - - - - - -
    Name:%s
    Age:%s
    Job:%s
    Salary:%d
    You will be retired in %s years
    - - - - - - - - - end- - - - - - - - - -
'''%(name,name,age,job,salary,65-age)

print(msg)
