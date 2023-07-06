import os
import shutil
import concurrent.futures


def process_folder(path):
    # Отримуємо список всіх файлів та папок у поточній директорії
    items = os.listdir(path)

    # Розділяємо файли та папки
    files = [item for item in items if os.path.isfile(
        os.path.join(path, item))]
    folders = [item for item in items if os.path.isdir(
        os.path.join(path, item))]

    # Переміщуємо файли в папку з розширенням
    for file in files:
        extension = os.path.splitext(file)[1][1:]  # Отримуємо розширення файлу
        # Формуємо шлях до нового місця розташування
        destination = os.path.join(path, extension, file)
        # Створюємо папку з розширенням, якщо не існує
        os.makedirs(os.path.join(path, extension), exist_ok=True)
        shutil.move(os.path.join(path, file), destination)  # Переміщуємо файл

    # Рекурсивно обробляємо підкаталоги у окремих потоках
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for folder in folders:
            folder_path = os.path.join(path, folder)
            futures.append(executor.submit(process_folder, folder_path))

        # Очікуємо завершення всіх потоків
        for future in concurrent.futures.as_completed(futures):
            future.result()


# Вхідна точка програми
if __name__ == "__main__":
    # Шлях до папки, яку потрібно обробити
    folder_path = "Мотлох"
    process_folder(folder_path)
