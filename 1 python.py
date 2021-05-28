numbers = input("Input 3 integer separated by commas: ") 
N = numbers.split(",")
ts = tuple(N)
remove_RI=set(ts)
if len(N)>3:
    print("Enter 3 number only")
elif len(remove_RI)==len(N):
    print(0)
else:
    print(4-len(remove_RI))

