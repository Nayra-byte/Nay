print("Enter marks obtained in 4 subjects")
english=int(input("english:" ))
SST=int(input("SST:" ))
math=int(input("math:" ))
science=int(input("science:" ))
sum=science+math+SST+english
print("The total marks obtained are: ",sum)
perc=(sum/400)*100
print("The percentage is:",perc)