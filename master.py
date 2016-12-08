
import numpy as np
import time

class Master:

    def get_random_variables(self):
        x = np.random.rand(4)
        nfilters = 10 + int(90*x[0])                        #   in [10, 100]
        batch_size_train = int(pow(2.0, 4.0 + 4.0*x[1]))    #   in [2^4, 2^8] = [16, 256]
        M = float(x[2])                                     #   in [0, 1]
        LR = float(pow(10.0, -2 + 1.5*x[3]))                #   in [10^-2, 10^-0.5] = [0.01, ~0.31]

        return nfilters, batch_size_train, M, LR

    def write_new_line(self,filename,strng):
        f = open(filename,'w')
        f.write(strng)
        f.close()

    def read_first_line(self,filename):
        f = open(filename,'r')
        line = f.readline()
        f.close()
        return line

    def read_last_line(self,filename):
        f = open(filename,'r')
        lines = f.readlines()
        if lines != []:
            lastline = lines[-1]
        else:
            lastline = ""
        f.close()
        return lastline


    def main(self, nb_workers=2, confs=400):
        start = time.time()
        worker_file_list = []

        for i in range(0,nb_workers):
            filename = "worker_{}".format(i)
            f = open(filename,'w')
            # initiliaze with a random configuration
            nfilters, batch_size_train, M, LR = self.get_random_variables()
            f.write("{}\t{}\t{}\t{}".format(nfilters,batch_size_train,M,LR))
            f.close()
            f = open("solution_master_slave","w")
            f.close()
            worker_file_list.append(filename)

        counter = 1
        while(True):
            for filename in worker_file_list:

                if self.read_last_line(filename).strip() == "":
                    # append configuration (=firstline) to solution file
                    print("Configuration: {}".format(counter))
                    firstline = self.read_first_line(filename)
                    f = open("solution_master_slave","a")
                    f.write(firstline)
                    f.close()

                    nfilters, batch_size_train, M, LR = self.get_random_variables()
                    strng = "{}\t{}\t{}\t{}".format(nfilters,batch_size_train,M,LR)
                    self.write_new_line(filename,strng)

                    counter += 1

            if counter > confs:
                for filename in worker_file_list:
                    self.write_new_line(filename,"stop")
                break
        stop = time.time()
        total = stop - start
        f = open("timing","w")
        f.write("Total time: {}".format(total))
        f.close()

if __name__ == '__main__':
    m = Master()
    m.main()
