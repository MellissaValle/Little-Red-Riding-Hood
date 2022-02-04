import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
import time

##variables
speed = 100
starvation = 50
strength = 100
redHood= 0
flower=0
butterfly=0
red=0
grandma=0
mother=0
hunter=0
hoodon=0
grandmaGown=0
fight=0
town=0
forest=0
bearattack=0
def stats(): ## Stats and inventory
    global speed
    global starvation
    global strength
    global mother
    global hunter
    global grandma
    global red
    global redHood
    global grandmaGown
    time.sleep(1)
    print ("\n**************************")
    print ("    Speed =    " , speed )
    print ("    Strength = " , strength )
    print ("    Starvation = " , int(starvation))
    if (redHood==1):
        
        print ("    Red's Hood = ", redHood)
    if grandmaGown==1:
        print("    Grandma's Gown =", grandmaGown)
    if (red==1):
        print("You Ate Red Riding Hood")

    if (grandma==1):
        print("You Ate Grandma")

    if mother==1:
        print("You Ate Mother")
    if hunter==1:
        print("You Ate the Hunter")

    print("**************************")
def evilmerchant():
    global speed
    global starvation
    global strength
    global mother
    global hunter
    global grandma
    global red
    global redHood
    global grandmaGown
    color.write("\n You hear a sound of a crash nearby","STRING")
    time.sleep(3)
    color.write("\n You ignored the sound but as you walk closer to grandma's house, you saw fruits all over the floor. The merchant's cart appears to have fallen over.","STRING")
    time.sleep(4)
    choice=input("\n Should I go help him? or ignore him\n A: Help him \n B: Ignore him\n C: Eat him \n D: Steal his fruits\n")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b'):
        if (choice=='A' or choice =='a'):
            color.write("\n Merchant: What are you doing?!?!?","COMMENT")
            time.sleep(3)
            color.write("\n I'm helping you pick up your stuff and this is how you greet me?","KEYWORD")
            time.sleep(3)
            color.write("\n Merchant: Oh, I thought you were stealing my merchandise. In that case thank you for your help.","COMMENT")
            if redHood==1:
                time.sleep(3)
                color.write("\n By the way, that is a beautiful piece of clothing you have there.","COMMENT")
                time.sleep(3)
                color.write("\n It's not mine, just holding it for a friend","KEYWORD")
            time.sleep(3)
            color.write("\n After awhile you finish picking up all of the merchant's merchandise and he heads off after saying thanks","STRING")
            if redHood==1:
                
                time.sleep(3)
                color.write("\n The merchant fades away and you notice that now you're missing something","STRING")
                time.sleep(3)
                print ("\n You lost Red's Hood")
                redHood=0
            break
        elif (choice=='b' or choice=='B'):
            color.write("\n The merchant stares at you while you walk pass him.","STRING")
            time.sleep(3)
            break
        elif (choice=='C' or choice=='c'):
            color.write("\n You ran forward and attempted to eat the merchant but he screams and his hired mercenary appears behind the cart and slashed you in half","STRING")
            time.sleep(3)
            die()
            break
        elif (choice=='D' or choice=='d'):
            color.write("\n You walk closer to the merchant's cart and he does not realize anything","STRING")
            time.sleep(3)
            color.write("\n You take a basket of his apples and you ran off","STRING")
            time.sleep(3)
            color.write("\n Merchant: THIEF THIEF HE WENT THAT WAY!!!!","COMMENT")
            time.sleep(3)
            color.write("\n The merchant's hired mercenary comes out of nowhere, drew his bow and shot you in the legs","STRING")
            time.sleep(3)
            color.write("\n You managed to get away but you dropped the basket of apples while you trying to get away.","STRING")
            time.sleep(3)
            print("\n You lost 30 speed")
            speed-= 30
            break
        else:
            choice=input("\n What should I do with this merchant?\n")
            
            
def startstats():
    choice=input("Do you want to view your stats? \n A: Yes \n B: No\n ")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b'):
        if (choice=='A' or choice =='a'):
            stats()
            break
        elif(choice=='B' or choice=='b'):
            break
        else:
            choice=input("A or B\n")
            
    
             
def die(): ## You dead
    color.write("\nYou died")
    time.sleep(3)
    choice=input("\nDo you want to start over?\n A=Yes \n B=No")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b'):
        if (choice=='A' or choice =='a'):
            play()
            break
        elif(choice=='B' or choice=='b'):
            exit()
            break
        else:
            choice=input("A or B\n")

def win(): ## Winner
    print("\n###################################")
    print("#    CONGRATULATIONS YOU WIN      #")
    if (red==1 and grandma==1 and mother==1 and hunter==1):
              print("#      YOU ATE THEM ALL           # ")
    print("###################################")
        
    stats()
    quit()
def bear(): ## Bear scene
    global speed
    global starvation
    global strength
    global mother
    global hunter
    global grandma
    global red
    global redHood
    global bearattack
    color.write("\n Bear: Yo duuuude, mind helping me out?","COMMENT")
    choice=input("\n A: Ignore him \n B: Sure thing \n C: I'm busy \n D: Action: Try and eat him\n")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c' or choice !="D" or choice !="d"):
        if (choice=='A' or choice =='a'):
            color.write("\n You simply just walked pass him and pretended like he wasn't even there")
            time.sleep(3)
            color.write("\n *SNAP* Such bad luck you have, you stepped on a bear trap yourself","STRING")
            time.sleep(3)
            color.write("\n You managed to free yourself however the trap damaged your legs","STRING")
            time.sleep(3)
            print("\nYou lost 20 speed")
            speed -= 20
            bearatttack=1
            break
        elif (choice=='B' or choice == 'b'):
            if strength >= 90:
                color.write("\nYou pulled on the bear trap as hard as you could. *SNAP* The bear trap broke in half and the bear was free of the trap","STRING")
                time.sleep(3)
                color.write("\nBear: Woooaa! Thanks dude you saved me. Here, take my dinner as my gradatude","COMMENT")
                time.sleep(3)
                print("\nYou gained 10 Strength")
                print("You gained 10 Speed")
                print ("You gained 30 starvation")
                strength += 10
                speed+= 10
                starvation += 30
            else:
                time.sleep(3)
                color.write("\nYou pulled on the bear trap as hard as you could. In the end, the trap did not budge however, now you feel stronger","STRING")
                print("\nYou gained 10 Strength")
                strength += 10
            break
        elif (choice=='C' or choice=='c'):
            color.write("No can do, I'm busy","KEYWORD")
            time.sleep(3)
            color.write("Duuuuuuude, YOU'LL REGRET IT!!","COMMENT")
            time.sleep(3)
            color.write(" You continued to walk pass him, ignoring him","STRING")
            bearattack=1
            break
        elif (choice=='D' or choice=='d'):
            color.write("\nYou walk up to the bear. You opened your mouth and tried to bite the bear.","STRING")
            time.sleep(3)
            color.write("\n The bear noticed what you were doing and He smashed his arms against your head. He knocked you out.","STRING")
            time.sleep(3)
            color.write("\n That was the last thing you remembered","STRING")
            die()
            break
        else:
            choice=input("Should I help him, leave him be or eat him??")
            
            
            
    
    
