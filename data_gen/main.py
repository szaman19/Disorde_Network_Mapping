import numpy as np 
import scipy

def generate_hamiltonian(size,W):
    dims = (size,size)
    
    hamiltonian = np.zeros(dims)
    #print(hamiltonian)

    for i in range(size):
        j = i + 1
        if (j < size):
            hamiltonian[i][j] = 1
            hamiltonian[j][i] = 1
        
        rand = np.random.random_sample() - .5
        hamiltonian[i][i] = rand * W
    return hamiltonian

def eigen_values(matrix):
    print (matrix)

def main():

    H = generate_hamiltonian(5, 2)

    print(H)

main()
