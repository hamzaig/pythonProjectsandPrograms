from csv import writer
with open("wcomma.csv","w",newline="") as wf:
    csv_writer=writer(wf)
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['hamza','Pakistan'])
    # csv_writer.writerow(['ali','Pakistan'])
    csv_writer.writerows([['name','country'],['hamza','Pakistan'],['Atif','Pakistan']])