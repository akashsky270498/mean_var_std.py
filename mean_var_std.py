import numpy as np
def calculate(lst):
    try:
        if(len(lst) == 9):
            arr = np.array(lst)
            data = arr.reshape(3,3)
            dic = {}
            dic["mean"] = [np.mean(data, axis = 0).tolist(), np.mean(data, axis = 1).tolist(), np.mean(data.flatten()).tolist()]
            dic["varience"] = [np.var(data, axis = 0).tolist(), np.var(data, axis = 1).tolist(), np.var(data.flatten()).tolist()]
            dic["standard deviation"] = [np.std(data, axis = 0).tolist(), np.std(data, axis = 1).tolist(), np.std(data.flatten()).tolist()]
            dic["max"] = [np.max(data, axis = 0).tolist(), np.max(data, axis = 1).tolist(), np.max(data.flatten()).tolist()]
            dic["min"] = [np.min(data, axis = 0).tolist(), np.min(data, axis = 1).tolist(), np.min(data.flatten()).tolist()]
            dic["sum"] = [np.sum(data, axis = 0).tolist(), np.sum(data, axis = 1).tolist(), np.sum(data.flatten()).tolist()]
            return dic

    except ValueError:
        print("List must contain 9 digits!!")

result = calculate([0,1,2,3,4,5,6,7,8])
print(result)