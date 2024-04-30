import numpy as np

def calculate(my_list):
    if len(my_list)==9:
        calculations = {}
        my_result = []
        my_array = np.array(my_list)
        my_array = my_array.reshape([3,3])

        #calculating mean
        ary_columns = np.mean(my_array,axis=0).tolist()
        ary_rows = np.mean(my_array,axis=1).tolist()
        flattened = np.mean(my_array).tolist()
        my_result.append(ary_columns)
        my_result.append(ary_rows)
        my_result.append(flattened)
        calculations['mean'] = my_result
        my_result = []

        #calculating variance
        ary_columns = np.var(my_array,axis=0).tolist()
        ary_rows = np.var(my_array,axis=1).tolist()
        flattened = np.var(my_array).tolist()
        my_result.append(ary_columns)
        my_result.append(ary_rows)
        my_result.append(flattened)
        calculations['variance'] = my_result
        my_result = []

        #Standard Deviation
        ary_columns = np.std(my_array,axis=0).tolist()
        ary_rows = np.std(my_array,axis=1).tolist()
        flattened = np.std(my_array).tolist()
        my_result.append(ary_columns)
        my_result.append(ary_rows)
        my_result.append(flattened)
        calculations['standard deviation'] = my_result
        my_result = []

        #max
        ary_columns = np.max(my_array,axis=0).tolist()
        ary_rows = np.max(my_array,axis=1).tolist()
        flattened = np.max(my_array).tolist()
        my_result.append(ary_columns)
        my_result.append(ary_rows)
        my_result.append(flattened)
        calculations['max'] = my_result
        my_result = []

        #min
        ary_columns = np.min(my_array,axis=0).tolist()
        ary_rows = np.min(my_array,axis=1).tolist()
        flattened = np.min(my_array).tolist()
        my_result.append(ary_columns)
        my_result.append(ary_rows)
        my_result.append(flattened)
        calculations['min'] = my_result
        my_result = []

        #sum
        ary_columns = np.sum(my_array,axis=0).tolist()
        ary_rows = np.sum(my_array,axis=1).tolist()
        flattened = np.sum(my_array).tolist()
        my_result.append(ary_columns)
        my_result.append(ary_rows)
        my_result.append(flattened)
        calculations['sum'] = my_result
        my_result = []
    else:
        raise Exception("List must contain nine numbers.")



    return calculations