import random
import Day_eleven_art
start = input("Do ypu want to play a game of Blackjack? Type 'y' or 'n': ").lower()
def start_here():
      Day_eleven_art.clear()
      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
      my_choice = []
      pc_choice = []
      my_total = 0
      pc_total = 0
      pcFrist_num = []
      def play():


            myfirst_num = random.choice(cards)
            mysec_num = random.choice(cards)
            pcfirst_num = random.choice(cards)
            pcsec_num = random.choice(cards)
            my_total = myfirst_num + mysec_num
            my_choice.append(myfirst_num)
            my_choice.append(mysec_num)
            pc_choice.append(pcfirst_num)
            pc_choice.append(pcsec_num)
            pcFrist_num.append(pcfirst_num)
           
            print(f"Your cards: {my_choice}, current score: {my_total}")
            print(f"Computer's first card: {pcfirst_num}")
            return pcsec_num

            


      def next():
            
            con = input("Type 'y' to get another card, type 'n' to pass: ")

            if con == "y":
                  mythird_choice = random.choice(cards)
                  my_choice.append(mythird_choice)
                  my_total = sum(my_choice)
                  pc_total = sum(pc_choice)
                  
                  print(f"Your cards: {my_choice}, current score: {my_total}")
                  print(f"Computer's fisrt card: {pcFrist_num}")
                  if my_total > 21:
                        print( "You Lose")
                        another = input("Do you want to play again? 'y' or 'n'").lower()
                        if another =="y":
                           start_here()
                        return 0
                  if pc_total < 16:
                        pcthird_choice = random.choice(cards)
                        pc_choice.append(pcthird_choice)
                        pc_total = sum(pc_choice)
                  if pc_total > 21:
                        print("You win")
                        another = input("Do you want to play again? 'y' or 'n'").lower()
                        if another =="y":
                              start_here()
                      
                  next()
                  my_total = sum(my_choice)
                  pc_total = sum(pc_choice)
             
            else:
                  my_total = sum(my_choice)
                  pc_total = sum(pc_choice)
                  print(f"Your cards: {my_choice}, final score: {my_total}")
                  print(f"Computer's final hands: {pc_choice}, final score:{pc_total}")
                  if my_total > pc_total:
                        print("You win")
                        another = input("Do you want to play again? 'y' or 'n'").lower()
                        if another =="y":
                              start_here()
                  elif my_total < pc_total:
                        print("You lose")
                        another = input("Do you want to play again? 'y' or 'n'").lower()
                        if another =="y":
                              start_here()
                  
                        
                        

      if start == "y":
            Day_eleven_art.clear()
            print(Day_eleven_art.logo)
            play()
            next()
      else:
            print("Good bye")
start_here()