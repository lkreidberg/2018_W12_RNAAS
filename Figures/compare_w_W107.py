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
Ms_12 = 1.35
Ms_107 = 0.69

d_12 = 0.02293 #AU
d_107 = 0.055

Ts_12 = 6300.
Ts_107 = 4430.

amp_12 = H_12*R_12/Rs_12**2
amp_107 = H_107*R_107/Rs_107**2


Roche_107 = R_107*(2.*Ms_107/M_107)**0.3333
Roche_12 = R_12*(2.*Ms_12/M_12)**0.3333

print "relative Roche radii (Roche_107/Roche_12):", Roche_107/Roche_12
print "relative Roche transit depth:", (Roche_107/Roche_12)**2/(Rs_107/Rs_12)**2
print "relative Roche/star:", (Roche_107/Roche_12)/(Rs_107/Rs_12)

print "relative scale height amplitude", H_107/H_12
print "relative feature amplitude", amp_107/amp_12

print "relative bolometric flux (107/12)", (Ts_107**4/Ts_12**4)/(d_107/d_12)**2
print "relative bolometric flux (12/107)", ((Ts_107**4/Ts_12**4)/(d_107/d_12)**2)**(-1)
