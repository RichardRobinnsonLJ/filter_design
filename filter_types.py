import formula_filter

def RC():
    print("__________________________")
    print("What do you want to find?")
    print("1.Frequency")
    print("2.Resistor")
    print("3.Capacitor")
    choice = int(input("Enter the choice:  "))
    if(choice == 1):
        formula_filter.RC_for_f()
    elif(choice == 2):
        formula_filter.RC_for_r()
    elif(choice == 3):
        formula_filter.RC_for_c()
    else:
        print("Invalid Choice")
        exit()
def LC():
    print("__________________________")
    print("What do you want to find?")
    print("1.Frequency")
    print("2.Indcutor")
    print("3.Capacitor")
    choice = int(input("Enter the choice:  "))
    if(choice == 1):
        formula_filter.LC_for_f()
    elif(choice == 2):
        formula_filter.LC_for_l()
    elif(choice == 3):
        formula_filter.LC_for_c()
    else:
        print("Invalid Choice")
        exit()

def RL():
    print("__________________________")
    print("What do you want to find?")
    print("1.Frequency")
    print("2.Resistor")
    print("3.Inductor")
    choice = int(input("Enter the choice:  "))
    if(choice == 1):
        formula_filter.RL_for_f()
    elif(choice == 3):
        formula_filter.RL_for_l()
    elif(choice == 2):
        formula_filter.RL_for_r()
    else:
        print("Invalid Choice")
        exit()

def RCB():
    print("__________________________")
    print("What do you want to find?")
    print("1.Frequency")
    print("2.Resistor")
    print("3.Capacitor")
    choice = int(input("Enter the choice:  "))
    if(choice == 1):
        formula_filter.RCB_for_f()
    elif(choice == 2):
        formula_filter.RCB_for_r()
    elif(choice == 3):
        formula_filter.RCB_for_c()
    else:
        print("Invalid Choice")
        exit()
def LCB():
    print("__________________________")
    print("What do you want to find?")
    print("1.Frequency")
    print("2.Indcutor")
    print("3.Capacitor")
    choice = int(input("Enter the choice:  "))
    if(choice == 1):
        formula_filter.LCB_for_f()
    elif(choice == 2):
        formula_filter.LCB_for_l()
    elif(choice == 3):
        formula_filter.LCB_for_c()
    else:
        print("Invalid Choice")
        exit()

def RLB():
    print("__________________________")
    print("What do you want to find?")
    print("1.Frequency")
    print("2.Resistor")
    print("3.Inductor")
    choice = int(input("Enter the choice:  "))
    if(choice == 1):
        formula_filter.RLB_for_f()
    elif(choice == 3):
        formula_filter.RLB_for_l()
    elif(choice == 2):
        formula_filter.RLB_for_r()
    else:
        print("Invalid Choice")
        exit()

def RCS():
    print("__________________________")
    print("What do you want to find?")
    print("1.Frequency")
    print("2.Resistor")
    print("3.Capacitor")
    choice = int(input("Enter the choice:  "))
    if(choice == 1):
        formula_filter.RCS_for_f()
    elif(choice == 2):
        formula_filter.RCS_for_r()
    elif(choice == 3):
        formula_filter.RCS_for_c()
    else:
        print("Invalid Choice")
        exit()
def LCS():
    print("__________________________")
    print("What do you want to find?")
    print("1.Frequency")
    print("2.Indcutor")
    print("3.Capacitor")
    choice = int(input("Enter the choice:  "))
    if(choice == 1):
        formula_filter.LCS_for_f()
    elif(choice == 2):
        formula_filter.LCS_for_l()
    elif(choice == 3):
        formula_filter.LCS_for_c()
    else:
        print("Invalid Choice")
        exit()

def RLS():
    print("__________________________")
    print("What do you want to find?")
    print("1.Frequency")
    print("2.Resistor")
    print("3.Inductor")
    choice = int(input("Enter the choice:  "))
    if(choice == 1):
        formula_filter.RLS_for_f()
    elif(choice == 3):
        formula_filter.RLS_for_l()
    elif(choice == 2):
        formula_filter.RLS_for_r()
    else:
        print("Invalid Choice")
        exit()
