from Trajectories import Trajectory

def _load(modul):
    global module
    module = modul
    print("\nByl načten modul " + modul + "\n")

def load(para):
    global module
    if len(para) != 1:
        print("špatné použití příkazu load")
    else:
        target = para[0].capitalize()
        if target == "Traj" or target == "Trajectorie" or target == "Trajectories":
            _load("Trajectory")
        else:
            print("Modul " + target + " neexistuje!")
    

def execute(comm):
    spl = comm.split()
    if len(spl) < 1:
        return 0
    com = spl[0]
    para = spl[1:]
    if com == "quit":
        return "term"
    elif com == "load":
        load(para)
    return 0

print(
    "FyzCalc ver. 1.0\n"
    "Dokumentace se nachází ve složce Doc\n"
    "By Rotundista\n"
    )
run = True
module = "FyzCalc"
while run:
    try:
        command = input(module + ">")
        if module == "FyzCalc":
            ret = execute(command)
            if module == "Trajectory":
                traj = Trajectory()
        elif module == "Trajectory":
            ret = traj.execute(command)
        else:
            print("Problém s modulem")
            run = False
        if ret == "term":
            run = False
    except KeyboardInterrupt:
        print("Na ukončení je potřeba použít příkaz quit")
    except:
        print("Došlo k neznámému problému")