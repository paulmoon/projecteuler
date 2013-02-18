import time

def check(n):
    n_list = [x for x in str(n)]
    return sorted(n_list)

def main():
    start = time.clock()
    i = 0
    found = False

    while not found:
        for j in range(10**i, ((10**(i+1))//6)+1):
            if check(j) == check(j*2) == check(j*3) == check(j*4) == check(j*5) == check(j*6):
                found = True
                break
        i += 1
    print (j)
    print (time.clock() - start)

if __name__ == '__main__':
    main()