def fullness0(): ## 0 starvation , LOSE
    global starvation
    if(starvation<= 0):
        color.write ("\nYou died of hunger","STRING")
        exit()
def fullnessdrop(): ## Drops starvation as time goes
    print("\n As time went by, your starvation drops")
    global starvation
    global speed
    starvation = starvation - (10+(250/speed)+(250/strength))

def scene10(): ##Eat Mother/ END
    global speed
    global starvation
    global strength
    global mother
    global hunter
    global grandma
    global red
    global redHood
    global hoodon
    global grandmaGown
    global flower
    global butterfly
    global fight
    global town
    global bearattack
    time.sleep(3)
    print("\n====================== The Forest =======================")
    time.sleep(4)
    color.write("\n You've decided to head back into the forest because you know Red's mother is somewhere here","STRING")
    time.sleep(3)
    color.write("\n You come across a 3 way split road","STRING")
    print("\n Which was to go?")
    choice=input("\n A: Left \n B: Right \n C: Foward\n")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice!= 'c' or choice != 'C'):
       if (choice == 'A' or choice == 'a'):
          color.write("\n You went left and walked on. You stepped on a fall pit but something grabs you by the hand","STRING")
          time.sleep(3)
          color.write("\n You looked up and it was the bear from earlier","STRING")
          time.sleep(3)
          if bearattack==1:
             color.write("\n Thanks for saving me, that was close","KEYWORD")
             time.sleep(3)
             color.write("\n Bear: Duuddee you're that wolf that didn't help me earlier. I told you you'll regret it","COMMENT")
             time.sleep(3)
             color.write("\n The bear lets go and you fall to your death","STRING")
             die()
          else:
             color.write("\n Bear: Duuddeee you're that wolf that helped me earlier","COMMENT")
             time.sleep(3)
             color.write("\n Bear: Hold on tight dude","COMMENT")
             time.sleep(3)
             color.write("\n The bear grabs your arm and flung you into the air, you landed on the ground without any damage","STRING")
             time.sleep(3)
             color.write("\n Thanks for saving me duude","KEYWORD")
             time.sleep(3)
             color.write("\n Yea bro, no problem","COMMENT")
             time.sleep(4)
             color.write("\n You continued to search for Red's mother and you come across another split road that looks similar to the last one","STRING")
             time.sleep(4)
             print("\n Which was to go?")
             choice=input("\n A: Left \n B: Right \n C: Foward\n")
             while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice!= 'c' or choice != 'C'):
                if (choice == 'A' or choice == 'a'):
                   color.write("\n You went left and walked on for about 10minutes. You spot Red's mother and you ran towards her.","STRING")
                   time.sleep(4)
                   color.write("\n *SNAP* You stepped on an extra large bear trap and it snapped you in half","STRING")
                   time.sleep(3)
                   die()
                   break
                elif (choice=='b' or choice=='B'):
                   color.write("\n You went right and walked on. You tripped on a trigger wire and a huge log came swinging in from the trees","STRING")
                   time.sleep(3)
                   color.write("\n The huge log smacked you in the head and you became unconcious due to blunt force","STRING")
                   time.sleep(3)
                   color.write("\n A group of hunters came by and collected their hunt.","STRING")
                   die()
                   break
                elif (choice=='c' or choice=='C'):
                   color.write("\n You went foward and you spot Red's Mother searching around","STRING")
                   time.sleep(3)
                   color.write("\n You leaped forward and ate her.","STRING")
                   time.sleep(3)
                   color.write("\n You are now very full and you fell asleep right on the spot.","STRING")
                   time.sleep(3)
                   mother=1
                   win()
                   break
                else:
                  
                   choice=input("\nI must go in one of these directions\n")
          break
       elif (choice =='c' or choice=='C'):
          color.write("\n You went foward and you spot Red's Mother searching around","STRING")
          time.sleep(3)
          color.write("\n You leaped forward and ate her.","STRING")
          time.sleep(3)
          color.write("\n You are now very full and you fell asleep right on the spot.","STRING")
          time.sleep(3)
          mother=1
          win()
          break
       elif (choice== 'b' or choice=='B'):
          color.write("\n You went right and walked on. You tripped on a trigger wire and a huge log came swinging in from the trees","STRING")
          time.sleep(3)
          color.write("\n The huge log smacked you in the head and you became unconcious due to blunt force","STRING")
          time.sleep(3)
          color.write("\n A group of hunters came by and collected their hunt.","STRING")
          die()
          break
       else:
          choice=input("\nI must go in one of these directions\n")
         

             
    
   
    
