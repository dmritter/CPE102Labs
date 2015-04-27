
def map(func1, list1):
    ret_list = []
    for i in range(len(list1)):
        ret_list.append(func1(list1[i]))
    return ret_list

def add(x):
    def g(y):
        return x+y
    return g

def create_counter(init_val):
    dict1={}
    dict1['initial'] = init_val
    def ret_func():
        a = dict1['initial']
        dict1['initial'] = dict1['initial'] + 1
        return a
    return ret_func
