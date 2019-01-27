#1.0
# _user ="xiaohuo"
# _password="1234"
#
# passed_authentication  =False  #标志位 假，不成立
#
#
# for i in range(3):
#     username =input("Name:")
#     password =input("Password:")
#     if username == _user and password == _password:
#         print("Welcome %s login ....." % _user)
#         passed_authentication=True      #条件成立，真的情况
#         break               #中断，退出
#     else:
#         print("Invalid username or password!")
# if not  passed_authentication:          #只有再True的情况下，条件成立
#     print("要不要脸，臭流氓，小虎")
#
#
# 1.1
# _user ="xiaohuo"
# _password="1234"
#
# for i in range(3):
#     username =input("Name:")
#     password =input("Password:")
#     if username == _user and password == _password:
#         print("Welcome %s login ....." % _user)
#         break               #中断，退出 break for过后，就不会执行最后面的
#     else:
#         print("Invalid username or password!")
# else:          #只有再True的情况下，条件成立
#     print("要不要脸，臭流氓，小虎")

#1.2
_user ="xiaohuo"
_password="1234"

counter = 0
while counter< 3:
    username =input("Name:")
    password =input("Password:")
    if username == _user and password == _password:
        print("Welcome %s login ....." % _user)
        break               #中断，退出 break for过后，就不会执行最后面的
    else:
        print("Invalid username or password!")
    counter += 1
    if counter==3:
        keep_going_choice =input("还想继续尝试吗？[Yes/No]")
        if keep_going_choice=="Yes":
            counter=0
else:          #只有再True的情况下，条件成立
    print("要不要脸，臭流氓，你个糟老头子坏得很！")





