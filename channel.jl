"""
Author: Yosiyoshi
"""

function channel_test()
	Channel(ctype=String, csize=23) do channel::Channel{String}
		i = 1
		while i > 0
			sl, i = rand([("A", i+1), ("B", +(i<5))])
			put!(channel, sl)
		end
	put!(channel, "CDEFG")
	end
end

channel_test()