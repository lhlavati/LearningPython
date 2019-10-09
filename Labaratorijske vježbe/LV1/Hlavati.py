#TASK 1
def count_evens(lst):
	count = 0
	for number in lst:
		if number % 2 == 0:
			count += 1
	return count
		
print (count_evens([2,3,4,5,6,7,8,9]))

#TASK 2
def centered_average(lst):
        sortedList = sorted(lst)
        sortedList.pop(0)
        sortedList.pop(len(sortedList)-1)
        print (sortedList)
        if len(sortedList) % 2 != 0:
                return sortedList[len(sortedList) // 2]
        else:
                middle = (len(sortedList) // 2) - 1
                median = (sortedList[middle] + sortedList[middle + 1]) // 2
                return median
  
print (centered_average([1,2,3,4,5,6]))

#TASK 3
def next(lst):
        for index in range(len(lst)-1):
                if lst[index] == 2 and lst[index+1] == 2:
                        return True
        else:
                return False
                
print (next([1,2,3,2,3,4,5,6,7,2,3,2]))


####### practicepython.org #######

#TASK 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for number in a:
        if number < 5:
                print (number)

#TASK 11
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print (is_prime(9))

#TASK 6
def palindrome():
        string = input("Enter a word: ")
        stringBackwards = string [::-1]
        string.lower()
        if string == stringBackwards:
                return print ("String is a palindrome")
        else:
                return print ("String is not a palindrome")

palindrome()

def rock_paper_scissors():
        p1 = input("R\t|\tP\t|\tS")
        p2 = input("R\t|\tP\t|\tS")
        scorep1 = 0
        scorep2 = 0
        if p1 == "R" and p2 == "P":
                print ("Player 2 wins!")
                scorep2 += 1
        elif p1 == "R" and p2 == "S":
                print ("Player 1 wins!")
                scorep1 += 1
        elif p1 == "P" and p2 == "S":
                print ("")                

#ZADATAK 8
def rock_paper_scissors():
    scorep1 = 0
    scorep2 = 0
    while (scorep1 < 3 and scorep2 < 3):
        p1 = input("Choose: R | P | S --> ")
        p2 = input("Choose: R | P | S --> ")
        if p1 == p2:
            print ("It's a TIE!")
        elif p1 == "R":
            if p2 == "P":
                scorep2 += 1
                print ("Player 2 wins!\nP1 | P2\n" + str(scorep1) + "  | " + str(scorep2)) 
            else:
                scorep1 += 1
                print ("Player 1 wins!\nP1 | P2\n" + str(scorep1) + "  | " + str(scorep2)) 
        elif p1 == "P":
            if p2 == "R":
                scorep1 += 1
                print ("Player 1 wins!\nP1 | P2\n" + str(scorep1) + "  | " + str(scorep2)) 
            else:
                scorep2 += 1
                print ("Player 2 wins!\nP1 | P2\n" + str(scorep1) + "  | " + str(scorep2)) 
        elif p1 == "S":
            if p2 == "P":
                scorep1 += 1
                print ("Player 1 wins!\nP1 | P2\n" + str(scorep1) + "  | " + str(scorep2)) 
            else:
                scorep2 += 1
                print ("Player 2 wins!\nP1 | P2\n" + str(scorep1) + "  | " + str(scorep2)) 
        else:
            print("Invalid input, Please try again!")
            
    if scorep1 > scorep2:
        print ("Congratulations Player 1! You win!\nFinal score: \nP1 | P2\n" + str(scorep1) + "  | " + str(scorep2))
    else:
        print ("Congratulations Player 2! You win!\nFinal score: \nP1 | P2\n" + str(scorep1) + "  | " + str(scorep2))
        
    newgame = input("\nDo you want to play a new game? Y/N --> ")
    
    while newgame != "Y" and newgame != "N":
        newgame = input("Invalid input! Please use Y or N --> ")
    
    if newgame == "Y":
        rock_paper_scissors()
    else:
        print ("Thanks for playing!")
    
rock_paper_scissors()