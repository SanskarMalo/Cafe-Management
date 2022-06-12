import sys
class Home:
    def homeFun(this):
        print("\n\n====================================================================================================================")
        print("1- Menu")
        print("2- New Customer")
        print("3- Exit")
        ch1=int(input("Enter your choice :"))
        return ch1
        
class Customer(Home):
    c=[]
    def custFun(this):
        print("\n\n======================================================================================================================")
        nm=input("Enter Customer Name - ")
        cid=input("Enter Customer ID - ")
        this.c.append(cid)
        this.c.append(nm)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

   

class Menu(Customer):
    total=0
    def disMenu(this):
        print('\n\n==================================================== MENU =============================================================')
        print('1- Pizza')
        print('2- Burger')
        print('3- Sandwich')
        print('4- Ice-Cream')
        print('5- Tea')
        print('6- Coffe')
        print('7- Cold Drinks')
        print('8- Juice')
        print('9- Snacks')
        print('10- Exit')
        mc=int(input('\nEnter your choice-'))
        return mc

class Pizza(Menu):
    p=[]
    pt=1
    def disPizza(this):
        print('\n\n================================================== Pizza Items ================================================')
        print('Item Name \t\t\t\t Price')
        print("---------------------------------------------------------------------------------------------------------------------")
        print('a- Margherita \t\t\t\t ₹ 70')
        print('b- Cheese Margherita \t\t\t ₹ 100')
        print('c- Paneer Makhani \t\t\t ₹ 80')
        print('d- Tandoori Paneer \t\t\t ₹ 90')
        pc=input('\nEnter your order-')
        pq=int(input('Enter quantity-'))
        if pc=='a':
            pc='Margherita'
            pt=70*pq
        if pc=='b':
            pc='Cheese Margherita'
            pt=100*pq
        if pc=='c':
            pc='Paneer Makhani'
            pt=80*pq
        if pc=='d':
            pc='Tandoori Paneer'
            pt=90*pq
        this.p.append(pc)
        this.p.append(pq)
        this.p.append(pt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Burger(Pizza):
    b=[]
    bt=1
    def disBurger(this):
        print('\n\n========================================== Burger Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Veg Burger \t\t\t\t ₹ 70')
        print('b- Crunchy Veg Burger \t\t\t ₹ 80')
        print('c- Chicken Burger \t\t\t ₹ 90')
        print('d- Crunchy Chicken Burger \t\t\t ₹ 100')
        bc=input('\nEnter your order-')
        bq=int(input('Enter quantity-'))
        if bc=='a':
            bc='Veg Burger'
            bt=70*bq
        if bc=='b':
            bc='Crunchy Veg Burger'
            bt=80*bq
        if bc=='c':
            bc='Chicken Burger'
            bt=90*bq
        if bc=='d':
            bc='Crunchy Chicken Burger'
            bt=100*bq
        this.b.append(bc)
        this.b.append(bq)
        this.b.append(bt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Sandwich(Burger):
    s=[]
    st=1
    def disSandwich(this):
        print('\n\n========================================== Sandwich Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Veg Sandwich \t\t\t\t ₹ 40')
        print('b- Cheese  Sandwich \t\t\t ₹ 50')
        print('c- Chicken Sandwich \t\t\t ₹ 60')
        print('d- Egg Sandwich \t\t\t ₹ 45')
        sc=input('\nEnter your order-')
        sq=int(input('Enter quantity-'))
        if sc=='a':
            sc='Veg Sandwich'
            st=40*sq
        if sc=='b':
            sc='Cheese Sandwich'
            st=50*sq
        if sc=='c':
            sc='Chicken Sandwich'
            st=60*sq
        if sc=='d':
            sc='Egg Sandwich'
            st=45*sq
        this.s.append(sc)
        this.s.append(sq)
        this.s.append(st)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Ice_cream(Sandwich):
    i=[]
    it=1
    def disIce_cream(this):
        print('\n\n========================================== Ice-Cream Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Vanila Ice-Cream \t\t\t\t ₹ 40')
        print('b- Chocolate Ice-Cream \t\t\t ₹ 50')
        print('c- Kulfi \t\t\t ₹ 20')
        print('d- Mango Ice-Cream \t\t\t ₹ 30')
        ic=input('\nEnter your order-')
        iq=int(input('Enter quantity-'))
        if ic=='a':
            ic='Vanila Ice-Cream'
            it=40*iq
        if ic=='b':
            ic='Chocolate Ice-Cream'
            it=50*iq
        if ic=='c':
            ic='Kulfi'
            it=20*iq
        if ic=='d':
            ic='Mango Ice-Cream'
            it=30*iq
        this.i.append(ic)
        this.i.append(iq)
        this.i.append(it)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Tea(Ice_cream):
    t=[]
    tt=1
    def disTea(this):
        print('\n\n========================================== Tea Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- White Tea \t\t\t\t ₹ 10')
        print('b- Black Tea \t\t\t ₹ 15')
        print('c- Green \t\t\t ₹ 20')
        print('d- Herbal Tea\t\t\t ₹ 30')
        tc=input('\nEnter your order-')
        tq=int(input('Enter quantity-'))
        if tc=='a':
            tc='White Tea'
            tt=10*tq
        if tc=='b':
            tc='Black Tea'
            tt=15*tq
        if tc=='c':
            tc='Green Tea'
            tt=20*tq
        if tc=='d':
            tc='Herbal Tea'
            tt=30*tq
        this.t.append(tc)
        this.t.append(tq)
        this.t.append(tt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Coffee(Tea):
    cf=[]
    cft=1
    def disCoffee(this):
        print('\n\n========================================== Coffee Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Cold Coffee \t\t\t\t ₹ 100')
        print('b- Hot Coffee \t\t\t ₹ 50')
        print('c- Chocolate Coffee \t\t\t ₹ 150')
        cfc=input('\nEnter your order-')
        cfq=int(input('Enter quantity-'))
        if cfc=='a':
            cfc='Cold Coffee'
            cft=100*cfq
        if cfc=='b':
            cfc='Hot Coffee'
            cft=50*cfq
        if cfc=='c':
            cfc='Chocolate Coffee'
            cft=150*cfq
        this.cf.append(cfc)
        this.cf.append(cfq)
        this.cf.append(cft)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class ColdDrink(Coffee):
    cd=[]
    cdt=1
    def disColdDrink(this):
        print('\n\n========================================== Cold Drink Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Thumbs-up \t\t\t\t ₹ 20')
        print('b- Sprite \t\t\t ₹ 30')
        print('c- Mountain-Dew \t\t\t ₹ 50')
        print('d- Mirinda \t\t\t ₹ 50')
        print('e- CoCo-Cola \t\t\t ₹ 30')
        print('f- Jira-Soda \t\t\t ₹ 30')
        print('g- Red-Bull \t\t\t ₹ 100')
        cdc=input('\nEnter your order-')
        cdq=int(input('Enter quantity-'))
        if cdc=='a':
            cdc='Thumbs-up'
            cdt=20*cdq
        if cdc=='b':
            cdc='Sprite'
            cdt=30*cdq
        if cdc=='c':
            cdc='Mountain-Dew'
            cdt=50*cdq
        if cdc=='d':
            cdc='Mirinda'
            cdt=50*cdq
        if cdc=='e':
            cdc='CoCo-Cola'
            cdt=30*cdq
        if cdc=='f':
            cdc='Jira-Soda'
            cdt=30*cdq
        if cdc=='g':
            cdc='Red-Bull'
            cdt=100*cdq
        this.cd.append(cdc)
        this.cd.append(cdq)
        this.cd.append(cdt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Juice(ColdDrink):
    j=[]
    jt=1
    def disJuice(this):
        print('\n\n========================================== Juice Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Mango \t\t\t\t ₹ 30')
        print('b- Pineapple \t\t\t ₹ 30')
        print('c- Apple \t\t\t ₹ 50')
        print('d- Banana \t\t\t ₹ 20')
        print('e- Orange \t\t\t ₹ 20')
        print('f- Water-Melon \t\t\t ₹ 20')
        jc=input('\nEnter your order-')
        jq=int(input('Enter quantity-'))
        if jc=='a':
            jc='Mango'
            jt=30*jq
        if jc=='b':
            jc='Pineapple'
            jt=30*jq
        if jc=='c':
            jc='Apple'
            jt=50*jq
        if jc=='d':
            jc='Banana'
            jt=20*jq
        if jc=='e':
            jc='Orange'
            jt=20*jq
        if jc=='f':
            jc='Water-Melon'
            jt=20*jq
        this.j.append(jc)
        this.j.append(jq)
        this.j.append(jt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Snacks(Juice):
    sn=[]
    snt=1
    def disSnacks(this):
        print('\n\n========================================== Snaks Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- French-Fry \t\t\t\t ₹ 20')
        print('b- Pop-corn \t\t\t ₹ 20')
        print('c- Potato-Chips \t\t\t ₹ 20')
        print('d- Banana-Chips \t\t\t ₹ 20')
        print('e- Kurkure \t\t\t ₹ 20')
        snc=input('\nEnter your order-')
        snq=int(input('Enter quantity-'))
        if snc=='a':
            snc='French-Fry'
            snt=20*snq
        if snc=='b':
            snc='Pop-corn'
            snt=20*snq
        if snc=='c':
            snc='Potato-Chips'
            snt=20*snq
        if snc=='d':
            snc='Banana-Chips'
            snt=20*snq
        if snc=='e':
            snc='Kurkure'
            snt=20*snq
        this.sn.append(snc)
        this.sn.append(snq)
        this.sn.append(snt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy
    
    def end(this):
        cl=len(this.c)
        pl=len(this.p)
        bl=len(this.b)
        sl=len(this.s)
        il=len(this.i)
        tl=len(this.t)
        cfl=len(this.cf)
        cdl=len(this.cd)
        jl=len(this.j)
        snl=len(this.sn)
        if cl>0:
            print("\n\n********************************************************************************************************************")
            print("\n================================================== BILL ===============================================================")
            print("Customer Details-")
            print("ID - "+this.c[0])
            print("Name - "+this.c[1])
            print('\n\n=====================================================================================================================')
            print('Item Name \t\t\t\t\t Quantity \t\t\t Total')
            print("-------------------------------------------------------------------------------------------------------------------------")
            if pl>0:
                temp=0
                
                try:
                    while temp<=pl:
                        print(this.p[temp],' \t\t\t\t\t ',end='')
                        temp+=1
                        print(this.p[temp],end='')
                        temp+=1
                        print('\t\t\t\t',this.p[temp])
                        this.total=this.total+int(this.p[temp])
                        temp+=1
                except IndexError:
                    pass
            

            if bl>0:
                temp=0
                try:
                    while temp<=bl:
                        print(this.b[temp],' \t\t\t\t\t ',end='')
                        temp+=1
                        print(this.b[temp],end='')
                        temp+=1
                        print('\t\t\t\t',this.b[temp])
                        this.total=this.total+int(this.b[temp])
                        temp+=1
                except IndexError:
                    pass

            if sl>0:
                temp=0
                try:
                    while temp<=sl:
                        print(this.s[temp],' \t\t\t\t\t ',end='')
                        temp+=1
                        print(this.s[temp],end='')
                        temp+=1
                        print('\t\t\t\t',this.s[temp])
                        this.total=this.total+int(this.s[temp])
                        temp+=1
                except IndexError:
                    pass

            if il>0:
                temp=0
                try:
                    while temp<=il:
                        print(this.i[temp],' \t\t\t\t\t ',end='')
                        temp+=1
                        print(this.i[temp],end='')
                        temp+=1
                        print('\t\t\t\t',this.i[temp])
                        this.total=this.total+int(this.i[temp])
                        temp+=1
                except IndexError:
                    pass

            if tl>0:
                temp=0
                try:
                    while temp<=tl:
                        print(this.t[temp],' \t\t\t\t\t ',end='')
                        temp+=1
                        print(this.t[temp],end='')
                        temp+=1
                        print('\t\t\t\t',this.t[temp])
                        this.total=this.total+int(this.t[temp])
                        temp+=1
                except IndexError:
                    pass

            if cfl>0:
                temp=0
                try:
                    while temp<=cfl:
                        print(this.cf[temp],' \t\t\t\t\t ',end='')
                        temp+=1
                        print(this.cf[temp],end='')
                        temp+=1
                        print('\t\t\t\t',this.cf[temp])
                        this.total=this.total+int(this.cf[temp])
                        temp+=1
                except IndexError:
                    pass

            if cdl>0:
                temp=0
                try:
                    while temp<=cdl:
                        print(this.cd[temp],' \t\t\t\t\t ',end='')
                        temp+=1
                        print(this.cd[temp],end='')
                        temp+=1
                        print('\t\t\t\t',this.cd[temp])
                        this.total=this.total+int(this.cd[temp])
                        temp+=1
                except IndexError:
                    pass

            if jl>0:
                temp=0
                try:
                    while temp<=jl:
                        print(this.j[temp],' \t\t\t\t\t ',end='')
                        temp+=1
                        print(this.j[temp],end='')
                        temp+=1
                        print('\t\t\t\t',this.j[temp])
                        this.total=this.total+int(this.j[temp])
                        temp+=1
                except IndexError:
                    pass

            if snl>0:
                temp=0
                try:
                    while temp<=snl:
                        print(this.sn[temp],' \t\t\t\t\t ',end='')
                        temp+=1
                        print(this.sn[temp],end='')
                        temp+=1
                        print('\t\t\t\t',this.sn[temp])
                        this.total=this.total+int(this.sn[temp])
                        temp+=1
                except IndexError:
                    pass
            
            print("--------------------------------------------------------------------------------------------------------------------")
            print('Total Amount : ',this.total)
            sys.exit()
                    
                          
        else:
            sys.exit()
        
    


while True:
    h=Snacks()
    ch=h.homeFun()
    if(ch==1):#for displaying menu
        mc=h.disMenu()
        if mc==10:#for displaying home menu
            ch=h.homeFun()
        if mc==1:#for displaying Pizza menu
            dy=h.disPizza()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if mc==2:#for displaying Burger menu
            dy=h.disBurger()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if mc==3:#for displaying Sandwich menu
            dy=h.disSandwich()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if mc==4:#for displaying Ice_cream menu
            dy=h.disIce_cream()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if mc==5:#for displaying Tea menu
            dy=h.disTea()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if mc==6:#for displaying Coffee menu
            dy=h.disCoffee()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if mc==7:#for displaying ColdDrink menu
            dy=h.disColdDrink()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if mc==8:#for displaying Juice menu
            dy=h.disJuice()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if mc==9:#for displaying Snaks menu
            dy=h.disSnacks()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
                
    if(ch==2):
        dy=h.custFun()
        if dy=='y':
            continue
        if dy=='n':
            h.end()
    if(ch==3):#for displaying exit
        h.end()
