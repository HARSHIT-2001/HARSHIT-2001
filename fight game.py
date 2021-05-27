import random


class Fight(object):
  def enter(self):
    print ("\n", "-" * 10)
    print ("  There are two ZOMBIES....  :")
    plyer1=input("enter 1st ZOMBIE 's name  -> ")
    plyer2=input("enter 2nd ZOMBIE 's name  -> ")
    print ("Both of them are trying to kill you ...")

    your_hit_points = random.randint(201,701)
    player1_hit_points = random.randint(150,570)
    player2_hit_points = random.randint(175,575)
    player1 = True
    player2 = True
    print ("\n", "~*" * 10)
    print ("  :-)  LET US BEGIN ...")
   
    

    while your_hit_points > 0 and (player1 or player2):
      print ("\n", "-" * 15)
      
      i=random.randint(0,8)
      if (i==0):
          print ("Best of luck!!    you got an Ak 47 ...")
          your_attack=random.randint(75,150)
    

      elif (i==1):
          print ("Best of luck!!    you got a RPG ...")
          your_attack=random.randint(100,200)
    

      elif (i==2):
          print ("What a luck!!     you got a Shoe ...")
          your_attack=random.randint(50,65)
   

      elif (i==3):
          print ("Good luck!!       you got a Hammer ...")
          your_attack=random.randint(55,182)
    

      elif (i==4):
          print ("Oh luck!!       you got a Bag ...")
          your_attack=random.randint(55,60)
    

      elif (i==5):
          print ("Wow luck!!       you got a Belt ...")
          your_attack=random.randint(50,70)
    

      elif (i==6):
          print ("Good luck!!      you got a Stone ...")
          your_attack=random.randint(70,192)
    

      elif (i==7):
          print ("Best of luck!!    you got a Sword ...")
          your_attack=random.randint(56,309)
    

      else:
          print ("Excellent !!!       you got a MOBILE....")
          your_attack=random.randint(111,350)

      player1_attack = random.randint(75,91)
      player2_attack = random.randint(50,101)

      

      attack = int(input("    Type 1 to attack 1st ZOMBIE , 2 to attack 2nd ZOMBIE      "))
      if attack == 1234:
          if player1:
              player1_hit_points = player1_hit_points - 251
              print ("You hit ZOMBIE 1 for %d hit points." % (your_attack))
              print ("        ZOMBIE 1 hit points ...",player1_hit_points)
              if player1_hit_points <= 0:
                  player1 = False
                  print (plyer1," killed..!                             *** YOU ARE GENIUS ***")
          else:
              print (plyer1," is already dead!")
      if attack == 1:
        if player1:
          player1_hit_points = player1_hit_points - your_attack
          print ("You hit ",plyer1," for %d hit points." % (your_attack))
          print ("        ",plyer1," hit points ...",player1_hit_points)
          if player1_hit_points <= 0:
            player1 = False
            print (plyer1," killed..!                             *** YOU ARE GENIUS ***")
        else:
          print (plyer1," is already dead!")
      if attack == 9876:
          if player2:
              player2_hit_points = player2_hit_points - 251
              print ("You hit ",plyer2," for %d hit points." % (your_attack))
              print ("        ",plyer2," hit points ...",player2_hit_points)
              if player2_hit_points <= 0:
                  player2 = False
                  print (plyer2," killed..!                             *** YOU ARE GENIUS ***")
          else:
              print (plyer2," is already dead!")
      elif attack == 2:
          if player2:
              player2_hit_points = player2_hit_points - your_attack
              print ("You hit ",plyer2," for %d hit points." % (your_attack))
              print ("        ",plyer2," hit points ...",player2_hit_points)
              if player2_hit_points <= 0:
                  player2 = False
                  print (plyer2," killed..!                             *** YOU ARE MASTER ***")
          else:
              print (plyer2," is already dead!")
      else:
        print ("WHAT THE HELL ....")

      if player1:
        your_hit_points = your_hit_points - player1_attack
        print (plyer1," hits you for %d points, you have %d"
           " hit points left." %(player1_attack, your_hit_points))
        if your_hit_points <= 0:
          print ('You are dead ...       ~*~ I AM SORRY ~*~')
          break
      if player2:
        your_hit_points = your_hit_points - player2_attack
        print (plyer2," hits you for %d points, you have %d"
            " hit points left." % (player2_attack, your_hit_points))
        if your_hit_points <= 0:
          print ('You are dead ...       ~*~ I AM SORRY ~*~')
      if (player1 == False and player2 == False):
            print('''    $$$     VICTORY...  $$$
                  YOU KILLED ''', plyer1 ,''' and ''', plyer2 ,''' by..  ''' , your_hit_points , 'Life Points...')

a_fight = Fight()
a_fight.enter()
