
#GRADES.PY

import math

def total(values)->float:
    result = 0
    for number in values:
        result += number

    return float(result)

def average(values)->float:
    if len(values) == 0:
        return math.nan
    else:
        return float(total(values) / len(values))

def median(values)->float:

    index = len(values) // 2
    sortedvalues = sorted(values)

    if len(values) == 0:
        raise ValueError
    
    else:

        if len(values) % 2 == 0: 
            result = (sortedvalues[index] + sortedvalues[index - 1]) / 2

        else:
            result = sortedvalues[index]
        
        return result