from queue import Queue
import time

request_queue = Queue()
request_id_counter = 0

def generate_request():
    global request_id_counter
    request_id_counter += 1
    request = {"id": request_id_counter, "created_at": time.strftime("%Y-%m-%d %H:%M:%S")}
    request_queue.put(request)
    print(f"Створено заявку #{request['id']} о {request['created_at']}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється заявка #{request['id']} (створена: {request['created_at']})")
    else:
        print("Черга порожня. Немає заявок для обробки.")

def main():
    print("Система обробки заявок (Queue).")
    print("Команди:")
    print("  g - згенерувати нову заявку")
    print("  p - обробити одну заявку з черги")
    print("  q - вийти з програми")

    while True:
        command = input("Введи команду (g/p/q): ").strip().lower()
        if command == "g":
            generate_request()
        elif command == "p":
            process_request()
        elif command == "q":
            print("Завершення роботи програми.")
            break
        else:
            print("Невідома команда. Спробуй ще раз.")

if __name__ == "__main__":
    main()
