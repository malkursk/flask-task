import numpy as np

def matrixToString(M):
    s = '\n'.join([''.join([str(u) for u in row]) for row in M])    
    return (s.replace('[', '')).replace(']', '').replace('\n',';')
    
def matrixReverse(data): # вычисляем обратную матрицу
    try:      
        return matrixToString((np.linalg.inv(np.matrix(data).T))) 
    except:
        return 'Fail'


def arraySum(data): # вычисляем сумму элементов массива
    M = data.split(' ')
    return np.sum(M,dtype=float)    