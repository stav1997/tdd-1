class BMI:

    def bmi(hight, weight):
        if hight < 0 or weight < 0:
            return -1
        if type(hight) == str or type(weight) == str:
            return -1
        else:
            return weight / hight ** 2


def result(bmi_result):
    if type(bmi_result) == str:
        return -1
    elif bmi_result < 0:
        return -1
    elif 0 >= bmi_result < 18.5:
        return "under weight"
    elif 18.5 >= bmi_result < 25:
        return "normal weight"
    elif 25 >= bmi_result < 29.9:
        return "over weight"
    elif 30 >= bmi_result < 34.9:
        return "obesity first degree"
    elif 35 >= bmi_result < 39.9:
        return "obesity second degree"
    elif bmi_result <= 40:
        return "obesity third degree"
    else:
        return -1

