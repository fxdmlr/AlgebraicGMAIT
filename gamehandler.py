
import utils
import evaluator as evl
import problem_set_calc
import calcI_int_problemset as cint

'''
The output of each function is as follows : 
[resulting_string, expected_result, conversion_functon]
'''

def string_sgn(x):
    if x > 0:
        return "+"
    elif x < 0:
        return "-"
    else:
        return "0"



def calc_game(inpt_dict):
    i = 0
    while not i:
        try:
            a, b = problem_set_calc.single_number_gen()
            moe = inpt_dict['moe']
            i = 1
        except:
            pass
    return utils.strpprint(a) + '\n > ', b, lambda x : b if abs(float(x)- b) < abs(moe * b) else b + 1

def integral_set_game(inpt_dict):
    i = 0
    while not i:
        try:
            a, b = cint.single_number_gen()
            moe = inpt_dict['moe']
            i = 1
        except:
            pass
    return utils.strpprint(a) + '\n > ', b, lambda x : b if abs(float(x)- b) < abs(moe * b) else b + 1

