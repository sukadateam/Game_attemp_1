import time,os,random
from vars import *
def loop1(lake1_cords,moving_to):
  global current_location, current_surrounding,time,stanima,dev
  fixed1=0
  fixed2=0
  fixed3=0
  time.sleep(1.5)#5
  if current_location[0]<lake1_cords[0]:
    fixed1=lake1_cords[0]-current_location[0]
  if current_location[0]>lake1_cords[0]:
    fixed1=current_location[0]-lake1_cords[0]
  if current_location[1]<lake1_cords[1]:
    fixed2=lake1_cords[1]-current_location[1]
  if current_location[1]>lake1_cords[1]:
    fixed2=current_location[1]-lake1_cords[1] #Up to this point is the same for all lakes
  if current_location[2]<lake1_cords[2]:
    fixed3=lake1_cords[2]-current_location[2]
  if current_location[2]>lake1_cords[2]:
    fixed3=current_location[2]-lake1_cords[2]
  total_distance=fixed1+fixed2+fixed3
  stanima1=total_distance/3.5
  stanima1=round(stanima1)
  if stanima1<stanima+1 or dev==True:
    print 'Moving to location...'
    print '\nTraveling cords:',fixed1,fixed2,fixed3
    current_surrounding=moving_to
    current_location=lake1_cords
    if dev==False:
      stanima-=stanima1
    print 'Total distance traveled:',total_distance,'(meters)'
    print 'Current area:',current_surrounding
    print 'Current cordinates:',current_location
    print 'Stanima:',stanima
  if stanima1+1>stanima and dev==False:
    if max_stanima>stanima1:
      print 'You need to sleep. You are too tired to keep moving.'
  if max_stanima<stanima1+1:
    print 'Your max_stanima is not high enough to proceed.'
  move_on=raw_input('Hit enter to exit change location:')
def loop2():
  global sides,choice
  if '(' in choice:
    choice = choice.replace('(','')
    sides=True
  if ')' in choice:
    choice = choice.replace(')','')
    sides=True
