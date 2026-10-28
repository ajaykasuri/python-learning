#try and except let you handle certain errors without crashing your program.

try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ValueError:
    raise ValueError("Number cannot be negative")
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
except Exception as error:
    print("Unexpected error:", error)

# try: Runs code that might cause an error.
# except ValueError: Handles invalid input, such as "hello".
# except ZeroDivisionError: Handles division by zero.

# raise → throw
# except → catch
# except ValueError as error → catch (error), with Python also specifying the error type.