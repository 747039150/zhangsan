"""
print ("你好，张三!") #字符串
print (2333) #整数
print (2.333) #小数
print (True) #布尔值
print (())  #元组
print ([]) #数组
print ({}) #字典
print (3*9)
print (2>3)
print (2.33+4445>400)
name = "张三"
print (name)
"""
'''a = input("输入的内容：")
print ("你输入的内容是："+a)'''
# b = float (input("请输入"))
# c = float (input("请输入"))
# d = float (input("请输入"))
# e = float (input("请输入"))
# i = float (b+c+d+e)
# print (i)

#算出有多少个字符(len())
# a = (input("请输入"))
# b = (input("请输入"))
# i = len(a+b)
# print("你输入了" ,str(i) ,"字符啦啦啦" ) 


# s1 = str (dasdasda"张三");
# s2 = str ("李四");
# s3 = str ("陈五");
# s = str ("他们都是同学："+s1 + s2 + s3)
# print (s)


#元组
# a = (1,2,3,4,5,"尼玛","尼玛","尼玛","尼玛","你妈",True,False)
# print (a[0:5])
# print (a[5:11])
# print (a[11:])
# print (len(a)) 
# print(a[5]) #查找下标为5的值，从0开始算
# print (a.index(input())) #从你输入的值，查找下标
# print (a.count(input())) #查找你输入的值，找到0开始最近那个下标，并且统计出与你输入的值有多少个
# print ("你输入的值下标是：", a.index(input()))



#二维元组
# b = (a,"打工","帅锅")
# print (b[0][3])


#数组
a = [1,2,3,4,5,"尼玛","尼玛","尼玛","尼玛","尼玛","你妈",True,False]
# #a.append("帅哥") #往数组中添加数据
# #a.append(input())#往数组中添加数据键盘上输入
# # a.insert(0,"姐姐")
# #append插入的值默认为是最后一个 insert是可以选择插在哪个下标之的格式:insert(下标,插入内容)
# # print (a)
# # b = a.pop(6)#pop剪切的意思
# # print(a)
# # print(b)
# #a.clear() #clear清空a里面的所有数组
# #print(a)
# x = ["你好","不好"]
# a.extend(x)
# print(a)
# a.remove("尼玛")
# print(a)
#元组与数组的区别，元组不能添加数据，而数组就可以


#字典的特点
"""
1、字典中的值没有顺序
2、字典的结构必须是 键值对的结果 key:value
3、字典的取值，是通过key去取value
"""
# a={"username":"张三","password":"zhangsan","age":"80"}
# # print(a["username"]) #取username的值
# # a["身高"] = "183" #增加一个身高
# # print(a)
# # a["username"] = "李四" #修改username张三的值改为李四
# # print(a)
# b = a.get("username")#取出username里面的值
# print(b)
# b = a.pop("username")#剪切出usename里面的值
# print(b)
# a.update(username="李四")#添加一个username并取值为李四，update可以修改，也可以新增
# print(a)
# a.update(name="陈武")
# print(a)
# del a["password"]
# print(a)
# del a[1]
# print(a)


# a={}
# a["name"] = str (input("请输入你的姓名："))
# a["age"] = int (input("请输入你的身高："))
# a["sex"] = int (input("请输入你的年龄"))
# print(str (a))
# name = a.get("name")
# age = a.get("age")
# sex = a.get("sex")
# print("姓名：" + name)
# print("身高："+ str (age))
# print("年龄:"+ str (sex))