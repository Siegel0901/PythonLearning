# -*- coding = utf-8 -*-
# @Time : 2024/5/26 11:38
# @Author : Siegel
# @File : 16_practice.py
# @Software : PyCharm
"""
编写一个简单的工资管理程序,系统可以管理以下四类人:
    工人(worker)、销售员(salesman)、经理(manager)、销售经理(salesManager)
所有员工都具有员工号,姓名,工资等属性,有设置姓名,获取姓名,获取员工号,计算工资等方法
    1. 工人:工人具有工作小时数和时薪的属性,工资计算方法为工作小时*时薪
    2. 销售员:具有销售额和提成比例的属性,工资计算方法为销售额*提成比例
    3. 经理:具有固定月薪的属性,工资计算方法为固定月薪
    4. 销售经理:工资计算方法为销售额*提成比例＋固定月薪
请根据以上要求设计合理的类,完成以下功能:
    1. 添加所有类型的人员
    2. 计算月薪
    3. 显示所有人工资情况
"""
import time


class Employee:
    __number = str()
    __name = str()
    __salary = float()

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def __init__(self, number, name):
        self.__number = number
        self.__name = name


class Worker(Employee):
    __hour = int()
    __hour_money = float()

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        self.__hour = hour

    @property
    def hour_money(self):
        return self.__hour_money

    @hour_money.setter
    def hour_money(self, hour_money):
        self.__hour_money = hour_money

    def count_salary(self):
        self.salary = self.__hour * self.__hour_money
        return self.salary

    def __init__(self, number, name, hour, hour_money):
        super(Worker, self).__init__(number, name)
        self.__hour = hour
        self.__hour_money = hour_money

    def __str__(self):
        return "{},工人,公司第{}位员工,工作小时数为{},时薪为{},工资为{}".format(self.name, self.number, self.hour, self.hour_money,
                                                            self.salary)


class Salesman(Employee):
    __sale_money = float()
    __rate = float()

    @property
    def sale_money(self):
        return self.__sale_money

    @sale_money.setter
    def sale_money(self, sale_money):
        self.__sale_money = sale_money

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate):
        self.__rate = rate

    def count_salary(self):
        self.salary = self.__sale_money * self.__rate
        return self.salary

    def __init__(self, number, name, sale_money, rate):
        super(Salesman, self).__init__(number, name)
        self.__sale_money = sale_money
        self.__rate = rate

    def __str__(self):
        return "{},销售员,公司第{}位员工,销售额为{},提成为{}%,工资为{}".format(self.name, self.number, self.sale_money, self.rate * 100,
                                                            self.salary)


class Manager(Employee):
    __month_money = float()

    @property
    def month_money(self):
        return self.__month_money

    @month_money.setter
    def month_money(self, month_money):
        self.__month_money = month_money

    def count_salary(self):
        self.salary = self.__month_money
        return self.salary

    def __init__(self, number, name, month_money):
        super(Manager, self).__init__(number, name)
        self.__month_money = month_money

    def __str__(self):
        return "{},经理,公司第{}位员工,月薪为{},工资为{}".format(self.name, self.number, self.__month_money, self.salary)


class SalesManager(Employee):
    __sale_money = float()
    __rate = float()
    __month_money = float()

    @property
    def sale_money(self):
        return self.__sale_money

    @sale_money.setter
    def sale_money(self, sale_money):
        self.__sale_money = sale_money

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate):
        self.__rate = rate

    @property
    def month_money(self):
        return self.__month_money

    @month_money.setter
    def month_money(self, month_money):
        self.__month_money = month_money

    def count_salary(self):
        self.salary = self.__sale_money * self.__rate + self.__month_money
        return self.salary

    def __init__(self, number, name, sale_money, rate, month_money):
        super(SalesManager, self).__init__(number, name)
        self.__month_money = month_money
        self.__sale_money = sale_money
        self.__rate = rate

    def __str__(self):
        return "{},销售经理,公司第{}位员工,销售额为{},提成为{}%,月薪为{},工资为{}".format(self.name, self.number, self.sale_money,
                                                                   self.rate * 100, self.__month_money, self.salary)


company = list()


def main():
    run_flag = True
    while run_flag:
        print("欢迎来到工资管理系统".center(30, '*'))
        print("1. 添加员工".rjust(20, " "))
        print("2. 计算月薪".rjust(20, " "))
        print("3. 显示所有人工资情况".rjust(25, " "))
        print("4. 退出程序".rjust(20, " "))
        print("".center(37, '*'))
        while True:
            choice = input("请选择功能(1234):")
            if choice == '1':
                add_employee()
                input("按任意键继续...")
                break
            elif choice == '2':
                count_month_salary()
                input("按任意键继续...")
                break
            elif choice == '3':
                show_all_salary()
                input("按任意键继续...")
                break
            elif choice == '4':
                print("正在退出程序...")
                run_flag = False
                time.sleep(2)
                break
            else:
                print("请选择正确的功能!")
    else:
        print("退出成功!")


def add_employee():
    print("添加员工".center(35, '-'))
    print("1. 工人".rjust(21, " "))
    print("2. 销售员".rjust(22, " "))
    print("3. 经理".rjust(21, " "))
    print("4. 销售经理".rjust(23, " "))
    print("5. 退出".rjust(21, " "))
    print("".center(38, '-'))
    while True:
        choice = input("请选择添加的员工类型(12345):")
        if choice == '1':
            name = input("请输入工人姓名:")
            hour = int(input("请输入工人工作小时数:"))
            hour_money = float(input("请输入工人时薪:"))
            worker = Worker(len(company) + 1, name, hour, hour_money)
            print("正在添加该工人..")
            time.sleep(0.5)
            company.append(worker)
            print("添加成功!")
            break
        elif choice == '2':
            name = input("请输入销售员姓名:")
            sale_money = float(input("请输入销售员的销售额:"))
            rate = float(input("请输入销售员提成比例:"))
            salesman = Salesman(len(company) + 1, name, sale_money, rate)
            print("正在添加该销售员..")
            time.sleep(0.5)
            company.append(salesman)
            print("添加成功!")
            break
        elif choice == '3':
            name = input("请输入经理姓名:")
            month_money = float(input("请输入经理的月薪:"))
            manager = Manager(len(company) + 1, name, month_money)
            print("正在添加该经理..")
            time.sleep(0.5)
            company.append(manager)
            print("添加成功!")
            break
        elif choice == '4':
            name = input("请输入销售经理姓名:")
            sale_money = float(input("请输入销售经理的销售额:"))
            rate = float(input("请输入销售经理提成比例:"))
            month_money = float(input("请输入销售经理的月薪:"))
            sales_manager = SalesManager(len(company) + 1, name, sale_money, rate, month_money)
            print("正在添加该销售经理..")
            time.sleep(0.5)
            company.append(sales_manager)
            print("添加成功!")
            break
        elif choice == '5':
            print("正在退出添加员工...")
            time.sleep(1)
            print("退出成功!")
            break
        else:
            print("请选择正确的功能!")


def count_month_salary():
    if len(company) == 0:
        print("当前员工人数为0,无需计算工资!")
        return
    print("正在计算所有人的工资...")
    time.sleep(0.5)
    for item in company:
        item.count_salary()
    print("计算成功!")


def show_all_salary():
    if len(company) == 0:
        print("当前员工人数为0!")
        return
    print("正在打印..")
    time.sleep(0.5)
    for item in company:
        print(item)


main()
