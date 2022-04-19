COLOR_CODES = {"Absolute Zero": "#0048ba", "Acid Green": "b0bf1a" ,
               "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
               "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0",
               "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4",
               "aquamarine2": "#76eec6",  "aquamarine4": "#458b74"}

color_name = input("Enter a color name: ")
while color_name != "":
    print("{} = {}".format(color_name, COLOR_CODES.get(color_name)))
    color_name = input("Enter a color name: ")