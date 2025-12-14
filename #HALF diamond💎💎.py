rs=int(input("enter the number of rows you want: "))
if rs%2== 0:
    hd=int(rs/2)
else:
    hd=int(rs/2)+1
sp=hd-1
for i in range(1,hd+1):
    for j in range(1,sp+1):
        print(end=" ")
        sp=sp-1
        n=1
        for j in range(2*i-1):
            print(end=str(n))
            n=n+1
        print()
        sp=1
        for i in range (1,hd):
            for j in range(1,sp+1):
                print(end=" ")
                sp=sp+1
                n=1
                for j in range(1,2*(hd-i)):
                    print(end=str(n))
                    n=n+1
                print()
