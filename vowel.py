txt="Dit is een boek."
h=[0,0,0,0,0,0]
h[0]=txt.count("oo")
h[1]=txt.count("y")
h[2]=txt.count("oe")
h[3]=txt.count("u")
h[4]=txt.count("ie")
h[5]=txt.count("ee")
print("txt:", txt)
print("oo:y:oe:u:ie existing in the text:", h)
if max(h)==h[0]:
    print("English?")
if max(h)==h[1]:
    print("English?")
if max(h)==h[2]:
    print("Dutch or Old Indonesian?")
if max(h)==h[3]:
    print("Malay, Japanese Romaji or African?")
if max(h)==h[4]:
    print("French or German?")
if max(h)==h[5]:
    print("Dutch?")
