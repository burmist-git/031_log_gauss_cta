import numba
from numba.pycc import CC
import numpy as np
import time

np.random.seed(1234567890)

def compile_cc():
    cc = CC('log_gaussian_numba_CC')
    # Uncomment the following line to print out the compilation steps
    cc.verbose = True
    #@cc.export('log_gaussian_numba_CC', 'f4[:,:,:](f4[:,:,:],f4[:,:,:],f4[:,:,:])')
    @cc.export('log_gaussian_numba_CC', 'f8[:,:,:](f8[:,:,:],f8[:,:,:],f8[:,:,:])')
    def log_gaussian_numba_CC(x,mean,sigma):
        log_pdf = np.empty(mean.shape)
        for i in range(mean.shape[0]):
            for j in range(mean.shape[1]):
                for k in range(mean.shape[2]):
                    log_pdf[i,j,k] = -(x[i,j,0] - mean[i,j,k])*(x[i,j,0] - mean[i,j,k])/2.0/sigma[i,j,k]/sigma[i,j,k] - np.log(np.sqrt(2*3.141592653589793)*sigma[i,j,k]);
        return log_pdf

    @cc.export('log_gaussian_numba2_CC', 'f8[:,:](f8[:,:],f8[:,:],f8[:,:])')
    def log_gaussian_numba2_CC(x,mean,sigma):
        log_pdf = np.empty(mean.shape)
        for i in range(mean.shape[0]):
            for j in range(mean.shape[1]):
                    log_pdf[i,j] = -(x[i,j] - mean[i,j])*(x[i,j] - mean[i,j])/2.0/sigma[i,j]/sigma[i,j] - np.log(np.sqrt(2*3.141592653589793)*sigma[i,j]);
        return log_pdf
    cc.compile()

def main():
    import log_gaussian_numba_CC
    #
    x_x_shape     =  (196, 609, 1)
    mean_x_shape  =  (196, 609, 38)
    sigma_x_shape =  (196, 609, 38)
    #
    x = np.random.normal(3, 1.0, size=x_x_shape)
    mean = np.random.normal(3, 1.0, size=mean_x_shape)
    sigma = np.random.normal(2.0, 0.001, size=sigma_x_shape)

    aaaa=str(type(x[0][0][0]))
    print(aaaa)
    if (type(x[0][0][0]) == '<class \'numpy.float64\'>') :
        print ('true')
    
    time01 = time.time()
    log_gaussian_numba_CC.log_gaussian_numba_CC(x, mean, sigma)
    time02 = time.time()
    print('CC (first call)  =',(time02-time01))
    time01 = time.time()
    log_gaussian_numba_CC.log_gaussian_numba_CC(x, mean, sigma)
    time02 = time.time()
    print('CC (second call) =',(time02-time01))

    nPoints = 1
    tottime = 0
    
    for i in range(nPoints):
        #
        time01 = time.time()
        log_pdf = log_gaussian_numba_CC.log_gaussian_numba_CC(x, mean, sigma)
        time02 = time.time()
        #print(np.sum(log_pdf))
        delta=(time02-time01)
        tottime = tottime + delta
        #print('aa-> ',np.sum(log_pdf));
    
    print('tottime/nPoints  = ',tottime/nPoints)
    
if __name__ == "__main__":
    compile_cc()
    main()
