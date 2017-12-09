from __future__ import print_function

while True:
    try:
        num1 = input("Enter the number1 ")
        num2 = input("Enter the number2 ")
        if num1 == 0 or num2 == 0:
            break
        z = (num1 / 2) / (num1 - num2)
        print("The result is : ", z)

    except ZeroDivisionError as e:
        print("This is exception 1  ....")
        print("Error message : " ,str(e) )
    except NameError as e:
        print("This is exception  2  ....")
        print("Error message : " ,str(e) )
    except Exception as e:
        print("This is exception 3  ....")
        print("Error message : " ,str(e) )
    finally:
        print("Done programme ")
