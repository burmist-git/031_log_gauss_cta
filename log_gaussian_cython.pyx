cimport numpy
import numpy as np
from libc.math cimport log
from libc.math cimport sqrt

def log_gaussian(numpy.ndarray[numpy.double_t, ndim=3] x, numpy.ndarray[numpy.double_t, ndim=3] mean, numpy.ndarray[numpy.double_t, ndim=3] sigma):
  cdef unsigned int xDim = mean.shape[0]
  cdef unsigned int yDim = mean.shape[1]
  cdef unsigned int zDim = mean.shape[2]
  cdef double[:,:,:] log_pdf = np.zeros((xDim,yDim,zDim),dtype=np.double)
  for i in range(xDim):
    for j in range(yDim):
      for k in range(zDim):
        log_pdf[i,j,k] = -(x[i][j][0] - mean[i][j][k])*(x[i][j][0] - mean[i][j][k])/2.0/sigma[i][j][k]/sigma[i][j][k] - log(sqrt(2*3.141592653589793)*sigma[i][j][k])
  return log_pdf
