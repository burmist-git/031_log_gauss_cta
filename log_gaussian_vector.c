#include <time.h>
#include "TRandom3.h"
#include <math.h>
#include <iostream>
#include <vector>

const unsigned int xDim = 196;
const unsigned int yDim = 609;
const unsigned int zDim = 38;

void log_gaussian(const auto (&x), const auto (&mean), const auto (&sigma), auto (&log_pdf));
double makesum(const auto (&log_pdf));

int main(){
  TRandom3 *rnd = new TRandom3(1234567890);
  std::vector<std::vector<std::vector<double>>> x;
  std::vector<std::vector<std::vector<double>>> mean;
  std::vector<std::vector<std::vector<double>>> sigma;
  std::vector<std::vector<std::vector<double>>> log_pdf;
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
  // x
  for ( i=0; i<xDim; i++){
    std::vector<std::vector<double>> ppx;
    for ( j=0; j<yDim; j++){
      std::vector<double> px;
      for ( k=0; k<1; k++){
	px.push_back(rnd->Gaus(x_mean,x_sigma));
      }
      ppx.push_back(px);
    }
    x.push_back(ppx);
  }
  // mean
  for ( i=0; i<xDim; i++){
    std::vector<std::vector<double>> ppx;
    for ( j=0; j<yDim; j++){
      std::vector<double> px;
      for ( k=0; k<zDim; k++){
	px.push_back(rnd->Gaus(x_mean,x_sigma));
      }
      ppx.push_back(px);
    }
    mean.push_back(ppx);
  }
  // sigma
  for ( i=0; i<xDim; i++){
    std::vector<std::vector<double>> ppx;
    for ( j=0; j<yDim; j++){
      std::vector<double> px;
      for ( k=0; k<zDim; k++){
	px.push_back(rnd->Gaus(sigma_mean,sigma_sigma));
      }
      ppx.push_back(px);
    }
    sigma.push_back(ppx);
  }
  // log_pdf
  for ( i=0; i<xDim; i++){
    std::vector<std::vector<double>> ppx;
    for ( j=0; j<yDim; j++){
      std::vector<double> px;
      for ( k=0; k<zDim; k++){
	px.push_back(0.0);
      }
      ppx.push_back(px);
    }
    log_pdf.push_back(ppx);
  }
  //
  unsigned int n=100;
  double tottime = 0.0;
  for(l=0;l<n;l++){
    clock_t tic = clock();
    log_gaussian(x, mean, sigma, log_pdf);
    clock_t toc = clock();
    //printf("%10.2f \n", makesum(log_pdf));
    tottime = tottime + (double)(toc - tic);
  }
  printf("Elapsed: %f seconds\n", tottime / CLOCKS_PER_SEC / n);
  //  
  return 0;
}

void log_gaussian(const auto (&x), const auto (&mean), const auto (&sigma), auto (&log_pdf)){
  unsigned int i = 0;
  unsigned int j = 0;
  unsigned int k = 0;
  for(i = 0;i<xDim;i++)
    for(j = 0;j<yDim;j++)
      for(k = 0;k<zDim;k++)
	log_pdf.at(i).at(j).at(k) = -(x.at(i).at(j).at(0) - mean.at(i).at(j).at(k))*(x.at(i).at(j).at(0) - mean.at(i).at(j).at(k))/2.0/sigma.at(i).at(j).at(k)/sigma.at(i).at(j).at(k) - log(sqrt(2*3.141592653589793)*sigma.at(i).at(j).at(k));
}

double makesum(const auto (&log_pdf)){
  unsigned int i = 0;
  unsigned int j = 0;
  unsigned int k = 0;
  double sum = 0;
  for(i = 0;i<xDim;i++)
    for(j = 0;j<yDim;j++)
      for(k = 0;k<zDim;k++)
	sum += log_pdf.at(i).at(j).at(k);
  return sum;
}