def scene9a(): ##Eat Red
    global speed
    global starvation
    global strength
    global mother
    global hunter
    global grandma
    global red
    global redHood
    global hoodon
    global grandmaGown
    global flower
    global butterfly
    global fight
    global town
    time.sleep (3)
    color.write("\n Red: 1..... 2..... 3.....","COMMENT")

    choice= input("\n A: Eat her \n B: Let her finish counting\n")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b'):
       if (choice == 'A' or choice == 'a'):
          
          color.write("\n You begin to open your mouth and ...","STRING")
          time.sleep(4)
          if town==1:
             
             color.write("\n *Door opens* Mother: Mom I forgot I didn't bring any money with me. Do you have any... AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH","COMMENT")
             time.sleep(3)
             color.write("\n You didnt not get a chance to eat Red and went to try to stop the screaming.","STRING")
             time.sleep(3)
             color.write("\n A Knight with a full suit of Armor appears ","STRING")
             time.sleep(3)
             color.write("\n Mother: Help my little girl PLEASE","COMMENT")
             time.sleep(3)
             color.write("\n The knight drew his sword. You tried to run but the knight slashed you before you got out","STRING")
             time.sleep(3)
             color.write("\n You're bleeding heavily and you eventually bled out","STRING")
             time.sleep(3)
             die()
          else:
            color.write("\n You gobbled Red up like a pie. She did not have a chance to scream or do anything","STRING")
            time.sleep(3)
            color.write("\n *burp*","STRING")
            time.sleep(4)
            print("\n You gained 30 starvation")
            starvation+= 30
            red=1
          break
       elif (choice=='B' or choice=='b'):
          color.write("\n Red: 9.... 10.... Now what Grandma?","COMMENT")
          time.sleep(3)
          color.write("\n I wasn't ready. Can you close your eyes and count to 10 again?","KEYWORD")
          time.sleep(3)
          color.write("\n Red: Grandmaaaaa, fine I'll count again","COMMENT")
          scene9a()
          break
       else:
          choice=input("\nWhat shall I do?\n")
    fullnessdrop()
    stats()
    fullness0()
    scene10()
          
def scene9(): ##Red and mother enters
    global speed
    global starvation
    global strength
    global mother
    global hunter
    global grandma
    global red
    global redHood
    global hoodon
    global grandmaGown
    global flower
    global butterfly
    global fight
    global town
    time.sleep (3)
    color.write("\n You went to close the doors but a hat was blocking the way. You picked it up and it Read Joe Gramps. Must have been the hunter's hat. You went back to grandma's bed and continued your nap","STRING")
    time.sleep(5)
    if red==1:
       color.write("\n You fell asleep in Grandma's bed and you felt accomplished.","STRING")
       win()
    else:
       
       print("\n Moments later")
       time.sleep(7)
       color.write("\n *knock* *knock* *knock*","STRING")
       time.sleep(3)
       color.write("\n Red: Grandma it's me Red. I've brought mother here","COMMENT")
       time.sleep(3)
       color.write("\n *knock* *knock* *knock*","STRING")
       time.sleep(3)
       color.write("\n You woke up to the sound of door knocks","STRING")
       time.sleep(3)
       color.write("\n You remembered that you told red to bring her mother here","STRING")
       time.sleep(3)
       color.write("\n Come in, it's not locked","KEYWORD")
       time.sleep(3)
       color.write("\n Red: Hey Grandma","COMMENT")
       time.sleep(3)
       color.write("\n Mother: Hi mom, Red said it was urgent? What is it?","COMMENT")
       time.sleep(3)
       choice= input("\n A: Can you go to town and buy some groceries \n B: Joe hasnt come home since yesterday.\n")
       while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b'):
          if (choice == 'A' or choice == 'a'):
             color.write("\n Mother: Really mom? you called me here for that","COMMENT")
             time.sleep(3)
             color.write("\n My back hurts and I can't move. Please just go buy some groceries for me","KEYWORD")
             time.sleep(3)
             color.write("\n Mother: Alright fine, I'll go. Red you don't have to come with me. Stay here and watch your Grandma","COMMENT")
             time.sleep(3)
             color.write("\n Red: Ok mom, I'll stay and play with Grandma","COMMENT")
             town=1
             break
          elif (choice == 'b' or choice=='B'):
             color.write("\n Joe went on a hunt with his hunting party yesterday and hasnt returned home since","KEYWORD")
             time.sleep(3)
             color.write("\n He usually comes home the day he goes out. I'm worried that he might be hurt. Please go find him","KEYWORD")
             time.sleep(3)
             color.write("\n Mother: Ok, did he tell you where he was going?","COMMENT")
             time.sleep(3)
             color.write("\n He told me he was going north, not far from our home.","KEYWORD")
             time.sleep(3)
             color.write("\n Mother: Red stay here and watch your Grandma","COMMENT")
             time.sleep(3)
             color.write("\n Red: Ok mom, I'll stay and play with Grandma","COMMENT")
             forest=1
             break
          else:
             choice=input(" What should I tell her?")
       color.write("\n Red's mother left in a hurry","STRING")
       time.sleep(3)
       color.write("\n Red come to Grandma, lets play a game.","KEYWORD")
       time.sleep(3)
       color.write("\n Red: What kind of game Grandma","COMMENT")
       time.sleep(3)
       color.write("\n Close your eyes, and count to 10","KEYWORD")
       time.sleep(3)
       color.write("\n Red closed her eyes and started counting","STRING")
       time.sleep (3)
       scene9a()

    
   
    
    
    
