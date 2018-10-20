# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:32:09 2018

@author: Yosiyoshi
"""
c1=c2=d1=d2=1.0
u0=v0=0.7
dt=0.05

def euler(u,v):
    u_calc=(1+dt*d1-dt*c1*v)*u
    v_calc=(1-dt*d2+dt*c2*u)*v
    u,v=u_calc,v_calc
    return u,v

print("Initial:",euler(u0,v0))
u,v=u0,v0
for i in range(1,11):
    u,v=euler(u,v)
    print("Step",i,":",u,v)