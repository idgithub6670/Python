def draw_grid(data):
    idata = data["idata"]
    hight = max(idata.values())

    for i in range(hight, 0, -1):
        row = ""
        for key in sorted(idata.keys()):
            if idata[key] >= i:
                row += "*  "
            else:
                row += "   "
        print(row)

    names = "  ".join(idata.keys())
    print(names)

input_data = {"idata": { "A": 5, "B": 8, "C": 3, "D": 1, "E": 6}}
draw_grid(input_data)
