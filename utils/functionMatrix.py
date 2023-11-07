import numpy as np

def reverse(data): # вычисляем обратную матрицу
    try:
        R = (np.linalg.inv(np.matrix(data).T))
        s = '\n'.join([''.join([str(u) for u in row]) for row in R])    
        s = (s.replace('[', '')).replace(']', '').replace('\n',';')
        return s 
    except:
        return 'Fail'