def scene8(): ## Hunter enters
    global speed
    global starvation
    global strength
    global mother
    global hunter
    global grandma
    global red
    global redHood
    global hoodon
    global grandmaGown
    global fight
    color.write("\n Now that Red is gone, what to do?","STRING")
    time.sleep(3)
    choice=input("\n A: Nap \n B: Search the house again \n C: Call it a day \n")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c'):
       if (choice == 'A' or choice == 'a'):
          color.write("You closed your eyes and tried to fall asleep in Grandma's bed","STRING")
          time.sleep(3)
          color.write("\n And suddendly the door opens again. Someone enters","STRING")
          time.sleep(3)
          color.write("\n Hunter: Honey, I'm home. There was no luck with the hunt today","COMMENT")
          time.sleep(3)
          color.write("\n Hunter: Is there anything to eat? I'm starving","COMMENT")
          time.sleep(3)
          choice=input("\n A: Yes, there's plenty to eat, come to me\n B: No honey, there's no food. Please go buy some food from the pub in town. \n C: Make a run for it \n D: Try and fight him\n")
          while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c' or choice!='D' or choice != 'd'):
              if (choice == 'A' or choice == 'a'):
                 color.write("\n As he stepped closer he noticed that you looked different","STRING")
                 time.sleep(3)
                 color.write("\n Hunter: Is it just me or do you look....","COMMENT")
                 time.sleep(3)
                 color.write("\n You quickly gobbled him up before he had a chance to do anything.","STRING")
                 time.sleep(3)
                 print("\n You gained 40 starvation")
                 starvation+= 40
                 hunter=1
                 break
              elif(choice=='B' or choice=='b'):
                 color.write("\n Hunter: Alright I'll on my way then","COMMENT")
                 time.sleep(3)
                 color.write("\n The hunter was suspicious since Grandma always has food around","STRING")
                 time.sleep(3)
                 color.write("\n You thought the hunter left but he backed around and snuck in the back","STRING")
                 time.sleep(3)
                 color.write("\n He drew his knife and surprised you","STRING")
                 time.sleep(3)
                 die()
                 break
              elif (choice =='c' or choice=='C'):
                 color.write("\n You attempt to make a run for it","STRING")
                 time.sleep(3)
                 color.write("\n You pushed the hunter aside and you ran as fast as you could","STRING")
                 time.sleep(3)
                 color.write("\n Suddendly, you stopped moving. There was a bolt through your legs","STRING")
                 time.sleep(3)
                 color.write("\n Another one came flying in and pierced you","STRING")
                 time.sleep(3)
                 die()
                 break
              elif(choice== 'D' or choice=='d'):
                 color.write("\n You attempt to fight the hunter","STRING")
                 time.sleep(3)
                 color.write("\n You lounged foward and ","STRING")
                 time.sleep(3)
                 if (strength>= 90 and speed>= 90):
                    color.write("\n With your superior speed and strength","STRING")
                    time.sleep(3)
                    color.write("\n You easily toppled him and knocked him out","STRING")
                    time.sleep(3)
                    color.write("\n You ate him while he was unconsicious","STRING")
                    time.sleep(3)
                    print("\n You gained 40 starvation")
                    starvation+= 40
                    hunter=1
                    fight=1
                    break
                 else:
                    color.write("\n The hunter outpowered you and knocked you out","STRING")
                    time.sleep(3)
                    color.write("\n That was the last of things you remembered","STRING")
                    time.sleep(3)
                    die()
              else:
                 choice=input(" \nWhat should I tell him or do?\n")
          break
       elif (choice =='b' or choice=='B'):
          color.write("\n You went around the house and searched for anything useful","STRING")
          time.sleep(3)
          color.write("\n You found a pie in the oven, you took it out and started eating it","STRING")
          time.sleep(3)
          color.write("\n The hunter came home and saw you in the kitchen eating the pie","STRING")
          time.sleep(3)
          color.write("\n He drew his crossbow and headshotted you","STRING")
          time.sleep(3)
          die()
          break
       elif(choice =='c' or choice=='C'):
          color.write("\n You quickly leave Grandma's house and headed back to the forest","STRING")
          time.sleep(3)
          color.write("\n You found a perfect spot to sleep near the river","STRING")
          time.sleep(3)
          color.write("\n You fell alseep in matters of seconds","STRING")
          time.sleep(3)
          win()
          break
       else:
          choice=input("\n What should I do?\n")
                       
    fullnessdrop()
    stats()
    fullness0()
    scene9()
                 
                 
                  
    

def scene7(): ## Red Enters
    global speed
    global starvation
    global strength
    global mother
    global hunter
    global grandma
    global red
    global redHood
    global hoodon
    global grandmaGown
    global flower
    global butterfly
    color.write("\n Seconds right after you laid on Grandma's bed, you hear someone enter the house","STRING")
    time.sleep(3)
    if butterfly==1:
       color.write("\n Red: Grandma!! Grandma!! it's me, Red.Sorry I came so late. I went and got some of the prettiest butterflies for you.","COMMENT")
       time.sleep(3)
    else:
       color.write("\n Red: Grandma!! Grandma!! it's me, Red.Sorry I came so late. I went and picked some of the prettiest flowers for you.","COMMENT")
       time.sleep(3)
    color.write("\n My dear Red, you finally came. Come closer to Grandma, Let me see you.","KEYWORD")
    time.sleep(3)
    color.write("\n Red gently drops everything and ran closer to you","STRING")
    time.sleep(3)
    color.write("\n As Red steps closer to the bed she noticed something was off","STRING")
    time.sleep(3)
    if grandmaGown==0:
       color.write("\n Red: Wait, you're not grandma. AHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!! YOU ATE GRANDMAAAAAAAAAA","COMMENT")
       time.sleep(3)
       color.write("\n Nonono I didnt eat your grandma, she's in the....","KEYWORD")
       time.sleep(3)
       color.write("\n A bolt went straight through your head as the hunter returned home and noticed you weren't his wife.","STRING")
       time.sleep(3)
       die()
    else:
       color.write("\n Red: Did you get bigger Grandma?","COMMENT")
       time.sleep(3)
       color.write("\n Yes, I had a biggggggg feast yesterday, that's why I'm sick now little Red","KEYWORD")
       time.sleep(3)
       color.write("\n Red: Oh, did you have a good time at the feast?","COMMENT")
       time.sleep(3)
       color.write("\n Now that Red is next to you, What to do?","STRING")
       choice=input("\n A: Eat Red \n B: Make a run for it \n C: Tell her to bring Mother\n")
       while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice!= 'C' or choice != 'c'):
          if (choice=='A' or choice=='a'):
             color.write("\n Come closer Red let grandma see how you've grown","KEYWORD")
             time.sleep(3)
             color.write("\n Red: Grandma, I met a nice big wolf today and he brought me to the...","COMMENT")
             time.sleep(3)
             color.write("\n You opened your mouth and ate her as she was speaking","STRING")
             time.sleep(3)
             print("\nYou gained 30 starvation")
             red=1
             starvation+= 30
             
             break
          elif(choice =='B' or choice =='b'):
             color.write("\n You instantly jumped out of bed, shocking Red and you ran out the door","STRING")
             time.sleep(3)
             color.write("\n Unfortunately you ran into the someone on your way out and fell","STRING")
             time.sleep(3)
             color.write("\n It was the hunter returning home from a hunt","STRING")
             time.sleep(3)
             color.write("\n He quickly drew his crossbow and shot you while you were still down","STRING")
             time.sleep(3)
             die()
             break
          elif(choice =='c' or choice=='C'):
             color.write("\n Red, can you please go home and bring your mother here? It's urgent","KEYWORD")
             time.sleep(3)
             color.write("\n Red: But I just got here grandma. Cant I stay for a little while first?","STRING")
             time.sleep(3)
             color.write("\n It's going to be dark soon, It's dangerous to travel at night. Hurry bring your mother here. It's very important","KEYWORD")
             time.sleep(3)
             color.write("\n Ok Grandma, I'll be leaving now then. See you later","COMMENT")
             break
          else:
             choice= input("\n What to do?\n ")
       fullnessdrop()
       stats()
       fullness0()
       scene8()
             
            
            
       
    

   

