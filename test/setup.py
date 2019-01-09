from distutils.core import setup
import py2exe

option = {
    'bundle_files':1,
    'compressed': True
}
setup(
    options = {'py2exe': option},
    windows =[{'script':'KoyominZ.py'}],
    zipfile = None, 
    )