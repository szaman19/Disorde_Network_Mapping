import matplotlib.pyplot as plt

def main():
    small_world = open('Pe-1d-500-Diffusion-Aij-NoRec-Small-World-Sigma-Self-Generated.txt','r')
    coefficients = []
    normalization = 0

    for each_val in small_world:
        vals = each_val.split()

        disorder = vals[1].split("=")[1].replace('d','.')
        if (float(disorder) == 0):
            normalization = float(vals[0])
        coefficients.append((float(vals[0]),float(disorder)))

        #print(vals[0],disorder)

    coefficients = [(x[0]/normalization,x[1]) for x in coefficients]
    labels = []
    vals = []
    for i in coefficients:
        labels.append(i[1])
        vals.append(i[0])
    plt.plot(labels,vals,'rs-')
    plt.title('Network Robustness')
    plt.xlabel('Disorder (W)')
    plt.ylabel('Small World Coefficients ($\sigma$)')
    plt.grid(True)
    plt.savefig('small_world.png')
    plt.show()
main()