def scene6(): ## Grandma's house
    global speed
    global starvation
    global strength
    global mother
    global hunter
    global grandma
    global red
    global redHood
    global hoodon
    global grandmaGown
    time.sleep(3)
    print("\n=================== Grandma's House======================")
    time.sleep(3)
    color.write("\nIt took awhile to get here, but you've finally made it","STRING")
    fullnessdrop()
    time.sleep(3)
    if redHood==1:
        color.write("\n Before you went inside, you remembered that red gave you her hood. Do you want to put it on?","STRING")
        time.sleep(3)
        choice=input("\n A: Yes \n B: No\n")
        while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b'):
            if (choice=='A' or choice=='a'):
                color.write("\n You quickly put on the hood red gave you","STRING")
                hoodon=1
                break
            elif (choice=='b' or choice=='B'):
                color.write("\n You decided not to put Red's hood on","STRING")
                break
            else:
                choice=input("On or Off?")
    time.sleep(3)
    color.write("\nYou open the door and immediately you hear a voice saying","STRING")
    time.sleep(3)
    color.write("\nGrandma: Red is that you?","COMMENT")
    time.sleep (3)
    print("\nWhat should I say?")
    choice=input("\n A: No it's me Wolf\n B: Yes it's me Red\n")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b'):
        if (choice=='b' or choice=='B'):
            color.write("\n You finally made it here Red. Come closer, let grandma take a good look at you","COMMENT")
            time.sleep(3)
            color.write("\n As you walk closer, Grandma saw you better","STRING")
            time.sleep(3)
            if hoodon==1:
                color.write("\n Grandma: Wow Red, you've grown so big!","COMMENT")
                time.sleep(3)
                print("\n Now that I'm next to Grandma, what should I do next?")
                time.sleep(3)
                choice=input("\n A: Eat Grandma\n B: Leave Grandma's house\n")
                while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b'):
                    if (choice=='A' or choice =='a'):
                        color.write("\n You opened your mouth as Grandma lifted her hand to feel you.","STRING")
                        time.sleep(3)
                        color.write("\n Grandma did not see that coming and you swallowed her whole","STRING")
                        time.sleep(3)
                        print("\n You gained 40 starvation")
                        starvation+= 40
                        grandma=1
                        break
                    elif (choice=='B' or choice =='b'):
                        color.write("\n You leave Grandma's house and decided to go back to the forest","STRING")
                        time.sleep(3)
                        color.write("\n Unfortunately, you ran into a pitfall and you were pierced by 10 stakes","STRING")
                        time.sleep(3)
                        die()
                        break
                    else:
                        choice=input("What to do??")
            else:
                color.write("\n Grandma: Wait you're not Red!!", "COMMENT")
                time.sleep(3)
                color.write("\n Grandma: AHHHH THERE'S A INTRUDER IN MY HOUSE!!!!!!","COMMENT")
                time.sleep(3)
                color.write("\n A group of nearby hunters heard Grandma's scream and rushed to her house.","STRING")
                time.sleep(3)
                color.write("\n The hunters came rushing in, they shot you at first sight","STRING")
                die()
            break
        elif(choice=='A' or choice=='a'):
            
            color.write("\n Grandma: AHHHH THERE'S A INTRUDER IN MY HOUSE!!!!!!","COMMENT")
            time.sleep(3)
            color.write("\n A group of nearby hunters heard Grandma's scream and rushed to her house.","STRING")
            time.sleep(3)
            color.write("\n The hunters came rushing in, they shot you at first sight","STRING")
            die()
            break
        else:
            choice=input("\n I need to tell her who it is\n")
    color.write("\n Now that grandma is gone, what should I do next?")
    time.sleep(3)
    choice=input("\n A: Take a nap \n B: Look around the house \n C: Go back to the forest and call it a day\n")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice !='c' or choice !='C'):
        if (choice=='A' or choice=='a'):
            color.write("\n You lay in the bed that Grandma used to be in.","STRING")
            time.sleep(3)
            color.write("\n You close your eyes and you quickly fell asleep.","STRING")
            time.sleep(3)
            color.write("\n That was the last of your days as the hunter found out that you weren't his wife while you were asleep","STRING")
            time.sleep(3)
            die()
            break
        elif (choice=='B' or choice=='b'):
            color.write("\n You take a look around Grandma's house","STRING")
            time.sleep(3)
            color.write("\n You stumble apon a closet full of Grandma's gowns.","STRING")
            time.sleep(3)
            color.write("\n You decide to take one.","STRING")
            time.sleep(3)
            choice=input("\n You currently have Red's hood on. Do you want to take off Red's Hood and put on Grandma's gown?\n A: Yes\n B: No\n")
            while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b'):
                if (choice=='A' or choice=='a'):
                    color.write("\nYou quickly put on the gown and went back to lay in the bed.","STRING")
                    time.sleep(3)
                    grandmaGown=1
                    break
                elif(choice=='b' or choice=='B'):
                    color.write("\n You didn't put Grandma's Gowns on and went back to the bed","STRING")
                    time.sleep(3)
                    break
                else:
                    choice=input("\nDo I put it on or no\n")
            break
        elif(choice=='C' or choice=='c'):
            color.write("\n You decided to head back into the forest","STRING")
            time.sleep(3)
            color.write("\n You found a perfect place under the tree and you slept peacefully","STRING")
            time.sleep(3)
            win()
            break
        else:
            choice=input("Hmm what to do?")
        break    
    fullnessdrop()
    stats()
    fullness0()
    scene7()
            




def scene5():  ##Run to Grandma's house
    global speed
    global starvation
    global strength
    global flower
    global butterfly
    global redHood
    global red
    print("\n================ The Forest ===================")
    time.sleep(3)
    color.write("\nYou quickly dash through the forest and you come across this bear stuck on a trap.","KEYWORD")
    time.sleep(3)
    bear()
    time.sleep(3)
    print("\n================ The Road ===================")     
    color.write("\n After a short run, you are back on the roads to grandma's house.","STRING")
    time.sleep(3)
    evilmerchant()
    fullnessdrop()
    stats()
    fullness0()
    ##
    ## Can do somethinghere on the road
    ##
    scene6()
    
