def print_colored_circles(D, K, color_code=44, scale=2):
    """
    D - нечётный диаметр круга
    K - количество кругов
    color_code - код цвета фона
    scale - коэффициент масштабирования (по умолчанию 2 для более толстых кругов)
    """
    # Создаем последовательность для круга: 1,2,3,...,max,...,3,2,1
    mid = (D + 1) // 2
    n_i = list(range(1, mid + 1)) + list(range(mid - 1, 0, -1))
    
    # Применяем масштабирование
    n_i = [n * scale for n in n_i]
    M = max(n_i)  # максимальная ширина после масштабирования
    
    for i in range(D):
        for k in range(K):
            # Вычисляем отступы для центрирования
            left_pad = (M - n_i[i]) // 2
            right_pad = M - n_i[i] - left_pad
            
            # Печатаем левый отступ
            print(' ' * left_pad, end='')
            
            # Печатаем закрашенную часть круга цветными пробелами
            print(f'\x1b[{color_code}m' + ' ' * n_i[i] + '\x1b[0m', end='')
            
            # Печатаем правый отступ
            print(' ' * right_pad, end='')
            
            # Добавляем пробелы между кругами
            if k < K - 1:
                print(' ' * scale, end='')  # Увеличиваем промежуток пропорционально масштабу
        print()

# Примеры с масштабированием:

print("Диаметр 9, синий цвет, масштаб 2:")
print_colored_circles(D=9, K=3, color_code=44, scale=2)

print("\n" + "="*70 + "\n")

print("Диаметр 7, красный цвет, масштаб 2:")
print_colored_circles(D=7, K=4, color_code=41, scale=2)

print("\n" + "="*70 + "\n")

print("Диаметр 11, зелёный цвет, масштаб 2:")
print_colored_circles(D=11, K=2, color_code=42, scale=2)

print("\n" + "="*70 + "\n")

# Можно экспериментировать с разными масштабами
print("Диаметр 9, magenta, масштаб 3 (еще толще):")
print_colored_circles(D=9, K=3, color_code=45, scale=3)