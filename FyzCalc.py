from moduly.Trajectories import Trajectory, cat


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
    elif com == "help":
        cat("doc/General.txt")
    else:
        if len(spl) > 0:
            print("Příkaz " + com + " neexistuje!\nPro seznam příkazů použijte příkaz help")
    return 0


print(
    "FyzCalc ver. 1.0\n"
    "Pro tutoriál použijte příkaz help\n"
    "By VP 2021\n"
)
run = True
default_mod = "FyzCalc"
module = default_mod
while run:
    try:
        command = input(module + ">")
        if module == default_mod:
            ret = execute(command)
            if ret == "term":
                run = False
            if module == "Trajectory":
                traj = Trajectory()
        elif module == "Trajectory":
            ret = traj.execute(command)
            if ret == "term":
                print("Modul Trajectories ukončen")
                module = default_mod
        else:
            print("\nFATAL ERROR 1\n")
            run = False
    except KeyboardInterrupt:
        print("Na ukončení je potřeba použít příkaz quit")
    except:
        print("Došlo k neznámému problému")