def scene4(): ## possible win 1
    global speed
    global starvation
    global strength
    global flower
    global butterfly
    global redHood
    global red
    if (red==1):
        color.write("\nShe was DELICIOUS. I remember her saying that her Grandma lives down the road.","KEYWORD")
        time.sleep(3)
        color.write("\nShould I go to grandma's house or should I just call it a day","KEYWORD")
        time.sleep(3)
        choice=input("\n A: Grandma's \n B: Call it a day \n") 
        while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b'):
            if (choice=='B' or choice =='b'):
                color.write("You've had your fill of food today and you went to sleep on the spot where Red was eaten.","STRING")
                time.sleep(3)
                color.write("The forest leaves were rustling and you quickly fell asleep","STRING")
                time.sleep(3)
                win()
                break
            elif(choice =='A' or choice=='a'):
                color.write("\n You quickly left the forest and went back on the road to Grandma's house","STRING")
                time.sleep(3)
                break
            else:
                choice=input("\nGrandma's or call it a day?\n")
    else:
        
        color.write("\n Now that Red is distracted, what do I do now?","KEYWORD")
        time.sleep(3)
        choice=input("\n A: Go to Grandma's house \n B: Walk away and head back deep into the forest \n")
        while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b'):
            if (choice=='B' or choice =='b'):
                color.write("\n You head deeper into the forest and you see a group of hunters. They noticed you and they start to chase after you. You ran as fast as you could but in the end, you did not outrun the hunters' arrows.","STRING")
                time.sleep(3)
                die()
                break
            elif(choice =='A' or choice=='a'):
                break
    scene5()

def scene3(): ## In butterfly/flower field
    global speed
    global starvation
    global strength
    global flower
    global butterfly
    global redHood
    global red
    time.sleep(3)
    print("================ The Field ===================")
    time.sleep(3) 
    if butterfly==1:
        color.write("\n After a short distant walk, you and Red arrived at the butterfly field","STRING")
        time.sleep(3)
        color.write("\n Red drops her basket and rushes towards the field","STRING")
        time.sleep(3)
        color.write("\n Red: You were right Mr.Wolf. These butterflies are beatiful. I'm going to catch one to show grandma for sure!","COMMENT")
        time.sleep(3)
    else:
        color.write("\n After a short distant walk, you and Red arrived at the field of flowers","STRING")
        time.sleep(3)
        color.write("\n Red drops her basket and rushes towards the field","STRING")
        time.sleep(3)
        color.write("\n Red: You were right Mr.Wolf. These flowers are beatiful. I'm going pick some of the prettiest ones to show grandma for sure!","COMMENT")
        time.sleep(3)
    color.write("\n I'm glad you love them!","KEYWORD")
    time.sleep(3)
    color.write("\n Red now seems to be occupied and not really paying attention to her surroundings","STRING")
    choice=input("\n A: Eat Red \n B: Ask her for her hood \n C: Invade Red's basket\n")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c'):
        if (choice == 'A' or choice == 'a'):
            color.write("\n You took a big leap foward and knocked Red over.","STRING")
            time.sleep(3)
            color.write("\n You ate her in one big bite before she could do anything.","STRING")
            time.sleep(3)
            print("\n You gained 30 starvation")
            starvation+=30
            red=1
            break
        elif(choice=='B' or choice=='b'):
            color.write("\n Hey Red you're going to get your hood dirty. I can hold it for you if you want","KEYWORD")
            time.sleep(3)
            color.write("\n Red: Yea it's going to get really dirty if I keep it on. If you dont mind, you could hold on to it for me","COMMENT")
            time.sleep(3)
            print("\n You gained Red's Hood")
            redHood=1
            break      
        elif (choice=='C' or choice=='c'):
            color.write("\n You snatch Red's basket of goodies and she does not seem to notice.","STRING")
            time.sleep(3)
            color.write("\n The basket was full of foods and drinks. You ate it all in matters of seconds and it was delicious", "STRING")
            time.sleep(3)
            print("\nYou gained 20 starvation")
            print("You gained 15 Strength")
            print("You gained 20 speed")
            starvation+= 20
            speed+= 20
            strength+=15
            break
            
        else:
            
            choice = input("\nHmmm, What should I do?")
    fullnessdrop()
    stats()
    fullness0()
    scene4()

def sceneflower(): ## Flower route
    global speed
    global starvation
    global strength
    print("================ The Forest ===================")
    time.sleep(3)
    color.write("\n Red! The flower field is just ahead of this huge log.","KEYWORD")
    time.sleep(3)
    color.write("\n Red: But how are we going to get across with this big log blocking us?","COMMENT")
    time.sleep(3)
    choice=input("\n A: Attempt to cross \n B: Give up\n")
    while (choice != "A" or choice != "B" or choice!="a" or choice !="b"):
       if (choice =="A" or choice =="a"):
          color.write("\n Don't worry, I'm very strong!! Move back! I got this.","KEYWORD")
          time.sleep(3)
          if strength>=90:
             
             color.write("\n You struggled to pick up the log but both of you ended up on other side safely","STRING")
             time.sleep(3)
             color.write("\n You are really strong Mr.Wolf","COMMENT")
             time.sleep(3)
             color.write("\n You feel weakened after lifting that huge log.","STRING")
             time.sleep(3)
             print("\n You lost 10 strength")
             strength -=10
          else:
            
             color.write("\n You attempt to lift the log.","STRING")
             time.sleep(3)
             color.write("\n You picked it up and Red quickly ran across but as you tried to move to the other side, you dropped the log on your leg but you managed to get your leg out before it was completely crushed by the log","STRING")
             time.sleep(3)
             print("\n You lost 30 speed")
             print("\n You lost 30 strength")
             speed -=30
             strength -=30
          break
       elif (choice=="B" or choice=='b'):
          color.write("\n Yea there's no way to get across. Let's head back","KEYWORD")
          time.sleep(3)
          fullnessdrop()
          stats()
          fullness0()
          scene2a()
          break
       else:
          choice=input("Should I try to cross or give up?")  
