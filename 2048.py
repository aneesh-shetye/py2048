import pynput 
import optparse
import random
import os

parser=optparse.OptionParser()
parser.add_option("-n","--number",dest="n",help="number of rows and columns")
parser.add_option("-w","--win",dest="win_no",help="Exponent of 2 greater than two reaching which you win")
(values,arguments)=parser.parse_args()


n=values.n
win_no=values.win_no

if type(n)==str:
    n=int(n)

print(n, type(n))
print(win_no)