class Game : 
    def __init__ (self): 
        while True : 
            print ('''
            Welcome .. 
            Chose your game number 
            1 for Divided By Game 
            2 for No Duplicaye Game  ''' )
            user_choice = int(input ("Plz enter your choice : "))
            if user_choice == 1 :
                x = int (input ("Enter first number : "))
                y = int (input ("Enter last number : "))
                self.divided_by(x,y)
            
            elif user_choice == 2 :
                sentence = input ("enter sentence :")
                self.no_duplicate (sentence)
                
            play_again = input ("Do you want to play again : ")
            if play_again == "n" : 
                print ("Good Bye")
                break

    def divided_by (self,x,y):
        for n in range (1,101) : 
            if  n % x == 0 and n % y == 0 : 
                print (n) 

    def no_duplicate (self , sentence) :
        words = []
        for x in sentence.split(" ") : 
            if x not in words : 
                words.append(x)
        print (' '.join (words)) 

p1 = Game ()

