import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('hirst_2021.jpg', 30)

color_array = []
for color in colors:
    color_ = []
    not_background = False
    for i in range(3):
        color_.append(color.rgb[i])
        if color.rgb[i] < 225:
            #check if any of rgb is < 200 indicates its not a background color
            not_background = True
    if not_background:
        color_array.append(tuple(color_))

print(color_array)




#dots 20. in size, 50. between