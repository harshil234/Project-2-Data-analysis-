import csv
import matplotlib.pyplot as plt
with open('D:/[Coding Ninjas] Machine Learning and Data Science/10. Lecture 10 - Working With Files/20. Assignment/amazon.csv' , encoding="utf8") as file_obj:
    file_obj = csv.DictReader(file_obj , skipinitialspace = True)
    file_list = list(file_obj)
    dict = {}
    cnt1 = 0
    cnt2 = 0
    for row in file_list[1:]:
        key = row['BASIC QUALIFICATIONS']
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 0

    search_key3 = 'BA'
    search_key2 = 'BS'
    search_key1 = 'Bachelor'
    cnt5 = 0
    for key in dict:
        if search_key3 in key or search_key2 in key or search_key1 in key :
            cnt5 += dict[key]

    print("Bachlers" , cnt5)
