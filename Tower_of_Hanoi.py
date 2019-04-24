
## Author Name: Kasam Dhakal
  
def Tower_of_Hanoi(num,initial_destination,spare,final_destination,inF,outF):
    flag=0
    length=len(spare)
    

    if (inF[0]==outF[0] and flag!=1):
        flag=1
        Hanoi=1

        if(inF[Hanoi]!=outF[Hanoi]):
            if (inF[Hanoi]==initial_destination and outF[Hanoi]==final_destination):
                 disc_move(Hanoi,initial_destination,spare,final_destination)
            else:
                    if (inF[Hanoi]==initial_destination and outF[Hanoi]==spare):
                       disc_move(hanoi,initial_destination,final_destination,spare)
                    else:
                        if(inF[Hanoi]==spare and outF[Hanoi]==final_destination):
                           disc_move(Hanoi,spare,initial_destination,final_destination)
                        else:
                            if(inF[Hanoi]==spare and outF[Hanoi]==initial_destination):
                               disc_move(Hanoi,spare,final_destination,initial_destination)
                            else:
                                if(inF[Hanoi]==final_destination and outF[Hanoi]==spare):
                                    disc_move(Hanoi,final_destination,initial_destination,spare)
                                else:
                                   diasc_move(Hanoi,final_destination,spare,initial_destination)

            cat=outF[Hanoi]
            Hanoi+=1

           
            while (Hanoi!=num):
                if (inF[Hanoi]!=cat):
                    if(inF[Hanoi]==initial_destination and cat==final_destination):
                        disc_move(Hanoi,initial_destination,spare,final_destination)
                    else:
                        if(inF[Hanoi]==initial_destination and cat==spare):
                            disc_move(Hanoi,initial_destination,final_destination,spare)
                        else:
                            if(inF[Hanoi]==spare and cat==final_destination):
                                disc_move(Hanoi,spare,initial_destination,final_destination)
                            else:
                                if(inF[Hanoi]==spare and cat==initial_destination):
                                    disc_move(Hanoi,spare,final_destination,initial_destination)
                                else:
                                    if(inF[Hanoi]==final_destination and cat==spare):
                                        disc_move(Hanoi,final_destination,initial_destination,spare)
                                    else:
                                        disc_move(Hanoi,final_destination,spare,initial_destination)
                else:
                    if(inF[Hanoi]==initial_destination):
                        disc_move(Hanoi,initial_destination,spare,initial_destination)
                    else:
                        if(inF[Hanoi]==spare):
                            disc_move(Hanoi,spare,final_destination,spare)
                        else:
                            disc_move(Hanoi,final_destination,spare,final_destination)
                cat=outF[Hanoi]
                Hanoi+=1
            
           
            Hanoi=2

            if(cat==initial_destination):
                while (Hanoi!=num):
                    if(outF[Hanoi]==final_destination):
                        disc_move(Hanoi,inital_destination,spare,final_destination)
                    else:
                        if(outF[Hanoi]==spare):
                            disc_move(Hanoi,initial_destination,final_destination,spare)
                    spare+=1
            else:
                if(cat==spare):
                    while(Hanoi!=num):
                        if(outF[Hanoi]==final_destination):
                            disc_move(Hanoi,spare,initial_destination,final_destination)
                        else:
                            if(outF[Hanoi]==initial_destination):
                                disc_move(Hanoi,spare,initial_destination)
                        Hanoi+=1
                else:
                    while(Hanoi!=num):
                        if(outF[Hanoi]==initial_destination):
                            disc_move(Hanoi,final_destination,spare,initial_destination)
                        else:
                            if(outF[Hanoi]==spare):
                                disc_move(Hanoi,final_destination,initial_destination,spare)
                        Hanoi+=1
    
    
    if (inF[0]!=outF[0] and flag!=1):
        flag=1
        Hanoi=1

        cat=outF[Hanoi]
        while(Hanoi!=num):
            if(inF[Hanoi]!=cat):
                if(inF[Hanoi]==initial_destination):
                    disc_move(Hanoi,initial_destination,spare,final_destination)
                else:
                    if(inF[Hanoi]==spare):
                        disc_move(Hanoi,spare,initial_destination,final_destination)
                    else:
                        disc_move(Hanoi,final_destination,spare,final_destination)
            else:
                if(inF[Hanoi]==initial_destination):
                    disc_move(Hanoi,initial_destination,spare,final_destination)
                else:
                    if(inF[Hanoi]==spare):
                        disc_move(Hanoi,spare,initial_destination,final_destination)
                    else:
                        disc_move(Hanoi,final_destination,spare,final_destination)

            cat=outF[Hanoi]
            Hanoi+=1

        Hanoi=0
        if(outF[Hanoi]==spare and inF[Hanoi]==initial_destination):
            disc_move(Hanoi,initial_destination,final_destination,spare)

        Hanoi+=1

        while(Hanoi!=num):
            if(outF[Hanoi]!=final_destination and outF[Hanoi]!=final_destination):
                disc_move(Hanoi,final_destination,initial_destination,spare)
            else:
                if(outF[Hanoi]!=final_destination and outF[Hanoi]!=spare):
                    disc_move(Hanoi,final_destination,spare,initial_destination)
                else:
                    disc_move(Hanoi,final_destination,spare,final_destination)
            Hanoi+=1


def disc_move(number,initial,temp,destination):
    if (number>=0):
        print('Disc',number,' move from ',initial,' to ',destination)

def main() :
    
    print("INITIAL CONFIGURATION: ABCA TO FINAL_CONFIGURATION : ACBC")
    Tower_of_Hanoi(4,'A','B','C',['A','B','C','A'],['A','C','B','C'])
    
    
    
    print("INITIAL CONFIGURATION: ABCA TO FINAL CONFIGURATION : BCAA")
    Tower_of_Hanoi(4,'A','B','C',['A','B','C','A'],['B','C','A','A'])
main()
