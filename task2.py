from collections import deque

dq = deque()
text = input("Введіть рядок \n   >>> ").lower().replace(" ", "")
for charecter in text:
    dq.append(charecter)


def is_palindrom():
    for i in range(int(len(dq)/2)):
        if dq.pop() != dq.popleft():
            return False
    return True

if is_palindrom():
    print(f"{text} - паліндром")
else:
    print(f"{text} - не паліндром!")