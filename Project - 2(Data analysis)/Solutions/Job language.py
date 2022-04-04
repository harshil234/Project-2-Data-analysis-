import csv
with open('D:/[Coding Ninjas] Machine Learning and Data Science/10. Lecture 10 - Working With Files/20. Assignment/amazon.csv' , encoding="utf8") as file_obj:
    file_obj = csv.DictReader(file_obj , skipinitialspace = True)
    file_list = list(file_obj)
    dict = {}
    cnt1 = 0
    cnt2 = 0
    dict2 = {}
    for row in file_list[1:]:
        key = row['BASIC QUALIFICATIONS']
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 0

    search_key = 'BA'
    search_key2 = 'C++'
    res = [val for key, val in dict.items() if search_key in key and search_key2 in key]
    for i in range(len(res)):
        cnt2 += res[i]
    print("C++" , cnt2)

    cnt3 = 0
    search_key4 = 'Java'
    res2 = [val for key, val in dict.items() if search_key in key and search_key4 in key]
    for i in range(len(res2)):
        cnt3 += res2[i]
    print("Java" , cnt3)

    cnt4 = 0
    search_key6 = 'Python'
    res3 = [val for key, val in dict.items() if search_key in key and search_key6 in key]
    for i in range(len(res3)):
        cnt4 += res3[i]
    print("Python" , cnt4)
