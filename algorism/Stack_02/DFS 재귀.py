def func(n):
    if n <= 3:
        func(n+1)
        print(f'{n}번째 함수 발동!')

func(1)