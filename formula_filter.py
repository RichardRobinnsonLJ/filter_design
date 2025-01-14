import math

def RC_for_f():
    r=float(input("Enter value of Resistor: "))
    c=float(input("Enter value of Capacitor: "))
    f=(1/(2*math.pi*r*c))
    print("Value of Cutoff Frequency: "+str(f))

def RC_for_r():
    f=float(input("Enter value of Frequency: "))
    c=float(input("Enter value of Capacitor: "))
    r=(1/(2*math.pi*f*c))
    print("Value of Resistor:" + str(r))


def RC_for_c():
    f=float(input("Enter value of Frequency: "))
    r=float(input("Enter value of Resistor: "))
    c=(1/(2*math.pi*f*r))
    print("Value of Capacitor:" + str(c))

#_________________________________________________________________________________________________
def RL_for_f():
    r=float(input("Enter value of Resistor: "))
    l=float(input("Enter value of Inductor: "))
    f=(r/(2*math.pi*l))
    print("Value of Cutoff Frequency: "+str(f))

def RL_for_r():
    f=float(input("Enter value of Frequency: "))
    l=float(input("Enter value of Inductor: "))
    r=(2*math.pi*f*l)
    print("Value of Resistor:" + str(r))

def RL_for_l():
    f=float(input("Enter value of Frequency: "))
    r=float(input("Enter value of Resistor: "))
    l=(r/(2*math.pi*f))
    print("Value of Inductor:" + str(l))



#_________________________________________________________________________________________________
def LC_for_f():
    c=float(input("Enter value of Capacitor: "))
    l=float(input("Enter value of Inductor: "))
    f=(1/(2*math.pi*(math.sqrt(l*c))))
    print("Value of Cutoff Frequency: "+str(f))

def LC_for_c():
    f=float(input("Enter value of Frequency: "))
    l=float(input("Enter value of Inductor: "))
    c=(1/(4*(math.pi**2)*(f**2)*l))
    print("Value of Capacitor:" + str(c))

def LC_for_l():
    f=float(input("Enter value of Frequency: "))
    c=float(input("Enter value of Capacitor: "))
    l=(1/(4*(math.pi**2)*(f**2)*c))
    print("Value of Inductor:" + str(l))

#_________________________________________________________________________________________________

def RCB_for_f():
    r1=float(input("Enter value of Resistor_1: "))
    c1=float(input("Enter value of Capacitor_1: "))
    r2=float(input("Enter value of Resistor_2: "))
    c2=float(input("Enter value of Capacitor_2: "))
    if(r1*c1>r2*c2):
        fl=(1/(2*math.pi*r1*c1))
        fh=(1/(2*math.pi*r2*c2))
    else:
        fh=(1/(2*math.pi*r1*c1))
        fl=(1/(2*math.pi*r2*c2))
    val=RCB_Cutoff(fl,fh)
    print("Value of Cutoff Frequency: "+str(val))

def RCB_for_r():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    c=float(input("Enter value of Capacitor: "))
    r1=(1/(2*math.pi*fl*c))
    r2=(1/(2*math.pi*fh*c))
    print("Connect "+str(c)+" C in Series with "+ str(r1)+" R in parallel for HPF(Lower Cutoff Frequency)")
    print("Connect "+str(c)+" C in Parallel with "+ str(r2)+" R in series for LPF(Higher Cutoff Frequency)")
    


def RCB_for_c():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    r=float(input("Enter value of Resistor: "))
    c1=(1/(2*math.pi*fl*r))
    c2=(1/(2*math.pi*fh*r))
    print("Connect "+str(c1)+" C in Series with "+ str(r)+" R in parallel for HPF(Lower Cutoff Frequency)")
    print("Connect "+str(c2)+" C in Parallel with "+ str(r)+" R in series for LPF(Higher Cutoff Frequency)")

def RCB_Cutoff(fl,fh):
    val=math.sqrt(fl*fh)
    print("Value of Cutoff Frequency: "+str(val))
    return val
