try:
    # Trying to catch error
    # Don't combine lines with multiple in a single try block, like below.
    file = open("file.txt")
    a_dict = {'key': 'value'}
    print(a_dict['qwe'])
except FileNotFoundError:
    # Never use bare except
    # Will catch FileNotFoundError
    file = open("file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    # Will catch KeyError
    print(f"Key {error_message} not found")
else:
    # Will run if there is no error.
    content = file.readline()
    print(content)
finally:
    # Will run in all conditions
    file.close()

# Raise Exception
hg = int(input("Height(M): "))
wg = int(input("Weight(KG): "))

bmi = wg / hg ** 2

if hg > 3:
    raise ValueError("Normal human height can't be more than 3 meters.")

print(bmi)