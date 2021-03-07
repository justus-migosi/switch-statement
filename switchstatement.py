def month(i):
    switcher={
        0:'january',
        1:'february',
        2:'march',
        3:'april',
        4:'may',
        5:'june',
        6:'jully'
    }
    return switcher.get(i,"Invalid month of the year")

print(month(4))