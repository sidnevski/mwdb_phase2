from sklearn.preprocessing import MinMaxScaler
import numpy as np

def transform(DataMatrix):
    """
    Parameters:
        DataMatrix: A two dimentional matrix 
    
    Returns:
        Data_Matrix_transformed: Transformed mix max matrix 
    """
    try:
        DataMatrix = np.array(DataMatrix)
        
        Scaler = MinMaxScaler()
        Scaler.fit(DataMatrix)

        Data_matrix_transformed = Scaler.transform(DataMatrix)
        return Data_matrix_transformed
    except:
        print("Something went wrong in min_max_scaler.py file")


#Testing with a data matrix
#data = np.array([[-1, 2], [0, 6], [0, 10], [1, 18]])
#print(transform(data))