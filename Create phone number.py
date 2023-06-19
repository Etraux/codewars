def create_phone_number(n):
    #your code here
    result = ""
    if len(n) == 10:
        for i, val in enumerate(n):
            if i == 0:
                result = result + "(" + str(val)
            elif i == 2:
                result = result + str(val) + ")" + " "
            elif i == 5:
                result = result + str(val) + "-"
            else:
                result = result + str(val)
        return result