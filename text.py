import sys
# url = sys.stdin.readline()
# To store input here (0 1 1)  and (0 1 2).
# l=[]
t = 37
while t:
    #To store the size of array here (3).
    url = sys.stdin.readline()
    x = url.split('/')
    new_text = "https://surfrider-test.herokuapp.com/" + x[5]
    print(new_text)
    # for i in range(0 ,n):
    #     b=int(a[i])
    #     l.append(b)
    # #Do your job with the list l here just print !
    # print l
    # l=[] #empty list for next input ie (0 1 2).
    t=t-1