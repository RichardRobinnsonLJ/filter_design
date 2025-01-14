from filter_types import RC,LC,RL,RCB,RCS,LCB,LCS,RLB,RLS

def lpf():
    print("_____________________________________________________________")
    print("Choose your configuration for LPF")
    print("1.RC")
    print("2.LC")
    print("3.RL")
    config = int(input("Ënter you choice:  "))
    if(config == 1):
        RC()
        print("Connect R in Series and C in parallel")
    elif(config == 2):
        LC()
        print("Connect L in Series and C in parallel")
    elif(config == 2):
        RL()
        print("Connect L in Series and R in parallel")
    else:
        print("Unkown input")
        exit()  
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def hpf():
    print("_____________________________________________________________")
    print("Choose your configuration for HPF")
    print("1.RC")
    print("2.LC")
    print("3.RL")
    config = int(input("Ënter you choice:  "))
    if(config == 1):
        RC()
        print("Connect R in Parallel and C in Series")
    elif(config == 2):
        LC()
        print("Connect L in Parallel and C in Series")
    elif(config == 2):
        RL()
        print("Connect L in Parallel and R in Series")
    else:
        print("Unkown input")
        exit()    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bpf():
    print("_____________________________________________________________")
    print("Choose your configuration for BPF")
    print("1.RC")
    print("2.LC")
    print("3.RL")
    config = int(input("Ënter you choice:  "))
    if(config == 1):
        RCB()
    elif(config == 2):
        LCB()
    elif(config == 2):
        RLB()
    else:
        print("Unkown input")
        exit()  


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def bsf():
    print("_____________________________________________________________")
    print("Choose your configuration for LPF")
    print("1.RC")
    print("2.LC")
    print("3.RL")
    config = int(input("Ënter you choice:  "))
    if(config == 1):
        RCS()
    elif(config == 2):
        LCS()
    elif(config == 2):
        RLS()
    else:
        print("Unkown input")
        exit()  

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    print("____________________________________________________________")
    print("Choose a type of filer you want to design(Enter the digit)")
    print("1.LOW Pass filter")
    print("2.HIGH Pass filter")
    print("3.Band Pass filter")
    print("4.Band Stop filter")
    option = int(input("Ënter you choice:  "))
    if(option==1):
        lpf()
    elif(option == 2):
        hpf()
    elif(option ==3):
        bpf()
    elif(option==4):
        bsf()
    else:
        print("Unkown input")
        exit()




if __name__=="__main__":
    main()
