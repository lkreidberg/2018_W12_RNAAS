import numpy as np

T_12 = 2500.
T_107 = 780.

M_12 = 1.404
M_107 = 0.12

R_12 = 1.736
R_107 = 0.94

g_12 = M_12/R_12**2
g_107 = M_107/R_107**2

H_12 = T_12/g_12
H_107 = T_107/g_107

Rs_12 = 1.6
Rs_107 = 0.66

amp_12 = H_12*R_12/Rs_12**2
amp_107 = H_107*R_107/Rs_107**2

print "relative scale height amplitude", H_107/H_12
print "relative feature amplitude", amp_107/amp_12
