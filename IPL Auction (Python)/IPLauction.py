class File:
    def getAvailablePlayers(self):
        f=open("availablePlayers.txt")
        l=[]
        for i in f:
            d={}
            flag=False
            if i[:2]=="id":
                flag=True
                s=i.split(",")
                for j in s:
                    j=j.strip()
                    s1=j.split(":")
                    d.update({s1[0].strip():s1[1].strip()})
            if flag:
                l.append(d)
        f.close()
        return(l)
    def getSoldPlayers(self):
        f=open("soldPlayer.txt")
        l=[]
        for i in f:
            d={}
            flag=False
            if i[:2]=="id":
                flag=True
                s=i.split(",")
                for j in s:
                    j=j.strip()
                    s1=j.split(":")
                    d.update({s1[0].strip():s1[1].strip()})
            if flag:
                l.append(d)
        f.close()
        return(l)
    def getUnsoldPlayers(self):
        f=open("UnsoldPlayers.txt")
        l=[]
        for i in f:
            d={}
            flag=False
            if i[:2]=="id":
                flag=True
                s=i.split(",")
                for j in s:
                    j=j.strip()
                    s1=j.split(":")
                    d.update({s1[0].strip():s1[1].strip()})
            if flag:
                l.append(d)
        f.close()
        return(l)
    def getTeam(self):
        f=open("Teams.txt")
        l=[]
        for i in f:
            d={}
            flag=False
            if i[:4]=="Team":
                flag=True
                s=i.split(",")
                for j in s:
                    j=j.strip()
                    s1=j.split(":")
                    d.update({s1[0].strip():s1[1].strip()})
            if flag:
                l.append(d)
        f.close()
        return(l)
    def setAvailablePlayers(self,availablePlayer):
        f=open("availablePlayers.txt","w")
        f.write("      Available Players :\n")
        f.write("\n")
        for i in availablePlayer:
            f.write(f"id: {i['id']} , name: {i['name']} , role: {i['role']} , Base-Price: {i['Base-Price']}\n")
        f.close()
    def setSoldPlayers(self,soldPlayer):
        f=open("soldPlayer.txt","w")
        f.write("      Sold Players :\n")
        f.write("\n")
        for i in soldPlayer:
            f.write(f"id: {i['id']} , name: {i['name']} , role: {i['role']} , Base-Price: {i['Base-Price']} , Sold-Price: {i['Sold-Price']} , Team: {i['Team']}\n")
        f.close()
    def setUnsoldPlayers(self,unsoldPlayer):
        f=open("UnsoldPlayers.txt","w")
        f.write("    Unsold Players :\n")
        f.write("\n")
        for i in unsoldPlayer:
            f.write(f"id: {i['id']} , name: {i['name']} , role: {i['role']} , Base-Price: {i['Base-Price']}\n")
        f.close()
    def setTeam(self,team):
        f=open("Teams.txt","w")
        f.write("    Teams :\n")
        f.write("\n")
        for i in team:
            f.write(f"Team: {i['Team']} , Available Balance: {i['Available Balance']} , Total Spent: {i['Total Spent']}\n")
        f.close()
