def main():

    names = ['Эйнштейн', 'Ньютон', 'Коперник', 'Кеплер']
    for name in names:
        print(name)

    if 'Руби' in names:
        print('Привет, Руби!')
    else:
        print('Руби отсутствует.')

    numbers1 = []
    count = 1
    while count < 101:
        numbers1.append(count)
        count += 1
    print(numbers1)

    numbers2 = [] + numbers1
    print(numbers2)

    def sum_list(test_list):
        total_sum = sum(test_list)
        print(total_sum)

    sum_list(numbers1)


if __name__ == '__main__':
    main()