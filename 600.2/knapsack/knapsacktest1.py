# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:29:55 2018

@author: mzamp
"""
counter = 0
def knapsack(W, items):
    """
    Given a list of items with name, value and weight.
    Return the optimal value with total weight <= allowed weight and 
    list of picked items.
    """ 
    n = len(items)
    k = [[0 for x in range(W+1)] for x in range(n+1)]
    global counter
    for i in range(n+1):
        counter += 1
        for w in range(W+1):
            counter += 1
            if i == 0 or w == 0:
                k[i][w] = 0
            elif items[i-1][2] <= w:
                k[i][w] = max(items[i-1][1] + k[i-1][w-items[i-1][2]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]

    picked = []
    set_trace(k, n, W, items, picked)
    return k[n][W], picked

# find which item are picked
def set_trace(k, n, W, items, picked):
    for i in range(n, 0, -1):
        if k[i][W] != k[i-1][W]:
            picked.append(items[i-1])
            set_trace(k, i-1, W-items[i-1][2], items, picked)
            break


if __name__ == '__main__':
    items = [('Phone', 6, 1), ('Laptop', 4, 3), ('Keyboard', 5, 4), ('TV', 7, 5), ('Watch', 6, 3), ('Toaster', 1, 2)]
    max_value,  picked = knapsack(12, items)
    print("Maximum value:", max_value)
    print("Name", "Value", "Weight")
    for item in reversed(picked):
        print(item[0], ' '*2, item[1], ' '*3, item[2])
    print (counter)