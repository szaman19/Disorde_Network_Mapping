import matplotlib
import matplotlib.pyplot as plt
import sys

def main():
    cmap = plt.cm.get_cmap('hsv',len(sys.argv))     
    for i in range(1,len(sys.argv)):
        
        data_file = open(sys.argv[i])
        data_array = []
        Label = "W = " + sys.argv[i].split("-")[6].strip(".txt")
        for eachline in data_file:
            values = eachline.split("-")
            values.pop(0)
            stri = "-".join(values)
            stri = stri.strip('\n')
            #print(float(stri))
            data_array.append(float(stri))
            #if(len(eachline.split()) < 2):
            #    data_array.append(float(eachline))
            #if(len(eachline.split()) > 2):
            #    Label = eachline
        x=range(0,len(data_array))
        plt.title("Clustering Coefficient") 
        plt.plot(x,data_array, color=cmap(i),label=Label)
    plt.legend()
    plt.show()


main()
