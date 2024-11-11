import time as tm
import threading as thr
from datetime import datetime as dt

def write_words(words_count, file_name):
    file = open(file_name, 'w', encoding= 'utf-8')
    for i in range(words_count):
        file.write(f'Какое-то слово № {i+1} \n')
        tm.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start = dt.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

finish = dt.now()

print(f'Работа потоков: {finish - start}')

start_2 = dt.now()

thread1 = thr.Thread(target= write_words, args=(10, 'example5.txt', ))
thread2 = thr.Thread(target= write_words, args=(30, 'example6.txt', ))
thread3 = thr.Thread(target= write_words, args=(200, 'example7.txt', ))
thread4 = thr.Thread(target= write_words, args=(100, 'example8.txt', ))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

finish_2 = dt.now()

print(f'Работа потоков: {finish_2-start_2}')

print(f'Разница работы потоков и последовательных функций: {((finish-start) - (finish_2-start_2))}')


