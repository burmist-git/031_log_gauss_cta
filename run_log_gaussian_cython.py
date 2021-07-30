import numpy as np
import time
import log_gaussian_cython

np.random.seed(1234567890)

def main():

    x_x_shape     =  (196, 609, 1)
    mean_x_shape  =  (196, 609, 38)
    sigma_x_shape =  (196, 609, 38)
    #
    x = np.random.normal(3, 1.0, size=x_x_shape)
    mean = np.random.normal(3, 1.0, size=mean_x_shape)
    sigma = np.random.normal(2.0, 0.001, size=sigma_x_shape)
    
    nPoints = 10
    tottime = 0
    
    for i in range(nPoints):
        #
        time01 = time.time()
        log_pdf = log_gaussian_cython.log_gaussian(x, mean, sigma)
        time02 = time.time()
        #print(type(log_pdf))
        #print(np.sum(log_pdf))
        delta=(time02-time01)
        tottime = tottime + delta
        #print('aa-> ',np.sum(log_pdf));
    
    print('tottime/nPoints  = ',tottime/nPoints)
        
if __name__ == "__main__":
    main()
