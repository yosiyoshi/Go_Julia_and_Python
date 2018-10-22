"""
Author: Yoshiyosi
"""
function pythag(a,b)
    return √(a**2+b**2)
end

function pythag2(a,b)
    if a>=b
        return √(a**2-b**2)
    end
    if a<b
        return √(b**2-a**2)
    end
end

println(pythag(3,4))
println(pythag(√(2),√(2)))
println(pythag2(5,4))
println(pythag2(4,5))
