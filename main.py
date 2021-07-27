#!/usr/bin/python
# -*- coding: utf-8 -*-
#Version 0.1.9 Test 1 is out!
import time,os,random,math
dev=False#Default False
path='\\Users\\brobi\\Desktop\\Surnia'
os.chdir(path)
self_int=0
storage_int=0
print 'Main.py file location:',os.path.abspath('main.py')
print 'Save file location:',os.path.abspath('variables.py')
print 'Beta Save file location:',os.path.abspath('vars_beta.py')
if dev==True:
  from vars_beta import *
if dev==False:
  from variables import *
if cheat_amount>25:
  cheat_amount=25 #Max is 25
if dev==True:
  if set_cheatcode==True:
    cheat_wood=True
    cheat_dirt=True
    cheat_water=True
    cheat_rocks=True
    cheat_all=True
  if set_quest==True:
    quest1=True
    quest2=True
    quest3=True
    quest4=True
    quest5=True
    quest6=True
    quest7=True
    quest8=True
    quest9=True
    quest10-True
    quest11=True
    quest12=True
try:
  cheat_code=cheat_code.lower()
  if cheat_code == "wood_you?":
    if cheat_wood_int>0:
      wood+=cheat_amount
  if cheat_code == "i'm_special":
    if cheat_dirt_int>0:
      dirt+=cheat_amount
  if cheat_code == "voodoo_magic":
    if cheat_water_int>0:
      water+=cheat_amount
  if cheat_code == "hello_world!":
    if cheat_rocks_int>0:
      rocks+=cheat_amount
  if cheat_code == "all_of_the_above":
    if cheat_wood_int>0 and cheat_dirt_int>0:
      if cheat_water_int>0 and cheat_rocks_int>0:
        wood+=cheat_amount
        dirt+=cheat_amount
        water+=cheat_amount
        rocks+=cheat_amount
except:
  pass
break_it=False
def loop1(cords,moving_to):
  global current_location, current_surrounding,time,stanima,dev
  fixed1=0
  fixed2=0
  fixed3=0
  if current_location[0]<cords[0]:
    fixed1=cords[0]-current_location[0]
  if current_location[0]>cords[0]:
    fixed1=current_location[0]-cords[0]
  if current_location[1]<cords[1]:
    fixed2=cords[1]-current_location[1]
  if current_location[1]>cords[1]:
    fixed2=current_location[1]-cords[1] #Up to this point is the same for all lakes
  if current_location[2]<cords[2]:
    fixed3=cords[2]-current_location[2]
  if current_location[2]>cords[2]:
    fixed3=current_location[2]-cords[2]
  total_distance=fixed1+fixed2+fixed3
  stanima1=total_distance/3.5
  stanima1=round(stanima1)
  if stanima1<stanima+1 or dev==True:
    print 'Moving to location...'
    time.sleep(1.5)
    print '\nTraveling cords:',fixed1,fixed2,fixed3
    current_surrounding=moving_to
    current_location=cords
    if dev==False:
      stanima-=stanima1
    print 'Total distance traveled:',total_distance,'(meters)'
    print 'Current area:',current_surrounding
    print 'Current cordinates:',current_location
    print 'Stanima:',stanima
  if stanima1+1>stanima and dev==False:
    if max_stanima>stanima1:
      print 'You need to sleep. You are too tired to keep moving.'
  if max_stanima<stanima1+1 and dev==False:
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
def loop4(s,other,numbers,price):
  #s = (True)Shows other stuff and stats
  global self_storage,home_storage,stanima,max_stanima
  global current_surronding,current_location
  side='  ()'
  side1=1
  global axe,pickaxe,shovel
  global wood,rocks,water,dirt,clay,bowl,sticks,coal,iron,gold,diamond,copper,lapiz,zinc,cobalt,mica,manganese
  self_int=0
  self_int+=wood+rocks+water+dirt+clay+bowl+sticks
  self_int+=coal+iron+gold+diamond+copper+lapiz+zinc
  self_int+=cobalt+mica+manganese+axe+pickaxe+shovel
  print 'Minerals:'
  if price==True:
    print '      Item      Price for one'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Wood:',str(wood)+',      Price:',buy_price_wood
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Dirt:',str(dirt)+',      Price:',buy_price_dirt
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Water:',str(water)+',     Price:',buy_price_water
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Rocks:',str(rocks)+',     Price:',buy_price_rocks
    print 'Items:'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Clay:',str(clay)+',      Price:',buy_price_clay
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Bowls:',str(bowl)+',     Price:',buy_price_bowl
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Sticks:',str(sticks)+',    Price:',buy_price_sticks
    print 'Tools:'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Pickaxes:',str(pickaxe)+',   Price:',buy_price_pickaxe
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Shovels:',str(shovel)+',    Price:',buy_price_shovel
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Axes:',str(axe)+',      Price:',buy_price_axe
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print 'Goodies:'
    print side2+'Coal:',str(coal)+',      Price:',buy_price_coal
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Iron:',str(iron)+',      Price:',buy_price_iron
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Gold:',str(gold)+',      Price:',buy_price_gold
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Diamonds:',str(diamond)+',  Price:',buy_price_diamond
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Copper:',str(copper)+',    Price:',buy_price_copper
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Lapiz:',str(lapiz)+',     Price:',buy_price_lapiz
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Zinc:',str(zinc)+',      Price:',buy_price_zinc
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Cobalt:',str(zinc)+',    Price:',buy_price_cobalt
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Mica:',str(mica)+',      Price:',buy_price_mica
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Manganese:',str(mica)+', Price:',buy_price_manganese
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
    print side2+'Coal:',coal,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Iron:',iron,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Gold:',gold,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Diamonds:',diamond,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Copper:',copper,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Lapiz:',lapiz,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Zinc:',zinc,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Cobalt:',cobalt,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Mica:',mica,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Manganese:',manganese,'(lbs)'
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
    print '  Coal:',coal,'(lbs)'
    print '  Iron:',iron,'(lbs)'
    print '  Gold:',gold,'(lbs)'
    print '  Diamonds:',diamond,'(lbs)'
    print '  Copper:',copper,'(lbs)'
    print '  Lapiz:',lapiz,'(lbs)'
    print '  Zinc:',zinc,'(lbs)'
    print '  Cobalt:',cobalt,'(lbs)'
    print '  Mica:',mica,'(lbs)'
    print '  Manganese',manganese,'(lbs)'
  if s==True:
    print 'Storage:'
    print '  Inventory Storage:',self_storage,'(qty of items)'
    print '  Home Storage:',home_storage,'(qty of items)'
    print '  Inventory Capacity:',self_int,'out of',self_storage
    print 'Stats:'
    print '  Stanima:',stanima,'(%)'
    print '  Max Stanima:',max_stanima,'(%)'
    print '  Donations:',donated_money,'(cents)'
    print ''
    print 'Current money:',str(money)+' (cents)'
    print 'Current area:',current_surrounding
    print 'Current cordinates:',current_location
def clear():
  global normal_clear,repeat_amount
  if normal_clear==True:
    os.system('clear')
  if normal_clear==False:
    for i in range(repeat_amount):
      print ''
def dev_promt():
  print 'You must activate Dev_options to use this. This lock will be removed in future updates. Go to vars.py to see how to enable dev_options. It\'s at the bottom.'
def leave(a):
  global go_home,break_it,dev
  hi=True
  if go_home[0]==a:
    hi=False
  if go_home[1]==a:
    hi=False
  if go_home[2]==a:
    hi=False
  if dev==True:
    if hi==False:
      break_it=True
  #leave(choice)
  #if choice == "":
  #  if break_it==True:
  #    break_it=False
  #    something=1
  #    break
def self_int1():
  global self_int
  global wood,rocks,water,dirt,clay,bowl,sticks,coal,iron,gold,diamond,copper,lapiz,zinc,cobalt,mica,manganese
  global axe,pickaxe,shovel
  self_int=0
  self_int+=wood+rocks+water+dirt+clay+bowl+sticks
  self_int+=coal+iron+gold+diamond+copper+lapiz+zinc
  self_int+=cobalt+mica+manganese+axe+pickaxe+shovel
  if dev==True:
    choice=raw_input('System: Do you want to add extras to self_int:')
    if choice in "TruetrueyesYes":
      global silver,silicon,aluminum,bronze,lead
      self_int+=silver+silicon+aluminum+bronze+lead
def storage_int1():
  globals
  storage_int=0
  storage_int+=storage_water+storage_wood+storage_dirt
  storage_int+=storage_rocks+storage_clay+storage_bowl
  storage_int+=storage_sticks+storage_pickaxe+storage_axe
  storage_int+=storage_shovel+storage_copper+storage_lapiz
  storage_int+=storage_coal+storage_iron+storage_gold+storage_diamond
  storage_int+=storage_copper+storage_lapiz+storage_zinc+storage_cobalt
  storage_int+=storage_mica+storage_manganese
def screen_runoff(line_space):
  global run_off
  if run_off==True:
    ch_per_line=7
    p=len(line_space)
    round(p)
    a=int(0)
    b=int(chars_in_line)
    while p>0:
      try:
        #print avalable
        if line_space[a]==" ":
          bg=line_space[a+1:b]
        if line_space[a] is not " ":
          bg=line_space[a:b]
        #print
        print (bg)
        a+=chars_in_line
        b+=chars_in_line
        p-=1
      except IndexError:
        break
