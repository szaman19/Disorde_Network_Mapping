import numpy as np
from numpy import linalg as LA
import numpy.matlib
import scipy.linalg
import math
import matplotlib.pyplot as plt

def generate_hamiltonian(size,W):
    dims = (size,size)
    
    hamiltonian = np.zeros(dims, dtype=complex)
    #print(hamiltonian)

    for i in range(size):
        j = (i + 1 )% size
        if (j < size):
            hamiltonian[i][j] = -1
            hamiltonian[j][i] = -1
        
        rand = np.random.random_sample() - .5
        hamiltonian[i][i] = rand * W
    return hamiltonian

def generate_hamiltonian_mat(size,W):
    hamiltonian = np.matlib.eye(size,k=1,dtype=complex) + np.matlib.eye(size,k=-1)
    
    for i in range(size):
        j = (i + 1 )% size
        if (j < size):
            hamiltonian[i,j] = 1
            hamiltonian[j,i] = 1

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

def greens_matrix(hamiltonian,E, eta):
    
    eig_vals, eig_vectors = scipy.linalg.eigh(hamiltonian)
    dims = (len(eig_vals),len(eig_vals))    

    greens_operator = np.zeros(dims,dtype=complex)
    diffusion_operator = np.zeros(dims,dtype=complex)
    inv = np.zeros(dims,dtype=complex)
    for i in range(len(eig_vals)):
        vec = eig_vectors[:,i]
        mat = np.tensordot(vec,vec,axes=0)
        mat_c = mat * (1/(E-eig_vals[i]-np.complex(0,eta)))
        
        greens_operator += mat_c
        
    inv = np.transpose(np.conj(greens_operator)) 

    for i in range(len(eig_vals)):
        for j in range(len(eig_vals)):
            diffusion_operator[i][j] = np.abs(inv[j][i] * greens_operator[i][j])
                
    return diffusion_operator
def normalize_matrix(mat):
    max_num = -1
    for i in range(mat.shape[0]):
        for k in range(mat.shape[0]):
            if (np.abs(mat[i][k]) > max_num):
                max_num = mat[i][k]
            
    return mat/max_num
 
def invert_matrix(hamiltonian):
    dims = (hamiltonian.shape[0],hamiltonian.shape[0])
    identity = np.matlib.eye(dims[0], dtype='complex')
    numerical_stab = identity * np.complex(0,(.001))
    #print("*"*90)
    #pretty_print_mat(numerical_stab) 
    #print("Printing numerical stablitiy matrix")
    print("Hamiltonian")
    #pretty_print_mat(numerical_stab)

    i_h = numerical_stab - (hamiltonian) 
    pretty_print_mat(i_h)
    #print("*"*90)
    #print("Printing inverted matrix")
    inverse = scipy.linalg.inv(i_h) 
    print("inverted matrix")
    pretty_print_mat(inverse)

    #inverse_mat =np.matrix(inverse) 

    inverse_conj = np.conj(np.transpose(inverse))
    print("Conjugate transpose")
    pretty_print_mat(inverse_conj)

    greens_matrix = np.matmul(inverse,inverse_conj) 
    print("diffusion")
    pretty_print_mat(greens_matrix)
    return greens_matrix

    #pretty_print_mat(greens_matrix)
    #pretty_print(inverse_mat)

def output(mat,W):
    f_open = open('w-'+str(W).replace('.','-')+'-E-0-diffusion-500.txt','w')
    f_open.write("For disorder  = " + str(W)+'\n') 
    dims = mat.shape
    for i in range(dims[0]):
        for k in range(dims[0]):
            line = str(i+1) + '\t' + str(k+1) + '\t' + str(np.real(mat.item(i,k))) + '\n'
            f_open.write(line)
    f_open.close()

def pretty_print(mat):

    dims = mat.shape[0]
    print("*" * dims * 18)
    for i in range(dims):
        line = '|'
        for k in range(dims):
       
            line += "\t {0:.3f}".format(mat[i][k])
        line+= '\t|'
        print(line)
    print ("_"*dims*18)
def pretty_print_mat(mat):

    dims = mat.shape[0]
    print("*" * dims * 18)
    for i in range(dims):
        line = '|'
        for k in range(dims):
       
            line += " " + "{0:1.1f}".format(mat.item(i,k))
        line+= '\t|'
        print(line)
    print ("_"*dims*18)


def main(): 

    for i in range (0,16):
        W = i / 10
        Diffusion_Matrix = np.zeros((500,500),dtype=complex)
        for k in range(1000):
            print(k)
            H = generate_hamiltonian(500,W)
            Diffusion_Matrix += greens_matrix(H,0,0.01)
        Diffusion_Matrix = Diffusion_Matrix / 1000
        Diffusion_Matrix = normalize_matrix(Diffusion_Matrix)

        output(Diffusion_Matrix,W)
main()