def scenebutterfly(): #butterfly route
    global speed
    global starvation
    global strength
    time.sleep(3)
    print("\n================ Near the River ===================")
    color.write("\n Red! The butterfly field is just across this log bridge.","KEYWORD")
    time.sleep(3)
    color.write("\n Red: This log bridge doesn't seem very safe. Are you sure??","COMMENT")
    time.sleep(3)
    choice=input("\n A: Attempt to cross \n B: Give up\n")
    while (choice != "A" or choice != "B" or choice!="a" or choice !="b"):
       if (choice =="A" or choice =="a"):
          color.write("\n Don't worry, I'm very fast!! Get on my back, I'll carry you across","KEYWORD")
          time.sleep(3)
          if speed >= 90:
             color.write("\n You zoom across the log and landed safely on the other side.","STRING")
             time.sleep(3)
             color.write("\n Red: You are really fast Mr.Wolf","COMMENT")
             time.sleep(3)
             color.write("\n You feel tired after speeding through that log.","STRING")
             time.sleep(3)
             print("\n You lost 10 speed")
             speed -=10
          else:
             color.write("\n You attempt to dash across the log.","STRING")
             time.sleep(3)
             color.write("\n You ran as fast as you could but you slipped and both you and Red fell over the log into the water. The river was fierce and but you and red managed to get back to safety","STRING")
             time.sleep(3)
             print("\n You lost 30 speed")
             print("\n You lost 20 starvation")
             print("\n You lost 30 strength")
             speed -=30
             strength -= 30
             starvation -= 20
          break  
       elif (choice=="B" or choice=='b'):
          color.write("\n Yea there's no way to get across. Let's head back","KEYWORD")
          time.sleep(3)
          fullnessdrop()
          stats()
          fullness0()
          scene2a()
          break
       else:
          choice=input("Should I try to cross or give up?")

          
def scene2a(): ## Tricking Red
    global flower
    global butterfly
    color.write("\nRed: I'm heading down the road to my Grandmother's house now. Byebye.","COMMENT")
    time.sleep(3)
    color.write("\nRed slowly turns and heads down the road to her Grandmother's house.","STRING")
    time.sleep(3)
    choice=input ("\n A: Say: Wait Red, Does your Grandmother like flowers? \n B: Say: Wait Red, Does your Grandmother like butterflies? \n C: Action: Chase after red and try to eat her. \n D: Action: Watch her walk away and head back into the forest.\n")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c' or choice !="D" or choice !="d"):
       if (choice == 'A' or choice == 'a'):
           color.write("\nRed: Why yes she does!","COMMENT")
           time.sleep(3)
           color.write("\nI know this place in the forest filled with beautiful flowers. Do you want me to show you the way?","KEYWORD")
           time.sleep(3)
           color.write("\nRed: I want to go but I really shouldn't. I don't know if I have enough time to pick flowers, go to granny's house then go home.","COMMENT")
           time.sleep(3)
           choice=input("\n A: It's not far away \n B: Alright you shouldnt keep your grandma waiting.\n")
           while (choice != "A" or choice != "B" or choice!="a" or choice !="b"):
               if (choice =="A" or choice =="a"):
                   color.write("\n It's very close by. Your grandma would love these flowers, they're very pretty!","KEYWORD")
                   time.sleep(3)
                   color.write("\n Red: If it nearby then lets go!!. I bet grandma will love these flowers\n","COMMENT")
                   time.sleep(3)
                   print("\n Moments later")
                   time.sleep(5)
                   ## Sceneflower
                   flower=1
                   sceneflower()
                   break
               elif (choice == 'B' or choice == 'b'):

                   color.write("\n Ok you be on your way then. Thanks for your help!","KEYWORD")
                   time.sleep(3)
                   color.write("\n Red: See you around Mr.Wolf. I'll be sure to check out those flowers next time!","COMMENT")
                   time.sleep(3)
                   color.write("\n As Red walks down the road, you watch as she slowly disappears.","STRING")
                   time.sleep(3)
                   color.write("\n You return back to the forest but you see a group of hunters. They noticed you and they start to chase after you. You ran as fast as you could but in the end, you did not outrun the hunters' arrows.","STRING")
                   time.sleep(3)
                   die()
                   break
               else:
                    choice = input("\nShould I tell her it's not far or should I give up convincing?")
           break 

       elif (choice == 'B' or choice == 'b'):
           color.write("\nRed: Why yes she does!","COMMENT")
           time.sleep(3)
           color.write("\nI know this place in the forest with lots of beautiful butterflies. Do you want me to show you the way?","KEYWORD")
           time.sleep(3)
           color.write("\nRed: I want to go but I really shouldn't. I don't know if I have enough time to catch butterflies, go to granny's house then go home.","COMMENT")
           time.sleep(3)
           choice=input("\n A: It's not far away \n B: Alright you shouldnt keep your grandma waiting.\n")
           while (choice != "A" or choice != "B" or choice!="a" or choice !="b"):
               if (choice =="A" or choice =="a"):
                   color.write("\n It's very close by. Your grandma would love these butterflies, they're very pretty!","KEYWORD")
                   time.sleep(3)
                   color.write("\n Red: If it nearby then lets go!!. I bet grandma will love these butterflies","COMMENT")
                   time.sleep(3)
                   print("\n Moments later")
                   time.sleep(5)
                   ##scenebutterfly
                   butterfly =1
                   scenebutterfly()
                   break
               elif (choice == 'B' or choice == 'b'):

                   color.write("\n Ok you be on your way then. Thanks for your help!","KEYWORD")
                   time.sleep(3)
                   color.write("\n Red: See you around Mr.Wolf. I'll be sure to check out those butterflies next time!","COMMENT")
                   time.sleep(3)
                   color.write("\n As Red walks down the road, you watch as she slowly disappears.","STRING")
                   time.sleep(3)
                   color.write("\n You return back to the forest but you see a group of hunters. They noticed you and they start to chase after you. You ran as fast as you could but in the end, you did not outrun the hunters' arrows.","STRING")
                   die()
                   break
               else:
                    choice = input("\nShould I tell her it's not far or should I give up convincing?\n")
           break 

       elif (choice == 'C' or choice == 'c'):
           color.write("\n You start to run towards Red. She turns around and sees you running towards her.","STRING")
           time.sleep(3)
           color.write("\n AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH","COMMENT")
           time.sleep(3)
           color.write("\n A bunch of nearby hunter hears red screaming and they rushed towards her. They see you chasing after a helpless little girl and they shot you down.","STRING")
           time.sleep(3)
           die()
           break
       elif (choice == 'D' or choice == 'd'):
           color.write("\n As Red walks down the road, you watch as she slowly disappears.","STRING")
           time.sleep(3)
           color.write("\n You return back to the forest but you see a group of hunters. They noticed you and they start to chase after you. You ran as fast as you could but in the end, you did not outrun the hunters' arrows.","STRING")
           time.sleep(3)
           die()
           break

       else:
           choice = input("\nWhat should I do?")

    fullnessdrop()
    stats()
    fullness0()
    scene3()

    