class IPL(File):
    def __init__(self):
        self.availablePlayer=super().getAvailablePlayers()
        self.soldPlayer=super().getSoldPlayers()
        self.unsoldPlayer=super().getUnsoldPlayers()
        self.team=super().getTeam()
    def convert(n):
        n=str(n)
        price=''
        if len(n)>=8:
            price=str(int(n)/10000000)+'Cr'
        else:
            price=str(int(n)/100000)+'L'
        return(price)
    def auction(self):
        try:
            d={}
            while True:
                id=input("Enter Player Id : ")
                if id.isnumeric():
                    for i in self.availablePlayer:
                        if(id==i["id"]):
                            d=i
                            break
                    if(len(d)==0):
                        flag=True
                        if flag:
                            for i in self.soldPlayer:
                                if(id==i["id"]):
                                    flag=False
                                    print("This Player is Already Sold, Please Enter Valid ID")
                        if flag:
                            for i in self.unsoldPlayer:
                                if(id==i["id"]):
                                    flag=False
                                    print("This Player is Already Unsold, Please Enter Valid ID")
                        if flag:
                            print("Player Not Found, Please Enter Valid ID")
                    else:
                        break
                else:
                    print("Please Enter Valid Id..")
            print("------- Player Details -------")
            n=d["name"]
            print("Name :",n)
            print("Role :",d["role"])
            print("Base Price :",IPL.convert(d["Base-Price"]))
            print("------------------------------")
            print("--> Start Bidding...")
            l=[]
            for i in self.team:
                tn=i["Team"]
                while True:
                    bid=''
                    if len(d["Base-Price"])>=8:
                        bid=input(f"Enter {tn}'s Bid Amount for {n} (in Cr) : ").strip()
                        try:
                            bid=str(int(float(bid)*10000000))
                        except ValueError:
                            bid=''
                    else:
                        bid=input(f"Enter {tn}'s Bid Amount for {n} (in Lakh) : ").strip()
                        try:
                            bid=str(int(float(bid)*100000))
                        except ValueError:
                            bid=''
                    if bid.isnumeric():
                        if bid=='0':
                            break
                        elif int(bid)>=int(d["Base-Price"]):
                            if(int(i["Available Balance"])>=int(bid)):
                                l.append({"team":tn,"bid":bid,"budget":i["Available Balance"]})
                                break
                            else:
                                print(f"{tn}'s Bid Amount Out Of Budget,Please Enter Again..")
                        else:
                            print("Bid Amount is Less than Base Price,Please Enter Again..")
                    else:
                        print("Please Enter Valid Bid Amount..")
            if(len(l)==0):
                print("----------- Details -----------")
                print("Name :",d["name"])
                print("Role :",d["role"])
                print("No Bid, Player Going To UNSOLD")
                print("-------------------------------")
                print("Press 1 to Confirm Bid")
                print("Press 2 to Cancel Bid")
                while True:
                    ch=input()
                    if(ch=='1'):
                        self.availablePlayer.remove(d)
                        self.unsoldPlayer.append(d)
                        print("--------------------------------")
                        print(f"{n} Went UNSOLD")
                        print("--------------------------------")
                        break
                    elif(ch=='2'):
                        print("-- This Bid Has Been Cancelled --")
                        break
                    else:
                        print("Please Enter Valid Choice")
            else:
                bidTeam=''
                bid=0
                teamBudget=0
                for i in l:
                    if int(i['bid'])==bid:
                        if int(i['budget'])>teamBudget:
                            bidTeam=i['team']
                            bid=int(i['bid'])
                            teamBudget=int(i['budget'])
                    elif int(i['bid'])>bid:
                        bidTeam=i['team']
                        bid=int(i['bid'])
                        teamBudget=int(i['budget'])
                print("--------- Details ---------")
                print("Name :",d["name"])
                print("Role :",d["role"])
                print("Sold To :",bidTeam)
                print("Sold Price :",IPL.convert(bid))
                print("---------------------------")
                print("Press 1 to Confirm Bid")
                print("Press 2 to Cancel Bid")
                while True:
                    ch=input()
                    if(ch=='1'):
                        teamDict={}
                        for i in self.team:
                            if i['Team']==bidTeam:
                                teamDict=i
                                break
                        index=self.team.index(teamDict)
                        teamDict.update({"Available Balance":str(int(teamDict["Available Balance"])-bid)})
                        teamDict.update({"Total Spent":str(int(teamDict["Total Spent"])+bid)})
                        self.team[index]=teamDict
                        self.availablePlayer.remove(d)
                        d.update({"Sold-Price":str(bid)})
                        d.update({"Team":bidTeam})
                        self.soldPlayer.append(d)
                        print("==========================================")
                        print(f"{n} Sold To {bidTeam} For {IPL.convert(bid)}")
                        print("==========================================")
                        break
                    elif(ch=='2'):
                        print("-- This Bid Has Been Cancelled --")
                        break
                    else:
                        print("Please Enter Valid Choice")
        except Exception as e:
            print(e)


    def displayTeam(self):
        print("----- Print Team -----")
        l=["SRH","GT","RCB","CSK","MI"]
        while True:
            team=input("Enter Team Name : ").upper().strip()
            teamDict={}
            for i in self.team:
                if i["Team"]==team:
                    teamDict=i
            if(len(teamDict)!=0):
                print("========== Team ",team," ==========")
                print("Remaining Purse : ",IPL.convert(teamDict['Available Balance']))
                print("Total Spent : ",IPL.convert(teamDict['Total Spent']))
                print("-------------------------------")
                print("--> Batters :")
                for i in self.soldPlayer:
                    if(i['Team']==team and i['role']=='Batsman'):
                        print("-",i['name'],f"({IPL.convert(i['Sold-Price'])})")
                print()
                print("--> Wicket-Keepers :")
                for i in self.soldPlayer:
                    if(i['Team']==team and i['role']=='Wk-Batsman'):
                        print("-",i['name'],f"({IPL.convert(i['Sold-Price'])})")
                print()
                print("--> All-Rounders :")
                for i in self.soldPlayer:
                    if(i['Team']==team and i['role']=='All-Rounder'):
                        print("-",i['name'],f"({IPL.convert(i['Sold-Price'])})")
                print()
                print("--> Bowlers :")
                for i in self.soldPlayer:
                    if(i['Team']==team and i['role']=='Bowler'):
                        print("-",i['name'],f"({IPL.convert(i['Sold-Price'])})")
                print("================================")
                break
            else:
                print("Team Not Found , Enter Valid Team Name")


    def addNewPlayer(self):
        print("-------- Register New Player --------")
        l=[]
        for i in self.availablePlayer:
            l.append(i['id'])
        for i in self.soldPlayer:
            l.append(i['id'])
        for i in self.unsoldPlayer:
            l.append(i['id'])
        try:
            while True:
                id=input("Enter ID : ")
                if id in l:
                    print("ID Already Exist, Please Enter Different Player ID")
                else:
                    if(id.isnumeric()):
                        break
                    else:
                        print("Please Enter Valid ID")
            while True:
                name=input("Enter Player Name : ").strip()
                c=0
                for i in name.split():
                    if i.isalpha():
                        c=c+1
                if(len(name.split())==c):
                    break
                else:
                    print("Please Enter Valid Player Name")
            print(f'-- Select Role for {name} --')
            print('Press 1 For Batsman')
            print('Press 2 For Wk-Batsman')
            print('Press 3 For All-Rounder')
            print('Press 4 For Bowler')
            while True:
                ch=input("Enter Choice : ")
                if ch=='1':
                    role='Batsman'
                    break
                elif ch=='2':
                    role='Wk-Batsman'
                    break
                elif ch=='3':
                    role='All-Rounder'
                    break
                elif ch=='4':
                    role='Bowler'
                    break
                else:
                    print("Invalid Choice, Please Enter Valid Choice")
            print(f'-- Select Base Price For {name} --')
            print('Press 1 For 2.0Cr')
            print('Press 2 For 1.0Cr')
            print('Press 3 For 50.0L')
            print('Press 4 For 20.0L')
            while True:
                ch=input("Enter Choice : ")
                if ch=='1':
                    bPrice='20000000'
                    break
                elif ch=='2':
                    bPrice='10000000'
                    break
                elif ch=='3':
                    bPrice='5000000'
                    break
                elif ch=='4':
                    bPrice='2000000'
                    break
                else:
                    print("Invalid Choice, Please Enter Valid Choice")
            print("--------- Details ---------")
            print("ID :",id)
            print("Name :",name)
            print("Role :",role)
            print("Base Price :",IPL.convert(bPrice))
            print("---------------------------")
            print("Press 1 to Confirm")
            print("Press 2 to Cancel")
            while True:
                ch=input()
                if(ch=='1'):
                    self.availablePlayer.append({'id':id,'name':name,'role':role,'Base-Price':bPrice})
                    print(f"===== {name} Registered Successfully =====")
                    break
                elif(ch=='2'):
                    print("-- Player Registration Cancelled --")
                    break
                else:
                    print("Please Enter Valid Choice")
        except Exception as e:
            print("Invalid Value, Task Failed")


    def displaySoldPlayers(self):
        print("---------------- Sold Players ----------------")
        print("==============================================")
        for i in self.soldPlayer:
            print("ID :",i['id'],end='              ')
            print("Name :",i['name'])
            print("Role :",i['role'],end='       ')
            print("Base Price :",IPL.convert(i['Base-Price']))
            print("Team :",i['Team'],end='           ')
            print("Sold Price :",IPL.convert(i['Sold-Price']))
            print("==============================================")


    def displayUnsoldPlayers(self):
        print("--------------- Unsold Players ---------------")
        print("==============================================")
        for  i in self.unsoldPlayer:
            print("ID :",i['id'],end='              ')
            print("Name :",i['name'])
            print("Role :",i['role'],end='       ')
            print("Base Price :",IPL.convert(i['Base-Price']))
            print("==============================================")
    

    def __del__(self):
        super().setAvailablePlayers(self.availablePlayer)
        super().setSoldPlayers(self.soldPlayer)
        super().setUnsoldPlayers(self.unsoldPlayer)
        super().setTeam(self.team)
i=IPL()
print("==============================================")
print("=========== Welcome To IPL Auction ===========")
print("==============================================")
while True:
    print("------- Main Menu -------")
    print("1. Start Auction")
    print("2. Print Team Details")
    print("3. Register New Player")
    print("4. Print Sold Players")
    print("5. Print Unsold Players")
    print("6. EXIT")
    ch=input("Enter Your Choice : ").strip()
    if ch=='1':
        print("----- Auction Starts -----")
        i.auction()
        while True:
            print("1. Continue Auction")
            print("2. Back To Main Manu")
            ch1=input("Enter Your Choice : ")
            if ch1=='1':
                print("----- Continue Auction -----")
                i.auction()
            elif ch1=='2':
                break
            else:
                print("Please Enter Valid Choice")
    elif ch=='2':
        i.displayTeam()
    elif ch=='3':
        i.addNewPlayer()
    elif ch=='4':
        i.displaySoldPlayers()
    elif ch=='5':
        i.displayUnsoldPlayers()
    elif ch=='6':
        del i
        print("======== Thank Tou ========")
        break
    else:
        print("Please Enter Valid Choice")