#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-05-23 20:03:36
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 计算等额本息和等额本金各项数据

class HouseLoan(object):
    def __init__(self, loan_money, loan_year, loan_rate):
        """ 构造贷款金额、贷款年限、贷款利率
        :param loan_money: 贷款金额
        :param loan_year:  贷款年限
        :param loan_rate:  贷款利率
        """
        self.loan_money = loan_money            # A
        self.loan_month = loan_year * 12        # k
        self.loan_money_rate = loan_rate / 12   # β

    def get_average_capital_plus_interest_data(self):
        """ 返回等额本息计算方式的总金额、第一个月的还款金额
        计算每个月的还款金额公式 x = A * β * (1 + β) ^ k / [(1 + β) ^ k - 1]
        计算总金额的计算公式 C = x * k
        """
        month_repayment = self.loan_money * self.loan_money_rate * (1+self.loan_money_rate) ** self.loan_month / ((1+self.loan_money_rate) ** self.loan_month - 1)
        return round(month_repayment * self.loan_month, 2), round(month_repayment, 2)

    def get_average_capital(self):
        """ 返回等额本金计算方式的总金额、第一个月的还款金额
        计算第一个月的还款金额公式 x = A / k + A * β
        计算总金额的计算公式 C = A + A * β * (k + 1) / 2
        """
        fisrt_month_repayment = self.loan_money / self.loan_month + self.loan_money * self.loan_money_rate
        total_repayment = self.loan_money + self.loan_money * self.loan_money_rate * (self.loan_month+1) / 2
        return round(total_repayment, 2), round(fisrt_month_repayment, 2)


if __name__ == '__main__':
    loan = HouseLoan(580000, 10, 0.0325)
    print(loan.get_average_capital_plus_interest_data())
    print(loan.get_average_capital())
