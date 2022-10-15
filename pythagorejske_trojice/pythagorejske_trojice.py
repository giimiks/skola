for a in range(1, 100):
    for b in range(a+1, 100):
        for c in range(1, 100):
            if not a ** 2 + b ** 2 != c ** 2:
                print(f'{a}; {b}; {c}')
