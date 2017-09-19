#Program for post-processing of OpenFOAM data 
#for scalars
import matplotlib.pyplot as plt;
import numpy as np;
import pylab as pl;
import os;

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
	datafile=open('Q');
	lines=datafile.readlines();
	i=tfrom-tfromo;
	vdata[i]=lines[scell];
	os.chdir('..');
	tfrom=tfrom+1;

os.chdir('..');
tdata=np.arange(tfromo,tupto+1,1);
plt.line = plt.plot(tdata,vdata,'-s');
pl.xlabel('Time');
pl.ylabel('Q');
strcell=str(cell);
pl.title('Variation at Cell Number: '+strcell);
pl.savefig('Q_scalar_plot.png');
pl.show();


