import time
def countdown(t):
    while t:
        mins , secs = divmod(t,60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer ,end="\r")
        time.sleep(1)
        t -= 1
    # after loop
    print("Timer completed!")



t = input("Enter Ur Number :::: ")

countdown(int(t))














