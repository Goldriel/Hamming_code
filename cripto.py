def contr_bit(list):
    new_list = "00" + list[:1] + "0" + list[1:4] + "0" + list[4:11] + "0" + list[11:]
    return new_list