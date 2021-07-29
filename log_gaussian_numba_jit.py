import numba
import numpy as np
import time

np.random.seed(1234567890)

#x_x.shape          =  (44, 20, 1)
#mean_x.shape       =  (44, 20, 68)
#sigma_x.shape      =  (44, 20, 68)
#log_pdf_x.shape    =  (44, 20, 68)
#    N           Min           Max        Median           Avg        Stddev
#x 1825            23           196            46     57.349589     34.240562
#x 1825            16           609            51     63.782466     39.036017
#x 1825            20            38            22     22.550685     2.3254364            

#x shape     =  (196, 609, 1)
#mean shape  =  (196, 609, 38)
#sigma shape =  (196, 609, 38)
@numba.jit(nopython=True)
def log_gaussian_numba(x, mean, sigma):
    log_pdf = -(x - mean) ** 2 / (2 * sigma ** 2)
    log_pdf = log_pdf - np.log((np.sqrt(2 * np.pi) * sigma))
    return log_pdf

def main():

    x_x_shape     =  (196, 609, 1)
    mean_x_shape  =  (196, 609, 38)
    sigma_x_shape =  (196, 609, 38)
    
    nPoints = 100
    tottime = 0

    x = np.random.normal(3, 1.0, size=x_x_shape)
    mean = np.random.normal(3, 1.0, size=mean_x_shape)
    sigma = np.random.normal(2.0, 0.001, size=sigma_x_shape)

    time01 = time.time()
    log_gaussian_numba(x, mean, sigma)
    time02 = time.time()
    print('jit (first call)  =',(time02-time01))
    time01 = time.time()
    log_gaussian_numba(x, mean, sigma)
    time02 = time.time()
    print('jit (second call) =',(time02-time01))
    
    for i in range(nPoints):
        time01 = time.time()
        log_pdf = log_gaussian_numba(x, mean, sigma)
        time02 = time.time()
        #print(np.sum(log_pdf))
        delta=(time02-time01)
        tottime = tottime + delta
        
    print('tottime/nPoints   =',tottime/nPoints)
        
if __name__ == "__main__":
    main()
