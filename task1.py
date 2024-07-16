from queue import Queue
from random import randint

my_queue = Queue()

def generate_request():
    request = f"Request #{randint(1000, 9999)}"
    my_queue.put(request)
    print(f"{request} created")

def process_request():
    if my_queue.empty():
        print("queue is empty...")
    else:
        print(f"Executed: {my_queue.get()}")

print("Queue start")
while True:
    if input("Continue program? \n   >>> ").lower() == "yes":
        generate_request()
        process_request()
    else:
        print("Program ended")
        break