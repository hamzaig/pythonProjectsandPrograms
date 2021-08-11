from csv import DictReader
with open("comma.csv","r") as rf:
    csv_reader=DictReader(rf,delimiter=",")
    for i in csv_reader:
        print(i)
        print(i["email"])
        