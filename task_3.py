def move_disks(n, source, target, auxiliary, towers):
    if n == 1:
        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {towers}")
    else:
        move_disks(n - 1, source, auxiliary, target, towers)
        move_disks(1, source, target, auxiliary, towers)
        move_disks(n - 1, auxiliary, target, source, towers)

def main():
    try:
        n = int(input("Введіть кількість дисків: "))
        if n <= 0:
            print("Будь ласка, введіть число більше за 0.")
            return
    except ValueError:
        print("Введіть коректне ціле число.")
        return

    # Початковий стан
    towers = {
        'A': list(range(n, 0, -1)),  # [n, ..., 2, 1]
        'B': [],
        'C': []
    }

    print(f"Початковий стан: {towers}")
    move_disks(n, 'A', 'C', 'B', towers)
    print(f"Кінцевий стан: {towers}")

if __name__ == "__main__":
    main()
