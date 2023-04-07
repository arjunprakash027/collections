try:
    k = "10"
    print(k + 10)
except ZeroDivisionError:
    k = 20
    print(k)
except TypeError:
    k = int(k)
    print(k+10)
except SyntaxError:
    print("you gave the wrong systax")


def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A arjun is a very great programmer') from e
  

try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)
    if e.__cause__:
        print('Cause:', e.__cause__)


try:
    f = open("filename")
except (FileNotFoundError,PermissionError,NameError):
    raise FileNotFoundError("pls check")