#include <time.h>
#include "TRandom3.h"
#include <math.h>

const unsigned int xDim = 196;
const unsigned int yDim = 609;
const unsigned int zDim = 38;
//const double const1 = log(sqrt(2*3.141592653589793));
//log_pdf[i][j][k] = -(x[i][j][0] - mean[i][j][k])*(x[i][j][0] - mean[i][j][k])/2.0/sigma[i][j][k]/sigma[i][j][k] - log(sqrt(2*3.141592653589793)*sigma[i][j][k]);
//tmp1 = x[i][j][0] - mean[i][j][k];
//log_pdf[i][j][k] = -tmp1*tmp1/2.0/sigma[i][j][k]/sigma[i][j][k] - log(sigma[i][j][k]) - const1;
//log_pdf[i][j][k] = -(x[i][j][0] - mean[i][j][k])*(x[i][j][0] - mean[i][j][k])/2.0/sigma[i][j][k]/sigma[i][j][k] - log(sigma[i][j][k]) - const1;

void log_gaussian(const double (&x)[xDim][yDim][1], const double (&mean)[xDim][yDim][zDim], const double (&sigma)[xDim][yDim][zDim], double (&log_pdf)[xDim][yDim][zDim]);
//double sum_log_gaussian(const double (&log_pdf)[xDim][yDim][zDim]);

//c
//python
//   N           Min           Max        Median           Avg        Stddev
//x 100    -8451013.8    -8439433.1    -8446314.9      -8446048         2471
//   N           Min           Max        Median           Avg        Stddev
//x 100      -8452397    -8436518.6      -8445765      -8445778         2822
//
//                                                (8446048 - 8445778)/247.0 = 1.1
//

int main(){
  TRandom3 *rnd = new TRandom3(1234567890);
  //x shape     =  (196, 609, 1)
  //mean shape  =  (196, 609, 38)
  //sigma shape =  (196, 609, 38)
  //
  double x[xDim][yDim][1];
  double mean[xDim][yDim][zDim];
  double sigma[xDim][yDim][zDim];
  double log_pdf[xDim][yDim][zDim];
  //  
  unsigned int i = 0;
  unsigned int j = 0;
  unsigned int k = 0;
  unsigned int l = 0;
  //
  double x_mean = 3.0;
  double x_sigma = 1.0;
  double sigma_mean = 2.0;
  double sigma_sigma = 0.001;
  //
  for(i = 0;i<xDim;i++){
    for(j = 0;j<yDim;j++){
      x[i][j][0] = rnd->Gaus(x_mean,x_sigma);
      for(k = 0;k<zDim;k++){
	mean[i][j][k] = rnd->Gaus(x_mean,x_sigma);
	sigma[i][j][k] = rnd->Gaus(sigma_mean,sigma_sigma);
      }
    }
  }
  //
  unsigned int n=100;
  double tottime = 0.0;
  for(l=0;l<n;l++){
    clock_t tic = clock();
    log_gaussian(x, mean, sigma, log_pdf);
    clock_t toc = clock();
    tottime = tottime + (double)(toc - tic);
    //printf("aa-> %f \n",sum_log_gaussian(log_pdf));
  }
  printf("Elapsed: %f seconds\n", tottime / CLOCKS_PER_SEC / n);
  return 0;
}

//log_pdf = -(x - mean) ** 2 / (2 * sigma ** 2)
//log_pdf = log_pdf - np.log((np.sqrt(2 * np.pi) * sigma))
void log_gaussian(const double (&x)[xDim][yDim][1], const double (&mean)[xDim][yDim][zDim], const double (&sigma)[xDim][yDim][zDim], double (&log_pdf)[xDim][yDim][zDim]){
  unsigned int i = 0;
  unsigned int j = 0;
  unsigned int k = 0;
  //double tmp1;
  for(i = 0;i<xDim;i++){
    for(j = 0;j<yDim;j++){
      for(k = 0;k<zDim;k++){
	//log_pdf[i][j][k] = -(x[i][j][0] - mean[i][j][k])*(x[i][j][0] - mean[i][j][k])/2.0/sigma[i][j][k]/sigma[i][j][k] - log(2.506628274631*sigma[i][j][k]);
	log_pdf[i][j][k] = -(x[i][j][0] - mean[i][j][k])*(x[i][j][0] - mean[i][j][k])/2.0/sigma[i][j][k]/sigma[i][j][k] - log(sqrt(2*3.141592653589793)*sigma[i][j][k]);
      }
    }
  }
}

//double sum_log_gaussian(const double (&log_pdf)[xDim][yDim][zDim]){
//  unsigned int i = 0;
//  unsigned int j = 0;
//  unsigned int k = 0;
//  double sum = 0.0;
//  for(i = 0;i<xDim;i++)
//    for(j = 0;j<yDim;j++)
//      for(k = 0;k<zDim;k++)
//	sum += log_pdf[i][j][k];
//  return sum;
//}
