import numpy as np

def matrixToString(M):
    s = '\n'.join([''.join([str(u) for u in row]) for row in M])    
    return (s.replace('[', '')).replace(']', '').replace('\n',';')
    
def matrixReverse(data): # обратная матрицу
    try:      
        return matrixToString((np.linalg.inv(np.matrix(data).T))) 
    except:
        return 'Fail'

def arraySum(data): # сумма элементов массива
    M = data.split(' ')
    return np.sum(M,dtype=float)    

def matrixTransponse(M): # транспонированная матрица
    return matrixToString(np.matrix(M).T)