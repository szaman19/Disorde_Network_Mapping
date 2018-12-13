import matplotlib
import matplotlib.pyplot as plt
import sys

def main():
    file_list = []
    
    output_file_name = sys.argv[1]
    cmap = plt.cm.get_cmap('hsv',len(sys.argv))     
    for i in range(1,len(sys.argv)):
        
        data_file = open(sys.argv[i])
        data_array = []
        Label = ''
        for eachline in data_file:
            if(len(eachline.split()) < 2):
                data_array.append(float(eachline))
            if(len(eachline.split()) > 2):
                print(eachline.split())
                Label = eachline.split()[2]
        x=range(0,len(data_array))
        
        plt.plot(x,data_array, color=cmap(i),label=Label)
        plt.savefig(Label+'.png', dpi=400)
    plt.legend()
    plt.show()


main()
