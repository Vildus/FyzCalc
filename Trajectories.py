# Dokumentace
#
# FYZ Kalkulátor by Rotundista
# ver 1.2
# Program počítá s g=9.8 m/s2 (zatím nezměnitelné)
# Program pošítá pouze v SI jednotkách      ..zatím
# Výchozí hodnoty jsou jako default 0
# Program je schopný se vypořádat s debilitou uživatele
# Všechny příkazy:
# -----------------------
# quit
#   -Ukončí program
# set <parametr> <hodnota>
#   -Nastaví parametr na hodnotu
#   -Hodnata může být celá nebo desetinná, kladná nebo záporná
#   -Povolené parametry jsou:
#       v0 Počáteční rychlost (kladná-nahoru záporná-dolů)
#       h  Počáteční výška
#   -např. set v0 -3.6
# status
#   -Zobrazí aktuální zadané hodnoty
# calc <stav>
#   -Vypočítá zadaný stav
#   -Možné stavy jsou:
#      max    Vypočítá maximální výšku a čas, za jaký se k ní předmět dostane
#      impact Vypočítá, za jakou dobu a v jaké rychlosti narazí předmět do země
# sim <parametr> <hodnota>
#   -Asi nejvíc op příkaz
#   -Funguje podle parametru
#   -Parametry:
#      t Vypočítá výšku a rychlost dosaženou za zadaný čas
#      v Vypočítá čas, za který předmět dosáhne zadané rychlosti (Pozor na znaménko, směr dolů je záporný)
#      h Vypočítá, za jak douho předmět dosáhne zadané výšky

import math


class Trajectory:
    def __init__(self):
        self.v0 = 0
        self.h0 = 0
        self.g = 9.8

    def execute(self, inp):
        spl = inp.split()
        if len(spl) < 1:
            return 0
        com = spl[0]
        para = spl[1:]
        if com == "quit":
            return "term"
        elif com == "set":
            self.set(para)
        elif com == "status":
            self.status(para)
        elif com == "calc":
            self.calc(para)
        elif com == "sim":
            self.sim(para)
        else:
            print("Příkaz " + com + " neexistuje")
        return 0

    def set(self, para):
        if len(para) != 2:
            print("Chybné použití příkazu set")
            return 0
        var = para[0]
        try:
            value = float(para[1])
        except ValueError:
            print(str(para[1]) + " není platná hodnota")
            return 0
        if var == "v0":
            self.v0 = value
            print("Počáteční rychlost byla nastavena jako " + str(value) + " m/s")
        elif var == "h":
            self.h0 = value
            print("Počáteční výška byla nastavena jako " + str(value) + " m")
        else:
            print("Proměná " + var + " neexistuje")
        return 0

    def status(self, para):
        if len(para) != 0:
            print("Příkaz status nemá žádné parametry")
        print("Počáteční rychlost je " + str(self.v0) + " m/s")
        print("Počáteční výška je " + str(self.h0) + " m")
        return 0

    def calc(self, para):
        if len(para) != 1:
            print("Špatné použití příkazu calc")
            return 0
        typ = para[0]
        if typ == "max":
            if self.v0 < 0:
                print("K maximálnímu bodu již došlo")
                return 0
            t = self.v0 / self.g
            print("Maximálního bodu bude dosaženo za " + str(t) + " sec")
            max_h = self.h0 + self.v0 ** 2 / (2 * self.g)
            print("Bude dosažena maximální výška " + str(max_h) + " m")
        elif typ == "impact":
            t = (self.v0 + math.sqrt(self.v0 ** 2 + 2 * self.g * self.h0)) / self.g
            v = self.v0 - self.g * t
            if t < 0:
                print("K nárazu již došlo")
                return 0
            print("K nárazu dojde za " + str(t) + " sec\nV rychlosti " + str(-v) + " m/s")
        else:
            print("Stav " + typ + " není platný")
        return 0

    def sim(self, para):
        if len(para) != 2:
            print("Chybné použití příkazu sim")
            return 0
        var = para[0]
        try:
            value = float(para[1])
        except ValueError:
            print(str(para[1]) + " není platná hodnota")
            return 0
        if var == "t":
            v = self.v0 - value * self.g
            h = self.h0 + self.v0 * value - value ** 2 * self.g / 2
            print("Za " + str(value) + " sec bude:")
            print("Rychlost " + str(v) + " m/s")
            print("Výška " + str(h) + " metrů")
        elif var == "v":
            t = (self.v0-value)/self.g
            if t < 0:
                print("Rychlost dosažena leda tak v minulosi")
            else:
                print("Rychlost bude dosažena za " + str(t) + " sec")
        elif var == "h":
            if value == 0:
                self.calc(["impact"])
                return 0
            d = self.v0**2 + 2*self.g*(self.h0 - value)
            if d < 0:
                print("Výška nedosažitelná")
            else:
                sol1 = -(-self.v0+math.sqrt(d))/self.g
                sol2 = (self.v0+math.sqrt(d))/self.g
                if sol2 < 0:
                    print("Výška dosažitelná leda v minulosti")
                elif sol1 < 0:
                    print("Výška bude dosažena za " + str(sol2) + " sec")
                else:
                    print("Výška bude dosažena za " + str(sol1) + " sec a za " + str(sol2) + " sec")
        else:
            print("Hodnota " + var + " není simulovatelná")
        return 0


print(
    "Kalkulačka volného pádu a svislého hodu\n"
    "Dokumentace se nachází ve zdrojovém kódu\n"
    "By Rotundista\n"
    "ver 1.2\n"
)
run = True
traj = Trajectory()
while run:
    try:
        command = input("VP>")
        ret = traj.execute(command)
        if ret == "term":
            run = False
    except KeyboardInterrupt:
        print("Na ukončení je potřeba použít příkaz quit")
    except:
        print("Došlo k neznámému problému")
