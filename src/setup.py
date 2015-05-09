#from distutils.core import setup
#import numpy
#import py2exe
 
#setup(console=[''])

from distutils.core import setup
import py2exe
 
from distutils.filelist import findall
import os
import matplotlib
#matplotlibdatadir = matplotlib.get_data_path()
#matplotlibdata = findall(matplotlibdatadir)
matplotlibdata_files = []
#for f in matplotlibdata:
#    dirname = os.path.join('matplotlibdata', f[len(matplotlibdatadir)+1:])
#    matplotlibdata_files.append((os.path.split(dirname)[0], [f]))
  
matplotlibdata_files += matplotlib.get_py2exe_datafiles()  
setup(
    console=['x86_detection_experiment.py'],
    #options={
    #       'py2exe': {
    #             'packages' : ['matplotlib', 'pytz'],
    #                }
    #        },
    data_files=matplotlibdata_files
 )