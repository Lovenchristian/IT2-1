print("Gyldige operatorer er '+', '-', '*', '/', '^' og '!'. Du kan også bruke '(' og ')'")
spm = input("Skriv inn et mattestykke: ").replace(" ","")
siffere = ["1","2","3","4","5","6","7","8","9","0"]

def fakultet(tall):
    if (tall==1):
        return 1
    else:
        return tall* fakultet(tall-1)

d = 0
for i in range(1,len(spm)):
    if (spm[i+d]=="-"):
        print(i+d, ": ", spm[i+d], " : ", spm[i-1+d])
        try:
            siffere.index(spm[i-1+d])
            spm = spm[:i+d] + '+' + spm[i+d:]  
            d += 1
        except:
            pass

def regnUt(spm):
    sum_ = 0
    ledd = spm.split("+")
    for i in range(len(ledd)):
        faktor = ledd[i].split("*")
        ledd[i] = faktor
    
    for i in range(len(ledd)):
        for j in range(len(ledd[i])):
            divisor = ledd[i][j].split("/")
            ledd[i][j] = divisor
    
    for i in range(len(ledd)):
        for j in range(len(ledd[i])):
            for k in range(len(ledd[i][j])):
                potens = ledd[i][j][k].split("^")
                ledd[i][j][k] = potens
    
    print(f"Programmet organiserer informasjonen slik: {ledd}")
    
    #regn ut fakultet
    for i in range(len(ledd)):
        for j in range(len(ledd[i])):
            for k in range(len(ledd[i][j])):
                for l in range(len(ledd[i][j][k])):
                    item = ledd[i][j][k][l]
                    if (item[len(item)-1]=="!"):
                        item = item[:len(item)-1]
                        ledd[i][j][k][l] = str(fakultet(float(item)))
                    elif (item=="e"):
                        ledd[i][j][k][l] = "2.718281828459"
                    elif (item=="pi"):
                        ledd[i][j][k][l] = "3.141592653589793238"
    
    #regn ut resten
    for i in range(len(ledd)):
        produkt = 1
        for j in range(len(ledd[i])):
            grunntall = float(ledd[i][j][0][0])
            for l in range(1,len(ledd[i][j][0])):
                grunntall = grunntall**float(ledd[i][j][0][l])
            divident = grunntall
            for k in range(1,len(ledd[i][j])):                
                grunntall = float(ledd[i][j][k][0])
                for l in range(1,len(ledd[i][j][k])):
                    grunntall = grunntall**float(ledd[i][j][k][l])
                divident /= grunntall
            produkt *= divident
        sum_ += produkt
    return sum_

#isolerer paranteser of regner ut inni. Kjører till ale paranteser er regnet ut + en gang til

l = None
b = True
while b:   
    b = False
    for i in range(len(spm)):
        if (spm[i]=="("):
            l = i
            b = True
        elif (spm[i]==")"):
            spm = spm[:l] + str(regnUt(spm[l+1:i])) + spm[i+1:]
            break

print(f"Summen er lik: {regnUt(spm)}")