def scene2(): ## Meeting Red
    global speed
    global starvation
    global strength
    global butterfly
    global flower
    print("\n=================== The Road =====================")
    color.write ("\n You walk towards the roads and see a little girl wearing a red hood ","STRING")
    time.sleep(2)
    color.write ("\n You approach her, and she does not seem to be startled by your appearance","STRING")
    time.sleep(2)
    color.write ("\n Red: Hello big sir. I'm Red Riding hood, how are you today.","COMMENT")
    time.sleep(2)
    choice=input("\n A: A tree fell on me \n B: I'm tired \n C: I'm very hungry \n D: I'm doing fine how about you?\n") 
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c' or choice !="D" or choice !="d"):
        if (choice == 'A' or choice == 'a'):
            color.write ("\nI was following my rabbit friend but a tree fell on me.","KEYWORD")
            time.sleep(3)
            color.write ("\nI manage to dodge it but it hurt my legs.","KEYWORD")
            time.sleep(3)
            color.write ("\nRed: Ouch!! That must have hurt! Luckily I'm bringing food and medicine to my Grandma. Here, let me help you patch it up. ","COMMENT")
            time.sleep(3)
            print ("\nGained 10 speed")
            speed += 10
            stats()
            break
        elif (choice == 'B' or choice == 'b'):
            color.write ("\nI was following my rabbit friend and I followed him over a BIG hill","KEYWORD")
            time.sleep(3)
            color.write ("\nRed: WOW! You must be really tired. Luckily I'm bringing food and medicine to my Grandma. This is suppose to be for my Grandma but I guess you can have a sip. ONLY a sip!","COMMENT")
            time.sleep(3)
            color.write ("\nRed hands you a glass of milk. You take a sip and she stops you.","COMMENT")
            time.sleep(3)
            print ("\nGained 5 Strength")
            strength += 5
            stats()
            break
        elif (choice == 'C' or choice == 'c'):
            color.write ("\nI haven't had anything to eat yet. I'm starrrrrrrrving","KEYWORD")
            time.sleep(3)
            color.write ("\nShe pops open her basket and hands you a biscuit. ", "STRING")
            time.sleep(3)
            color.write ("\nRed: Luckily I'm bringing food and medicine to my Grandma. Here have this biscuit. It's for my grandma but I guess there is enough food here. A biscuit wouldn't kill her", "COMMENT")
            time.sleep(3)
            print("\nGained 10 starvation")
            starvation += 10
            stats()
            break
        elif (choice == 'D' or choice == 'd'):
            color.write ("\nRed: I'm doing great! I'm on my way to bring food and medicine to my Grandma","COMMENT")
            break
        else:
            choice = input("\nWhat should i tell her?? \n")
    time.sleep(3)
    scene2a()

    
def scene1(): ## Rabbit chase
    global speed
    global starvation
    global strength
    time.sleep(2)
    print("\n =================== The Forest =====================")
    time.sleep(2)
    color.write("*Grass rustling*","STRING")
    time.sleep(2)
    color.write("\nYou have nowhere to run rabbit","KEYWORD")
    time.sleep(2)
    color.write("\nYou were running so fast and did not look where you were going, and you tripped on a rock.","STRING")
    time.sleep(2)
    color.write("\n ARGGG Where did that rabbit go??","KEYWORD")
    time.sleep(2)
    color.write("\nDo you want to go left, right, forward, or stop chasing the rabbit?","STRING")
    time.sleep(2)
    choice = input ("\nWhere to go?\n A: Left \n B: Right \n C: Forward \n D: Stop chasing\n")
    while (choice != 'A' or choice != 'a' or choice != 'B' or choice != 'b' or choice != 'C' or choice != 'c' or choice !="D" or choice !="d"):
        if (choice == 'A' or choice == 'a'):
            color.write ("\nYou go left. A tree falls out of nowhere!!!","STRING")
            time.sleep(2)
            color.write ("\nYou manage to dodge it but it damaged your legs","STRING")
            time.sleep(2)
            color.write ("\nYou lost sight of the rabbit and you hear someone approaching near the roads.","STRING")
            time.sleep(2)
            color.write ("\nLost 20 Speed")
            speed -= 20
            break
        elif (choice == 'B' or choice == 'b'):
            color.write ("\nYou go right. You find yourself on the bottom of a hill.","STRING")
            time.sleep(2)
            color.write ("\nYou climb up the hill only to find that the rabbit isnt here.","STRING")
            time.sleep(2)
            color.write ("\nYou sat there exhausted but you hear someone approaching near the roads.","STRING")
            time.sleep(2)
            print ("\nLost 15 Strength")
            strength -= 15
            break
        elif (choice == 'C' or choice == 'c'):
            color.write ("\nYou continue running foward in the thick woods.","STRING")
            time.sleep(2)
            color.write ("\nYou pop out of a bush and you stepped on a bear trap. ","STRING")
            time.sleep(2)
            color.write ("\nYou tried to pull as hard as you could to free yourself but the trap was really strong.","STRING")
            time.sleep(2)
            color.write("\n After a few hard pulls, you finally got free","STRING")
            print ("\nLost 5 starvation")
            print ("Lost 20 Speed")
            print ("Lost 20 Strength")
            starvation -= 5
            strength-=20
            speed-=20
            break
        elif (choice == 'D' or choice == 'd'):
            color.write ("\nYou stop chasing the rabbit and you hear someone approaching near the roads.","STRING")
            time.sleep(2)
            break
        else:
            choice = input("\nHmmm, what to do? \n")
    fullnessdrop()
    stats()
    fullness0()
    scene2()    
def play():
    startstats()
    scene1()
play()

