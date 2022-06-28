# Создайте словарь генератором (где ключами и значениями будут числа от 1 до 9) и отобразите таблицу умножения.
dictionary = {i: i for i in range(1, 10)}   # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

for key in dictionary.keys():
    for value in dictionary.values():
        print(key * value, end="\t")
    print()
"""
1	2	3	4	5	6	7	8	9	
2	4	6	8	10	12	14	16	18	
3	6	9	12	15	18	21	24	27	
4	8	12	16	20	24	28	32	36	
5	10	15	20	25	30	35	40	45	
6	12	18	24	30	36	42	48	54	
7	14	21	28	35	42	49	56	63	
8	16	24	32	40	48	56	64	72	
9	18	27	36	45	54	63	72	81	
"""