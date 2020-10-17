# # # print("Hello, World!")

# # # a = 10
# # # b = 5

# # # c = a ** b
# # # print(c)
# # # print(c)
# # # print("nananana")

# # print("Tell us your name: ")
# # name = input()

# # print("Hello, "+ name+ '!')

# print ("Provide a number")
# number = int(input)

# if number  == 0:
#     print("You've typer ZERO!")
# elif 

# x=5 
# print("Start!")

# while x <= 10:
#     print(x)
   
#     # x=x+1
#     x += 1

# print ("Koniec!")

my_list = (1,3,5,7,9,0,2,4,6,8)


current_min = my_list[0]
for number in my_list:
    if number < current_min:
        current_min = number
print (current_min)
   


    
current_max = my_list[0]
for number in my_list:
    if number > current_max:
        current_max = number
print (current_max)



length1 = 0
for element in my_list:
    length1 += 1
print (length1)


def multiply(x,y):
    count = 1
    result =0
    while count <= x:
        result += y
        count +=1
        
    print (result)

multiply(3,4)

def pow(x,y):

return operator in hjkhjk

def is_number (input):
    try:
        return int(input)
    except:
        return None
def is_valid_operator(operator):
    return operator in ['+', '-', '*', '/']

def ask_for_a_number (force_valid_input = True):
    user_input = input ("Podaj liczbe: ")
    casted_value = is_number(user_input)
    if force_valid_input:
     while casted_value == None:
        user_input = input("Podaj liczbe: ")
        casted_value = is_number(user_input)
     return casted_value

def ask_for_an_operator (force_valid_input = True):
    user_input = input("Podaj operator: ")
    if force_valid_input:
        while not is_valid_operator(user_input):
            user_input = input("Podaj operator: ")
            return user_input
    else:
        if not is_valid_operator:
            return None
        else:
            return user_input

def calculate(operand1, operator, operand2):
    if operand1 == None or operator == None or operand2 == None:
        return None
    if operator == '+':
        return operand1 + operand2
        pass
    elif operator == '-':
        return operand1 - operand2
        pass
    elif operator == '*':
        return operand1 * operand2
        pass
    elif operator == '/':
        if operand2 == 0:
            print ("Error division by zero")
            return None
        else: 
            return operand1 / operand2
    else:
        return None 

  
def simple_calculator()
    end_cond = True
    while end_cond:
        print ("Podaj operand1")
        operand1 = ask_for_a_number(False)
        if operand1 == None:
            end_cond = False
        else:
            operator = ask_for_an_operator(True)
            print ("Podaj operand2")
            operand2 = ask_for_a_number (True)
            result = calculate(operand1,operator, operand2)
              
    pass
    
if __name__ == "__main__":
    simple_calculator()






        











    





   

   
