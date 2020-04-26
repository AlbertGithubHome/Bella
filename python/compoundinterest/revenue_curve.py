#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-4-25 22:20:46
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 计算在不同贷款选择下的收益曲线
#             目前全按照等额本息的方式计算


import numpy as np
import matplotlib.pyplot as plt

phf_loans_rate = 0.0325   # 公积金贷款
com_loans_rate = 0.0490   # 商业贷款

def get_refund_money_every_month(loans_year, loans_money, is_phf):
    """
    :param loans_year:  贷款年限
    :param loans_money: 贷款金额
    :param is_phf:      是否是公积金贷款
    :return:返回每个月交的贷款
    """
    month_rate = (phf_loans_rate if is_phf else com_loans_rate) / 12
    coefficient_a = (1 + month_rate) ** (loans_year * 12)
    refund_money = month_rate * coefficient_a * loans_money / (coefficient_a - 1)
    return refund_money


def get_cur_month_remain_money(earn_money, cur_month, cur_refund, loans_year):
    """
    :brief 計算第n個月工資去除貸款剩下的錢
    :param earn_money:  当月工资
    :param cur_month:   第n个月中的n
    :param cur_month:   当月应该还的贷款
    :param loans_year:  贷款年限
    :return:返回当第n個月工資去除貸款剩下的錢
    """
    if cur_month > loans_year * 12:
        return earn_money
    else:
        return earn_money - cur_refund

def get_list(loans_year, loans_money, is_phf, earn_money, revenue_rate):
    """
    :param loans_year:  贷款年限
    :param loans_money: 贷款金额
    :param is_phf:      是否是公积金贷款
    :param earn_money:  当月工资
    :param revenue_rate:年收益率
    :return:获取对应贷款和收益率的收益列表
    """
    month_refund = get_refund_money_every_month(loans_year, loans_money, is_phf)
    month_revenue_rate = revenue_rate / 12

    revenue_list = []
    revenue_value = 0
    for month in range(1,481):
        month_remain_money = get_cur_month_remain_money(earn_money, month, month_refund, loans_year)
        revenue_value = revenue_value * (1 + month_revenue_rate)+ month_remain_money
        revenue_list.append(revenue_value)

    revenue_list = list(map(lambda x: round(x, 2), revenue_list))
    return revenue_list[::12]



#print(get_refund_money_every_month(10, 580000, True))
#print(get_list(10, 580000, True, 6000, 0.01))

def draw_revenue_line(loans_year, loans_money, is_phf, earn_money, revenue_rate, c, marker, mec):
    revenue_value = get_list(loans_year, loans_money, is_phf, earn_money, revenue_rate)
    X = [x for x in range(len(revenue_value))]
    plt.plot(X, revenue_value, c = c, marker=marker, mec=mec, label=str(loans_year)+'years-'+str(revenue_rate))


def main():

    marker_list = ['x', 'D', 'v', 'o']
    colour_list = ['r', 'g', 'b']

    for c in range(3):
        for x in range(3):
            draw_revenue_line(10* (c + 1), 580000, True, 6000, round((x*2+1) / 100, 2), colour_list[c], marker_list[x], 'm')

    plt.title('recenue curve')
    plt.xlabel('years')
    plt.ylabel('revenue')
    plt.legend(loc=2) # upper left
    plt.show()


if __name__ == '__main__':
    main()

