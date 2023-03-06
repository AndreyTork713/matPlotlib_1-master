import matplotlib.pyplot as plt

def main():
    # список с координатами левого края
    left_adges = [0, 10, 20, 30, 40]

    # список с высотами каждого столбика
    heights = [100, 200, 300, 400, 500]

    # Ширина столбиков
    bar_width = 5

    # Построить гистограмму
    plt.bar(left_adges, heights, bar_width, color=('r', 'g', 'b', 'y'))
    plt.title("Продажи с разбивкой по годам")
    plt.xlabel("Год")
    plt.ylabel("Объём продаж")
    # plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()