#_________________________________________________________________________________________________



def RCS_for_f():
    r1=float(input("Enter value of Resistor_1: "))
    c1=float(input("Enter value of Capacitor_1: "))
    r2=float(input("Enter value of Resistor_2: "))
    c2=float(input("Enter value of Capacitor_2: "))
    if(r1*c1>r2*c2):
        fl=(1/(2*math.pi*r1*c1))
        fh=(1/(2*math.pi*r2*c2))
    else:
        fh=(1/(2*math.pi*r1*c1))
        fl=(1/(2*math.pi*r2*c2))
    val=RCB_Cutoff(fl,fh)
    print("Value of Cutoff Frequency: "+str(val))

def RCS_for_r():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    c=float(input("Enter value of Capacitor: "))
    r1=(1/(2*math.pi*fl*c))
    r2=(1/(2*math.pi*fh*c))
    print("Connect "+str(c)+" C in Parallel with "+ str(r1)+" R for (Lower Cutoff Frequency)")
    print("Connect "+str(c)+" C in Series with "+ str(r2)+"  R for (Higher Cutoff Frequency)")
    


def RCS_for_c():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    r=float(input("Enter value of Resistor: "))
    c1=(1/(2*math.pi*fl*r))
    c2=(1/(2*math.pi*fh*r))
    print("Connect "+str(c1)+" C in Parallel with "+ str(r)+" R for (Lower Cutoff Frequency)")
    print("Connect "+str(c2)+" C in Series with "+ str(r)+" R for (Higher Cutoff Frequency)")

#_________________________________________________________________________________________________

def RLB_for_f():
    r1=float(input("Enter value of Resistor_1: "))
    c1=float(input("Enter value of Inductor_1: "))
    r2=float(input("Enter value of Resistor_2: "))
    c2=float(input("Enter value of Inductor_2: "))
    if(r1*c1>r2*c2):
        fl=(r1/(2*math.pi*c1))
        fh=(r2/(2*math.pi*c2))
    else:
        fh=(r1/(2*math.pi*c1))
        fl=(r2/(2*math.pi*c2))
    val=RCB_Cutoff(fl,fh)
    print("Value of Cutoff Frequency: "+str(val))

def RLB_for_r():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    c=float(input("Enter value of Inductor: "))
    r1=(2*math.pi*fl*c)
    r2=(2*math.pi*fh*c)
    print("Connect "+str(c)+" L in Series with "+ str(r1)+" R in parallel for HPF(Lower Cutoff Frequency)")
    print("Connect "+str(c)+" L in Parallel with "+ str(r2)+" R in series for LPF(Higher Cutoff Frequency)")

def RLB_for_l():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    r=float(input("Enter value of Resistor: "))
    c1=(r1/(2*math.pi*fl))
    c2=(r/(2*math.pi*fh))
    print("Connect "+str(c1)+" L in Series with "+ str(r)+" in parallel for HPF(Lower Cutoff Frequency)")
    print("Connect "+str(c2)+" L in Parallel with "+ str(r)+" in series for LPF(Higher Cutoff Frequency)")

def RLS_for_f():
    r1=float(input("Enter value of Resistor_1: "))
    c1=float(input("Enter value of Inductor_2: "))
    r2=float(input("Enter value of Resistor_1: "))
    c2=float(input("Enter value of Inductor_2: "))
    if(r1*c1>r2*c2):
        fl=(r1/(2*math.pi*c1))
        fh=(r2/(2*math.pi*c2))
    else:
        fh=(r1/(2*math.pi*c1))
        fl=(r2/(2*math.pi*c2))
    val=RCB_Cutoff(fl,fh)
    print("Value of Cutoff Frequency: "+str(val))

def RLS_for_r():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    c=float(input("Enter value of Inductor: "))
    r1=(2*math.pi*fl*c)
    r2=(2*math.pi*fh*c)
    print("Connect "+str(c)+" L in Series with "+ str(r1)+" R in parallel for HPF(Lower Cutoff Frequency)")
    print("Connect "+str(c)+" L in Parallel with "+ str(r2)+" R in series for LPF(Higher Cutoff Frequency)")

