def addStringInts(str_in1 : str, str_in2 : str):
    fl_in1 = float(str_in1)
    fl_in2 = float(str_in2)

    fl_res = float(fl_in1 + fl_in2)
    str_res = f"{fl_res:0.0f}"

    return str_res

print(addStringInts("20","1002"))