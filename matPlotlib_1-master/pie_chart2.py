import matplotlib.pyplot as plt


def main():

    # Список объемов продаж
    sales = [100, 400, 300, 600]

    # Список меток долей
    slice_labels = ['I квартал', 'II квартал', 'III квартал', 'IV квартал']

    # Создать из этих значений круговую диаграмму
    plt.pie(sales, labels=slice_labels)

    # Добавить заголовок
    plt.title('Продажи с разбивкой по кварталам')

    # Показать диаграмму
    plt.show()


if __name__ == '__main__':
    main()