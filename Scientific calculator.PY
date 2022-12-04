def main():
    print("\n\n")
    print("*********** WELCOME TO MY CALCULATOR ************")
    
    print("-----> THIS CALCULATOR CAN OPERATE ON MAXIMUM TWO NUMBERS ONLY <-----")
    print("\n\n")
    name=input(" ENTER YOUR NAME:- ")
    
    print("\n")
    print(f"HEY {name} SELECT BELOW OPERATIONS:- ")
    print(""" 
    PRESS:-
    1.Addition(x,y) 
    2.Subtraction(x,y) 
    3.Multiplication(x,y) 
    4.Division(x,y) 
    5.Remainder_MOD{%}(x,y)
    6.Square_Root(x)
    7.Exponent(x,y) 
    8.Sin(x)  
    9.Cos(x) 
    10.Tan(x)
    11.Radian_Into_Degree(x)
    12.Degree_Into_Radian(x)

    """) 
    import math 
    nol=["no","NO","N","n"]
    yesl=["yes","YES","Y","y"]
    o = input("ENTER THE S.NO OF SELECTED OPERATION:- ") 
    
    if o == "1": 
        x = float(input("ENTER THE FIRST NUMBER:- ")) 
        y = float(input("ENTER THE SECOND NUMBER:- ")) 
        print("\n"+"THE RESULT OF ADDITION IS: ","\n",x,"+",y,"=",x+y)
         
    elif o == "2": 
        x = float(input("ENTER THE FIRST NUMBER:- ")) 
        y = float(input("ENTER THE SECOND NUMBER:- ")) 
        print("\n"+"THE RESULT OF SUBTRACTION IS: ","\n",x,"-",y,"=",x-y) 
        
    elif o == "3": 
        x = float(input("ENTER THE FIRST NUMBER:- ")) 
        y = float(input("ENTER THE SECOND NUMBER:- ")) 
        print("\n"+"THE RESULT OF MULTIPLICATION IS: ","\n",x,"x",y,"=",x*y) 
        
    elif o == "4": 
        x = float(input("ENTER THE FIRST NUMBER:- ")) 
        y = float(input("ENTER THE SECOND NUMBER:- ")) 
        print("\n"+"THE RESULT OF DIVISION IS: ","\n",x,"÷",y,"=",x/y) 
        
    elif o == "5": 
        x = float(input("ENTER THE FIRST NUMBER:- ")) 
        y = float(input("ENTER THE SECOND NUMBER:- ")) 
        print("\n"+"THE RESULT OF MODULUS FUNCTION IS: ","\n",x,"%",y,"=",math.fmod(x,y))  
        
    elif o == "6": 
        x = float(input("ENTER THE NUMBER:- "))
        print("\n"+"THE RESULT OF SQUARE ROOT OF: ","\n","√",x,"=",math.sqrt(x))
        
    elif o == "7": 
        x = float(input("ENTER THE FIRST NUMBER:- ")) 
        y = float(input("ENTER THE SECOND NUMBER:- ")) 
        print("\n"+"THE RESULT OF EXPONENTIAL FUNCTION OF: ","\n",x,"^",y,"=",math.pow(x,y))
        
    elif o == "8": 
        x = float(input("ENTER THE NUMBER:- ")) 
        print("\n"+"THE RESULT OF SIN FUNCTION OF: ","\n",x,"=",math.sin(x)) 
        
    elif o == "9": 
        x = float(input("ENTER THE NUMBER:- ")) 
        print("\n"+"THE RESULT OF COS FUNCTION OF: ","\n",x,"=",math.cos(x)) 
        
    elif o == "10": 
        x = float(input("ENTER THE NUMBER:- ")) 
        print("\n"+"THE RESULT OF TAN FUNCTION OF: ","\n",x,"=",math.tan(x)) 
        
    elif o == "11": 
        x = float(input("ENTER THE NUMBER:- ")) 
        print("\n"+"THE RESULT OF CONVERSION FROM RADIAN INTO DEGREE OF: ","\n",x,"=",math.degrees(x)) 
        
    elif o == "12": 
        x = float(input("ENTER THE NUMBER:- ")) 
        print("\n"+"THE RESULT OF COVERSION FROM DEGREE INTO RADIAN OF: ","\n",x,"=",math.radians(x))
     
    print("\n")
    restart=input("DO YOU WISH TO START AGAIN ? YES/NO :- ")
    if restart in yesl:
        main()
    else:
        print("\n")
        print(f"THANK YOU {name}.")
        print("\n")
main()
