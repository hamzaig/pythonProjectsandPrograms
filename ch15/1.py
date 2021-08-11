def even_gen(n):
    for i in range(1,n+1):
        if i%2==0 :
            yield(i)

print(even_gen(20))
for i in even_gen(20):
    print(i)