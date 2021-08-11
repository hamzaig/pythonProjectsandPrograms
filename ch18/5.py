from csv import reader

with open("comma.csv",'r') as rf:
    csv_reader=reader(rf)
    next(csv_reader)
    for i in csv_reader:
        print(i)
