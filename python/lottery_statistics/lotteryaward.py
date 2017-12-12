#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for statistics of lottery award

__author__ = 'AlbertS'

import csv

# list award classify
award_classify = {
    (6,1): 1,
    (6,0): 2,
    (5,1): 3,
    (5,0): 4,
    (4,1): 4,
    (4,0): 5,
    (3,1): 5,
    (3,0): 0,
    (2,1): 6,
    (2,0): 0,
    (1,1): 6,
    (1,0): 0,
    (0,1): 6,
    (0,0): 0
}

# count red balls and blue balls
def count_red_blue_balls(my_number, history_number):
    red_count, blue_count = 0, 0
    my_index, history_index = 0, 0
    while my_index < 6 and history_index < 6:
        if my_number[my_index] == history_number[history_index]:
            my_index += 1
            history_index += 1
            red_count += 1
        elif my_number[my_index] < history_number[history_index]:
            my_index += 1
        else:
            history_index += 1

    if my_number[6] == history_number[6]:
        blue_count = 1

    return red_count, blue_count

# count award situation of my number
def count_award_situation(my_number):
    local_award_statistics = [0,0,0,0,0,0,0]
    with open('lottery_history_data.csv', 'r') as file:
        data_content = csv.reader(file)
        for row_data in data_content:
            local_award_statistics[award_classify[count_red_blue_balls(my_number, list(map(int, row_data[1:8])))]] += 1
    return local_award_statistics

# show award statictics for a number
def show_award_result(my_number, award_statistics):
    print("my number is %s\n" %  my_number)
    print("history award record list:")

    for index in range(0,7):
        print("award %d: %4d times" % (index, award_statistics[index]))


# main function
if __name__ == '__main__':
    my_number = [5,6,10,11,25,30,11]
    #my_number = [5,8,10,15,26,30,6]
    award_statistics = count_award_situation(my_number)
    show_award_result(my_number, award_statistics)
'''
    print(count_red_blue_balls([1,2,3,4,10,11,13], [2,3,10,11,6,7,13]))
    print(award_classify[(6,1)])
    print(award_classify)
    print(award_classify[count_red_blue_balls([1,2,3,4,10,11,13], [2,3,10,11,6,7,13])])
'''