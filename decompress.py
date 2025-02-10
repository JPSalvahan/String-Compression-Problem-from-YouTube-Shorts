def decompress(in_str):
    
    sliced = in_str.split("(")
    count_list = sliced[-1].split(",")
    out_str = ""
    for i in range(len(count_list)):
        out_str += in_str[i] * int(count_list[i])
        
    return out_str