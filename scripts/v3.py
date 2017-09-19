#Program for post-processing of OpenFOAM data 
#for vectors with fft
import matplotlib.pyplot as plt;
import numpy as np;
import pylab as pl;
import os;
import math as mt;
from scipy.fftpack import fft;

directory='./case/'; 	#directory of OpenFOAM case
tfrom=1;		#start time
tupto=400;		#end time
cell=2837;		#cell number for which variation is to be observed


scell=21+cell;
zrn=tupto-tfrom+1;
vdata=np.zeros(zrn);
os.chdir(directory);
tfromo=tfrom;
while tfrom<tupto:
	stfrom=str(tfrom);
	os.chdir(stfrom);
	datafile=open('U');
	lines=datafile.readlines();
	sp=lines[scell];
	sp1=sp.replace("(","");
	sp2=sp1.replace(")","");
	Ux,Uy,Uz=sp2.split();	
	Ux=float(Ux);
	Uy=float(Uy);
	Uz=float(Uz);
	Urs=(Ux*Ux)+(Uy*Uy)+(Uz*Uz);
	Ur=math.sqrt(Urs);
	i=tfrom-tfromo;
	vdata[i]=Ur;
	os.chdir('..');
	tfrom=tfrom+1;

os.chdir('..');
tdata=np.arange(tfromo,tupto+1,1);

ut=fft(vdata);
uts=np.fft.fftshift(ut);
utl=np.log(uts);
k1=2.00*(mt.pi)/400;

k2=np.arange(-200,200,1);

k=k1*k2;
knew=np.arange(-200,200,1);
pl.plot(k,utl);
#fftdata=fft(vdata);
#plt.line = plt.plot(tdata,vdata,'-s');
#plt.line = plt.plot(tdata,vdata);
pl.xlabel('Frequency');
pl.ylabel('Velocity');
strcell=str(cell);
pl.title('Variation at Cell Number: '+strcell);
#pl.savefig('velocity_fft_plot.png');
pl.show();


