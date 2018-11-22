import numpy as np
from numpy import linalg as LA

import scipy
import math
import matplotlib.pyplot as plt

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
    eig_vals = LA.eigvalsh(matrix)
    #print (eig_vals)
    return eig_vals

def DOS (eig_vals, eta, energy):
    retVal = 0
    for i in eig_vals:
        retVal += eta / ((energy - i)**2 + eta **2)
    retVal /= math.pi
    retVal /= eig_vals.shape[0]
    return retVal

def greens_matrix(hamiltonian,E):
    #inv_hamiltonian = LA.inv(hamiltonian)
    identity = np.eye(hamiltonian.shape[0])
    print(identity)

    #for i in range(identity.size):
    #    identity[i][i] = identity[i][i]*E
    identity = identity * E
    print(identity)
    return identity - hamiltonian
    

def main():
    
    W = 0
    '''for k in range (5):
        W = k * 2
        H = generate_hamiltonian(10000, W)
    
        energies = eigen_values(H)
 
        vals = []
        
        for i in range (-1000,1000):
            vals.append(DOS(energies, .5, i/100))
        label = "W = " + str(W)
        plt.plot(range(-1000,1000),vals,label=label)
        plt.xticks(np.arange(-1000, 1100, step=100),range(-10,11,))
    
    plt.title('Density of States')
    plt.xlabel("E")
    plt.legend()
    plt.savefig("10000-W-0-8.svg", format="svg", dpi= 1200)
    #plt.show()
    '''
    #print(H)

    H = generate_hamiltonian(5,W)
    energies = eigen_values(H)

    greens_matrix(H,0)


main()
