import numba
from numba.pycc import CC
import numpy as np
import time

np.random.seed(1234567890)

def compile_cc():
    cc = CC('log_gaussian_numba_CC')
    # Uncomment the following line to print out the compilation steps
    cc.verbose = True
    #x shape     =  (196, 609, 1)
    #mean shape  =  (196, 609, 38)
    #sigma shape =  (196, 609, 38)
    #@cc.export('log_gaussian_numba_CC', 'f8[:][:][:](f8[:][:][:],f8[:][:][:],f8[:][:][:])')
    #def log_gaussian_numba_CC(x, mean, sigma):
    #    for i in range(196):
    #        for j in range(609):
    #            for k in range(38):
    #                log_pdf[i][j][k] = -(x[i][j][0] - mean[i][j][k])*(x[i][j][0] - mean[i][j][k])/2.0/sigma[i][j][k]/sigma[i][j][k] - log(sqrt(2*3.141592653589793)*sigma[i][j][k]);
    #    return log_pdf
    #@cc.export('log_gaussian_numba_CC', 'f8[:](f8[:][:],f8,f8,i8,i8,i8)')
    #def log_gaussian_numba_CC( x, mean, sigma, n_x, n_y, n_z):
    #   log_pdf = 0
    #log_pdf = x + mean + sigma
    #  for i in range(n_x):
    #     for j in range(n_y):
    #        log_pdf[i] = log_pdf[i] + x[i][j]
    #for i in range(196):
    #    for j in range(609):
    #        for k in range(38):
    #            log_pdf[i][j][k] = -(x[i][j][0] - mean[i][j][k])*(x[i][j][0] - mean[i][j][k])/2.0/sigma[i][j][k]/sigma[i][j][k] - log(sqrt(2*3.141592653589793)*sigma[i][j][k]);
    #return log_pdf
    #@cc.export('log_gaussian_numba_CC', '(f8[:][:])')
    #def log_gaussian_numba_CC(x):
    #    for i in range(1):
    #        for j in range(1):
    #            print(x[i][j])
    @cc.export('log_gaussian_numba_CC', 'f8[:,:,:](f8[:,:,:])')
    def log_gaussian_numba_arr_cc(x):
        log_pdf = np.empty(x.shape)
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                for k in range(x.shape[2]):
                    log_pdf[i,j,k] = x[i,j,k]
                    #print(i," ",j," ",k," ",x[i,j,k])
        return log_pdf
    cc.compile()

def main():
    import log_gaussian_numba_CC
    A = np.transpose(np.array([[[1.0,2.0,3.0,4.0],[5.0,6.0,7.0,8.0],[9.0,10.0,11.0,12.0]]]))
    print(np.shape(A))
    print(A)
    #log_gaussian_numba_CC.log_gaussian_numba_CC(A)
    print(log_gaussian_numba_CC.log_gaussian_numba_CC(A))
        
if __name__ == "__main__":
    compile_cc()
    main()
