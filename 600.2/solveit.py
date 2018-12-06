# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 18:57:42 2018

@author: mzamp
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    x = 0
    while test(x) != True:
        x+=1
    return x
        




#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))


#So I just finished this course and wanted to post a follow up to anyone who might just be seeing this or admins that think they can improve the quality of this course for future students.
#
#Coming from 600.1x I was just beginning to learn python and assumed that these courses were a way to learn python programming. I think the huge jump from learning some python basics and early computer programming theory (in 600.1) , to this class, is large enough, that this class might need to be labeled 600.3x or even you should have enough material to create a 600.1.5x. I was completely lost without python tutor and if i wasn't very determined to continue through I would have given up this class by lecture 3.
#
#I strongly believe that you can add an extra course that continues python basics to intermediate before taking this class. While I was able to struggle through and complete this class certificate. I feel that I have adapted 'bad habits' that early learners without proper guidance will make and possibly retain for their whole programming careers.
#
#Apart from this recommendation, the amount of typos and corrections seemed higher than that of other moocs I've taken. Also, the coherency of the videos posted leaves much to be desired. Some aspects of the videos need to be further explained, possibly in more (and smaller) videos, I feel that this would explain some of the more difficult concepts in greater detail while allowing students to digest smaller chunks of the code. Rather than just opening up a 200 line.py handout after a brief explanation and having to back trace the entire program.
#
#Lastly, I would like to THANK YOU for providing this content freely online for those of us who don't have the time or the money to pursue quality education. All in all, if you persevere and put in the work, you will learn some AMAZING concepts(ones that completely blew my mind). I would recommend this class to anyone new to these topics of computer science but not for those trying to learn python programming.