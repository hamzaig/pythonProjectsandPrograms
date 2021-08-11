with open('youtube.html') as webpage:
    with open("o.txt",'a') as wf:
        for line in webpage.readlines():
            if '<a href=' in line:
                pos=line.find("<a href=")
                first_q=line.find('\"',pos)
                last_q=line.find('\"',first_q+1)
                wf.write(url+'\n')
                url = line[first_q+1:last_q]
