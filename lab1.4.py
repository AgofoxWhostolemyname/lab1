def analyze_sequence():
        with open('sequence.txt', 'r', encoding='utf-8') as file:
            numbers = []
            for line in file:
                clean_line = line.strip()
                if clean_line: 
                        number = float(clean_line)
                        numbers.append(number)
                        continue

            filtered_numbers = []
            for num in numbers:
                if (5 <= num <= 10) or (-10 <= num <= -5):
                    filtered_numbers.append(num)
        
        positive_count = 0
        negative_count = 0
        
        for num in filtered_numbers:
            if num > 0:
                positive_count += 1
            else:
                negative_count += 1
        
        total_count = len(filtered_numbers)
        
        positive_percent = (positive_count / total_count) * 100
        negative_percent = (negative_count / total_count) * 100

        print("РЕЗУЛЬТАТЫ АНАЛИЗА:")
        print(f"Диапазон [5;10]:    {positive_percent:6.1f}% ({positive_count} чисел)")
        print(f"Диапазон [-10;-5]:  {negative_percent:6.1f}% ({negative_count} чисел)")
        print(f"Всего подходящих чисел: {total_count}")
        
        print("\nГРАФИК:")
        bar_length = 30
        pos_bar = " " * int(positive_percent * bar_length / 100)
        neg_bar = " " * int(negative_percent * bar_length / 100)
        
        print(f"[5;10]   \x1b[48;5;124m{pos_bar} {positive_percent:.1f}%\x1b[0m")
        print(f"[-10;-5] \x1b[48;5;27m{neg_bar} {negative_percent:.1f}%\x1b[0m")
        

analyze_sequence()