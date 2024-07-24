im, ic = 3, 3
fm, fc = 0, 0
status, flag, select = 0, 0, 0

def display(bpass1, bpass2):
    global fm, fc, flag, im, ic
    print("\n\n\n", end='')
    for i in range(fm):
        print(" M ", end='')
    for i in range(fc):
        print(" C ", end='')
    if flag == 0:
        print(f"     _________WATER__B0({bpass1},{bpass2})AT  ", end='')
    else:
        print(f"     BO({bpass1},{bpass2})AT_WATER__________  ", end='')
    for i in range(im):
        print(" M ", end='')
    for i in range(ic):
        print(" C ", end='')

def win():
    global fc, fm
    if fc == 3 and fm == 3:
        return 0
    else:
        return 1

def solution():
    global im, ic, fm, fc, flag, select
    while win():
        if flag == 0:
            if select == 1:
                display('C', ' ')
                ic += 1
            elif select == 2:
                display('C', 'M')
                ic += 1
                im += 1

            if ((im - 2) >= ic and (fm + 2) >= fc) or (im - 2) == 0:
                im -= 2
                select = 1
                display('M', 'M')
                flag = 1
            elif ((ic - 2) < im and (fm == 0 or (fc + 2) <= fm)) or im == 0:
                ic -= 2
                select = 2
                display('C', 'C')
                flag = 1
            elif (ic - 1) <= (im - 1) and (fm + 1) >= (fc + 1):
                ic -= 1
                im -= 1
                select = 3
                display('M', 'C')
                flag = 1
        else:
            if select == 1:
                display('M', 'M')
                fm += 2
            elif select == 2:
                display('C', 'C')
                fc += 2
            elif select == 3:
                display('M', 'C')
                fc += 1
                fm += 1

            if win():
                if (fc > 1 and fm == 0) or im == 0:
                    fc -= 1
                    select = 1
                    display('C', ' ')
                    flag = 0
                elif (ic + 2) > im:
                    fc -= 1
                    fm -= 1
                    select = 2
                    display('C', 'M')
                    flag = 0

if __name__ == "__main__":
    print("MISSIONARIES AND CANNIBALS")
    display(' ', ' ')
    solution()
    display(' ', ' ')
    print("\n\n")
