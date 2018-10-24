"""
Created on Wed Oct 24 11:29:07 2018

@author: Yosiyoshi
"""
function pow_array(n)
    n^2
end

result=zeros(Float64,10)
Threads.@threads for i=1:10
    result[i]=pow_array(i)
end
println(result)