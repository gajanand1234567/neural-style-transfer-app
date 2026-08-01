import sys
import os

# Add NST_Code directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'NST_Code'))

# Change working directory to NST_Code so all relative paths inside app.py resolve correctly
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'NST_Code'))

from app import app

if __name__ == '__main__':
    app.run()
