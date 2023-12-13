import time

timing1 = int(input("write any number: "))

for x in range(timing1,0,-1):
    seconds=x % 60 
    minutes=int(x / 60) % 60
    hours=int(x/3600) 
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)
print("Job Done!")