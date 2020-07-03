def number_to_text(number):
    number = str(int(number))
    number_length = len(number)

    single_numb = ["","մեկ","երկու","երեք","չորս","հինգ","վեց","յոթ","ութ","ինը"]
    ten_number = ["","տաս","քսան","երեսուն","քառասուն","հիսուն","վաթսուն","յոթանասուն","ութսուն","իննսուն"]

    if number_length == 1:
        number_text = single_numb[int(number)] if single_numb[int(number)] != "" else "0"
    elif number == '10':
        number_text = "տաս"
    elif number_length == 2 and number[0] == '1':
        number_text = "տասն" + single_numb[int(number[1])]
    elif number_length == 2:
        number_text = ten_number[int(number[0])] + single_numb[int(number[1])]
    elif number_length == 3:
        number_text = number_to_text(number[-3]) + " հարյուր " + number_to_text(number[-2:])

    return number_text

def number_convert(numb):
    suf     = ["միլիարդ","միլիոն","հազար",""]
    num_str = str(numb).zfill(12)
    numb_converted = ""

    if int(numb) == 0:
        numb_converted = "Զրո"
    else:
        j = 0
        for i in suf:
            if number_to_text(num_str[0+j:3+j]) != "0":
                numb_converted += number_to_text(num_str[0+j:3+j]) + " " + i + " "
            j+=3

    return numb_converted

def number_float_convert(numb):
    numb_str  = str(float(numb)).split('.')
    numb_pre  = numb_str[0]
    numb_suf  = numb_str[1][:3]
    numb_suf_len  = len(numb_suf)
    sufix     = ["","տասնորդական","հարյուրերորդական","հազարերորդական"]

    if numb_suf != '0':
        float_text = number_convert(numb_pre) + "ամբողջ " + number_convert(numb_suf) + sufix[numb_suf_len]

    else:
        float_text = number_convert(numb_pre)

    return float_text




num = input("Խնդրում ենք մուտքագրել 1-ից 12 նիշանոց թիվ։ ")
while True:
    try:
        #print(number_convert(num))
        print(number_float_convert(num))
        break
    except:
        num = input("Կրկին փորձիր։ ")