#move_on=raw_input('Hit enter to exit :')
p=True
first=True
while p==True:
  if first==False:
    clear()
  if first==True:
    first=False
    print ''
  if version==True:
    screen_runoff('Current Version: 0.1.9 Test 1')
  if dev==True:
    screen_runoff('Dev_options: Enabled')
    if normal_clear==True:
      screen_runoff('Normal_clear: Enabled')
    if normal_clear==False:
      screen_runoff('Normal_clear: Disabled')
  show_exit=True
  screen_runoff('(1)Gather Resources')
  screen_runoff('(2)Change Location')
  screen_runoff('(3)Go Back Home')
  screen_runoff('(4)Crafting Menu')
  screen_runoff('(5)Sleep')
  screen_runoff('(6)Tips')
  screen_runoff('(7)Exersice')
  screen_runoff('(8)Sell')
  screen_runoff('(9)Mining')
  screen_runoff('(10)Quests')
  screen_runoff('(11)Buy')
  screen_runoff('(12)Cheat Codes')
  screen_runoff('(13)Donate')
  screen_runoff('(*)Show Inventory')
  screen_runoff('(@)Settings')
  screen_runoff('\nOthers:')
  screen_runoff(' (save)Save Data')
  screen_runoff(' (bye)Exit')
  screen_runoff(' (updates)Show Patch Notes')
  screen_runoff(' (help)What do I do?')
  if dev==True:
    screen_runoff('\nDev tools:')
    screen_runoff(' Dev_menu()  #Free items')
    screen_runoff(' Dev_var()   #Variables')
    screen_runoff(' Vars_beta() #Loads vars_beta.py')
    screen_runoff('\nTo get help type (help)')
  if dev==False:
    screen_runoff('\n\nTo get help type (help)')
  choice=raw_input('Choose an option or enter code:') #Do not lowercase
  if choice==dev_options:
    use=False
    if dev==False:
      screen_runoff('Dev_options: Enabled')
      dev=True
      use=True
    if use==False:
      if dev==True:
        screen_runoff('Dev_options: Disabled')
        dev=False
    time.sleep(1)
  clear()
  loop2()
  if choice == "help":
    screen_runoff('Enter the items corresponding character to select an item. Characters include but not limited to letters, number and/or symbols.\n')
    move_on=raw_input('Hit enter to exit help:')
  if choice == "1" or choice.lower() == "gather resources":
    something=0
    while something<1:
      loop=False
      warn=False
      loop_count=1
      ah=False#If user uses quick leave the this var will not allow self_int1() to be used.
      if gather_loop==True:
        screen_runoff('(1)Loop')
        screen_runoff('(2)Do not loop')
        if hints==True:
          screen_runoff('\nHint: Loop will repeat this function.')
        choice=raw_input('What do you choose:')
        if choice=="":
          if quick_leave==True:
            show_exit=False
            loop_count=0
            if hints==True:
              clear()
              screen_runoff('Quick exit...')
              time.sleep(1)
              ah=True
        leave(choice)
        if break_it==True:
          break_it=False
          something=1
          break
        if choice in "loop1" and choice is not "":
          try:
            loop_count=raw_input('How many times:')
            leave(loop_count)
            if break_it==True:
              break_it=False
              something=1
              break
            loop_count=int(loop_count)
          except ValueError:
            if error_message==True:
              screen_runoff('System message: ValueError')
              screen_runoff('Reason: A number was not entered.')
        if choice == "loop":
          loop=True
      clear()
      if ah==False:
        self_int1()
      while loop_count>0:
        #for i in range(int(loop_count)):
        if int(self_int)+1>int(self_storage):
          warn=True
          break
        if self_int<self_storage+1:
          #Water + Dirt = Clay
          #Wood = house, water holder, storage
          screen_runoff('(1)Wood')
          screen_runoff('(2)Water')
          screen_runoff('(3)Dirt')
          screen_runoff('(4)Rocks')
          screen_runoff('(5)Sticks')
          screen_runoff('(*)Exit')
          screen_runoff('(os)Clear Text')
          choice=raw_input('What would you like to gather:')
          leave(choice)
          if break_it==True:
            break_it=False
            something=1
            break
          loop2()
          if choice=="":
            if quick_leave==True:
              show_exit=False
              loop_count=0
              if hints==True:
                clear()
                screen_runoff('Quick exit...')
                time.sleep(1)
                ah=True
          if choice == "os":
            clear()
            loop_count+=1
          if choice == "*":
            show_exit=False
            break
          if choice == "1":
            if dev==False:
              if current_surrounding not in dirt_biomes:
                screen_runoff('You must be in the forest to gather sticks.')
            if current_surrounding in dirt_biomes or dev==True:
              if self_storage<self_int+3:
                screen_runoff('Your inventory is full.')
                choice='blah'
              if choice == "1":
                if axe>0:
                  screen_runoff('Gathering wood...')
                  time.sleep(3)
                  wood+=2
                  screen_runoff('Gathered 2 wood')
                  time.sleep(1)
                if axe<1:
                  screen_runoff('You need more axe(s)')
          if choice == "2":
            if dev==False:
              if current_surrounding not in water_biomes:
                screen_runoff('You need to be near a lake or a river to gather water.')
            if current_surrounding in water_biomes or dev==True:
              if self_storage<self_int+2:
                choice='blah'
              if choice == "2":
                screen_runoff('Gathering water...')
                time.sleep(3)
                water+=1
                screen_runoff('Gathered 1 water')
                time.sleep(1)
          if choice == "3":
            if current_surrounding in dirt_biomes or dev==True:
              if self_storage<self_int+2:
                choice='blah'
              if choice == "3":
                if shovel>0:
                  screen_runoff('Gathering dirt...')
                  time.sleep(3)
                  dirt+=1
                  screen_runoff('Gathered 1 dirt')
                  time.sleep(1)
                if shovel<1:
                  screen_runoff('You need more shovel(s)')
            if dev==False:
              if current_surrounding not in dirt_biomes:
                screen_runoff('You must be in the forest to gather dirt.')
          if choice == "4":
            if current_surrounding in clay_biomes or current_surrounding in dirt_biomes or dev==True:
              if self_storage<self_int+2:
                choice = 'blah'
              if choice == "4":
                screen_runoff('Gathering rocks...')
                time.sleep(3)
                rocks+=2
                screen_runoff('Gathered 2 rocks.')
                time.sleep(1)
            if dev==False:
              if current_surrounding not in clay_biomes or dirt_biomes:
                screen_runoff('You must at clay mountian or the forest to gather rocks.')
          if choice == "5":
            if current_surrounding in dirt_biomes or dev==True:
              if self_storage<self_int+1:
                choice="blah"
              if choice == "5":
                screen_runoff('Gathering sticks...')
                time.sleep(3)
                sticks+=4
                screen_runoff('Gathered 4 sticks.')
                time.sleep(1)
            if dev==False:
              if current_surrounding not in dirt_biomes:
                screen_runoff('You must be in the forest to gather sticks.')
        loop_count-=1
      choice=''
      if warn==True:
        screen_runoff('Your inventory is full.')
      something=1
      if show_exit==True or hit_to_exit==True:
        move_on=raw_input('Hit enter to exit Gather Resources:')
  if choice == "2" or choice.lower() == "change location":
    screen_runoff('Current location: '+str(current_surrounding))
    screen_runoff('(1)Lake')
    screen_runoff('(2)River')
    screen_runoff('(3)Clay mountian')
    screen_runoff('(4)Exercise mountian')
    screen_runoff('(5)Desert')
    screen_runoff('(6)Abandoned city')
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
  if choice == "3" or choice.lower() == "go back home":
    loop1(home_location,'home')
    choice = ''
  if choice == "4" or choice.lower() == "crafting menu":
    screen_runoff('(1)Clay     Needs - Dirt: 1, Water: 1')
    screen_runoff('(2)Bowl     Needs - Wood: 2')
    screen_runoff('(3)Sticks   Needs - Wood: 1')
    screen_runoff('(4)Pickaxe  Needs - Sticks: 2, Rocks: 3')
    screen_runoff('(5)Shovel   Needs - Sticks: 2, Rocks: 1')
    screen_runoff('(6)Axe      Needs - Sticks: 2, Rocks: 2')
    choice = raw_input('What would you like to make:')
    if choice=="":
      if quick_leave==True:
        show_exit=False
        if hints==True:
          clear()
          screen_runoff('Quick exit...')
          time.sleep(1)
    loop2()
    if choice == "1":
      if dirt>0:
        if water>0:
          screen_runoff('Making clay...')
          time.sleep(2)
          screen_runoff('Made 1 clay')
          clay+=1
          dirt-=1
          water-=1
          screen_runoff('You have '+str(clay)+' clay')
      if dirt<1:
        screen_runoff('You need more dirt')
        screen_runoff('You have '+str(dirt)+' dirt')
      if water<1:
        screen_runoff('You need more water')
        screen_runoff('You have '+str(water)+' water')
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "2":
      if wood>1:
        screen_runoff('Making a bowl...')
        time.sleep(2)
        screen_runoff('Made 1 bowl')
        bowl+=1
        wood-=2
        screen_runoff('You have '+str(bowl)+' bowl(s)')
      if wood<2:
        screen_runoff('You need more wood')
        screen_runoff('You have '+str(wood)+' wood')
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "3":
      if wood>0:
        screen_runoff('Making sticks...')
        time.sleep(2)
        screen_runoff('Made 4 sticks.')
        sticks+=4
        wood-=1
        screen_runoff('You have '+str(sticks)+' stick(s)')
      if wood<1:
        screen_runoff('You need more wood')
        screen_runoff('You have '+str(wood)+' wood')
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "4":
      if sticks>1:
        if rocks>2:
          screen_runoff('Making a pickaxe...')
          time.sleep(2)
          screen_runoff('Made 1 pickaxe.')
          pickaxe+=1
          sticks-=2
          rocks-=3
          screen_runoff('You have '+str(pickaxe)+' pickaxe(s)')
      if sticks<2:
        screen_runoff('You need more stick(s).')
        screen_runoff('You have '+str(sticks)+' stick(s)')
      if rocks<3:
        screen_runoff('You need more rock(s)')
        screen_runoff('You have '+str(rocks)+' rock(s)')
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "5":
      if sticks>1:
        if rocks>0:
          screen_runoff('Making a shovel...')
          time.sleep(2)
          screen_runoff('Made 1 shovel.')
          shovel+=1
          sticks-=2
          rocks-=1
          screen_runoff('You have '+str(shovel)+' shovel(s)')
      if sticks<2:
        screen_runoff('You need more stick(s).')
        screen_runoff('You have '+str(sticks)+' stick(s)')
      if rocks<1:
        screen_runoff('You need more rock(s)')
        screen_runoff('You have '+str(rocks)+' rock(s)')
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "6":
      if sticks>1:
        if rocks>1:
          screen_runoff('Making a axe...')
          time.sleep(2)
          screen_runoff('Made 1 axe.')
          axe+=1
          sticks-=2
          rocks-=2
          screen_runoff('You have '+str(axe)+' axe(s)')
      if sticks<2:
        screen_runoff('You need more stick(s).')
        screen_runoff('You have '+str(sticks)+' stick(s)')
      if rocks<2:
        screen_runoff('You need more rock(s)')
        screen_runoff('You have '+str(rocks)+' rock(s)')
      move_on=raw_input('Hit enter to exit crafting:')
    choice = ''
  if choice == "5" or choice.lower() == "sleep":
    if dev==False:
      if stanima+21>max_stanima:
        print 'You are not tired.'
        print 'Stanima:',stanima,'out of',max_stanima
        move_on=raw_input('Hit enter to exit sleep:')
      if stanima<max_stanima-20:
        print 'Stanima before:',stanima,'out of',max_stanima
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
        print 'Stanima after:',stanima,'out of',max_stanima
        if hints==True:
          print 'Hint: Stanima Before and After sleep'
        move_on=raw_input('\nHit enter to exit sleep:')
    if dev==True:
      stanima=max_stanima
      print 'Stanima reset to max.'
      time.sleep(1)
    choice = ''
  if choice == "6" or choice.lower() == "tips":
    repeat=1
    if hints_loop==True:
      print '(1)Loop'
      print '(2)Do not loop'
      if hints==True:
        print '\nHint: Loop will repeat this function.'
      choice=raw_input('What do you choose:')
      if choice in "loop1" and choice is not "":
        choice=raw_input('How many times:')
        try:
          repeat=int(choice)
        except ValueError:
          if error_message==True:
            print 'System message: ValueError'
            print 'Reason: A number was not entered.'
    for i in range(repeat):
      print 'Welcome to Brandon\'s game.'
      print 'For info on each item. Type the items corresponding number.'
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
      print '(12)Cheat Codes'
      print '(13)Donate'
      print '(14)Show inventory'
      print '(15)Settings'
      print '(16)Save'
      if dev==False:
        print '\nTo store store items at home. Do this. \n1. Make sure you are at home\n2. Open inventory\n3. Instead of hiting enter to exit type (storage) to store items.\nHint: You can also grab items back from doing this.'
      choice=raw_input('Which item:')
      clear()
      if choice=="":
        if quick_leave==True:
          show_exit=False
          if hints==True:
            print 'Quick exit...'
            time.sleep(1)
            break
            #if show_exit==True or hit_to_exit==True:
      if choice == "1":
        print 'This is where you collect resources. You can get these items: Wood, Water, Dirt, Rocks, and sticks.'
        if hints==True:
          print 'Hint: Check change location on tips for more info on gathering.'
          print 'Hint: Quick exit doesn\'t work when in the gathering menu. Only on the loop menu in this function. To exit use the exit command.'
      if choice == "2":
        print 'This is where you move to different areas of the world. Each place allows you to get different items on (gather resources).'
        print 'Wood: Forest'
        print 'Water: Lake, River'
        print 'Dirt: Forest'
        print 'Rocks: Clay mountian'
        print 'Sticks: Forest'
      if choice == "3":
        print 'This will bring you back home.'
      if choice == "4":
        print 'This is where you craft items.'
      if choice == "5":
        print 'When your stanima is low, go here to sleep and regain your energy. Maximum Stanima can increase by exercising.'
      if choice == "6":
        print 'Well, your already here. I bet you can guess what this is.'
        if hints==True:
          print 'Hint: Hints setting does nothing on this page. Just a heads up. It\'s kinda needed here.'
      if choice == "7":
        print 'When your stanima doesn\'t go as high as you would like you can exercise to increase you Maximum stanima.'
      if choice == "8":
        print 'Have things you don\'t want? Then sell them.'
      if choice == "9":
        print 'Grab minerals and sell them for a profit. This does require a pickaxe.'
      if choice == "10":
        print 'Complete quests for a reward. Rewards are usually money. Not always.'
      if choice == "11":
        print 'Don\'t have things you want? Then buy them.'
      if choice == "12":
        print 'Nothing is free in the world not even in game. Cheat Codes gives you free stuff but it may cost money to buy uses on them. You will have to unlock cheat codes by donating.'
      if choice == "13":
        print 'Giving to others will lead to others giving to you. To see what you can earn open donate then type rewards.'
      if choice == "14":
        print 'Shows what you currently have on you. To access storage, type (storage) instead of hitting enter to exit.'
      if choice == "15":
        print 'Change the game up if you want to. Change some settings to your liking. Go ahead, don\'t be shy!'
      if choice == "16":
        print 'Never loose your progress in the game when you save it. Let\'s go!'
        if hints==True:
          print 'Hint: If you want to start over go to settings and toggle (New Save) to Enabled. The save the game. A new save file will be overwriten.'
      if show_exit==True or hit_to_exit==True:
        move_on=raw_input('Hit enter to exit tips:')
      choice = ''
  if choice == "7" or choice.lower() == "exersice":
    if current_surrounding=="exercise mountian #1" or dev==True:
      if stanima<30 and dev==False:
        print 'You are to tired to dance your heart away.'
      if stanima>29 or dev==True:
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
        print 'All credit goes to Rick for these lyrics.'
        time.sleep(1.5)
        print '\nStanima decreased by 30'
        print 'Max_Stanima increased by 15'
        stanima-=30
        max_stanima+=15
        print 'Recommended to go to sleep.'
    if current_surrounding is not "exercise mountian #1":
      if dev==False:
        print 'You need to travel to exersice mountian to use this function.'
    move_on=raw_input('Hit enter to exit exercise:')
  if choice == "8" or choice.lower() == "sell":
    clear()
    loop4(s=False,other=False,numbers=True,price=False)
    choice=raw_input('What would you like to sell:')
    if choice=="":
      if quick_leave==True:
        show_exit=False
        if hints==True:
          clear()
          print 'Quick exit...'
          time.sleep(1)
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
            print 'Cents:',money
            print 'Wood:',wood
          except ValueError:
            if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Dirt:',dirt
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Water:',water
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Rock(s):',rocks
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Clay:',clay
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
      choice=''
    if choice=="6":
      if bowl<1:
        print 'You don\'t have any to sell'
      if bowl>0:
        choice=raw_input('How many:')
        try:
          if bowl==int(choice) or bowl>int(choice):
            money+=int(choice)*price_bowl
            bowl-=int(choice)
            print 'Current holdings:'
            print 'Cents:',money
            print 'Bowl(s):',bowl
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Stick(s):',sticks
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Pickaxe(s):',pickaxe
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Shovel(s):',shovel
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Axe(s):',axe
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Coal:',coal
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Iron:',iron
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Gold:',gold
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
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
            print 'Cents:',money
            print 'Diamond:',diamond
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
      choice=''
    if choice=="15":
      if copper<1:
        print 'You don\'t have any to sell'
      if copper>0:
        choice=raw_input('How many:')
        try:
          if copper==int(choice) or copper>int(choice):
            money+=int(choice)*price_copper
            copper-=int(choice)
            print 'Current holdings:'
            print 'Cents:',money
            print 'Copper:',copper
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
      choice=''
    if choice=="16":
      if lapiz<1:
        print 'You don\'t have any to sell'
      if lapiz>0:
        choice=raw_input('How many:')
        try:
          if lapiz==int(choice) or lapiz>int(choice):
            money+=int(choice)*price_lapiz
            lapiz-=int(choice)
            print 'Current holdings:'
            print 'Cents:',money
            print 'Lapiz:',lapiz
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
      choice=''
    if choice=="17":
      if zinc<1:
        print 'You don\'t have any to sell'
      if zinc>0:
        choice=raw_input('How many:')
        try:
          if zinc==int(choice) or zinc>int(choice):
            money+=int(choice)*price_zinc
            zinc-=int(choice)
            print 'Current holdings:'
            print 'Cents:',money
            print 'Zinc:',zinc
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
      choice=''
    if choice=="18":
      if cobalt<1:
        print 'You don\'t have any to sell'
      if cobalt>0:
        choice=raw_input('How many:')
        try:
          if cobalt==int(choice) or cobalt>int(choice):
            money+=int(choice)*price_cobalt
            cobalt-=int(choice)
            print 'Current holdings:'
            print 'Cents:',money
            print 'Cobalt:',cobalt
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
      choice=''
    if choice=="19":
      if mica<1:
        print 'You don\'t have any to sell'
      if mica>0:
        choice=raw_input('How many:')
        try:
          if mica==int(choice) or mica>int(choice):
            money+=int(choice)*price_mica
            mica-=int(choice)
            print 'Current holdings:'
            print 'Cents:',money
            print 'Mica:',mica
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
      choice=''
    if choice=="20":
      if manganese<1:
        print 'You don\'t have any to sell'
      if manganese>0:
        choice=raw_input('How many:')
        try:
          if manganese==int(choice) or manganese>int(choice):
            money+=int(choice)*price_manganese
            manganese-=int(choice)
            print 'Current holdings:'
            print 'Cents:',money
            print 'Manganese:',manganese
        except ValueError:
          if error_message==True:
              print 'System message: ValueError'
              print 'Reason: A number was not entered.'
      choice=''
    if show_exit==True or hit_to_exit==True:
      move_on=raw_input('Hit enter to exit sell:')
  if choice == "9" or choice.lower() == "mining":
    self_int1()
    if dev==True:
      print 'Inventory capacity:',self_int,'out of',self_storage
    if pickaxe<1 and dev==False:
      print 'You need at least one pickaxe to mine.'
      time.sleep(1.5)
    if pickaxe>0 or dev==True:
      if self_storage>self_int+1 or dev==True:
        if stanima>24 or dev==True:
          print 'Going into the mines...'
          time.sleep(2.5)
          clear()
          print '(1)Coal       Est: 2 sec'
          print '(2)Iron       Est: 5 sec'
          print '(3)Gold       Est: 9 sec'
          print '(4)Diamond    Est: 15 secs'
          print '(5)Copper     Est: 10 sec'
          print '(6)Lapiz      Est: 17 sec'
          print '(7)Zinc       Est: 23 sec'
          print '(8)Cobalt     Est: 20 sec'
          choice = raw_input('What would you like to mine:')
          if choice=="":
            if quick_leave==True:
              show_exit=False
              if hints==True:
                clear()
                print 'Quick exit...'
                time.sleep(1)
          if choice == "1":
            print 'Going to find some coal...'
            time.sleep(1)
            print 'Found some coal. \nMining the coal...'
            print 'Est: 2s'
            time.sleep(2)
            coal+=1
            pickaxe-=1
            print '\nYou got 1 coal! But lost 1 pickaxe :('
          if choice == "2":
            print 'Going to find some iron...'
            time.sleep(1)
            print 'Found some iron. \nMining the iron...'
            print 'Est: 5s'
            time.sleep(5)
            iron+=1
            pickaxe-=1
            print '\nYou got 1 iron! But lost 1 pickaxe :('
          if choice == "3":
            print 'Going to find some gold...'
            time.sleep(1)
            print 'Found some gold. \nMining the gold...'
            print 'Est: 9s'
            time.sleep(9)
            gold+=1
            pickaxe-=1
            print '\nYou got 1 gold! But lost 1 pickaxe :('
          if choice == "4":
            print 'Going to find some diamonds...'
            time.sleep(1)
            print 'Found some diamonds. \nMining the diamonds...'
            print 'Est: 15s'
            time.sleep(15)
            diamond+=1
            pickaxe-=1
            print '\nYou got 1 diamond! But lost 1 pickaxe :('
          if choice == "5":
            print 'Going to find some copper...'
            time.sleep(1)
            print 'Found some copper. \nMining the copper...'
            print 'Est: 10s'
            time.sleep(10)
            copper+=1
            pickaxe-=1
            print '\nYou got 1 copper! But lost 1 pickaxe :('
          if choice == "6":
            print 'Going to find some lapiz...'
            time.sleep(1)
            print 'Found some lapiz. \nMining the lapiz...'
            print 'Est: 17s'
            time.sleep(17)
            lapiz+=1
            pickaxe-=1
            print '\nYou got 1 lapiz! But lost 1 pickaxe :('
          if choice == "7":
            print 'Going to find some zinc...'
            time.sleep(1)
            print 'Found some zinc. \nMining the zinc...'
            print 'Est: 23s'
            time.sleep(23)
            zinc+=2
            pickaxe-=1
            print '\nYou got 2 zinc! But lost 1 pickaxe :('
          if choice == "8":
            print 'Going to find some cobalt...'
            time.sleep(1)
            print 'Found some cobalt. \nMining the cobalt...'
            print 'Est: 20s'
            time.sleep(20)
            cobalt+=2
            pickaxe-=1
            print '\nYou got 2 cobalt! But lost 1 pickaxe :('
          stanima-=25
        if stanima<21 and dev==False:
          print 'You need to go to sleep.'
        print 'Stanima:',stanima,'out of',max_stanima
        print 'Pickaxe(s):',pickaxe
      if self_storage+1<self_int and dev==False:
        print 'Your storage is full. Empty your storage in show: inventory. Then type: storage'
        time.sleep(1.5)
    if show_exit==True or hit_to_exit==True:
      move_on=raw_input('Hit enter to exit mining:')
    choice = ''
  if choice == "10" or choice.lower() == "quests" or choice.lower() == "quest":
    hi=True
    if sticks<5:
      print 'Sorry, but you do not. Come back when you do.'
    if quest1==False:
      hi=False
      print 'Your first quest is to get me: 5 sticks'
      print 'Reward: 25 Cents'
      choice=raw_input('Do you have 5 sticks:').lower()
      if choice == "yes":
        print 'Checking...'
        time.sleep(1)
        if sticks>4:
          print 'Congrats you finished your first quest!'
          print 'You got 25 Cents.'
          sticks-=5
          money+=25
          quest1=True
      if choice == "no":
        print 'Okay then.'
    if quest2==False:
      if hi==True:
        hi=False
        print 'Your second quest is to get me: 2 pickaxe(s)'
        print 'Reward: 32 Cents'
        choice=raw_input('Do you have 2 pickaxe(s)').lower()
        if choice == "yes":
          print 'Checking...'
          time.sleep(1)
          if pickaxe<2:
            print 'Sorry, but you do not. Come back when you do.'
          if pickaxe>1:
            print 'Congrats you finished your second quest!'
            print 'You got 32 Cents.'
            pickaxe-=2
            money+=32
            quest2=True
    if quest3==False:
      if hi==True:
        hi=False
        print 'Your third quest is to get me: 5 wood'
        print 'Reward: 30 Cents'
        choice=raw_input('Do you have 5 wood:').lower()
        if choice == "yes":
          print "Checking..."
          time.sleep(1)
          if wood<5:
            print 'Sorry, but you do not. Come back when you do.'
          if wood>4:
            print 'Congrats you finished your third quest'
            print 'You got 30 Cents.'
            wood-=5
            money+=30
            quest3=True
    if quest4==False:
      if hi==True:
        hi=False
        print 'Your 4th quest is to get me: 15 sticks'
        print 'Reward: 45 Cents'
        choice=raw_input('Do you have 15 sticks:').lower()
        if choice == "yes":
          print 'Checking...'
          time.sleep(1)
          if sticks<15:
            print 'Sorry, but you do not. Come back when you do.'
          if sticks>14:
            print 'Congrats you finished your 4th quest'
            print 'You got 45 Cents'
            sticks-=15
            money+=45
            quest4=True
    if quest5==False:
      if hi==True:
        hi=False
        print 'Your 5th quest is to get me: 4 bowls'
        print 'Reward: 35 Cents'
        choice=raw_input('Do you have 4 bowls:').lower()
        if choice == "yes":
          print 'Checking...'
          time.sleep(1)
          if bowl<4:
            print 'Sorry, but you do not. Come back when you do.'
          if bowl>3:
            print 'Congrats you finished your 5th quest'
            print 'You got 45 Cents'
            bowl-=4
            money+=35
            quest5=True
    if quest6==False:
      if hi==True:
        hi=False
        print 'Your 6th quest is to get me: 5 clay'
        print 'Reward: 30 Cents'
        choice=raw_input('Do you have 5 clay:').lower()
        if choice == "yes":
          print 'Checking...'
          time.sleep(1)
          if clay<5:
            print 'Sorry, but you do not. Come back when you do.'
          if clay>4:
            print 'Congrats you finished your 6th quest'
            print 'You got 30 Cents'
            clay-=5
            money+=30
            quest6=True
    if quest7==False:
      if hi==True:
        hi=False
        print 'Your 7th quest is to get me: 2 copper'
        print 'Reward: 25 Cents'
        choice=raw_input('Do you have 2 copper:').lower()
        if choice == "yes":
          print 'Checking...'
          time.sleep(1)
          if copper<2:
            print 'Sorry, but you do not. Come back when you do.'
          if copper>1:
            print 'Congrats you finished your 7th quest'
            print 'You got 25 Cents'
            copper-=2
            money+=25
            quest7=True
    if quest8==False:
      if hi==True:
        hi=False
        print 'Your 8th quest is to get me: 2 lapiz'
        print 'Reward: 30 Cents'
        choice=raw_input('Do you have 2 lapiz:').lower()
        if choice == "yes":
          print 'Checking...'
          time.sleep(1)
          if lapiz<2:
            print 'Sorry, but you do not. Come back when you do.'
          if lapiz>1:
            print 'Congrats you finished your 8th quest'
            print 'You got 30 Cents'
            lapiz-=2
            money+=30
            quest8=True
    if quest9==False:
      if hi==True:
        hi=False
        print 'Your 9th quest is to get me: 3 Gold'
        print 'Reward: 33 Cents'
        choice=raw_input('Do you have 3 Gold:').lower()
        if choice == "yes":
          print 'Checking...'
          time.sleep(1)
          if gold<3:
            print 'Sorry, but you do not. Come back when you do.'
          if gold>2:
            print 'Congrats you finished your 9th quest'
            print 'You got 33 Cents'
            gold-=3
            money+=33
            quest9=True
    if quest10==False:
      if hi==True:
        hi=False
        print 'Your 10th quest is to get me: 5 Coal'
        print 'Reward: 15 Cents'
        choice=raw_input('Do you have 5 coal:').lower()
        if choice == "yes":
          print 'Checking...'
          time.sleep(1)
          if coal<5:
            print 'Sorry, but you do not. Come back when you do.'
          if coal>4:
            print 'Congrats you finished your 10th quest'
            print 'You got 15 Cents'
            coal-=5
            money+=15
            quest10=True
    if quest11==False:
      if hi==True:
        hi=False
        print 'Your 11th quest is to get me: 6 Wood'
        print 'Reward: 22 Cents'
        choice=raw_input('Do you have 6 wood:').lower()
        if choice == "yes":
          print 'Checking...'
          time.sleep(1)
          if wood<6:
            print 'Sorry, but you do not. Come back when you do.'
          if wood>5:
            print 'Congrats you finished your 11th quest'
            print 'You got 22 Cents'
            wood-=6
            money+=22
            quest11=True
    if quest12==False:
      if hi==True:
        hi=False
        print 'Your 12th quest is to get me: 1 Axe'
        print 'Reward: 10 Cents'
        choice=raw_input('Do you have 1 axe:').lower()
        if choice == "yes":
          print 'Checking...'
          time.sleep(1)
          if axe<1:
            print 'Sorry, but you do not. Come back when you do.'
          if axe>0:
            print 'Congrats you finished your 12th quest'
            print 'You got 10 Cents'
            axe-=1
            money+=10
            quest12=True
    if quest1==True and quest2==True:
      if quest3==True and quest4==True:
        if quest5==True and quest6==True:
          if quest7==True and quest8==True:
            if quest9==True and quest10==True:
              if quest11==True and quest12==True:
                print 'You have completed all of the quests.'
    move_on=raw_input('Hit enter to exit quest:')
    choice=''
  if choice == "11" or choice.lower() == "buy":
    self_int1()
    if self_int<self_storage+1:
      loop4(s=False,other=False,numbers=False,price=True)
      print 'Storage capacity:'
      print '  (21)More inventory storage'
      print '  (22)More home storage'
      print '\nYour money:',money,'cents'
      choice=raw_input('What would you like to buy:')
      if choice=="":
        if quick_leave==True:
          show_exit=False
          if hints==True:
            clear()
            print 'Quick exit...'
            time.sleep(1)
      if choice == "1":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_wood*int(choice):
            money-=buy_price_wood*int(choice)
            wood+=int(choice)
            print 'You now have:',wood
          if money<buy_price_wood*int(choice):
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'wood'
            print 'Total cost:',buy_price_wood*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'dirt'
            print 'Total cost:',buy_price_dirt*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'water'
            print 'Total cost:',buy_price_water*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'rocks'
            print 'Total cost:',buy_price_rocks*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'clay'
            print 'Total cost:',buy_price_clay*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'bowl'
            print 'Total cost:',buy_price_bowl*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'sticks'
            print 'Total cost:',buy_price_sticks*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'pickaxe'
            print 'Total cost:',buy_price_pickaxe*int(choice),'Cents'
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'shovel'
            print 'Total cost:',buy_price_shovel*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'axe'
            print 'Total cost:',buy_price_axe*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'coal'
            print 'Total cost:',buy_price_coal*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'iron'
            print 'Total cost:',buy_price_iron*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'gold'
            print 'Total cost:',buy_price_gold*int(choice),'Cents'
        except ValueError:
          if error_message==True:
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
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'diamond'
            print 'Total cost:',buy_price_diamond*int(choice),'Cents'
        except ValueError:
          if error_message==True:
            print 'System message: ValueError'
            print 'Reason: A number was not entered.'
      if choice == "15":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_copper*int(choice):
            money-=buy_price_copper*int(choice)
            copper+=int(choice)
            print 'You now have:',copper
          if money<buy_price_copper*int(choice):
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'copper'
            print 'Total cost:',buy_price_copper*int(choice),'Cents'
        except ValueError:
          if error_message==True:
            print 'System message: ValueError'
            print 'Reason: A number was not entered.'
      if choice == "16":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_lapiz*int(choice):
            money-=buy_price_lapiz*int(choice)
            lapiz+=int(choice)
            print 'You now have:',lapiz
          if money<buy_price_lapiz*int(choice):
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'lapiz'
            print 'Total cost:',buy_price_lapiz*int(choice),'Cents'
        except ValueError:
          if error_message==True:
            print 'System message: ValueError'
            print 'Reason: A number was not entered.'
      if choice == "17":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_zinc*int(choice):
            money-=buy_price_zinc*int(choice)
            zinc+=int(choice)
            print 'You now have:',zinc
          if money<buy_price_zinc*int(choice):
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'zinc'
            print 'Total cost:',buy_price_zinc*int(choice),'Cents'
        except ValueError:
          if error_message==True:
            print 'System message: ValueError'
            print 'Reason: A number was not entered.'
      if choice == "18":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_cobalt*int(choice):
            money-=buy_price_cobalt*int(choice)
            cobalt+=int(choice)
            print 'You now have:',cobalt
          if money<buy_price_cobalt*int(choice):
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'cobalt'
            print 'Total cost:',buy_price_cobalt*int(choice),'Cents'
        except ValueError:
          if error_message==True:
            print 'System message: ValueError'
            print 'Reason: A number was not entered.'
      if choice == "19":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_mica*int(choice):
            money-=buy_price_mica*int(choice)
            mica+=int(choice)
            print 'You now have:',mica
          if money<buy_price_mica*int(choice):
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'mica'
            print 'Total cost:',buy_price_mica*int(choice),'Cents'
        except ValueError:
          if error_message==True:
            print 'System message: ValueError'
            print 'Reason: A number was not entered.'
      if choice == "20":
        choice = raw_input('How many:')
        clear()
        try:
          if money+1>buy_price_manganese*int(choice):
            money-=buy_price_manganese*int(choice)
            manganese+=int(choice)
            print 'You now have:',manganese
          if money<buy_price_manganese*int(choice):
            print 'You don\'t have enough Cents'
            print 'Total asked:',choice,'manganese'
            print 'Total cost:',buy_price_manganese*int(choice),'Cents'
        except ValueError:
          if error_message==True:
            print 'System message: ValueError'
            print 'Reason: A number was not entered.'
      if choice == "21":
        print 'Price: 1 item = 3 Cents'
        try:
          choice = raw_input('How much more storage:')
          if int(choice)*3>money:
            print 'You don\'t have enough Cents'
          if int(choice)*3<money+1:
            self_storage+=int(choice)
            money-=int(choice)*3
            print 'Inventory Storage:',self_storage,'(qty of items)'
        except ValueError:
          if error_message==True:
            print 'System message: ValueError'
            print 'Reason: A number was not entered.'
      if choice == "22":
        print 'Price: 1 item = 5 Cents'
        try:
          choice = raw_input('How much more storage:')
          if int(choice)*5>money:
            print 'You don\'t have enough Cents'
          if int(choice)*5<money+1:
            home_storage+=int(choice)
            money-=int(choice)*5
            print 'Home Storage:',home_storage,'(qty of items)'
        except ValueError:
          if error_message==True:
            print 'System message: ValueError'
            print 'Reason: A number was not entered.'
      choice=''
    if self_int+1>self_storage:
      print 'Your inventory is at capacity.'
    if show_exit==True or hit_to_exit==True:
      move_on=raw_input('Hit enter to exit buy:')
  if choice == "12" or choice.lower() == "cheat codes":
    print 'Here are cheat code you can buy. Each can be used 2 times. You can buy as many as you want!'
    print '(1)Wood cheat code:  30 cents'
    print '(1)Dirt cheat code:  15 cents'
    print '(3)Water cheat code: 15 cents'
    print '(4)Rocks cheat code: 15 cents'
    print '(5)All in one cheat code: 65 cents'
    print '(*)Use cheat code\n'
    choice=raw_input('Which item:')
    print
    if choice=="":
      if quick_leave==True:
        show_exit=False
        if hints==True:
          clear()
          print 'Quick exit...'
          time.sleep(1)
    if choice=="1":
      if cheat_wood==False and dev==False:
        print 'Sorry you don\'t have this unlocked.'
      if cheat_wood==True or dev==True:
        move_on=money#Setting a temporary var
        if money<30 and dev==False:
          print 'You don\'t have enough cents.'
        if money>29 or dev==True:
          print 'Cents before purchase:',move_on
          money-=30
          print 'Cents after purchase:',money
          cheat_wood_int+=2
    if choice=="2":
      if cheat_dirt==False and dev==False:
        print 'Sorry you don\'t have this unlocked.'
      if cheat_dirt==True or dev==True:
        move_on=money#Setting a temporary var
        if money<15 and dev==False:
          print 'You don\'t have enough cents.'
        if money>14 or dev==True:
          print 'Cents before purchase:',move_on
          money-=15
          print 'Cents after purchase:',money
          cheat_dirt_int+=2
    if choice=="3":
      if cheat_water==False and dev==False:
        print 'Sorry you don\'t have this unlocked.'
      if cheat_water==True or dev==True:
        move_on=money#Setting a temporary var
        if money<15 and dev==False:
          print 'You don\'t have enough cents.'
        if money>14 or dev==True:
          print 'Cents before purchase:',move_on
          money-=15
          print 'Cents after purchase:',money
          cheat_water_int+=2
    if choice=="4":
      if cheat_rocks==False and dev==False:
        print 'Sorry you don\'t have this unlocked.'
      if cheat_rocks==True or dev==True:
        move_on=money#Setting a temporary var
        if money<15 and dev==False:
          print 'You don\'t have enough cents.'
        if money>14 or dev==True:
          print 'Cents before purchase:',move_on
          money-=15
          print 'Cents after purchase:',money
          cheat_rocks_int+=2
    if choice=="5":
      if cheat_all==False and dev==False:
        print 'Sorry you don\'t have this unlocked.'
      if cheat_all==True or dev==True:
        move_on=money#Setting a temporary var
        if money<65 and dev==False:
          print 'You don\'t have enough cents.'
        if money>64 or dev==True:
          print 'Cents before purchase:',move_on
          money-=65
          print 'Cents after purchase:',money
          cheat_all_int+=2
    if choice=="*":
      print 'Amount given for cheat code:',cheat_amount,'items'
      cheat_code=raw_input('Cheat code:')
      if cheat_code == "wood_you?":
        if cheat_wood==False and dev==False:
          print 'Sorry you don\'t have this unlocked.'
        if cheat_wood==True or dev==True:
          if cheat_wood_int>0:
            wood+=cheat_amount
            cheat_wood_int-=1
            print 'Cheat code applied.'
          else:
            print 'You ran out of uses on this cheat code.'
      elif cheat_code == "i'm_special":
        if cheat_dirt==False and dev==False:
          print 'Sorry you don\'t have this unlocked.'
        if cheat_dirt==True or dev==True:
          if cheat_dirt_int>0:
            dirt+=cheat_amount
            cheat_dirt_int-=1
            print 'Cheat code applied.'
          else:
            print 'You ran out of uses on this cheat code.'
      elif cheat_code == "voodoo_magic":
        if cheat_water==False and dev==False:
          print 'Sorry you don\'t have this unlocked.'
        if cheat_water==True or dev==True:
          if cheat_water_int>0:
            water+=cheat_amount
            cheat_water_int-=1
            print 'Cheat code applied.'
          else:
            print 'You ran out of uses on this cheat code.'
      elif cheat_code == "hello_world!":
        if cheat_rocks==False and dev==False:
          print 'Sorry you don\'t have this unlocked.'
        if cheat_rocks==True or dev==True:
          if cheat_rocks_int>0:
            rocks+=cheat_amount
            cheat_rocks_int-=1
            print 'Cheat code applied.'
          else:
            print 'You ran out of uses on this cheat code.'
      elif cheat_code == "all_of_the_above":
        if cheat_all==False and dev==False:
          print 'Sorry you don\'t have this unlocked.'
        if cheat_all==True or dev==True:
          if cheat_all_int<1:
            print '\nCheat code not applied.'
          if cheat_all_int>0 or dev==True:
            cheat_all_int-=1
            wood+=cheat_amount
            dirt+=cheat_amount
            water+=cheat_amount
            rocks+=cheat_amount
            print 'Cheat code applied.'
      else:
        print 'Incorrect cheat code.'
    choice=''
    move_on=''#Clearing temporary var
    if hints==True:
      print 'Hint: To see cheat codes go to inventory the type cheats.'
    if show_exit==True or hit_to_exit==True:
      move_on=raw_input('Hit enter to exit cheat codes:')
  if choice == "13" or choice.lower() == "donate":
    print 'To see reward list: rewards'
    print 'To donate: donate'
    print 'To claim rewards: claim'
    choice=raw_input('Which one:')
    if choice=="":
      if quick_leave==True:
        show_exit=False
        if hints==True:
          clear()
          print 'Quick exit...'
          time.sleep(1)
    if choice == "claim":
      hi=True
      clear()
      if donated_money>14:
        if donated_tf[0]==0:
          donated_tf[0]=1
          print 'Reward: 5 cobalt'
          cobalt+=5
          hi=False
      if donated_money>29:
        if donated_tf[1]==0:
          donated_tf[1]=1
          print 'Reward: 3 pickaxe(s)'
          pickaxe+=3
          hi=False
      if donated_money>44:
        if donated_tf[2]==0:
          donated_tf[2]=1
          print 'Reward: 3 zinc'
          zinc+=6
          hi=False
      if donated_money>59:
        if donated_tf[3]==0:
          donated_tf[3]=1
          print 'Reward: 3 pickaxe(s)'
          pickaxe+=3
          hi=False
      if donated_money>74:
        if donated_tf[4]==0:
          donated_tf[4]=1
          print 'Reward: 4 diamond(s)'
          diamond+=4
          hi=False
      if donated_money>89:
        if donated_tf[5]==0:
          donated_tf[5]=1
          print 'Reward: 2 pickaxe(s)'
          pickaxe+=2
          hi=False
      if donated_money>104:
        if donated_tf[6]==0:
          donated_tf[6]=1
          print 'Reward: First Cheat Unlocked'
          cheat_wood=True
          hi=False
      if donated_money>119:
        if donated_tf[7]==0:
          donated_tf[7]=1
          print 'Reward: Second Cheat Unlocked'
          cheat_dirt=True
          hi=False
      if donated_money>134:
        if donated_tf[8]==0:
          donated_tf[8]=1
          print 'Reward: Third Cheat Unlocked'
          cheat_water=True
          hi=False
      if donated_money>149:
        if donated_tf[9]==0:
          donated_tf[9]=1
          print 'Reward: Fourth Cheat Unlocked'
          cheat_rocks=True
          hi=False
      if donated_money>164:
        if donated_tf[10]==0:
          donated_tf[10]=1
          print 'Reward: Fifth Cheat Unlocked'
          cheat_all=True
          hi=False
      if hi==True:
        print 'Nothing to claim.'
    if choice == "rewards" or choice == "reward":
      clear()
      print 'Donated = Lifetime donations\n'
      print 'Donated:      Reward:'
      print '15 cents      5 cobalt'
      print '30 cents      3 pickaxe(s)'
      print '45 cents      6 zinc'
      print '60 cents      3 pickaxe(s)'
      print '75 cents      4 diamond(s)'
      print '90 cents      2 pickaxe(s)'
      print '105 cents     First Cheat'
      print '120 cents     Second Cheat'
      print '135 cents     Third Cheat'
      print '150 cents     Fourth Cheat'
      print '165 cents     Fifth Cheat'
    if choice == "donate":
      clear()
      choice=raw_input('How much to donate:')
      try:
        if int(choice)<money+1:
          print 'Sorry your card was declined'
        if int(choice)+1>money:
          money-=int(choice)
          donated_money+=int(choice)
          print 'Money donated:',int(choice)
          print 'Lifetime donations:',donated_money
      except ValueError:
        if error_message==True:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
    choice=''
    if show_exit==True or hit_to_exit==True:
      move_on=raw_input('Hit enter to exit donate:')
  if choice in exit_pos:
    print 'Goodbye.'
    p=False
  if choice == "*" or choice.lower() == "inventory":
    loop4(s=True,other=True,numbers=False,price=False)
    print '\nOptions: (storage), (leave) or (cheats)'
    print '         (quests)'
    #clay,bowl,storage
    move_on=raw_input('Hit enter to exit bag:').lower()
    if move_on=="":
      if quick_leave==True:
        show_exit=False
        if hints==True:
          clear()
          print 'Quick exit...'
          time.sleep(1)
    if move_on=="leave":
      pass
    if move_on=="quests":
      count=0
      if quest1==True:
        count+=1
      if quest2==True:
        count+=1
      if quest3==True:
        count+=1
      if quest4==True:
        count+=1
      if quest5==True:
        count+=1
      if quest6==True:
        count+=1
      if quest7==True:
        count+=1
      if quest8==True:
        count+=1
      if quest9==True:
        count+=1
      if quest10==True:
        count+=1
      if quest11==True:
        count+=1
      if quest12==True:
        count+=1
      clear()
      print 'Quests completed:',count
      print 'Total quests:',quest_count
    if move_on=="storage":
      clear()
      choice1=''
      choice2=''
      storage_int1()
      self_int1()
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
              print '(11)Coal:',storage_coal,'(Qty)'
              print '(12)Iron:',storage_iron,'(Qty)'
              print '(13)Gold:',storage_gold,'(Qty)'
              print '(14)Diamond:',storage_diamond,'(Qty)'
              print '(15)Copper:',storage_copper,'(Qty)'
              print '(16)Lapiz:',storage_lapiz,'(Qty)'
              print '(17)Zinc:',storage_zinc,'(Qty)'
              print '(18)Cobalt:',storage_cobalt,'(Qty)'
              print '(19)Mica:',storage_mica,'(Qty)'
              print '(20)Manganese:',storage_manganese,'(Qty)'
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
              if choice == "15":
                if storage_copper<1:
                  print 'You don\'t have enough.'
                if storage_copper>0:
                  choice=raw_input('How many to withdraw:')
                  try:
                    if int(choice)<storage_copper+1:
                      copper+=int(choice)
                      storage_copper-=int(choice)
                      print 'Current holding:'
                      print 'Copper in storage:',storage_copper
                      print 'Copper in inventory:',copper
                  except ValueError, TypeError:
                    print 'You need to enter a number.'
              if choice == "16":
                if storage_lapiz<1:
                  print 'You don\'t have enough.'
                if storage_lapiz>0:
                  choice=raw_input('How many to withdraw:')
                  try:
                    if int(choice)<storage_lapiz+1:
                      lapiz+=int(choice)
                      storage_lapiz-=int(choice)
                      print 'Current holding:'
                      print 'Lapiz in storage:',storage_lapiz
                      print 'Lapiz in inventory:',lapiz
                  except ValueError, TypeError:
                    print 'You need to enter a number.'
              if choice == "17":
                if storage_zinc<1:
                  print 'You don\'t have enough.'
                if storage_zinc>0:
                  choice=raw_input('How many to withdraw:')
                  try:
                    if int(choice)<storage_zinc+1:
                      zinc+=int(choice)
                      storage_zinc-=int(choice)
                      print 'Current holding:'
                      print 'Zinc in storage:',storage_zinc
                      print 'Zinc in inventory:',zinc
                  except ValueError, TypeError:
                    print 'You need to enter a number.'
              if choice == "18":
                if storage_cobalt<1:
                  print 'You don\'t have enough.'
                if storage_cobalt>0:
                  choice=raw_input('How many to withdraw:')
                  try:
                    if int(choice)<storage_cobalt+1:
                      cobalt+=int(choice)
                      storage_cobalt-=int(choice)
                      print 'Current holding:'
                      print 'Cobalt in storage:',storage_cobalt
                      print 'Cobalt in inventory:',cobalt
                  except ValueError, TypeError:
                    print 'You need to enter a number.'
              if choice == "19":
                if storage_mica<1:
                  print 'You don\'t have enough.'
                if storage_mica>0:
                  choice=raw_input('How many to withdraw:')
                  try:
                    if int(choice)<storage_mica+1:
                      mica+=int(choice)
                      storage_mica-=int(choice)
                      print 'Current holding:'
                      print 'Mica in storage:',storage_mica
                      print 'Mica in inventory:',mica
                  except ValueError, TypeError:
                    print 'You need to enter a number.'
              if choice == "20":
                if storage_manganese<1:
                  print 'You don\'t have enough.'
                if storage_manganese>0:
                  choice=raw_input('How many to withdraw:')
                  try:
                    if int(choice)<storage_manganese+1:
                      manganese+=int(choice)
                      storage_manganese-=int(choice)
                      print 'Current holding:'
                      print 'Manganese in storage:',storage_manganese
                      print 'Manganese in inventory:',manganese
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
              print '(15)Copper:',copper,'(Qty)'
              print '(16)Lapiz:',lapiz,'(Qty)'
              print '(17)Zinc:',zinc,'(Qty)'
              print '(18)Cobalt:',cobalt,'(Qty)'
              print '(19)Mica:',mica,'(Qty)'
              print '(20)Manganese',manganese,'(Qty)'
              choice = raw_input('What would you like to deposite:')
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
              if choice == "15":
                if copper<1:
                  print 'You don\'t have enough.'
                if copper>0:
                  choice=raw_input('How many to deposit:')
                  try:
                    if int(choice)<copper+1:
                      copper-=int(choice)
                      storage_copper+=int(choice)
                      print 'Current holding:'
                      print 'Copper in storage:',storage_copper
                      print 'Copper in inventory:',copper
                  except ValueError, TypeError:
                    print 'You need to enter a number.'
              if choice == "16":
                if lapiz<1:
                  print 'You don\'t have enough.'
                if lapiz>0:
                  choice=raw_input('How many to deposit:')
                  try:
                    if int(choice)<lapiz+1:
                      lapiz-=int(choice)
                      storage_lapiz+=int(choice)
                      print 'Current holding:'
                      print 'Lapiz in storage:',storage_lapiz
                      print 'Lapiz in inventory:',lapiz
                  except ValueError, TypeError:
                    print 'You need to enter a number.'
              if choice == "17":
                if zinc<1:
                  print 'You don\'t have enough.'
                if zinc>0:
                  choice=raw_input('How many to deposit:')
                  try:
                    if int(choice)<zinc+1:
                      zinc-=int(choice)
                      storage_zinc+=int(choice)
                      print 'Current holding:'
                      print 'Zinc in storage:',storage_zinc
                      print 'Zinc in inventory:',zinc
                  except ValueError, TypeError:
                    print 'You need to enter a number.'
              if choice == "18":
                if cobalt<1:
                  print 'You don\'t have enough.'
                if cobalt>0:
                  choice=raw_input('How many to deposit:')
                  try:
                    if int(choice)<cobalt+1:
                      cobalt-=int(choice)
                      storage_cobalt+=int(choice)
                      print 'Current holding:'
                      print 'Cobalt in storage:',storage_cobalt
                      print 'Cobalt in inventory:',cobalt
                  except ValueError, TypeError:
                    print 'You need to enter a number.'
              if choice == "19":
                if mica<1:
                  print 'You don\'t have enough.'
                if mica>0:
                  choice=raw_input('How many to deposit:')
                  try:
                    if int(choice)<mica+1:
                      mica-=int(choice)
                      storage_mica+=int(choice)
                      print 'Current holding:'
                      print 'Mica in storage:',storage_mica
                      print 'Mica in inventory:',mica
                  except ValueError, TypeError:
                    print 'You need to enter a number.'
              if choice == "20":
                if manganese<1:
                  print 'You don\'t have enough.'
                if manganese>0:
                  choice=raw_input('How many to deposit:')
                  try:
                    if int(choice)<manganese+1:
                      manganese-=int(choice)
                      storage_manganese+=int(choice)
                      print 'Current holding:'
                      print 'Manganese in storage:',storage_manganese
                      print 'Manganese in inventory:',manganese
                  except ValueError, TypeError:
                    print 'You need to enter a number.'
            if choice2 == "3":
              clear()
              print 'By!'
    if move_on=="cheats":
      clear()
      if cheat_wood==True or dev==True:
        print "Wood: wood_you?"
      if cheat_dirt==True or dev==True:
        print "Dirt: i'm special"
      if cheat_water==True or dev==True:
        print 'Water: voodoo_magic'
      if cheat_rocks==True or dev==True:
        print 'Rocks: hello_world!'
      if cheat_all==True or dev==True:
        print 'All: all_of_the_above'
      if cheat_all==False and cheat_rocks==False:
        if cheat_water==False and cheat_dirt==False:
          if cheat_wood==False and dev==False:
            print 'You have not unlocked any cheat codes yet.'
    choice = ''
    if show_exit==True or hit_to_exit==True:
      move_on=raw_input('Hit enter to exit storage:')
  if choice == "@" or choice.lower() == "settings":
    if error_message==True:
      print '(1)Error Messages: Enabled'
    if error_message==False:
      print '(1)Error Messages: Disabled'
    if version==True:
      print '(2)Version Info: Enabled'
    if version==False:
      print '(2)Version Info: Disabled'
    if gather_loop==True:
      print '(3)Gather Resource Loop: Enabled'
    if gather_loop==False:
      print '(3)Gather Resource Loop: Disabled'
    if hints_loop==True:
      print '(4)Hints Loop: Enabled'
    if hints_loop==False:
      print '(4)Hints Loop: Disabled'
    if hints==True:
      print '(5)Hints: Enabled'
    if hints==False:
      print '(5)Hints: Disabled'
    if create_new_save==True:
      print '(6)New Save: Enabled'
    if create_new_save==False:
      print '(6)New Save: Disabled'
    if quick_leave==True:
      print '(7)Quick Leave: Enabled'
    if quick_leave==False:
      print '(7)Quick Leave: Disabled'
    if hit_to_exit==True:
      print '(8)Exit Confirm: Enabled'
    if hit_to_exit==False:
      print '(8)Exit Confirm: Disabled'
    if normal_clear==True:
      print '(9)Normal Screen Clean: Clear'
    if normal_clear==False:
      print '(9)Normal Screen Clean: Print Repeat'
    if run_off==True:
      print '(10)Screen Run Off Value:',chars_in_line,', Enabled'
    if run_off==False:
      print '(10)Screen Run Off Value:',chars_in_line,', Disabled'
    print 'Print Repeat Info:'
    print ' Current Value:',repeat_amount
    print '(*)Change Print Repeat Value'
    choice=raw_input('Enter number to toggle:')
    if choice == "1":
      hi=True
      if error_message==True:
        error_message=False
        hi=False
      if error_message==False:
        if hi==True:
          error_message=True
    if choice == "2":
      hi=True
      if version==True:
        version=False
        hi=False
      if version==False:
        if hi==True:
          version=True
    if choice == "3":
      hi=True
      if gather_loop==True:
        gather_loop=False
        hi=False
      if gather_loop==False:
        if hi==True:
          gather_loop=True
    if choice == "4":
      hi=True
      if hints_loop==True:
        hints_loop=False
        hi=False
      if hints_loop==False:
        if hi==True:
          hints_loop=True
    if choice == "5":
      hi=True
      if hints==True:
        hints=False
        hi=False
      if hints==False:
        if hi==True:
          hints=True
    if choice == "6":
      hi=True
      if create_new_save==True:
        create_new_save=False
        hi=False
      if create_new_save==False:
        if hi==True:
          create_new_save=True
    if choice == "7":
      hi=True
      if quick_leave==True:
        quick_leave=False
        hi=False
      if quick_leave==False:
        if hi==True:
          quick_leave=True
    if choice == "8":
      hi=True
      if hit_to_exit==True:
        hit_to_exit=False
        hi=False
      if hit_to_exit==False:
        if hi==True:
          hit_to_exit=True
    if choice == "9":
      hi=True
      if normal_clear==True:
        normal_clear=False
        hi=False
      if normal_clear==False:
        if hi==True:
          normal_clear=True
    if choice == "10":
      print '(1)Change Value\n(2)Enable/Disable'
      choice = raw_input("Choose one:")
      if choice == "1":
        try:
          chars_in_line=int(raw_input('What is the new value:'))
        except ValueError:
          if error_message==True:
            print 'System message: ValueError'
            print 'Reason: A number was not entered.'
            print 'Please wait 2.5 seconds.'
            choice=raw_input('Hit enter to continue:')
            choice=''
      if choice == "2":
        hi=True
        if run_off==True:
          run_off=False
          hi=False
        if hi==True:
          if run_off==False:
            run_off=True
    if choice == "*":
      try:
        repeat_amount=int(raw_input('What is the new value:'))
      except ValueError:
        if error_message==True:
          print 'System message: ValueError'
          print 'Reason: A number was not entered.'
          print 'Please wait 2.5 seconds.'
          choice=raw_input('Hit enter to continue:')
          choice=''
  if choice == "save" or choice.lower() == "save data":
    #save.write('='+str()+'\n')`s`
    save_fail=False
    try:
      save1=file("variables.py",'r')
    except:
        if error_message==True:
          save_fail=True
          print 'System message: ImportError'
          print 'Reason: Cannot find file'
    save=file("variables.py",'w')
    #Writes over existing save file
    if save_fail==False and create_new_save==False:
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
      save.write('copper='+str(copper)+'\n')
      save.write('lapiz='+str(lapiz)+'\n')
      save.write('zinc='+str(zinc)+'\n')
      save.write('cobalt='+str(cobalt)+'\n')
      save.write('mica='+str(mica)+'\n')
      save.write('manganese='+str(manganese)+'\n')
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
      save.write('storage_coal='+str(storage_coal)+'\n')
      save.write('storage_iron='+str(storage_iron)+'\n')
      save.write('storage_gold='+str(storage_gold)+'\n')
      save.write('storage_diamond='+str(storage_diamond)+'\n')
      save.write('storage_copper='+str(storage_copper)+'\n')
      save.write('storage_lapiz='+str(storage_lapiz)+'\n')
      save.write('storage_zinc='+str(storage_zinc)+'\n')
      save.write('storage_cobalt='+str(storage_cobalt)+'\n')
      save.write('storage_mica='+str(storage_mica)+'\n')
      save.write('storage_manganese'+str(storage_manganese)+'\n')
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
      save.write('money='+str(money)+' #Default 125\n')
      save.write('stanima='+str(stanima)+' #Starting Max 100, Default 100\n')
      save.write('max_stanima='+str(max_stanima)+' #Default 100\n')
      save.write("exit_pos=['bye','goodbye','exit','leave','moving on','adios','adiós']\n")
      save.write('donated_money='+str(donated_money)+'\n')
      save.write('donated_tf=['+str(donated_tf[0])+','+str(donated_tf[1])+','+str(donated_tf[2])+','+str(donated_tf[3])+','+str(donated_tf[4])+','+str(donated_tf[5])+','+str(donated_tf[6])+','+str(donated_tf[7])+','+str(donated_tf[8])+','+str(donated_tf[9])+','+str(donated_tf[10])+'] #0=False, 1=True. Items are in order on donate/rewards\n')
      save.write("go_home=['help','leave','break']\n")
      save.write('repeat_amount='+str(repeat_amount)+'\n')
      save.write('chars_in_line='+str(chars_in_line)+'\n')
      save.write('#Quests\n')
      save.write('quest_count='+str(quest_count)+'\n')
      save.write('quest1='+str(quest1)+' #False=Not done\n')
      save.write('quest2='+str(quest2)+' #True=Done\n')
      save.write('quest3='+str(quest3)+'\n')
      save.write('quest4='+str(quest4)+'\n')
      save.write('quest5='+str(quest5)+'\n')
      save.write('quest6='+str(quest6)+'\n')
      save.write('quest7='+str(quest7)+'\n')
      save.write('quest8='+str(quest8)+'\n')
      save.write('quest9='+str(quest9)+'\n')
      save.write('quest10='+str(quest10)+'\n')
      save.write('quest11='+str(quest11)+'\n')
      save.write('quest12='+str(quest12)+'\n')
      save.write('#Uses on cheat codes\n')
      save.write('cheat_wood_int='+str(cheat_wood_int)+'\n')
      save.write('cheat_dirt_int='+str(cheat_dirt_int)+'\n')
      save.write('cheat_water_int='+str(cheat_water_int)+'\n')
      save.write('cheat_rocks_int='+str(cheat_rocks_int)+'\n')
      save.write('cheat_all_int='+str(cheat_all_int)+'\n')
      save.write('#Cheats unlocked\n')
      save.write('cheat_wood='+str(cheat_wood)+'\n')
      save.write('cheat_dirt='+str(cheat_dirt)+'\n')
      save.write('cheat_water='+str(cheat_water)+'\n')
      save.write('cheat_rocks='+str(cheat_rocks)+'\n')
      save.write('cheat_all='+str(cheat_all)+'\n')
      save.write('#Settings\n')
      save.write('error_message='+str(error_message)+'\n')
      save.write('version='+str(version)+'\n')
      save.write('gather_loop='+str(gather_loop)+'\n')
      save.write('hints_loop='+str(hints_loop)+'\n')
      save.write('hints='+str(hints)+'\n')
      save.write('create_new_save='+str(create_new_save)+'\n')
      save.write('quick_leave='+str(quick_leave)+'\n')
      save.write('hit_to_exit='+str(hit_to_exit)+'\n')
      save.write('normal_clear='+str(normal_clear)+'\n')
      save.write('run_off='+str(run_off)+'\n')
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
      save.write('price_diamond='+str(price_diamond)+'\n')
      save.write('price_copper='+str(price_copper)+'\n')
      save.write('price_lapiz='+str(price_lapiz)+'\n')
      save.write('price_zinc='+str(price_zinc)+'\n')
      save.write('price_cobalt='+str(price_cobalt)+'\n')
      save.write('price_mica='+str(price_mica)+'\n')
      save.write('price_manganese='+str(price_manganese)+'\n')
      save.write('\n#Buy prices\n')
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
      save.write('buy_price_diamond='+str(buy_price_diamond)+'\n')
      save.write('buy_price_copper='+str(buy_price_copper)+'\n')
      save.write('buy_price_lapiz='+str(buy_price_lapiz)+'\n')
      save.write('buy_price_zinc='+str(buy_price_zinc)+'\n')
      save.write('buy_price_cobalt='+str(buy_price_cobalt)+'\n')
      save.write('buy_price_mica='+str(buy_price_mica)+'\n')
      save.write('buy_price_manganese='+str(buy_price_manganese)+'\n')
      save.write('\n# --- CODES IN GAME ---\n')
      save.write("dev_options='W3rS3cur3' #In the main menu enter this to activate.")
      save.write('\ncheat_code=""')
      save.write('\ncheat_amount='+str(cheat_amount)+'#The amount to add when using cheat code. #MAX IS 25 items')
    #Created save file if one is not found
    if save_fail==True or create_new_save==True:
      save.write('#Materials\n')
      save.write('wood=10 #logs\n')
      save.write('water=10 #oz\n')
      save.write('dirt=10 #lbs\n')
      save.write('rocks=10 #Qty\n')
      save.write('#Things you can make\n')
      save.write('clay=10 #lbs\n')
      save.write('bowl=10 #Qty\n')
      save.write('sticks=10 #Qty\n')
      save.write('#Goodies\n')
      save.write('coal=1\n')
      save.write('iron=1\n')
      save.write('gold=1\n')
      save.write('diamond=1\n')
      save.write('copper=1\n')
      save.write('lapiz=1\n')
      save.write('zinc=1\n')
      save.write('cobalt=1\n')
      save.write('mica=1\n')
      save.write('manganese=1\n')
      save.write('#Home storage vars\n')
      save.write('storage_wood=5\n')
      save.write('storage_water=5\n')
      save.write('storage_dirt=5\n')
      save.write('storage_rocks=5\n')
      save.write('storage_clay=5\n')
      save.write('storage_bowl=5\n')
      save.write('storage_sticks=5\n')
      save.write('storage_pickaxe=5\n')
      save.write('storage_shovel=5\n')
      save.write('storage_axe=5\n')
      save.write('storage_coal=2\n')
      save.write('storage_iron=2\n')
      save.write('storage_gold=2\n')
      save.write('storage_diamond=2\n')
      save.write('storage_copper=2\n')
      save.write('storage_lapiz=2\n')
      save.write('storage_zinc=2\n')
      save.write('storage_cobalt=2\n')
      save.write('storage_mica=2\n')
      save.write('storage_manganese=2\n')
      save.write('#Storage\n')
      save.write('self_storage=300 #Qty of items\n')
      save.write('home_storage=500 #Qty of items\n')
      save.write('#Tools\n')
      save.write('pickaxe=5 #Qty, Can be used 1 time\n')
      save.write('shovel=2 #Qty, Can be used 1 time\n')
      save.write('axe=3 #Qty, Can be used 1 time\n')
      save.write('#Cords\n')
      save.write('lake1_cords=[27,0,69]\n')
      save.write('lake2_cords=[27,0,103]\n')
      save.write('lake3_cords=[27,0,409]\n')
      save.write('river1_cords=[10, 0, 32]\n')
      save.write('river2_cords=[10, 0, 210]\n')
      save.write('river3_cords=[10, 0, 122]\n')
      save.write('clay_mountian1_cords=[103, 100, 495]\n')
      save.write('clay_mountian2_cords=[103, 120, 123]\n')
      save.write('clay_mountian3_cords=[103, 80, 249]\n')
      save.write('desert1_cords=[521, 10, 52]\n')
      save.write('desert2_cords=[521, 10, 420]\n')
      save.write('desert3_cords=[521, 10, 231]\n')
      save.write('city1_cords=[245, 0, 245]\n')
      save.write('city2_cords=[245, 0, 12]\n')
      save.write('city3_cords=[245, 0, 478]\n')
      save.write('forest1_cords=[34, 5, 23]\n')
      save.write('forest2_cords=[34, 5, 78]\n')
      save.write('forest3_cords=[34, 5, 103]\n')
      save.write('exercise_mountian1_cords=[378, 207, 300]\n')
      save.write('#Locations\n')
      save.write('home_location=[0, 0, 0]\n')
      save.write('current_location=[0, 0, 0]\n')
      save.write("current_surrounding='home'\n")
      save.write('#Biomes\n')
      save.write("water_biomes=['lake #1','lake #2','lake #3','river #1','river #2','river #3']\n")
      save.write("clay_biomes=['clay mountian #1','clay mountian #2','clay mountian #3']\n")
      save.write("sand_biomes=['desert #1','desert #2','desert #3','abandoned city','city #1','city #2','city #3']\n")
      save.write("dirt_biomes=['forest #1','forest #2','forest #3']\n")
      save.write('#Others\n')
      save.write('sides=False\n')
      save.write('money=125 #Default 125\n')
      save.write('stanima=100 #Starting Max 100, Default 100\n')
      save.write('max_stanima=100 #Default 100\n')
      save.write("exit_pos=['bye','goodbye','exit','leave','moving on','adios','adiós']\n")
      save.write('donated_money=0\n')
      save.write('donated_tf=[0,0,0,0,0,0,0,0,0,0,0] #0=False, 1=True. Items are in order on donate/rewards\n')
      save.write("go_home=['help','leave','break']\n")
      save.write('repeat_amount=25\n')
      save.write('chars_in_line=55\n')
      save.write('#Quests\n')
      save.write('quest_count=12\n')
      save.write('quest1=False #False=Not done\n')
      save.write('quest2=False #True=Done\n')
      save.write('quest3=False\n')
      save.write('quest4=False\n')
      save.write('quest5=False\n')
      save.write('quest6=False\n')
      save.write('quest7=False\n')
      save.write('quest8=False\n')
      save.write('quest9=False\n')
      save.write('quest10=False\n')
      save.write('quest11=False\n')
      save.write('quest12=False\n')
      save.write('#Uses on cheat codes\n')
      save.write('cheat_wood_int=0\n')
      save.write('cheat_dirt_int=0\n')
      save.write('cheat_water_int=0\n')
      save.write('cheat_rocks_int=0\n')
      save.write('cheat_all_int=0\n')
      save.write('#Cheats unlocked\n')
      save.write('cheat_wood=False\n')
      save.write('cheat_dirt=False\n')
      save.write('cheat_water=False\n')
      save.write('cheat_rocks=False\n')
      save.write('cheat_all=False\n')
      save.write('#Settings\n')
      save.write('error_message=True\n')
      save.write('version=True\n')
      save.write('gather_loop=True\n')
      save.write('hints_loop=True\n')
      save.write('hints=True')
      save.write('create_new_save=True\n')
      save.write('quick_leave=True\n')
      save.write('hit_to_exit=False\n')
      save.write('normal_clear=False\n')
      save.write('run_off=True')
      save.write("\n#Though all cords = distance\n")
      save.write("#Lake = 27,0,?\n")
      save.write("#River = 10,0,?\n")
      save.write("#Clay mountian = 103,?,?\n")
      save.write("#Exercise mountian = 378,207,?\n")
      save.write("#Desert = 521,10,?\n")
      save.write("#Abandoned city = 245,0,?\n")
      save.write("#Forest = 34,5,?\n\n")
      save.write('#Sell prices\n')
      save.write('price_wood=2\n')
      save.write('price_dirt=1\n')
      save.write('price_water=1\n')
      save.write('price_rocks=1\n')
      save.write('price_clay=3\n')
      save.write('price_bowl=5\n')
      save.write('price_sticks=1\n')
      save.write('price_pickaxe=7\n')
      save.write('price_shovel=4\n')
      save.write('price_axe=5\n')
      save.write('price_coal=1\n')
      save.write('price_iron=3\n')
      save.write('price_gold=5\n')
      save.write('price_diamond=7\n')
      save.write('price_copper=2\n')
      save.write('price_lapiz=3\n')
      save.write('price_zinc=3\n')
      save.write('price_cobalt=4\n')
      save.write('price_mica=4\n')
      save.write('price_manganese=5\n')
      save.write('\n#Buy prices\n')
      save.write('buy_price_wood=3\n')
      save.write('buy_price_dirt=2\n')
      save.write('buy_price_water=2\n')
      save.write('buy_price_rocks=2\n')
      save.write('buy_price_clay=4\n')
      save.write('buy_price_bowl=7\n')
      save.write('buy_price_sticks=2\n')
      save.write('buy_price_pickaxe=9\n')
      save.write('buy_price_shovel=5\n')
      save.write('buy_price_axe=7\n')
      save.write('buy_price_coal=2\n')
      save.write('buy_price_iron=4\n')
      save.write('buy_price_gold=6\n')
      save.write('buy_price_diamond=8\n')
      save.write('buy_price_copper=5\n')
      save.write('buy_price_lapiz=6\n')
      save.write('buy_price_zinc=5\n')
      save.write('buy_price_cobalt=6\n')
      save.write('buy_price_mica=6\n')
      save.write('buy_price_manganese=7\n')
      save.write('\n# --- CODES IN GAME ---\n')
      save.write("dev_options='W3rS3cur3' #In the main menu enter this to activate.")
      save.write('\ncheat_code=""')
      save.write('\ncheat_amount=10 #The amount to add when using cheat code. #MAX IS 25 items')
    save.close()
    if save_fail==True or create_new_save==True:
      print 'Save file created.'
    if save_fail==False and create_new_save==False:
      print 'Save file overwriten.'
    if create_new_save==True:
      create_new_save=False
      print 'New Save set to: False'
    print 'Save file location:',os.path.abspath('variables.py')
    if hints==True:
      print 'Hint: Make sure your save file is located at this location. You may also put the all other game files here.'
    move_on=raw_input('Hit enter to exit save:')
  if choice == "update" or choice.lower() == "updates" or choice.lower() == "show patch notes":
    print "Patch notes for 0.1.9\n"
    print '1. Vars.py file has been changed to variables.py'
    print '2. Hints setting will now save.'
    print '3. Gather Resources now says dirt instead of dir when showing a list of options.'
    print '4. Gather Resources now doesn\'t say "Hit enter to exit" when you choose exit as an option.'
    print '5. Gather Resources can now use quick leave in the list of options. Use by hitting enter with nothing typed.'
    print '6. Change Location will no longer give a error when using.'
    print '7. Change the way some text appears on Crafting Menu.'
    print '8. Crafting Menu now adds () to s, after you craft an item. Ex: stick(s).'
    print '9. Sleep will no longer say "sleeping..." if it says "You are not tired".'
    print '10. Sleep now shows your stanima before you sleep.'
    print '11. Sleep now has a hint. To turn it off change it in settings.'
    print '12. You can now only sleep if you are 20 or more stanima below max.'
    print '13. Fixed a bug where you couldn\'t sell any bowls.'
    print '14. Buy will now show you how much money you have while it displays the items you can buy.'
    print '15. Storage in inventory is now updated with the mica and manganese.'
    print '16. Edited the look of cheat codes function.'
    print '17. Updates now has a hint.'
    if hints==True:
      print '\nHint: For a full look at the patch notes. Please check the updates.txt file.'
    move_on=raw_input('Hit enter to exit updates:')
  if choice == "Dev_menu":
    if dev==True:
      if sides == True:
        print '(1)Give - Gives free stuff'
        print '(2)Remove - Removes stuff'
        print '(3)Everything is cheap'
        choice = raw_input('Choose an option:')
        if choice == "1":
          clear()
          loop4(s=False,other=False,numbers=True,price=False)
          choice=raw_input('Choose an option:')
          if choice == "1":
            choice = raw_input('How many:')
            try:
              wood+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "2":
            choice = raw_input('How many:')
            try:
              dirt+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "3":
            choice = raw_input('How many:')
            try:
              water+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "4":
            choice = raw_input('How many:')
            try:
              rocks+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "5":
            choice = raw_input('How many:')
            try:
              clay+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "6":
            choice = raw_input('How many:')
            try:
              bowl+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "7":
            choice = raw_input('How many:')
            try:
              sticks+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "8":
            choice = raw_input('How many:')
            try:
              pickaxe+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "9":
            choice = raw_input('How many:')
            try:
              shovel+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "10":
            choice = raw_input('How many:')
            try:
              axe+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "11":
            choice = raw_input('How many:')
            try:
              coal+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "12":
            choice = raw_input('How many:')
            try:
              iron+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "13":
            choice = raw_input('How many:')
            try:
              gold+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "14":
            choice = raw_input('How many:')
            try:
              diamond+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "15":
            choice = raw_input('How many:')
            try:
              copper+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "16":
            choice = raw_input('How many:')
            try:
              lapiz+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "17":
            choice = raw_input('How many:')
            try:
              zinc+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
          if choice == "18":
            choice = raw_input('How many:')
            try:
              cobalt+=int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
            choice = ''
        if choice == "2":
          clear()
          loop4(s=False,other=False,numbers=True,price=False)
          choice=raw_input('Choose an option:')
          if choice == "1":
            print '(*)Remove all'
            choice = raw_input('How many:')
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
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
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
              if choice == "*":
                diamond=0
              if choice is not "*":
                if diamond==int(choice) or diamond>int(choice):
                  diamond-=int(choice)
                else:
                  print 'You don\'t have enough. Sorry :('
                  time.sleep(1.5)
            choice = ''
          if choice == "15":
            print '(*)Remove all'
            choice = raw_input('How many:')
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
              if choice == "*":
                copper=0
              if choice is not "*":
                if copper==int(choice) or copper>int(choice):
                  copper-=int(choice)
                else:
                  print 'You don\'t have enough. Sorry :('
                  time.sleep(1.5)
            choice = ''
          if choice == "16":
            print '(*)Remove all'
            choice = raw_input('How many:')
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
              if choice == "*":
                lapiz=0
              if choice is not "*":
                if lapiz==int(choice) or lapiz>int(choice):
                  lapiz-=int(choice)
                else:
                  print 'You don\'t have enough. Sorry :('
                  time.sleep(1.5)
            choice = ''
          if choice == "17":
            print '(*)Remove all'
            choice = raw_input('How many:')
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
              if choice == "*":
                zinc=0
              if choice is not "*":
                if zinc==int(choice) or zinc>int(choice):
                  zinc-=int(choice)
                else:
                  print 'You don\'t have enough. Sorry :('
                  time.sleep(1.5)
            choice = ''
          if choice == "18":
            print '(*)Remove all'
            choice = raw_input('How many:')
            ah=False
            try:
              int(choice)
            except ValueError:
              if error_message==True:
                print 'System message: ValueError'
                print 'Reason: A number was not entered.'
                ah=True
            if ah==False:
              if choice == "*":
                cobalt=0
              if choice is not "*":
                if cobalt==int(choice) or cobalt>int(choice):
                  cobalt-=int(choice)
                else:
                  print 'You don\'t have enough. Sorry :('
                  time.sleep(1.5)
            choice = ''
        if choice == "3":
          price_wood=1
          price_dirt=1
          price_water=1
          price_rocks=1
          price_clay=1
          price_bowl=1
          price_sticks=1
          price_pickaxe=1
          price_shovel=1
          price_axe=1
          price_coal=1
          price_iron=1
          price_gold=1
          price_diamond=1
          price_copper=1
          price_lapiz=1
          price_zinc=1
          price_cobalt=1
          buy_price_wood=1
          buy_price_dirt=1
          buy_price_water=1
          buy_price_rocks=1
          buy_price_clay=1
          buy_price_bowl=1
          buy_price_sticks=1
          buy_price_pickaxe=1
          buy_price_shovel=1
          buy_price_axe=1
          buy_price_coal=1
          buy_price_iron=1
          buy_price_gold=1
          buy_price_diamond=1
          buy_price_copper=1
          buy_price_lapiz=1
          buy_price_zinc=1
          buy_price_cobalt=1
        choice = ''
  if choice == "Dev_var":
    if dev==True:
      if sides == True:
        choice=raw_input('(1)Vars or (2)Quests:')
        if choice == "1":
          print '(1)Dev          #Developer stuff'
          print '(2)Dev_options  #Developer passcode'
          print '(3)Self_storage #Space in inventory'
          print '(4)Home_storage #Space at home'
          print '(5)Stanima      #Energy'
          print '(6)Max_stanima  #Max energy'
          choice=raw_input('Choose an item:')
          if choice == "1":
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
          if choice == "2":
            print 'This is case sensitive.\nHit enter to not change password.'
            print '\nCurrent password:',dev_options
            choice = raw_input('New password:')
            if choice is not "":
              dev_options=choice
            choice=''
          if choice == "3":
            print 'Hit enter to not change.'
            print '\nCurrent capacity:',self_storage
            choice=raw_input('New capacity:')
            if choice is not "":
              try:
                self_storage=int(choice)
              except ValueError:
                if error_message==True:
                  print 'System message: ValueError'
                  print 'Reason: A number was not entered.'
                move_on=raw_input('Hit enter to leave:')
            choice=''
          if choice == "4":
            print 'Hit enter to not change.'
            print '\nCurrent capacity:',home_storage
            choice=raw_input('New capacity:')
            if choice is not "":
              try:
                home_storage=int(choice)
              except ValueError:
                if error_message==True:
                  print 'System message: ValueError'
                  print 'Reason: A number was not entered.'
                move_on=raw_input('Hit enter to leave:')
            choice=''
          if choice == "5":
            print 'Hit enter to not change.'
            print '\nCurrent setting:',stanima
            choice=raw_input('New setting:')
            if choice is not "":
              try:
                if int(choice)+1>max_stanima:
                  stanima=max_stanima
                if int(choice)<max_stanima+1:
                  stanima=int(choice)
              except ValueError:
                if error_message==True:
                  print 'System message: ValueError'
                  print 'Reason: A number was not entered.'
                move_on=raw_input('Hit enter to leave:')
            choice=''
          if choice == "6":
            print 'Hit enter to not change.'
            print '\nCurrent setting:',max_stanima
            choice=raw_input('New setting:')
            if choice is not "":
              try:
                max_stanima=int(choice)
              except ValueError:
                if error_message==True:
                  print 'System message: ValueError'
                  print 'Reason: A number was not entered.'
                move_on=raw_input('Hit enter to leave:')
            choice=''
        if choice == "2":
          hi=True
          print '(a1)Quest1   (b1)Quest7'
          print '(a2)Quest2   (b2)Quest8'
          print '(a3)Quest3   (b3)Quest9'
          print '(a4)Quest4   (b4)Quest10'
          print '(a5)Quest5   (b5)Quest11'
          print '(a6)Quest6   (b6)Quest12'
          print '(*)All of the quests'
          choice=raw_input('Choose an item:')
          if choice == "a1":
            if quest1==True:
              quest1=False
              hi=False
            if quest1==False:
              if hi==True:
                quest1=True
            choice=''
          if choice == "a2":
            if quest2==True:
              quest2=False
              hi=False
            if quest2==False:
              if hi==True:
                quest2=True
            choice=''
          if choice == "a3":
            if quest3==True:
              quest3=False
              hi=False
            if quest3==False:
              if hi==True:
                quest3=True
            choice=''
          if choice == "a4":
            if quest4==True:
              quest4=False
              hi=False
            if quest4==False:
              if hi==True:
                quest4=True
            choice=''
          if choice == "a5":
            if quest5==True:
              quest5=False
              hi=False
            if quest5==False:
              if hi==True:
                quest5=True
            choice=''
          if choice == "a6":
            if quest6==True:
              quest6=False
              hi=False
            if quest6==False:
              if hi==True:
                quest6=True
            choice=''
          if choice == "b1":
            if quest7==True:
              quest7=False
              hi=False
            if quest7==False:
              if hi==True:
                quest7=True
            choice=''
          if choice == "b2":
            if quest8==True:
              quest8=False
              hi=False
            if quest8==False:
              if hi==True:
                quest8=True
            choice=''
          if choice == "b3":
            if quest9==True:
              quest9=False
              hi=False
            if quest9==False:
              if hi==True:
                quest9=True
            choice=''
          if choice == "b4":
            if quest10==True:
              quest10=False
              hi=False
            if quest10==False:
              if hi==True:
                quest10=True
            choice=''
          if choice == "b5":
            if quest11==True:
              quest11=False
              hi=False
            if quest11==False:
              if hi==True:
                quest11=True
            choice=''
          if choice == "b6":
            if quest12==True:
              quest12=False
              hi=False
            if quest12==False:
              if hi==True:
                quest12=True
            choice=''
          if choice == "*":
            clear()
            print 'True = Completed'
            print 'False = Not yet complete'
            choice=raw_input('True of False:').lower()
            if choice in "true":
              quest1=True
              quest2=True
              quest3=True
              quest4=True
              quest5=True
              quest6=True
              quest7=True
              quest8=True
              quest9=True
              quest10=True
              quest11=True
              quest12=True
            if choice in "false":
              quest1=False
              quest2=False
              quest3=False
              quest4=False
              quest5=False
              quest6=False
              quest7=False
              quest8=False
              quest9=False
              quest10=False
              quest11=False
              quest12=False
  if choice == "vars_beta":
    if dev==True:
      if sides==True:
        try:
          from vars_beta import *
        except ImportError:
          if error_message==True:
            print 'System message: ImportError'
            print 'Reason: Cannot find file.'
      if dev==False:
        dev_promt()
        move_on=raw_input('Hit enter to exit vars_beta:')

