from time import sleep
for i in range(1,15,2):
    s = i+2
    print("{:^33}".format(i*"i"))
    print("{:^33}".format(s*"i"))
sleep(.75)