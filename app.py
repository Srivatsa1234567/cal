atk=float(input("enter atk of character"))
scaling=float(input("enter dmg scaling of character"))
crit=float(input("enter crit dmg% of character"))
bonus=float(input("enter elemental/physical dmg bonus of character"))
lvl=float(input("enter charcater level"))
res=float(input("enter resitance of enemy"))
elvl=float(input("enter level fo enemy"))

r = float(elvl*5+500)
reduction=float(r/(r+5*lvl+500))

#d=float(lvl+100/(1-0)*(elvl+100)+(lvl+100))


dmg=float(atk*(scaling/100)*(1+crit/100)*(bonus/100)*(1-res/100)*(1-reduction/100)*(1-reduction/100))

print(dmg)
print(reduction)