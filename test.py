from genetic import *
from board import *

n = 6

objects = [board(n),board(n),board(n),board(n),board(n),board(n)]

test = genetic(objects,n)

test.preformGenetic()

test.getSolution().show()


