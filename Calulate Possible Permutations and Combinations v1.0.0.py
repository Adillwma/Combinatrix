# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:01:17 2022
Calulate Possible Permutations and Combinations v1.0.0
@author: Adill Al-Ashgar
"""

#######PRE-REQUISITES######
#import math
from scipy.special import factorial

#####FUNCTION#######
def permutations_combinations(number_of_possible_choices,number_of_choices_to_make,repetitions_allowed=0):       #i.e for a combination lock with 10 possible choices of number per ring (0-9) and three rings to choose gives n=10 and r=3
    n=number_of_possible_choices
    r=number_of_choices_to_make
      
    if repetitions_allowed == 0:
        precalc_array_1 = [n, r, (n-r)]
        precalc_1 = factorial(precalc_array_1,True)    #precalculations stop the code from having to recalculate the same factorials for each output, saving cpu cycles. Also the factorial method used (scipy.special.factorial) takes an array and only calculates the largest values factorial explicitly, the other array values are found as byproducts of that calulation, this again reduces cpu requirment        
        combinations_without_repetition = precalc_1[0] / (precalc_1[1] * precalc_1[2])    #combinations are the amount of unique outputs without taking order into account
        permutations_without_repetition =   precalc_1[0] / precalc_1[2]                   #permutations are the amount of unique outputs where the order of outputs matters
        output=combinations_without_repetition,permutations_without_repetition
    else:
        precalc_array_2 = [(n+r-1), r, (n-1)]
        precalc_2 = factorial(precalc_array_2,True)
        combinations_w_repetition = precalc_2[0]/ (precalc_2[1] * precalc_2[2]) 
        permutations_w_repetition = n**r                            #permutations are the amount of unique outputs where the order of outputs matters
        output = combinations_w_repetition, permutations_w_repetition    
    return(output)


########DRIVER#########
out=permutations_combinations(5,3,1)
print("Combinations =",out[0])
print("Permutations =",out[1])