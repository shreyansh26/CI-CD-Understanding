import scipy
import pandas
import numpy
import matplotlib
from matplotlib import pyplot as plt
####### Here I start the solution to the fizz buzz problem #######
def fizz_buzz(n: int) -> str:
    if n % 15 == 0: return 'fizzbuzz'
    elif n % 5 == 0: return 'buzz'
    elif n % 3 == 0: return 'fizz'
    else: return str(n)