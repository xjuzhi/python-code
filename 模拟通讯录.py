# -*- codeing = utf-8 -*-
# @time   :  2022/5/12 13:59
# @Auther :  xjuzhi
# @file   :  模拟通讯录.py
mail = {}  # 空通讯录
# 通讯录存储开始
value_name = input("请输入要存储的联系人姓名:")
value_number = input("请输入要存储的联系人电话号码:")
while len(value_number) != 11:  # 判断输入电话号码是否正确
    print("输入电话号码有误，请从新输入:")
    value_number = input("请重新输入要存储的联系人电话号码:")
mail[value_name] = value_number  # 将获取的值保存到字典里边
print(mail)
# 通讯录存储结束
# 通讯录查询开始
find_name = input("请输入要查询的姓名:")
print(mail.get(find_name, "通讯录不存在此人"))  # 通过get获取值，不存在则输出后面语句
# 通讯录查询结束
# 通讯录修改开始
al_name = input("请输入要修改的姓名:")
al_name_1 = input("请输入修改后的姓名:")
if al_name != al_name_1:  # 判断修改前后姓名是否一样，一样则不修改
    mail[al_name_1] = mail[al_name]  # 将新的键值替代旧的键值
    del mail[al_name]  # 删除旧键值
print(mail)
al_name_number = input("请输入要修改电话号码的姓名:")
al_number = input("请输入要修改的电话号码:")
if mail[al_name_number] != al_number:  # 判断修改前后电话号码是否一样，一样则不修改
    while len(al_number) != 11:  # 判断电话号码是否正确
        al_number = input("输入有误，请重新输入要修改的电话号码:")
    mail[al_name_number] = al_number  # 将新电话号码值替代原本的旧值
print(mail)
# 通讯录修改结束
# 通讯录遍历开始
for key, value in mail.items():
    print("姓名：{},电话号码：{}".format(key, value))
# 通讯录遍历结束
