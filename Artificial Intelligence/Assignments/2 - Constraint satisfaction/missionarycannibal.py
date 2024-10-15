im = 3  # Initial missionaries on the initial side
ic = 3  # Initial cannibals on the initial side
fm = 0  # Final missionaries on the other side
fc = 0  # Final cannibals on the other side
flag = 0  # Position of the boat: 0 = left side, 1 = right side
select = 0  # Selection of the next move

def display(bpass1, bpass2):
    print("\n\n\n")
    # Display final side
    for _ in range(fm):
        print(" M ", end="")
    for _ in range(fc):
        print(" C ", end="")

    if flag == 0:
        print(f"     __________WATER___________BO({bpass1},{bpass2})AT  ", end="")
    else:
        print(f"     BO({bpass1},{bpass2})AT__________WATER___________  ", end="")

    # Display initial side
    for _ in range(im):
        print(" M ", end="")
    for _ in range(ic):
        print(" C ", end="")
    print()

# Check if the game is won
def win():
    return not (fc == 3 and fm == 3)

# Solve the problem
def solution():
    global im, ic, fm, fc, flag, select
    while win():
        if flag == 0:  # Boat on the left side
            if select == 1:
                display('C', ' ')
                ic += 1
            elif select == 2:
                display('C', 'M')
                ic += 1
                im += 1
            
            if (im - 2 >= ic and fm + 2 >= fc) or (im - 2 == 0):
                im -= 2
                select = 1
                display('M', 'M')
                flag = 1
            elif ic - 2 < im and (fm == 0 or fc + 2 <= fm) or im == 0:
                ic -= 2
                select = 2
                display('C', 'C')
                flag = 1
            elif ic - 1 <= im - 1 and fm + 1 >= fc + 1:
                ic -= 1
                im -= 1
                select = 3
                display('M', 'C')
                flag = 1

        else:  # Boat on the right side
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
                if fc > 1 and fm == 0 or im == 0:
                    fc -= 1
                    select = 1
                    display('C', ' ')
                    flag = 0
                elif ic + 2 > im:
                    fc -= 1
                    fm -= 1
                    select = 2
                    display('C', 'M')
                    flag = 0

# Main function
def main():
    print("MISSIONARIES AND CANNIBALS")
    display(' ', ' ')
    solution()
    display(' ', ' ')
    print("\n\n")

if __name__ == "__main__":
    main()
