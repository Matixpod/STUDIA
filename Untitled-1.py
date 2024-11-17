class test(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y 


    def add(self, z):
        return self.x + self.y + z
    
    def multiply(self, z):
        return self.x * self.y * z


# test(2,4).multiply(3)

import time
import sys

def loading_bar(total, length=30):
    for i in range(total):
        # Procent postępu
        percent = (i + 1) / total
        # Ilość znaków do wyświetlenia
        filled_length = int(length * percent)
        # Pasek ładowania
        bar = '█' * filled_length + '-' * (length - filled_length)
        # Wyświetlanie paska z procentami
        sys.stdout.write(f'\r{bar} {int(percent * 100)}%')
        sys.stdout.flush()
        # Symulacja opóźnienia
        time.sleep(0.1)

    # Zakończenie linii po zakończeniu paska
    print("\nŁadowanie zakończone!")

# Wywołanie paska ładowania
loading_bar(100)




