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
    #inv_hamiltonian = LA.inv(hamiltonian)
    
    #print("*"*80)
    #print("Calculating Eigenvalues and Eigenvectors")
    eig_vals, eig_vectors = scipy.linalg.eigh(hamiltonian)
    dims = (len(eig_vals),len(eig_vals))
    #print("*"*80)
    #print("Printing each Eigenvalue")
    #print(eig_vals)
    #print("*"*80)
    #print("Printing each Eigenstate")
    '''
    for i in range(len(eig_vals)):
        print("eigenvalue :", eig_vals[i])
        print("*"*60)
        print("eigenvector :",eig_vectors[:,i])
        print("*"*60)
        print(np.dot(hamiltonian,eig_vectors[:,i])," == ", eig_vals[i]*eig_vectors[:,i])
        #print(eig_vals[i],eig_vectors[:,i].shape,eig_vectors[:,i])
    '''
    #print("*"*80)
    #print("Creating the matrices")
    for i in range(len(eig_vals)):
        row_vec = np.transpose(eig_vectors[:,i])
        #print("Shape", row_vec.shape,row_vec)
    #print("*"*80)

    #print("Sum of the |n><n|: should be I")
    I = np.zeros(dims,dtype=complex)
    for i in range(len(eig_vals)):
        vec = np.transpose(eig_vectors[:,i])
        mat = np.tensordot(vec,vec,axes=0)
        I += mat
        #print("Shape ", mat.shape, mat)
    #print(I)
    #print("Doing the scalar multiplication")
    
    greens_operator = np.zeros(dims,dtype=complex)
    diffusion_operator = np.zeros(dims,dtype=complex)
    inv = np.zeros(dims,dtype=complex)
    for i in range(len(eig_vals)):
        #for j in range(diffusion_operator.shape[0]):

        #    D_ij = 0 

        #    for n in range(len(eig_vals)):
        #        D_ij += (eig_vectors[:,n][i] * eig_vectors[:,n][j])**2/ ((E-eig_vals[n])**2 + eta **2)
        #    diffusion_operator[i][j] = D_ij
        vec = eig_vectors[:,i]
        mat = np.tensordot(vec,vec,axes=0)
        mat_c = mat * (1/(E-eig_vals[i]-np.complex(0,eta)))
        #mat_r = mat * (1/ (E - eig_vals[i]+np.complex(0,eta)))
        greens_operator += mat_c
        #inv += mat_r
    #print("Advanced greens function")

    #pretty_print(greens_operator)
    inv = np.transpose(np.conj(greens_operator)) 
    #print("Retarded greens function")
    #pretty_print(inv)

    max_element = -1

    for i in range(len(eig_vals)):
        for j in range(len(eig_vals)):
            #print(mat_r[j,i],mat_c[i,j])
            if (i == j):
                diffusion_operator[i][j] = 0
            else:
                diffusion_operator[i][j] = np.abs(inv[j][i] * greens_operator[i][j])
            if (np.abs(inv[j][i] * greens_operator[i][j]) > max_element):
                max_element = np.abs(inv[j][i] * greens_operator[i][j])
            
    #diffusion_operator = np.matmul(inv,greens_operator)

    #print("*"*80)
    #print("Finished creating diffusion operator")
    #print(greens_operat
    #pretty_print(diffusion_operator)
    #for i in range(dims[0]):
    #    print("1 \t",i+1,"\t",diffusion_operator[0][i])
    
    return diffusion_operator / max_element
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

def output(mat):
    f_open = open('w-0-E-0-diffusion-500.txt','w')
    dims = mat.shape
    for i in range(dims[0]):
        for k in range(dims[0]):
            line = str(i+1) + '\t' + str(k+1) + '\t' + str(mat.item(i,k)) + '\n'
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
    H = generate_hamiltonian(500,W)
    #pretty_print_mat(H)
    #print("*"*80)
    #print("Generating Hamiltonian")
    #pretty_print(H)
    #diffusion = invert_matrix(H)

    #output(diffusion)
    #energies = eigen_values(H)
    
    #reens_matrix(H,0,0)
    #print(greens_matrix(H,0,0.001))
    
    #diff_op_avg = np.zeros((500,500),dtype=complex)


    #for i in range (100):
    #    H = generate_hamiltonian(500,W-(i*.1))
    #    H_2 = generate_hamiltonian(500,W+(i*.1))
    #    diffusion = greens_matrix(H,0,0.01)
    #    diffusion_2 = greens_matrix(H_2,0,0.01)
    #    diff_op_avg += diffusion + diffusion_2
    #diff_op_avg = diff_op_avg / 200
    #output(diff_op_avg)
    output(greens_matrix(H,0,0.01))
main()