def loop3():
  #Use clear() before entering
  global storage_wood,wood,storage_water,water
  global storage_dirt,dirt,storage_rocks,rocks
  global storage_clay,clay,storage_bowl,bowl
  global storage_sticks,sticks,storage_pickaxe,pickaxe
  global storage_axe,axe,storage_shovel,shovel
  global home_storage,dev
  choice1=''
  choice2=''
  storage_int=0
  storage_int+=storage_water+storage_wood+storage_dirt
  storage_int+=storage_rocks+storage_clay+storage_bowl
  storage_int+=storage_sticks+storage_pickaxe+storage_axe
  storage_int+=storage_shovel
  self_int=0
  self_int+=wood+water+dirt+rocks+clay+bowl+sticks
  self_int+=pickaxe+axe+shovel
  if dev==True:
    print 'self_int:',self_int
    print 'storage_int:',storage_int
    print 'home_storage:',home_storage
    print 'self_storage:',self_storage
  if storage_int+1<home_storage+1:
    if self_int+1>self_storage:
      print 'Both Your Home and inventory are full. In order to use this function, you must remove some items.'
      print '\nHint: Sell the things you don\'t need'
    if self_int>self_storage+1:
      print 'Your home storage is full. You can not add things to it. But, you may take things away.'
      print '(1)Withdraw\n(2)Leave'
      move_on=raw_input('1 or 2:').lower()
      choice1='hi'
      if move_on=="1":
        choice2="1"
      if move_on=="2":
        choice1="wefhgef"
    if choice1 is not 'hi':
      if choice1 is not "wefhgef":
        print '(1)Withdraw\n(2)Deposit\n(3)Leave'
        choice2=raw_input("Choose one of the options:")
        clear()
        if choice2 == "1":
          print 'Items stored:'
          print '(1)Wood:',storage_wood,'(logs)'
          print '(2)Water:',storage_water,'(oz)'
          print '(3)Dirt:',storage_dirt,'(lbs)'
          print '(4)Rocks:',storage_rocks,'(Qty)'
          print '(5)Clay:',storage_clay,'(lbs)'
          print '(6)Bowl:',storage_bowl,'(Qty)'
          print '(7)Sticks:',storage_sticks,'(Qty)'
          print '(8)Pickaxes:',storage_pickaxe,'(Qty)'
          print '(9)Shovels:',storage_shovel,'(Qty)'
          print '(10)Axes:',storage_axe,'(Qty)'
          print '(11)Coal:',coal,'(Qty)'
          print '(12)Iron:',iron,'(Qty)'
          print '(13)Gold:',gold,'(Qty)'
          print '(14)Diamond:',diamond,'(Qty)'
          choice = raw_input('What would you like to withdraw:')
          if choice == "1":
            if storage_wood<1:
              print 'You don\'t have enough.'
            if storage_wood>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_wood+1:
                  wood+=int(choice)
                  storage_wood-=int(choice)
                  print 'Current holding:'
                  print 'Wood in storage:',storage_wood
                  print 'Wood in inventory:',wood
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "2":
            if storage_water<1:
              print 'You don\'t have enough.'
            if storage_water>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_water+1:
                  water+=int(choice)
                  storage_water-=int(choice)
                  print 'Current holding:'
                  print 'Water in storage:',storage_water
                  print 'Water in inventory:',water
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "3":
            if storage_dirt<1:
              print 'You don\'t have enough.'
            if storage_dirt>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_dirt+1:
                  dirt+=int(choice)
                  storage_dirt-=int(choice)
                  print 'Current holding:'
                  print 'Dirt in storage:',storage_dirt
                  print 'Dirt in inventory:',dirt
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "4":
            if storage_rocks<1:
              print 'You don\'t have enough.'
            if storage_rocks>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_rocks+1:
                  rocks+=int(choice)
                  storage_rocks-=int(choice)
                  print 'Current holding:'
                  print 'Rocks in storage:',storage_rocks
                  print 'Rocks in inventory:',rocks
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "5":
            if storage_clay<1:
              print 'You don\'t have enough.'
            if storage_clay>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_clay+1:
                  clay+=int(choice)
                  storage_clay-=int(choice)
                  print 'Current holding:'
                  print 'Clay in storage:',storage_clay
                  print 'Clay in inventory:',clay
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "7":
            if storage_sticks<1:
              print 'You don\'t have enough.'
            if storage_sticks>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_clay+1:
                  clay+=int(choice)
                  storage_clay-=int(choice)
                  print 'Current holding:'
                  print 'Sticks in storage:',storage_clay
                  print 'Sticks in inventory:',clay
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "6":
            if storage_bowl<1:
              print 'You don\'t have enough.'
            if storage_bowl>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_bowl+1:
                  bowl+=int(choice)
                  storage_bowl-=int(choice)
                  print 'Current holding:'
                  print 'Bowl in storage:',storage_bowl
                  print 'Bowl in inventory:',bowl
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "8":
            if storage_pickaxe<1:
              print 'You don\'t have enough.'
            if storage_pickaxe>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_pickaxe+1:
                  pickaxe+=int(choice)
                  storage_pickaxe-=int(choice)
                  print 'Current holding:'
                  print 'Pickaxe(s) in storage:',storage_pickaxe
                  print 'Pickaxe(s) in inventory:',pickaxe
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "9":
            if storage_shovel<1:
              print 'You don\'t have enough.'
            if storage_shovel>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_shovel+1:
                  shovel+=int(choice)
                  storage_shovel-=int(choice)
                  print 'Current holding:'
                  print 'Shovel(s) in storage:',storage_shovel
                  print 'Shovel(s) in inventory:',shovel
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "10":
            if storage_axe<1:
              print 'You don\'t have enough.'
            if storage_axe>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_axe+1:
                  axe+=int(choice)
                  storage_axe-=int(choice)
                  print 'Current holding:'
                  print 'Axe(s) in storage:',storage_axe
                  print 'Axe(s) in inventory:',axe
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "11":
            if storage_coal<1:
              print 'You don\'t have enough.'
            if storage_coal>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_coal+1:
                  coal+=int(choice)
                  storage_coal-=int(choice)
                  print 'Current holding:'
                  print 'Coal in storage:',storage_coal
                  print 'Coal in inventory:',coal
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "12":
            if storage_iron<1:
              print 'You don\'t have enough.'
            if storage_iron>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_iron+1:
                  iron+=int(choice)
                  storage_iron-=int(choice)
                  print 'Current holding:'
                  print 'Iron in storage:',storage_iron
                  print 'Iron in inventory:',iron
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "13":
            if storage_gold<1:
              print 'You don\'t have enough.'
            if storage_gold>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_gold+1:
                  gold+=int(choice)
                  storage_gold-=int(choice)
                  print 'Current holding:'
                  print 'Gold in storage:',storage_gold
                  print 'Gold in inventory:',gold
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "14":
            if storage_diamond<1:
              print 'You don\'t have enough.'
            if storage_diamond>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_diamond+1:
                  diamond+=int(choice)
                  storage_diamond-=int(choice)
                  print 'Current holding:'
                  print 'Diamond(s) in storage:',storage_diamond
                  print 'Diamond(s) in inventory:',diamond
              except ValueError, TypeError:
                print 'You need to enter a number.'
          move_on=raw_input('Hit enter to exit crafting:')
          choice=''
        if choice2 == "2":
          print 'You have:'
          print '(1)Wood:',wood,'(logs)'
          print '(2)Water:',water,'(oz)'
          print '(3)Dirt:',dirt,'(lbs)'
          print '(4)Rocks:',rocks,'(Qty)'
          print '(5)Clay:',clay,'(lbs)'
          print '(6)Bowl:',bowl,'(Qty)'
          print '(7)Sticks:',sticks,'(Qty)'
          print '(8)Pickaxes:',pickaxe,'(Qty)'
          print '(9)Shovels:',shovel,'(Qty)'
          print '(10)Axes:',axe,'(Qty)'
          print '(11)Coal:',coal,'(Qty)'
          print '(12)Iron:',iron,'(Qty)'
          print '(13)Gold:',gold,'(Qty)'
          print '(14)Diamond:',diamond,'(Qty)'
          choice = raw_input('What would you like to withdraw:')
          if choice == "1":
            if wood<1:
              print 'You don\'t have enough.'
            if wood>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<wood+1:
                  wood-=int(choice)
                  storage_wood+=int(choice)
                  print 'Current holding:'
                  print 'Wood in storage:',storage_wood
                  print 'Wood in inventory:',wood
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "2":
            if water<1:
              print 'You don\'t have enough.'
            if water>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<water+1:
                  water-=int(choice)
                  storage_water+=int(choice)
                  print 'Current holding:'
                  print 'Water in storage:',storage_water
                  print 'Water in inventory:',water
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "3":
            if dirt<1:
              print 'You don\'t have enough.'
            if dirt>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<dirt+1:
                  dirt-=int(choice)
                  storage_dirt+=int(choice)
                  print 'Current holding:'
                  print 'Dirt in storage:',storage_dirt
                  print 'Dirt in inventory:',dirt
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "4":
            if rocks<1:
              print 'You don\'t have enough.'
            if rocks>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<rocks+1:
                  rocks-=int(choice)
                  storage_rocks+=int(choice)
                  print 'Current holding:'
                  print 'Rock(s) in storage:',storage_rocks
                  print 'Rock(s) in inventory:',rocks
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "5":
            if clay<1:
              print 'You don\'t have enough.'
            if clay>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<clay+1:
                  clay-=int(choice)
                  storage_clay+=int(choice)
                  print 'Current holding:'
                  print 'Clay in storage:',storage_clay
                  print 'Clay in inventory:',clay
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "6":
            if bowl<1:
              print 'You don\'t have enough.'
            if bowl>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<bowl+1:
                  bowl-=int(choice)
                  storage_bowl+=int(choice)
                  print 'Current holding:'
                  print 'Bowl(s) in storage:',storage_bowl
                  print 'Bowl(s) in inventory:',bowl
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "7":
            if sticks<1:
              print 'You don\'t have enough.'
            if sticks>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<sticks+1:
                  sticks-=int(choice)
                  storage_sticks+=int(choice)
                  print 'Current holding:'
                  print 'Stick(s) in storage:',storage_sticks
                  print 'Stick(s) in inventory:',sticks
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "8":
            if pickaxe<1:
              print 'You don\'t have enough.'
            if pickaxe>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<pickaxe+1:
                  pickaxe-=int(choice)
                  storage_pickaxe+=int(choice)
                  print 'Current holding:'
                  print 'Pickaxe(s) in storage:',storage_pickaxe
                  print 'Pickaxe(s) in inventory:',pickaxe
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "9":
            if shovel<1:
              print 'You don\'t have enough.'
            if shovel>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<shovel+1:
                  shovel-=int(choice)
                  storage_shovel+=int(choice)
                  print 'Current holding:'
                  print 'Shovel(s) in storage:',storage_shovel
                  print 'Shovel(s) in inventory:',shovel
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "10":
            if axe<1:
              print 'You don\'t have enough.'
            if axe>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<axe+1:
                  axe-=int(choice)
                  storage_axe+=int(choice)
                  print 'Current holding:'
                  print 'Axe(s) in storage:',storage_axe
                  print 'Axe(s) in inventory:',axe
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "11":
            if coal<1:
              print 'You don\'t have enough.'
            if coal>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<coal+1:
                  coal-=int(choice)
                  storage_coal+=int(choice)
                  print 'Current holding:'
                  print 'Coal in storage:',storage_coal
                  print 'Coal in inventory:',coal
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "12":
            if iron<1:
              print 'You don\'t have enough.'
            if iron>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<iron+1:
                  iron-=int(choice)
                  storage_iron+=int(choice)
                  print 'Current holding:'
                  print 'Iron in storage:',storage_iron
                  print 'Iron in inventory:',iron
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "13":
            if gold<1:
              print 'You don\'t have enough.'
            if gold>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<gold+1:
                  gold-=int(choice)
                  storage_gold+=int(choice)
                  print 'Current holding:'
                  print 'Gold in storage:',storage_gold
                  print 'Gold in inventory:',gold
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "14":
            if diamond<1:
              print 'You don\'t have enough.'
            if diamond>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<diamond+1:
                  diamond-=int(choice)
                  storage_diamond+=int(choice)
                  print 'Current holding:'
                  print 'Diamond(s) in storage:',storage_diamond
                  print 'Diamond(s) in inventory:',diamond
              except ValueError, TypeError:
                print 'You need to enter a number.'
          
          move_on=raw_input('Hit enter to exit crafting:')
          choice=''
  if dev==True:
    blah=raw_input("Hit enter to continue:")
