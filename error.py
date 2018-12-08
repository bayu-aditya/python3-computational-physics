#module
""" 
    untuk memunculkan teks dan menghentikan program
"""
import sys
def err(string):
    print(string)
    input('Tekan enter untuk menghentikan program')
    sys.exit()