def RLS_for_l():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    r=float(input("Enter value of Resistor: "))
    c1=(r1/(2*math.pi*fl))
    c2=(r/(2*math.pi*fh))
    print("Connect "+str(c1)+" L in Series with "+ str(r)+" in parallel for HPF(Lower Cutoff Frequency)")
    print("Connect "+str(c2)+" L in Parallel with "+ str(r)+" in series for LPF(Higher Cutoff Frequency)")

#_________________________________________________________________________________________________

def LCB_for_f():
    r1=float(input("Enter value of Resistor_1: "))
    c1=float(input("Enter value of Inductor_2: "))
    r2=float(input("Enter value of Resistor_2: "))
    c2=float(input("Enter value of Inductor_2: "))
    if(r1*c1>r2*c2):
        fl=(r1/(2*math.pi*c1))
        fh=(r2/(2*math.pi*c2))
    else:
        fh=(r1/(2*math.pi*c1))
        fl=(r2/(2*math.pi*c2))
    val=RCB_Cutoff(fl,fh)
    print("Value of Cutoff Frequency: "+str(val))

def LCB_for_c():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    l=float(input("Enter value of Inductor: "))
    c1=(1/(4*(math.pi**2)*(fl**2)*l))
    c2=(1/(4*(math.pi**2)*(fh**2)*l))
    print("Connect "+str(l+" L in Series with "+ str(c1)+" C (Lower Cutoff Frequency)"))
    print("Connect "+str(l+" L in Parallel with "+ str(c2)+" C (Higher Cutoff Frequency)"))

def LCB_for_l():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    c=float(input("Enter value of Capacitor: "))
    l1=(1/(4*(math.pi**2)*(fl**2)*r))
    l2=(1/(4*(math.pi**2)*(fh**2)*r))
    print("Connect "+str(l1)+" L in Series with "+ str(c)+" C (Lower Cutoff Frequency)")
    print("Connect "+str(l2)+" L in Parallel with "+ str(c)+" C F(Higher Cutoff Frequency)")

def LCS_for_f():
    r1=float(input("Enter value of Capacitor_1: "))
    c1=float(input("Enter value of Inductor_1: "))
    r2=float(input("Enter value of Capacitor_2: "))
    c2=float(input("Enter value of Inductor_2: "))
    if(r1*c1>r2*c2):
        fl=(1/(2*math.pi*(math.sqrt(r1*c1))))
        fh=(1/(2*math.pi*(math.sqrt(r2*c2))))
    else:
        fh=(1/(2*math.pi*(math.sqrt(r1*c1))))
        fl=(1/(2*math.pi*(math.sqrt(r2*c2))))
    val=RCB_Cutoff(fl,fh)
    print("Value of Cutoff Frequency: "+str(val))

def LCS_for_c():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    l=float(input("Enter value of Inductor: "))
    c1=(1/(4*(math.pi**2)*(fl**2)*l))
    c2=(1/(4*(math.pi**2)*(fh**2)*l))
    print("Connect "+str(l)+" L in Series with "+ str(c1)+" C (Lower Cutoff Frequency)")
    print("Connect "+str(l)+" L in Parallel with "+ str(c2)+" C (Higher Cutoff Frequency)")

def LCS_for_l():
    fl=float(input("Enter value of lower Frequency: "))
    fh=float(input("Enter value of Higher Frequency: "))
    c=float(input("Enter value of Capacitor: "))
    l1=(1/(4*(math.pi**2)*(fl**2)*r))
    l2=(1/(4*(math.pi**2)*(fh**2)*r))
    print("Connect "+str(l1)+" L in Series with "+ str(c)+" C (Lower Cutoff Frequency)")
    print("Connect "+str(l2)+" L in Parallel with "+ str(c)+" C (Higher Cutoff Frequency)")