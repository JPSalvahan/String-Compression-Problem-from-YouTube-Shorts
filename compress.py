def compress(in_str):
    
    char_slice = in_str[0]
    count_slice = "("
    count = 1
    for i in range(len(in_str)-1):
        if in_str[i] != in_str[i+1]:
            char_slice += in_str[i+1]
            count_slice += str(count) + ","
            count = 1
        else:
            count += 1

    count_slice += str(count)
        
    return char_slice + count_slice