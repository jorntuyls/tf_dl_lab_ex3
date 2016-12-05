
import numpy as np

class Master:
    
    def main(self, nb_workers=2, confs=5):
        worker_file_list = []
        nvariables = 4
        
        for i in range(0,nb_workers):
            filename = "worker_{}".format(i)
            worker_file_list.append(filename)
        
        counter = 0
        while(True):
            if counter >= confs-1:
                break
            
            for filename in worker_file_list:
                f = open(filename, 'a+')
                lines = f.readlines()
                if lines != []:
                    lastline = lines[-1]
                else:
                    lastline = ""
                    
                print(lastline)
                if lastline.strip() == '':
                    x = np.random.rand(nvariables)
                    nfilters = 10 + int(90*x[0])                        #   in [10, 100]
                    batch_size_train = int(pow(2.0, 4.0 + 4.0*x[1]))    #   in [2^4, 2^8] = [16, 256]
                    M = float(x[2])                                     #   in [0, 1]
                    LR = float(pow(10.0, -2 + 1.5*x[3]))                #   in [10^-2, 10^-0.5] = [0.01, ~0.31]
                    
                    f.write("{}\t{}\t{}\t{}".format(nfilters,batch_size_train,M,LR))
                    
                    counter += 1
                    print("Configuration: {}".format(counter))
                    
                f.close()
        
if __name__ == '__main__':
    m = Master()
    m.main()
                
                
            
            
        
        
