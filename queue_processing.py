import queue
import time
import random

# Створити чергу заявок
request_queue = queue.Queue()

# Змінна для відстеження номеру заявки
request_counter = 0

# Функція генерації нової заявки
def generate_request():
    global request_counter
    request_counter += 1
    # Створити нову заявку
    new_request = {"id": request_counter, "timestamp": time.time()}
    # Додати заявку до черги
    request_queue.put(new_request)
    print(f"Request {new_request['id']} added to queue.")

# Функція обробки заявки
def process_request():
    if not request_queue.empty():
        # Видалити заявку з черги
        processed_request = request_queue.get()
        # Імітуємо обробку заявки
        print(f"Request {processed_request['id']} processed.")
    else:
        print("Queue is empty. Waiting for new requests.")

# Головний цикл програми
try:
    while True:
        # Випадково визначаємо, чи створювати нову заявку для більш випадкового наповнення черги
        if random.choice([True, False]):
            # Виконати generate_request() один раз або двічі для створення нових заявок
            generate_request()
            if random.choice([True, False]):
                generate_request()

        # Виконати process_request() для обробки заявок
        process_request()
        # Затримка перед генерацією нової заявки або обробкою
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user.")