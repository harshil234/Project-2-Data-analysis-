import csv
import matplotlib.pyplot as plt
with open('D:/[Coding Ninjas] Machine Learning and Data Science/10. Lecture 10 - Working With Files/20. Assignment/amazon.csv' , encoding="utf8") as file_obj:
    file_obj = csv.DictReader(file_obj , skipinitialspace = True)
    file_list = list(file_obj)
    dict = {}
    cnt1 = 0
    cnt2 = 0
    for row in file_list[1:]:
        key = row['Posting_date']
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 0

    search_key = 'Mar-18'
    cnt3 = 0
    for key in dict:
        if search_key in key:
            cnt3 += dict[key]

    print("March" , cnt3)

    search_key2 = 'Feb-18'
    cnt4 = 0
    for key in dict:
        if search_key2 in key:
            cnt4 += dict[key]

    print("February", cnt4)

    search_key3 = 'Jan-18'
    cnt5 = 0
    for key in dict:
        if search_key3 in key:
            cnt5 += dict[key]


    print("january" , cnt5)
    print(cnt3 + cnt4 + cnt5)
