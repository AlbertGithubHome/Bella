#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-11-28 10:35:45
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : a star algorithm

import sys

MAP = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,1,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

class node:
    def __init__(self, g, h, f, pos):
        self.g_score = g
        self.h_score = h
        self.f_score = f
        self.parent_pos = pos

    def show(self):
        print("     node.show({0},{1},{2},({3},{4}))".format(self.g_score , self.h_score, self.f_score, self.parent_pos.x, self.parent_pos.y))

class coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 1024 + self.y

    def show(self):
        print("coord.show({0},{1})".format(self.x , self.y))


open_list = {}
close_list = {}


def find_min_f_in_openlist():
    key = None
    fmin = sys.maxsize
    for k, v in open_list.items():
        if v.f_score < fmin:
            fmin = v.f_score
            key = k
    return (key, open_list.pop(key)) if key else None


def get_distance_between_two_coords(pos1, pos2):
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)


def update_open_list(open_pos, open_node):
    open_pos.show()
    if open_pos not in open_list or open_node.f_score < open_list[open_pos].f_score:
        open_list[open_pos] = open_node


def is_valid_coord(cur_coord):
    if cur_coord in close_list:
        return False

    if cur_coord.x < 0 or cur_coord.x >= len(MAP[0]):
        return False

    if cur_coord.y < 0 or cur_coord.y >= len(MAP):
        return False

    return MAP[cur_coord.y][cur_coord.x] == 0


def get_neighbor_coords(cur_coord):
    return [coord(cur_coord.x - 1, cur_coord.y),
        coord(cur_coord.x, cur_coord.y - 1),
        coord(cur_coord.x + 1, cur_coord.y),
        coord(cur_coord.x, cur_coord.y + 1)]


def show(openlist, closelist):
    print("openlist")
    for k,v in openlist.items():
        k.show()
        v.show()

    print("closelist")
    for k,v in closelist.items():
        k.show()
        v.show()

def start(start_pos, end_pos):

    if start_pos == end_pos:
        print("start pos is just end pos")
        return

    cur_h = get_distance_between_two_coords(start_pos, end_pos)
    cur_node = node(0, cur_h, 0 + cur_h, coord(-1, -1))
    update_open_list(start_pos, cur_node)
    while open_list:
        minf_coord, minf_node = find_min_f_in_openlist()
        close_list[minf_coord] = minf_node
        neighbor_coords = get_neighbor_coords(minf_coord)
        for neighbor_coord in neighbor_coords:
            if is_valid_coord(neighbor_coord):
                cur_h = get_distance_between_two_coords(neighbor_coord, end_pos)
                cur_node = node(minf_node.g_score + 1, cur_h, minf_node.g_score + 1 + cur_h, minf_coord)
                update_open_list(neighbor_coord, cur_node)

        if end_pos in open_list:
            close_list[end_pos] = open_list[end_pos]
            break

    result = []
    if end_pos not in open_list:
        print('not find')
    else:
        #show(open_list, close_list)
        print("the path is:")
        cur_pos = end_pos
        while cur_pos.x >= 0 and cur_pos.y >= 0:
            print("({0},{1})".format(cur_pos.x, cur_pos.y))
            result.append(cur_pos)
            cur_pos = close_list[cur_pos].parent_pos

    for row in range(len(MAP[0])):
        print("\n", end='')
        for col in range(len(MAP[0])):
            if coord(col, row) == start_pos:
                print(' s', end='')
            elif coord(col, row) == end_pos:
                print(' e', end='')
            elif MAP[row][col] > 0:
                print(' @', end='')
            elif coord(col, row) in result:
                print(' o', end='')
            else:
                print(' .', end='')
    print("\n", end='')


if __name__ == '__main__':
    start_pos = coord(3, 4)
    end_pos = coord(6, 5)
    start(start_pos, end_pos)





