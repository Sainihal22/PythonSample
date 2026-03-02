# Exception Handling

# Even if an error occurs, application / program should not crash.

# Block format : 

# try:
#     # risky code
# except:
#     # error handling code


# n = int(input("Enter a number : "))
# print(n)
# print("App is stopped")

# try : 
#     n = int(input("Enter a number : "))
#     print(n)
# except ValueError:
#     print("Issue with Value given")
# except:
#     print("Exception")

# try : 
#     n = int(input("Enter a number : "))
#     a = 10/n
#     print(a)
# except ZeroDivisionError:
#     print("Value cannot be divided by 0")
# except Exception as e: 
#     print("Issue with input : ", e)

# try:
#     pass
# except:
#     pass
# else: it runs when try block is success
#     pass

# try:
#     x = int("abc")
# except Exception as e:
#     print("Error : ", e)
# else:
#     print("Success").

# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass

# print("App is stopped")

try : 
    n = int(input("Enter a number : "))
    a = 10/n
    print(a)
except ZeroDivisionError:
    print("Value cannot be divided by 0")
except Exception as e: 
    print("Issue with input : ", e)
finally:
    print("App is stopped")
