h = zeros(Float64, 3, 3, 1)
h[1,1,1] = 1
h[2,2,1] = 3
h[3,3,1] = 5
println(h)
sum(h)