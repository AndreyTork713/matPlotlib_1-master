import matplotlib.pyplot as plt

def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Построить линейный график

    plt.plot(x_coords, y_coords, marker='o')
    plt.title("Продажи с разбивкой по годам")
    plt.xlabel("Год")
    plt.ylabel("Объём продаж")
    # Настроить метки делений
    plt.xticks([0, 1, 2, 3, 4], [2017, 2018, 2019, 2020, 2021])
    plt.yticks([0, 1, 2, 3, 4, 5], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    plt.grid(True)

    # Показать линейный график
    plt.show()


if __name__ == '__main__':
    main()