def loop4(s,other,numbers,price):
  #s = (True)Shows other stuff and stats
  global dirt,wood,rocks,water,clay,bowl,sticks
  global self_storage,home_storage,stanima,max_stanima
  global current_surronding,current_location
  global pickaxe,axe,shovel,diamond,coal,iron,gold
  side='  ()'
  side1=1
  self_int=0
  self_int+=wood+water+dirt+rocks+clay+bowl+sticks
  self_int+=pickaxe+axe+shovel+diamond+coal+iron+gold
  print 'Minerals:'
  if price==True:
    print '      Item      Price for one'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Wood:',str(wood)+',     Price:',buy_price_wood
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Dirt:',str(dirt)+',     Price:',buy_price_dirt
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Water:',str(water)+',    Price:',buy_price_water
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Rocks:',str(rocks)+',    Price:',buy_price_rocks
    print 'Items:'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Clay:',str(clay)+',     Price:',buy_price_clay
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Bowls:',str(bowl)+',    Price:',buy_price_bowl
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Sticks:',str(sticks)+',   Price:',buy_price_sticks
    print 'Tools:'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Pickaxes:',str(pickaxe)+',  Price:',buy_price_pickaxe
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Shovels:',str(shovel)+',   Price:',buy_price_shovel
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Axes:',str(axe)+',     Price:',buy_price_axe
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print 'Goodies:'
    print side2+'Coal:',str(coal)+',     Price:',buy_price_coal
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Iron:',str(iron)+',     Price:',buy_price_iron
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Gold:',str(gold)+',     Price:',buy_price_gold
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Diamonds:',str(diamond)+', Price:',buy_price_diamond
  if numbers==True:
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Wood:',wood,'(logs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Dirt:',dirt,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Water:',water,'(oz)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Rocks:',rocks,'(Qty)'
    print 'Items:'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Clay:',clay,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Bowls:',bowl,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Sticks:',sticks,'(Qty)'
    print 'Tools:'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Pickaxes:',pickaxe,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Shovels:',shovel,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Axes:',axe,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print 'Goodies:'
    print side2+'Coal:',coal,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Iron:',iron,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Gold:',gold,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Diamonds:',diamond,'(Qty)'
  if numbers==False:
    if price==False:
      print '  Wood:',wood,'(logs)'
      print '  Dirt:',dirt,'(lbs)'
      print '  Water:',water,'(oz)'
      print '  Rocks:',rocks,'(Qty)'
      print 'Items:'
      print '  Clay:',clay,'(lbs)'
      print '  Bowls:',bowl,'(Qty)'
      print '  Sticks:',sticks,'(Qty)'
      print 'Tools:'
      print '  Pickaxes:',pickaxe,'(Qty)'
      print '  Shovels:',shovel,'(Qty)'
      print '  Axes:',axe,'(Qty)'
  if other==True:
    print 'Goodies:'
    print '  Coal:',coal,'(Qty)'
    print '  Iron:',iron,'(Qty)'
    print '  Gold:',gold,'(Qty)'
    print '  Diamonds:',diamond,'(Qty)'
  if s==True:
    print 'Storage:'
    print '  Inventory Storage:',self_storage,'(qty of items)'
    print '  Home storage:',home_storage,'(qty of items)'
    print '  Inventory capacity:',self_int,'out of',self_storage
    print 'Stats:'
    print '  Stanima:',stanima,'(%)'
    print '  Max_stanima',max_stanima,'(%)'
    print ''
    print 'Current money:',str(money)+' (cents)'
    print 'Current area:',current_surrounding
    print 'Current cordinates:',current_location
def clear():
  os.system('clear')
def dev_promt():
  print 'You must activate Dev_options to use this. This lock will be removed in future updates. Go to vars.py to see how to enable dev_options. It\'s at the bottom.'
#move_on=raw_input('Hit enter to exit crafting:')
p=True
dev=True#Default False
while p==True:
  clear()
  if dev==True:
    print 'Dev_options: Enabled\n'
  print 'Please read tips if this is the first time playing. Thank you!'
  print '(1)Gather resources'
  print '(2)Change location'
  print '(3)Go back home'
  print '(4)Crafting menu'
  print '(5)Sleep'
  print '(6)Tips'
  print '(7)Exersice'
  print '(8)Sell'
  print '(9)Mining'
  print '(10)Quests'
  print '(11)Buy'
  print '(*)Show inventory'
  print '\nOthers:'
  print '(save)Save data'
  print '(bye)Exit'
  if dev==True:
    print '\nDev tools:'
    print 'Dev_menu()'
    print 'Dev_var()\n'
  print '\nTo get help type (help)'
  choice=raw_input('Choose an option or enter code:')
  if choice==dev_options:
    use=False
    if dev==False:
      print 'Dev_options: Enabled'
      dev=True
      use=True
    if use==False:
      if dev==True:
        print 'Dev_options: Disabled'
        dev=False
    time.sleep(1)
  clear()
  loop2()
  if choice == "1":
    self_int=0
    self_int+=wood+water+dirt+rocks+clay+bowl+sticks
    self_int+=pickaxe+axe+shovel+diamond+coal+iron+gold
    #Water + Dirt = Clay
    #Wood = house, water holder, storage
    print '(1)Wood\n(2)Water\n(3)Dirt\n(4)Rocks\n(5)Sticks'
    choice=raw_input('What would you like to gather:')
    loop2()
    if choice == "1":
      if self_storage<self_int+3:
        print 'Your inventory is full.'
        choice='blah'
      if choice == "1":
        if axe>0:
          print 'Gathering wood...'
          time.sleep(3)
          wood+=3
          print 'Gathered wood'
          time.sleep(1)
        if axe<1:
          print 'You need more axe(s)'
    if choice == "2":
      if dev==False:
        if current_surrounding not in water_biomes:
          print 'You need to be near a lake or a river to gather water.'
      if current_surrounding in water_biomes or dev==True:
        if self_storage<self_int+2:
          choice='blah'
        if choice == "2":
          print 'Gathering water...'
          time.sleep(3)
          water+=2
          print 'Gathered water'
          time.sleep(1)
    if choice == "3":
      if current_surrounding in dirt_biomes or dev==True:
        if self_storage<self_int+2:
          choice='blah'
        if choice == "3":
          if shovel>0:
            print 'Gathering dirt...'
            time.sleep(3)
            dirt+=2
            print 'Gathered dirt'
            time.sleep(1)
          if shovel<1:
            print 'You need more shovel(s)'
      if dev==False:
        if current_surrounding not in dirt_biomes:
          print 'You must be in the forest to gather dirt.'
    if choice == "4":
      if current_surrounding in clay_biomes or current_surrounding in dirt_biomes or dev==True:
        if self_storage<self_int+2:
          choice = 'blah'
        if choice == "4":
          print 'Gathering rocks...'
          time.sleep(3)
          rocks+=2
          print 'Gathered 2 rocks.'
          time.sleep(1)
      if dev==False:
        if current_surrounding not in clay_biomes or dirt_biomes:
          print 'You must at clay mountian or the forest to gather rocks.'
    if choice == "5":
      if current_surrounding in dirt_biomes or dev==True:
        if self_storage<self_int+1:
          choice="blah"
        if choice == "5":
          print 'Gathering sticks...'
          time.sleep(3)
          sticks+=2
          print 'Gathered 2 sticks.'
          time.sleep(1)
      if dev==False:
        if current_surrounding not in dirt_biomes:
          print 'You must be in the forest to gather sticks.'
    choice=''
    move_on=raw_input('Hit enter to exit crafting:')
  if choice == "2":
    print 'Current location:',current_surrounding
    print '(1)Lake\n(2)River\n(3)Clay mountian\n(4)Exercise mountian\n(5)Desert\n(6)Abandoned city'
    choice = raw_input('Where would you like to go:')
    loop2()
    if choice == "1":
      hi=random.randint(1,3)
      if hi==1:
        loop1(lake1_cords,'lake #1')
      if hi==2:
        loop1(lake2_cords,'lake #2')
      if hi==3:
        loop1(lake3_cords,'lake #3')
    if choice == "2":
      hi=random.randint(1,3)
      if hi==1:
        loop1(river1_cords,'river #1')
      if hi==2:
        loop1(river2_cords,'river #2')
      if hi==3:
        loop1(river3_cords,'river #3')
    if choice == "3":
      hi=random.randint(1,3)
      if hi==1:
        loop1(clay_mountian1_cords,'clay mountian #1')
      if hi==2:
        loop1(clay_mountian2_cords,'clay mountian #2')
      if hi==3:
        loop1(clay_mountian3_cords,'clay mountian #3')
    if choice == "4":
      loop1(exercise_mountian1_cords,'exercise mountian #1')
    if choice == "5":
      hi=random.randint(1,3)
      if hi==1:
        loop1(desert1_cords,'desert #1')
      if hi==2:
        loop1(desert2_cords,'desert #2')
      if hi==3:
        loop1(desert3_cords,'desert #3')
    if choice == "6":
      hi=random.randint(1,3)
      if hi==1:
        loop1(city1_cords,'city #1')
      if hi==2:
        loop1(city2_cords,'city #2')
      if hi==3:
        loop1(city3_cords,'city #3')
    choice = ''
  if choice == "3":
    loop1(home_location,'home')
    choice = ''
  if choice == "4":
    print '(1)Clay     Needs - Dirt:1 Water:1'
    print '(2)Bowl     Needs - Wood:2'
    print '(3)Sticks   Needs - Wood:1'
    if dev==True:
      print '(4)Pickaxe  Needs - Sticks:2 Rocks:3'
      print '(5)Shovel   Needs - Sticks:2 Rocks:1'
      print '(6)Axe      Needs - Sticks:2 Rocks:2'
    choice = raw_input('What would you like to make:')
    loop2()
    if choice == "1":
      if dirt>0:
        if water>0:
          print 'Making clay...'
          time.sleep(2)
          print 'Made 1 clay'
          clay+=1
          dirt-=1
          water-=1
          print 'You have',clay,'clay'
      if dirt<1:
        print 'You need more dirt'
        print 'You have',dirt,'dirt'
      if water<1:
        print 'You need more water'
        print 'You have',water,'water'
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "2":
      if wood>1:
        print 'Making a bowl...'
        time.sleep(2)
        print 'Made 1 bowl'
        bowl+=1
        wood-=2
        print 'You have',bowl,'bowl(s)'
      if wood<2:
        print 'You need more wood'
        print 'You have',wood,'wood'
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "3":
      if wood>0:
        print 'Making sticks...'
        time.sleep(2)
        print 'Made 4 sticks.'
        sticks+=4
        wood-=1
        print 'You have',sticks,'stick(s)'
      if wood<1:
        print 'You need more wood'
        print 'You have',wood,'wood'
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "4":
      if sticks>1:
        if rocks>2:
          print 'Making a pickaxe...'
          time.sleep(2)
          print 'Made 1 pickaxe.'
          pickaxe+=1
          sticks-=2
          rocks-=3
          print 'You have',pickaxe,'pickaxe(s)'
      if sticks<2:
        print 'You need more sticks.'
        print 'You have',sticks,'sticks'
      if rocks<3:
        print 'You need more rocks'
        print 'You have',rocks,'rocks'
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "5":
      if sticks>1:
        if rocks>0:
          print 'Making a shovel...'
          time.sleep(2)
          print 'Made 1 shovel.'
          shovel+=1
          sticks-=2
          rocks-=1
          print 'You have',shovel,'shovel(s)'
      if sticks<2:
        print 'You need more sticks.'
        print 'You have',sticks,'sticks'
      if rocks<1:
        print 'You need more rocks'
        print 'You have',rocks,'rocks'
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "6":
      if sticks>1:
        if rocks>1:
          print 'Making a axe...'
          time.sleep(2)
          print 'Made 1 axe.'
          axe+=1
          sticks-=2
          rocks-=2
          print 'You have',axe,'axe(s)'
      if sticks<2:
        print 'You need more sticks.'
        print 'You have',sticks,'sticks'
      if rocks<2:
        print 'You need more rocks'
        print 'You have',rocks,'rocks'
      move_on=raw_input('Hit enter to exit crafting:')
    choice = ''
  if choice == "5":
    if dev==False:
      if stanima==max_stanima:
        print 'You are not tired.'
      if stanima<max_stanima:
        print 'Sleeping...'
        stanima1=max_stanima-stanima
        sleep_time=stanima1/3
        sleep_time=round(sleep_time)
        if sleep_time>15:
          sleep_time=15
        if current_surrounding == "home":
          sleep_time/=2
        print 'Est:',sleep_time,'seconds'
        time.sleep(sleep_time)
        stanima=max_stanima
        move_on=raw_input('Hit enter to exit sleep:')
    if dev==True:
      stanima=max_stanima
    choice = ''
  if choice == "6":
    print 'Things with (*) at the end are locked. At the end, not the beggining. Just making that clear.'
    print '\nYou can be anywhere when entering the mines. There is a mine in every location.'
    if dev==True:
      print '\nTo store store items at home. Do this. \n1. Make sure you are at home\n2. Open inventory\n3. Instead of hiting enter to exit type (storage) to store items.\nHint: You can also grab items back from doing this.'
    move_on=raw_input('\nHit enter to exit tips:')
    choice = ''
  if choice == "7":
    if current_surrounding=="exercise mountian #1" or dev==True:
      print 'Getting in the mood...'
      time.sleep(2.5)
      print 'Moving to the beat...'
      time.sleep(2.5)
      print 'Singing the lyrics...'
      time.sleep(1)
      print 'Never gonna give you up'
      print 'Never gonna let you down'
      print 'Never gonna run around and desert you'
      print 'Never gonna make you cry'
      print 'Never gonna say goodbye'
      print 'Never gonna tell a lie and hurt you'
      print 'By: Rick Astley'
      print
      print 'Stanima decreased by 30'
      print 'Max_Stanima increased by 15'
      stanima-=30
      max_stanima+=15
      print 'Recommended to go to sleep.'
    if current_surrounding is not "exercise mountian #1":
      print 'You need to travel to exersice mountian to use this function.'
    move_on=raw_input('Hit enter to exit exercise:')
  if choice == "8":
    clear()
    loop4(s=False,other=False,numbers=True,price=False)
    choice=raw_input('What would you like to sell:')
    if choice=="1":
      if wood<1:
        print 'You don\'t have any to sell'
      if wood>0:
        choice=raw_input('How many:')
        if wood==int(choice) or wood>int(choice):
          try:
            money+=int(choice)*price_wood
            wood-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Wood:',wood
          except ValueError:
            print 'You need to enter a number.'
      choice=''
    if choice=="2":
      if dirt<1:
        print 'You don\'t have any to sell'
      if dirt>0:
        choice=raw_input('How many:')
        try:
          if dirt==int(choice) or dirt>int(choice):
            money+=int(choice)*price_dirt
            dirt-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Dirt:',dirt
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="3":
      if water<1:
        print 'You don\'t have any to sell'
      if water>0:
        choice=raw_input('How many:')
        try:
          if water==int(choice) or water>int(choice):
            money+=int(choice)*price_water
            water-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Water:',water
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="4":
      if rocks<1:
        print 'You don\'t have any to sell'
      if rocks>0:
        choice=raw_input('How many:')
        try:
          if rocks==int(choice) or rocks>int(choice):
            money+=int(choice)*price_rocks
            rocks-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Rock(s):',rocks
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="5":
      if clay<1:
        print 'You don\'t have any to sell'
      if clay>0:
        choice=raw_input('How many:')
        try: 
          if clay==int(choice) or clay>int(choice):
            money+=int(choice)*price_clay
            clay-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Clay:',clay
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="6":
      if bowls<1:
        print 'You don\'t have any to sell'
      if bowls>0:
        choice=raw_input('How many:')
        try:
          if bowls==int(choice) or bowls>int(choice):
            money+=int(choice)*price_bowls
            bowls-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Bowl(s):',bowls
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="7":
      if sticks<1:
        print 'You don\'t have any to sell'
      if sticks>0:
        choice=raw_input('How many:')
        try:
          if sticks==int(choice) or sticks>int(choice):
            money+=int(choice)*price_sticks
            sticks-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Stick(s):',sticks
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="8":
      if pickaxe<1:
        print 'You don\'t have any to sell'
      if pickaxe>0:
        choice=raw_input('How many:')
        try:
          if pickaxe==int(choice) or pickaxe>int(choice):
            money+=int(choice)*price_pickaxe
            pickaxe-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Pickaxe(s):',pickaxe
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="9":
      if shovel<1:
        print 'You don\'t have any to sell'
      if shovel>0:
        choice=raw_input('How many:')
        try:
          if shovel==int(choice) or shovel>int(choice):
            money+=int(choice)*price_shovel
            shovel-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Shovel(s):',shovel
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="10":
      if axe<1:
        print 'You don\'t have any to sell'
      if axe>0:
        choice=raw_input('How many:')
        try:
          if axe==int(choice) or axe>int(choice):
            money+=int(choice)*price_axe
            axe-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Axe(s):',axe
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="11":
      if coal<1:
        print 'You don\'t have any to sell'
      if coal>0:
        choice=raw_input('How many:')
        try:
          if coal==int(choice) or coal>int(choice):
            money+=int(choice)*price_coal
            coal-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Coal:',coal
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="12":
      if iron<1:
        print 'You don\'t have any to sell'
      if iron>0:
        choice=raw_input('How many:')
        try:
          if iron==int(choice) or iron>int(choice):
            money+=int(choice)*price_iron
            iron-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Iron:',iron
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="13":
      if gold<1:
        print 'You don\'t have any to sell'
      if gold>0:
        choice=raw_input('How many:')
        try:
          if gold==int(choice) or gold>int(choice):
            money+=int(choice)*price_gold
            gold-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Gold:',gold
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    if choice=="14":
      if diamond<1:
        print 'You don\'t have any to sell'
      if diamond>0:
        choice=raw_input('How many:')
        try:
          if diamond==int(choice) or diamond>int(choice):
            money+=int(choice)*price_diamond
            diamond-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Diamond:',diamond
        except ValueError:
          print 'You need to enter a number.'
      choice=''
    move_on=raw_input('Hit enter to exit sell:')
  if choice == "9":
    self_int=0
    self_int+=wood+water+dirt+rocks+clay+bowl+sticks
    self_int+=pickaxe+axe+shovel+diamond+coal+iron+gold
    if dev==True:
      print 'Inventory capacity:',self_int,'out of',self_storage
    if pickaxe<1:
      print 'You need at least one pickaxe to mine.'
      time.sleep(1.5)
    if pickaxe>0:
      if self_storage>self_int+1 or dev==True:
        if stanima>59 or dev==True:
          print 'Going into the mines...'
          time.sleep(2.5)
          clear()
          print '(1)Coal       Est: 5 sec'
          print '(2)Iron       Est: 15 sec'
          print '(3)Gold       Est: 30 sec'
          print '(4)Diamond    Est: 1 min'
          choice = raw_input('What would you like to mine:')
          if choice == "1":
            print 'Going to find some coal...'
            time.sleep(1)
            print 'Found some coal. \nMining the coal...'
            print 'Est: 2s'
            time.sleep(2)
            coal+=1
            pickaxe-=1
            print 'You got 1 coal! But lost 1 pickaxe :('
          if choice == "2":
            print 'Going to find some iron...'
            time.sleep(1)
            print 'Found some iron. \nMining the iron...'
            print 'Est: 5s'
            time.sleep(5)
            iron+=1
            pickaxe-=1
            print 'You got 1 iron! But lost 1 pickaxe :('
          if choice == "3":
            print 'Going to find some gold...'
            time.sleep(1)
            print 'Found some gold. \nMining the gold...'
            print 'Est: 9s'
            time.sleep(9)
            gold+=1
            pickaxe-=1
            print 'You got 1 gold! But lost 1 pickaxe :('
          if choice == "4":
            print 'Going to find some diamonds...'
            time.sleep(1)
            print 'Found some diamonds. \nMining the diamonds...'
            print 'Est: 15s'
            time.sleep(15)
            diamond+=1
            pickaxe-=1
            print 'You got 1 diamond! But lost 1 pickaxe :('
        if stanima<60 or dev==False:
          clear()
          print 'You need to go to sleep.'
      if self_storage+1<self_int and dev==False:
        print 'Your storage is full. Empty your storage in show: inventory. Then type: storage'
        time.sleep(1.5)
    move_on=raw_input('Hit enter to exit mining:')
    choice = ''
  if choice == "10":
    if dev==False:
      print 'Nothing here currently...'
    if dev==True:
      hi=True
      if quest1==False:
        hi=False
        print 'Your first quest is to get me: 5 sticks'
        print 'Reward: 25 money'
        choice=raw_input('Do you have 5 sticks:').lower()
        if choice == "yes":
          print 'Checking...'
          time.sleep(1)
          if sticks>4:
            print 'Congrats you finished your first quest!'
            print 'You got 25 money.'
            sticks-=5
            money+=25
            quest1=True
          if sticks<5:
            print 'Sorry, but you do not. Come back when you do.'
        if choice == "no":
          print 'Okay then.'
      if quest2==False:
        if hi==True:
          print 'Your second quest is to get me: 2 pickaxe(s)'
          print 'Reward: 32 money'
          choice=raw_input('Do you have 2 pickaxe(s)').lower()
          if choice == "yes":
            print 'Checking...'
            time.sleep(1)
            if pickaxe>1:
              print 'Congrats you finished your second quest!'
              print 'You got 32 money.'
              pickaxe-=2
              money+=32
              quest2=True
            if pickaxe<2:
              print 'Sorry, but you do not. Come back when you do.'
      if quest1==True and quest2==True:
        print 'You have completed all of the quests.'
    move_on=raw_input('Hit enter to exit quest:')
    choice=''
  if choice == "11":
    self_int=0
    self_int+=wood+water+dirt+rocks+clay+bowl+sticks
    self_int+=pickaxe+axe+shovel+diamond+coal+iron+gold
    print 'This page is in the works.'
    if self_int<self_storage+1:
      loop4(s=False,other=False,numbers=False,price=True)
      choice=raw_input('What would you like to buy:')
      if choice == "1":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_wood*int(choice):
            money-=buy_price_wood*int(choice)
            wood+=int(choice)
            print 'You now have:',wood
          if money<buy_price_wood*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'wood'
            print 'Total cost:',buy_price_wood*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "2":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_dirt*int(choice):
            money-=buy_price_dirt*int(choice)
            dirt+=int(choice)
            print 'You now have:',dirt
          if money<buy_price_dirt*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'dirt'
            print 'Total cost:',buy_price_dirt*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "3":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_water*int(choice):
            money-=buy_price_water*int(choice)
            water+=int(choice)
            print 'You now have:',water
          if money<buy_price_water*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'water'
            print 'Total cost:',buy_price_water*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "4":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_rocks*int(choice):
            money-=buy_price_rocks*int(choice)
            rocks+=int(choice)
            print 'You now have:',rocks
          if money<buy_price_rocks*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'rocks'
            print 'Total cost:',buy_price_rocks*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "5":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_clay*int(choice):
            money-=buy_price_clay*int(choice)
            clay+=int(choice)
            print 'You now have:',clay
          if money<buy_price_clay*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'clay'
            print 'Total cost:',buy_price_clay*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "6":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_bowl*int(choice):
            money-=buy_price_bowl*int(choice)
            bowl+=int(choice)
            print 'You now have:',bowl
          if money<buy_price_wood*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'bowl'
            print 'Total cost:',buy_price_bowl*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "7":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_sticks*int(choice):
            money-=buy_price_sticks*int(choice)
            sticks+=int(choice)
            print 'You now have:',sticks
          if money<buy_price_sticks*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'sticks'
            print 'Total cost:',buy_price_sticks*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "8":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_pickaxe*int(choice):
            money-=buy_price_pickaxe*int(choice)
            pickaxe+=int(choice)
            print 'You now have:',pickaxe
          if money<buy_price_pickaxe*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'pickaxe'
            print 'Total cost:',buy_price_pickaxe*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "9":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_shovel*int(choice):
            money-=buy_price_shovel*int(choice)
            shovel+=int(choice)
            print 'You now have:',wood
          if money<buy_price_shovel*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'shovel'
            print 'Total cost:',buy_price_shovel*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "10":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_axe*int(choice):
            money-=buy_price_axe*int(choice)
            axe+=int(choice)
            print 'You now have:',axe
          if money<buy_price_axe*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'axe'
            print 'Total cost:',buy_price_axe*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "11":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_coal*int(choice):
            money-=buy_price_coal*int(choice)
            coal+=int(choice)
            print 'You now have:',coal
          if money<buy_price_coal*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'coal'
            print 'Total cost:',buy_price_coal*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "12":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_iron*int(choice):
            money-=buy_price_iron*int(choice)
            iron+=int(choice)
            print 'You now have:',iron
          if money<buy_price_iron*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'iron'
            print 'Total cost:',buy_price_iron*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "13":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_gold*int(choice):
            money-=buy_price_gold*int(choice)
            gold+=int(choice)
            print 'You now have:',gold
          if money<buy_price_gold*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'gold'
            print 'Total cost:',buy_price_gold*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      if choice == "14":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_diamond*int(choice):
            money-=buy_price_diamond*int(choice)
            diamond+=int(choice)
            print 'You now have:',diamond
          if money<buy_price_diamond*int(choice):
            print 'You don\'t have enough money'
            print 'Total asked:',choice,'diamond'
            print 'Total cost:',buy_price_diamond*int(choice),'money'
        except ValueError:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
      choice=''
    if self_int+1>self_storage:
      print 'Your inventory is at capacity.'
    move_on=raw_input('Hit enter to exit buy:')
  if choice in exit_pos:
    print 'Goodbye.'
    p=False
  if choice == "*":
    loop4(s=True,other=True,numbers=False,price=False)
    #clay,bowl,storage
    move_on=raw_input('Hit enter to exit bag:').lower()
    if move_on=="storage":
      if dev==True:
        clear()
        loop3()
      if dev==False:
        clear()
        dev_promt()
        move_on=raw_input('Hit enter to exit storage:')
    choice = ''
  if choice == "save":
    #save.write('='+str()+'\n')
    save=file('vars.py','w')
    save.write('#Materials\n')
    save.write('wood='+str(wood)+' #logs\n')
    save.write('water='+str(water)+' #oz\n')
    save.write('dirt='+str(dirt)+' #lbs\n')
    save.write('rocks='+str(rocks)+' #Qty\n')
    save.write('#Things you can make\n')
    save.write('clay='+str(clay)+' #lbs\n')
    save.write('bowl='+str(bowl)+' #Qty\n')
    save.write('sticks='+str(sticks)+' #Qty\n')
    save.write('#Goodies\n')
    save.write('coal='+str(coal)+'\n')
    save.write('iron='+str(iron)+'\n')
    save.write('gold='+str(gold)+'\n')
    save.write('diamond='+str(diamond)+'\n')
    save.write('#Home storage vars\n')
    save.write('storage_wood='+str(storage_wood)+'\n')
    save.write('storage_water='+str(storage_water)+'\n')
    save.write('storage_dirt='+str(storage_dirt)+'\n')
    save.write('storage_rocks='+str(storage_rocks)+'\n')
    save.write('storage_clay='+str(storage_clay)+'\n')
    save.write('storage_bowl='+str(storage_bowl)+'\n')
    save.write('storage_sticks='+str(storage_sticks)+'\n')
    save.write('storage_pickaxe='+str(storage_pickaxe)+'\n')
    save.write('storage_shovel='+str(storage_shovel)+'\n')
    save.write('storage_axe='+str(storage_axe)+'\n')
    save.write('#Storage\n')
    save.write('self_storage='+str(self_storage)+' #Qty of items\n')
    save.write('home_storage='+str(home_storage)+' #Qty of items\n')
    save.write('#Tools\n')
    save.write('pickaxe='+str(pickaxe)+' #Qty, Can be used 1 time\n')
    save.write('shovel='+str(shovel)+' #Qty, Can be used 1 time\n')
    save.write('axe='+str(axe)+' #Qty, Can be used 1 time\n')
    save.write('#Cords\n')
    save.write('lake1_cords='+str(lake1_cords)+'\n')
    save.write('lake2_cords='+str(lake2_cords)+'\n')
    save.write('lake3_cords='+str(lake3_cords)+'\n')
    save.write('river1_cords='+str(river1_cords)+'\n')
    save.write('river2_cords='+str(river2_cords)+'\n')
    save.write('river3_cords='+str(river3_cords)+'\n')
    save.write('clay_mountian1_cords='+str(clay_mountian1_cords)+'\n')
    save.write('clay_mountian2_cords='+str(clay_mountian2_cords)+'\n')
    save.write('clay_mountian3_cords='+str(clay_mountian3_cords)+'\n')
    save.write('desert1_cords='+str(desert1_cords)+'\n')
    save.write('desert2_cords='+str(desert2_cords)+'\n')
    save.write('desert3_cords='+str(desert3_cords)+'\n')
    save.write('city1_cords='+str(city1_cords)+'\n')
    save.write('city2_cords='+str(city2_cords)+'\n')
    save.write('city3_cords='+str(city3_cords)+'\n')
    save.write('forest1_cords='+str(forest1_cords)+'\n')
    save.write('forest2_cords='+str(forest2_cords)+'\n')
    save.write('forest3_cords='+str(forest3_cords)+'\n')
    save.write('exercise_mountian1_cords='+str(exercise_mountian1_cords)+'\n')
    save.write('#Locations\n')
    save.write('home_location='+str(home_location)+'\n')
    save.write('current_location='+str(current_location)+'\n')
    save.write("current_surrounding='"+str(current_surrounding)+"'\n")
    save.write('#Biomes\n')
    save.write("water_biomes=['lake #1','lake #2','lake #3','river #1','river #2','river #3']\n")
    save.write("clay_biomes=['clay mountian #1','clay mountian #2','clay mountian #3']\n")
    save.write("sand_biomes=['desert #1','desert #2','desert #3','abandoned city','city #1','city #2','city #3']\n")
    save.write("dirt_biomes=['forest #1','forest #2','forest #3']\n")
    save.write('#Others\n')
    save.write('sides='+str(sides)+'\n')
    save.write('money='+str(money)+'\n')
    save.write('stanima='+str(stanima)+' #Starting Max 100, Default 100\n')
    save.write('max_stanima='+str(max_stanima)+'\n')
    save.write("exit_pos=['bye','goodbye','exit','leave','moving on','adios','adiós']\n")
    save.write('#Quests\n')
    save.write('quest1='+str(quest1)+' #False=Not done\n')
    save.write('quest2='+str(quest2)+' #True=Done\n')
    save.write("\n#Though all cords = distance\n")
    save.write("#Lake = 27,0,?\n")
    save.write("#River = 10,0,?\n")
    save.write("#Clay mountian = 103,?,?\n")
    save.write("#Exercise mountian = 378,207,?\n")
    save.write("#Desert = 521,10,?\n")
    save.write("#Abandoned city = 245,0,?\n")
    save.write("#Forest = 34,5,?\n\n")
    save.write('#Sell prices\n')
    save.write('price_wood='+str(price_wood)+'\n')
    save.write('price_dirt='+str(price_dirt)+'\n')
    save.write('price_water='+str(price_water)+'\n')
    save.write('price_rocks='+str(price_rocks)+'\n')
    save.write('price_clay='+str(price_clay)+'\n')
    save.write('price_bowl='+str(price_bowl)+'\n')
    save.write('price_sticks='+str(price_sticks)+'\n')
    save.write('price_pickaxe='+str(price_pickaxe)+'\n')
    save.write('price_shovel='+str(price_shovel)+'\n')
    save.write('price_axe='+str(price_axe)+'\n')
    save.write('price_coal='+str(price_coal)+'\n')
    save.write('price_iron='+str(price_iron)+'\n')
    save.write('price_gold='+str(price_gold)+'\n')
    save.write('price_diamond='+str(price_diamond)+'\n\n')
    save.write('#Buy prices\n')
    save.write('buy_price_wood='+str(buy_price_wood)+'\n')
    save.write('buy_price_dirt='+str(buy_price_dirt)+'\n')
    save.write('buy_price_water='+str(buy_price_water)+'\n')
    save.write('buy_price_rocks='+str(buy_price_rocks)+'\n')
    save.write('buy_price_clay='+str(buy_price_clay)+'\n')
    save.write('buy_price_bowl='+str(buy_price_bowl)+'\n')
    save.write('buy_price_sticks='+str(buy_price_sticks)+'\n')
    save.write('buy_price_pickaxe='+str(buy_price_pickaxe)+'\n')
    save.write('buy_price_shovel='+str(buy_price_shovel)+'\n')
    save.write('buy_price_axe='+str(buy_price_axe)+'\n')
    save.write('buy_price_coal='+str(buy_price_coal)+'\n')
    save.write('buy_price_iron='+str(buy_price_iron)+'\n')
    save.write('buy_price_gold='+str(buy_price_gold)+'\n')
    save.write('buy_price_diamond='+str(buy_price_diamond)+'\n\n')
    save.write('# --- CODES IN GAME ---\n')
    save.write("dev_options='W3rS3cur3' #In the main menu enter this to activate.")
    save.close()
  if choice == "Dev_menu":
    if dev==True:
      if sides == True:
        print '(1)Give - Gives free stuff'
        print '(2)Remove - Removes stuff'
        choice = raw_input('Choose an option:')
        if choice == "1":
          clear()
          loop4(s=False,other=False,numbers=True)
          choice=raw_input('Choose an option:')
          if choice == "1":
            choice = raw_input('How many:')
            wood+=int(choice)
            choice = ''
          if choice == "2":
            choice = raw_input('How many:')
            dirt+=int(choice)
            choice = ''
          if choice == "3":
            choice = raw_input('How many:')
            water+=int(choice)
            choice = ''
          if choice == "4":
            choice = raw_input('How many:')
            rocks+=int(choice)
            choice = ''
          if choice == "5":
            choice = raw_input('How many:')
            clay+=int(choice)
            choice = ''
          if choice == "6":
            choice = raw_input('How many:')
            bowl+=int(choice)
            choice = ''
          if choice == "7":
            choice = raw_input('How many:')
            sticks+=int(choice)
            choice = ''
          if choice == "8":
            choice = raw_input('How many:')
            pickaxe+=int(choice)
            choice = ''
          if choice == "9":
            choice = raw_input('How many:')
            shovel+=int(choice)
            choice = ''
          if choice == "10":
            choice = raw_input('How many:')
            axe+=int(choice)
            choice = ''
          if choice == "11":
            choice = raw_input('How many:')
            coal+=int(choice)
            choice = ''
          if choice == "12":
            choice = raw_input('How many:')
            iron+=int(choice)
            choice = ''
          if choice == "13":
            choice = raw_input('How many:')
            gold+=int(choice)
            choice = ''
          if choice == "14":
            choice = raw_input('How many:')
            diamond+=int(choice)
            choice = ''
        if choice == "2":
          clear()
          loop4(s=False,other=False,numbers=True)
          choice=raw_input('Choose an option:')
          if choice == "1":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              wood=0
            if choice is not "*":
              if wood==int(choice) or wood>int(choice):
                wood-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "2":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              dirt=0
            if choice is not "*":
              if dirt==int(choice) or dirt>int(choice):
                dirt-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "3":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              water=0
            if choice is not "*":
              if water==int(choice) or water>int(choice):
                water-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "4":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              rocks=0
            if choice is not "*":
              if rocks==int(choice) or rocks>int(choice):
                rocks-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "5":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              clay=0
            if choice is not "*":
              if clay==int(choice) or clay>int(choice):
                clay-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "6":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              bowl=0
            if choice is not "*":
              if bowl==int(choice) or bowl>int(choice):
                bowl-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "7":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              sticks=0
            if choice is not "*":
              if sticks==int(choice) or sticks>int(choice):
                sticks-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "8":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              pickaxe=0
            if choice is not "*":
              if pickaxe==int(choice) or pickaxe>int(choice):
                pickaxe-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "9":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              shovel=0
            if choice is not "*":
              if shovel==int(choice) or shovel>int(choice):
                shovel-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "10":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              axe=0
            if choice is not "*":
              if axe==int(choice) or axe>int(choice):
                axe-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "11":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              coal=0
            if choice is not "*":
              if coal==int(choice) or coal>int(choice):
                coal-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "12":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              iron=0
            if choice is not "*":
              if iron==int(choice) or iron>int(choice):
                iron-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "13":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              gold=0
            if choice is not "*":
              if gold==int(choice) or gold>int(choice):
                gold-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "14":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              diamond=0
            if choice is not "*":
              if diamond==int(choice) or diamond>int(choice):
                diamond-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
        choice = ''
  if choice == "Dev_var":
    if dev==True:
      if sides == True:
        print 'Vars:'
        print '(1)Dev'
        print '(2)Dev_options'
        print '(3)Self_storage'
        print '(4)Home_storage'
        print '(5)Stanima'
        print '(6)Max_stanima'
        print '\nQuest:'
        print '(1)Quest1'
        print '(2)Quest2'
        print '\nFor quest type quest1 or quest2. That\'s it.'
        print 'Type var then the number. \nUppercase/lowercase does not matter.'
        print 'Ex: Var 1'
        print 'Ex: Quest2'
        choice=raw_input('Do not add the (s):').lower()
        if choice == "var 1":
          if dev==True:
            print 'Currently set to: True'
          if dev==False:
            print 'Currently set to: False'
          choice = raw_input('True or False:').lower()
          if choice=="true":
            dev=True
          if choice=="false":
            dev=False
          choice=''
        if choice == "var 2":
          print 'This is case sensitive.\nHit enter to not change password.'
          print '\nCurrent password:',dev_options
          choice = raw_input('New password:')
          if choice is not "":
            dev_options=choice
          choice=''
        if choice == "var 3":
          print 'Hit enter to not change.'
          print '\nCurrent capacity:',self_storage
          choice=raw_input('New capacity:')
          if choice is not "":
            try:
              self_storage=int(choice)
            except ValueError:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
              move_on=raw_input('Hit enter to leave:')
          choice=''
        if choice == "var 4":
          print 'Hit enter to not change.'
          print '\nCurrent capacity:',home_storage
          choice=raw_input('New capacity:')
          if choice is not "":
            try:
              home_storage=int(choice)
            except ValueError:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
              move_on=raw_input('Hit enter to leave:')
          choice=''
        if choice == "var 5":
          print 'Hit enter to not change.'
          print '\nCurrent setting:',stanima
          choice=raw_input('New setting:')
          if choice is not "":
            try:
              if int(choice)>max_stanima:
                stanima=max_stanima
              if int(choice)<max_stanima:
                stanima=int(choice)
            except ValueError:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
              move_on=raw_input('Hit enter to leave:')
          choice=''
        if choice == "var 6":
          print 'Hit enter to not change.'
          print '\nCurrent setting:',max_stanima
          choice=raw_input('New setting:')
          if choice is not "":
            try:
              max_stanima=int(choice)
            except ValueError:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
              move_on=raw_input('Hit enter to leave:')
          choice=''
        if choice == "quest1":
          if quest1==True:
            print 'Currently set to: True'
          if quest1==False:
            print 'Currently set to: False'
          choice = raw_input("True or False:").lower()
          if choice=="true":
            quest1=True
          if choice=="false":
            quest1=False
          choice=''
        if choice == "quest2":
          if quest2==True:
            print 'Currently set to: True'
          if quest2==False:
            print 'Currently set to: False'
          choice = raw_input("True or False:").lower()
          if choice=="true":
            quest2=True
          if choice=="false":
            quest2=False
          choice=''



