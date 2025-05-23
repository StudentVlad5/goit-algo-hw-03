# Завдання 1

import shutil
from pathlib import Path

def copy_and_sort_files(src_dir: Path, dest_dir: Path = Path("dist")):
    if not src_dir.is_dir():
        print(f"Шлях {src_dir} не є директорією або не існує.")
        return

    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Помилка створення директорії призначення: {e}")
        return

    try:
        for item in src_dir.iterdir():
            if item.is_dir():
                # Рекурсивно обробляємо підкаталоги
                copy_and_sort_files(item, dest_dir)
            elif item.is_file():
                # Визначаємо розширення файлу
                ext = item.suffix[1:] if item.suffix else "no_extension"
                target_subdir = dest_dir / ext

                try:
                    target_subdir.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, target_subdir / item.name)
                    print(f"Скопійовано: {item} → {target_subdir / item.name}")
                except PermissionError:
                    print(f"Доступ заборонено: {item}")
                except OSError as e:
                    print(f"Помилка копіювання файлу {item}: {e}")
    except Exception as e:
        print(f"Помилка читання директорії {src_dir}: {e}")


if __name__ == "__main__":
    source = Path("my_folder")        # Вихідна директорія
    destination = Path("vvv")        # Директорія призначення (необов'язково)

    # Можна викликати без другого аргументу: copy_and_sort_files(source)
    copy_and_sort_files(source, destination)
