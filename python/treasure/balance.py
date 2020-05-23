#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-5-23 21:16:10
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 计算各种选择最终的财富值

from houseloan import HouseLoan
import matplotlib.pyplot as plt

class LoanBalance(object):
    def __init__(self, money, year, loan_rate, investment_rate):
        self.money = money
        self.year = year
        self.loan_rate = loan_rate
        self.investment_rate = investment_rate

        self.loan_object = HouseLoan(self.money, self.year, self.loan_rate)
        self.month_loan_rate = self.loan_rate / 12
        self.total_month = self.year * 12

        self.month_investment_rate = self.investment_rate / 12

    def calc_whole_loan(self, show_msg=False):
        """
        在有全款的情况下，计算交完首付后全贷款，采用等额本息的还款方式
        """
        total_money, month_repayment = self.loan_object.get_average_capital_plus_interest_data()
        final_money = self.money * (1 + self.month_investment_rate) ** self.total_month
        if show_msg:
            print(total_money, month_repayment)
            print('采用【贷款】的情况下，贷款还完时手中财富{0:.2f}, 本金[{1:.2f}]+利息[{2:.2f}]'.format(final_money, self.money, final_money - self.money))
        return final_money


    def calc_no_loan(self, show_msg=False):
        """
        在有全款的情况下，计算直接交全款，将原来需要交的每月房贷进行等利率投资
        """
        total_money, month_repayment = self.loan_object.get_average_capital_plus_interest_data()
        final_money = 0
        for i in range(self.total_month):
            final_money = final_money * (1 + self.month_investment_rate) + month_repayment
        if show_msg:
            print('采用【全款】的情况下，贷款还完时手中财富{0:.2f}, 本金[{1:.2f}]+利息[{2:.2f}]'.format(final_money, total_money, final_money - total_money))
        return final_money

def diff_loan():
    diff_range = 60
    x = [i * 0.001 for i in range (diff_range)]
    y = []
    y1 = []
    y2 = []
    for i in range(diff_range):
        balance = LoanBalance(580000, 10, 0.0325, x[i])
        a1 = balance.calc_whole_loan()
        a2 = balance.calc_no_loan()
        diff_value = a1 - a2
        y.append(diff_value)
        y1.append(a1)
        y2.append(a2)

    plt.title("loan simple demo")
    plt.xlabel("rate")
    plt.ylabel("treasure")
    plt.plot(x, y, marker='x')
    plt.plot(x, y1, marker='D')
    plt.plot(x, y2, marker='o')
    plt.show()



if __name__ == '__main__':
    balance = LoanBalance(580000, 10, 0.0325, 0.0326)
    diff_value = balance.calc_whole_loan(True) - balance.calc_no_loan(True)
    print('贷款-全款 收益差值{}'.format(diff_value))

    diff_loan()

