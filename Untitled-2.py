import math

# # -------------------- Problem N --------------------------

# # # temp_f = int(input("Sláðu inn Farenheight: "))
# # # temp_c = ((temp_f-32)*5)/9
# # # print(round(temp_c))

# # -------------------- Problem J --------------------------

# # improvements_since = int(input("Improvements since frozen: "))
# # improvements_recevied = int(input("Improvements received every year: "))

# # current_year = (2022+(improvements_since // improvements_recevied))

# # print(current_year)

# # ---------------------------------------------------------

# # import math 
# # y= math.radians(float(input()))
# # x= int(50)
# # s= x*(math.tan(y))
# # Þyrfti að bæta við round til að laga verkefnið
# # print(round(s,1))

# # -------------------- Problem C - Week1.2 --------------------------

# # budget = int(input())
# # proj1 = int(input())
# # proj2 = int(input())
# # proj3 = int(input())

# # x = proj1 + proj2 + proj3

# # if x <= budget:
# # 	print("Budget is sufficient.")
# # elif x >= budget:
# # 	print("Budget is insufficient.")
# # else:
# #   print("Þú hefur slegið inn eitthvað vitlaust!")

# # # -------------------- Problem E - Week1.2 --------------------------

# # rating = int(input())

# # if rating <= 999:
# #     print("Invalid")
# # elif rating < 2400:
# #     print("Amateur")
# # elif rating >= 2400 and rating < 2500:
# #     print("International grandmaster")
# # elif rating >= 2500 and rating < 2700:
# #     print("Grandmaster")
# # elif rating >= 2700:
# #     print("Super grandmaster")

# # -------------------- Problem A - Week1.2 --------------------------

# # num = int(input())

# # if (num % 2 == 0):
# #     print("The Number is even!")
# # elif (num % 2 == 1):
# #     print("The number is odd!")
# # else:
# #     print("Input type doesnt match")

# # -------------------- Problem E - Week2.1 --------------------------

# while True:

#     print("You need something doubled? (Y)es or (N)o?")

#     answer = input()

#     if answer == "Y":
        
#         print("All right, then. Give me a number, and I’ll double it for ya: ")

#         num = float(input())

#         num = num * 2

#         print(num)

#     elif answer == "N":
#         break
    

# n = int(input())

# contains_seven = False

# while n > 0:
#     if n % 10 == 7:
#         contains_seven = True
#         break
#     n //= 10

# if contains_seven:
#     print("The number contains 7.")
# else:
#     print("The number does not contain 7.")

# # -------------------- Problem D - Week2.2 --------------------------

# n = int(input())

# for i in range(n):
#     if i == 0 or i == n - 1:
#         print('* ' * (n - 1) + '*')
#     else:
#         print('*' + ' ' * (2 * n - 3) + '*')

# # -------------------- Problem I - Week2.2 --------------------------

# waveCount = int(input())
# lineCount = int(input())

# for i in range(lineCount):

#     # Calculate the radiants of the line.
#     radiantsLine = waveCount * 2 * math.pi / lineCount

#     # Calculate the value of sin & 
#     sinValue = math.sin(i * radiantsLine)
#     numX = round((sinValue + 1) * 20) 
#     # numX = int(normValue * (lineCount // 2)) + 1
#     print('X' * numX)

# # -------------------- Problem I - Week3.1 --------------------------

# n = int(input()) 

# a = [1,2,   3]

# for i in range(n):
#     if i >= 3:
#         a.append(a[i-1] + a[i-2] + a[i-3])
#     print(a[i])

# # -------------------- Problem  - Week3.2 --------------------------
