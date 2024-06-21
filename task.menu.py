x=180
menu=[10,20,40,80,100,140,200]
y=False
for i in range(len(menu)):
    for j in range (i+1,len(menu)):
        if menu [i]+menu[j]==x:
            print(f"the two items that add up to ",x,"are",menu[i], "and",menu[j])
            y = True
            break
        if y:
            break
        if not y:
            print("no two items add up to ",x)
            