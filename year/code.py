def count_days(n):
    if n in [1,3,5,7,8,10,12]:
        return 31
    elif n in [4,6,9,11]:
        return 30
    elif n==2:
        return 28


