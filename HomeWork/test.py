import csv


def read_csv_file(file_name):
    """Читає CSV-файл та повертає список рядків."""
    rows = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


def generate_unique_ids(data):
    """Генерує унікальні айді для кожного запису та повертає словник з айдішниками та даними."""
    id_index = {}
    for row in data:
        unique_id = hash(tuple(row))  # Генеруємо унікальний ID на основі даних рядка
        id_index[unique_id] = {
            'model': row[0],
            'category': row[1],
            'brand': row[2],
            'price': row[3]
        }
    return id_index


def generate_category_index(data):
    """Генерує індекс за категоріями та повертає словник з категоріями та списком айдішників."""
    category_index = {}
    for row in data:
        category = row[1]
        unique_id = hash(tuple(row))
        if category in category_index:
            category_index[category].append(unique_id)
        else:
            category_index[category] = [unique_id]
    return category_index


def generate_brand_index(data):
    """Генерує індекс за брендами та повертає словник з брендами та списком айдішників."""
    brand_index = {}
    for row in data:
        brand = row[2]
        unique_id = hash(tuple(row))
        if brand in brand_index:
            brand_index[brand].append(unique_id)
        else:
            brand_index[brand] = [unique_id]
    return brand_index


def print_brand_category_stats(data):
    """Виводить статистику кількості товарів за брендами та категоріями."""
    brand_stats = {}
    category_stats = {}

    for row in data:
        brand = row[2]
        category = row[1]

        if brand in brand_stats:
            brand_stats[brand] += 1
        else:
            brand_stats[brand] = 1

        if category in category_stats:
            category_stats[category] += 1
        else:
            category_stats[category] = 1

    print("Статистика за брендами:")
    for brand, count in brand_stats.items():
        print(f"{brand}: {count} товарів")

    print("\nСтатистика за категоріями:")
    for category, count in category_stats.items():
        print(f"{category}: {count} товарів")


def print_items_by_brand_and_category(data, brand, category):
    """Виводить повну інформацію про товари вибраного бренда та категорії."""
    print(f"Товари бренда '{brand}' у категорії '{category}':")
    for row in data:
        if row[2] == brand and row[1] == category:
            print(f"Модель: {row[0]}, Ціна: {row[3]}")


def calculate_brand_distribution(data):
    """Розраховує розподіл товарів по брендам для кожної категорії."""
    category_brand_distribution = {}

    for row in data:
        brand = row[2]
        category = row[1]

        if category in category_brand_distribution:
            if brand in category_brand_distribution[category]:
                category_brand_distribution[category][brand] += 1
            else:
                category_brand_distribution[category][brand] = 1
        else:
            category_brand_distribution[category] = {brand: 1}

    print("\nРозподіл товарів по брендам для кожної категорії:")
    for category, distribution in category_brand_distribution.items():
        print(f"\nКатегорія: {category}")
        for brand, count in distribution.items():
            print(f"{brand}: {count} товарів")


def main():
    file_name = 'tech_inventory.csv'
    rows = read_csv_file(file_name)

    id_index = generate_unique_ids(rows)
    category_index = generate_category_index(rows)
    brand_index = generate_brand_index(rows)

    print_brand_category_stats(rows)

    brand = input("Введіть назву бренду: ").title()
    category = input("Введіть назву категорії: ").title()
    print_items_by_brand_and_category(rows, brand, category)

    calculate_brand_distribution(rows)


if __name__ == '__main__':
    main()
