#masih ngerasa codenya tidak optimal secara struktur
def tambahMundur(x, y):
    try: #reversing variabel x, belum ada error handling
	    reverseX = int(str(x)[::-1])
	    print('Angka 1 Yang Dibalik : ', reverseX)
    except ValueError: #error handling variable x
	    print('Invalid Input!')
    
    try: #reversing variable y, belum ada error handling
	    reverseY = int(str(y)[::-1])
	    print('Angka 2 Yang Dibalik : ', reverseY)
    except ValueError: 
	    print('Invalid Input!')
    
    totalReverse = reverseX + reverseY
    print('Total Value Angka Yang Dibalik :', totalReverse)
    
x = int(input('Masukkan Angka 1 : '))
y = int(input('Masukkan Angka 2 : '))

tambahMundur(x, y)