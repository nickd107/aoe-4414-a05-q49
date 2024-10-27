# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv..
# Determines the output shape and operation count of a fully-connected layer

# Parameters:
# c_in: input channel count
# n_wv: number of weight vectors

# Output:
# c_out:  output channel count
# h_out:  output height count
# w_out:  output width count
# adds:   number of additions performed
# muls:   number of multiplications performed
# divs:   number of divisions performed
#
# Written by Nick Dickson

# import Python modules
import math # math module
import sys # argv

# constants
R_E_KM = 6378.137
E_E    = 0.081819221456


# initialize script arguments
c_in = float('nan') 
n_wv = float('nan') 

# parse script arguments
if len(sys.argv) == 3:
  c_in = int(sys.argv[1])
  n_wv = int(sys.argv[2])
else:
  print(\
    'Usage: '\
    'python3 full_ops.py c_in n_wv'\
  )
  exit()

### script below this line ###

h_out = 1

w_out = 1

muls = n_wv * c_in

adds = n_wv * c_in

divs = 0 #Check this

c_out = n_wv 

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed