﻿"""
Author: Yosiyoshi
"""
C1 = C2 = D1 = D2 = 1.0
u0 = v0 = 0.7
dt = 0.05
 
function euler(u,v)
    u_calc = (1 + dt*D1 - dt*C1*v) * u
    v_calc = (1 - dt*D2 + dt*C2*u) * v
    u,v = u_calc, v_calc
    return u, v
end

euler(u0,v0)
u,v = u0, v0
uv_sq = [ u0, v0 ]

for i in 1:500
    u,v = euler(u,v) 
end