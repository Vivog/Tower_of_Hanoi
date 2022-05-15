# This script show's right moves for win this game
def hanoy(n,x,y,z):
    if n == 1:
        print (f'{x} - {z}')
        return
    hanoy(n-1, x, z, y)
    print(f'{x} - {z}')
    hanoy(n-1, y, x, z)
# Input n-numbers of disk's
n = int(input())
hanoy(n,'1','2','3')