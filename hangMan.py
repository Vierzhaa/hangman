import random
import sys
sr = ['   _______'," //     |",'||   ','||   ','||   ','||   ','||_____']
keyword=['tokyo','toronto','london','lyon','washington','warsaw','beijing','berlin','jakarta','jeddah','paris','prague']
word=random.choice(keyword)
def goto(x,y):
    print(f"\033[{y};{x}H", end="")
    sys.stdout.flush()
print('\n'.join(map(str, sr)))
man=[" O ","<|>"," /`"]
goto(15,5)
print("Clue --> ")
goto(0,10)
lx=24
ly=12
i=0
j=5 
print("Tebak Kota")
tebak=""
while tebak != word:
    tebak=input("")
    if tebak != word:
        goto(len(tebak) + 2,ly-1)
        print('X(salah)')
        goto(lx,5)
        print(word[i])
        goto(8,j)
        print(man[i])
        j+=1
        i+=1
        lx+=1
        if i == 3:
            goto(0,ly)
            print(f"kamu kalah, katanya adalah {word}")
            break
        goto(0,ly)
        ly+=1
    else:
        goto(0,ly)
        print("kamu menang")
        
