import pynput 
import optparse
import random
import os

parser=optparse.OptionParser()
parser.add_option("-n","--number",dest="n",help="number of rows and columns")
parser.add_option("-w","--win",dest="win_no",help="Exponent of 2 greater than two reaching which you win")
(values,arguments)=parser.parse_args()


n=values.n
win_no=values.win_no

if type(n)==str:
	try:
		n=int(n)
	except ValueError:
		print("Invalid Input Hence we go with n=5")
		n=5
else: 
    n=5


if type(win_no)==str:
	try:
		win_no=int(win_no)
	except ValueError:
		print("Invalid Input Hence we go with w=2048")
else: 
	win_no=2048

if n==1:
	tyles=[0]
	if win_no==2:
		print("!!You won!!")
	else:
		print("!!!You lost!!!")
	
else:
    tyles= [[0]*n for x in range(n)]
    

def win(tyles=tyles, win_no=2048):
	flag=0
	for i in tyles:
		if win_no in i:
			flag=1
			break
	return flag

def end(tyles):
	flag=1
	for i in tyles:
		if 0 in i:
			flag=0
			break
	return flag

def custom_print(tyles):
	for i in tyles:
		print(i)

     


def up(tyles):
	for c in range(n):
		d=[]
	
		for i in tyles:
			if i[c]!=0:
				d.append(i[c])
		q=len(d)
		if q !=0:

			for x in range(q-1):
				if d[x]==d[x+1]:
					d[x]+=d[x+1]
					for k in range(x+1,q-1):
						d[k]=d[k+1]
					d[q-1]=0
					

			for p in range(len(d)):
				tyles[p][c]=d[p]

			for y in range(len(d),n):
				tyles[y][c]=0

def clear():

	if os.name=='nt':
		os.system('cls')
	else:
		os.system('clear')




def down(tyles):
	for c in range(n):
		d=[]
		for i in range(n-1,-1,-1):
			if tyles[i][c]!=0:
				d.append(tyles[i][c])
		q=len(d)
		if q !=0:

			for x in range(q-1):
				if d[x]==d[x+1]:
					d[x]+=d[x+1]
					for k in range(x+1,q-1):
						d[k]=d[k+1]
					d[q-1]=0
				
			for p in range(len(d)):
				tyles[n-p-1][c]=d[p]
			for y in range(n-len(d)):
				tyles[y][c]=0


def left(tyles):
		for c in range(n):
			d=[]

			for i in range(n):
				if tyles[c][i]!=0:
					d.append(tyles[c][i])
			q=len(d)
			if q !=0:

				for x in range(q-1):
					if d[x]==d[x+1]:
						d[x]+=d[x+1]
						for k in range(x+1,q-1):
							d[k]=d[k+1]
						d[q-1]=0
						
				for p in range(len(d)):
					tyles[c][p]=d[p]
				for y in range(len(d),n):
					tyles[c][y]=0

def right(tyles):
		for c in range(n):
			d=[]
			
			for i in range(n-1,-1,-1):
				if tyles[c][i]!=0:
					d.append(tyles[c][i])
			q=len(d)
			if q !=0:

				for x in range(q-1):
					if d[x]==d[x+1]:
						d[x]+=d[x+1]
						for k in range(x+1,q-1):
							d[k]=d[k+1]
						d[q-1]=0
						
				for p in range(len(d)):
					tyles[c][n-p-1]=d[p]
				for y in range(n-len(d)):
					tyles[c][y]=0


def fill(tyles):
    while True:
        column_no=random.choice(range(n-1))
        row_no=random.choice(range(n-1))
        if tyles[column_no][row_no]==0:
                 tyles[column_no][row_no]=2
                 break

fill(tyles)
custom_print(tyles)
print(" ")



from pynput.keyboard import Key, Listener 

def on_press(key): 



    try: 
        #print('alphanumeric key {0} pressed'.format(type(key.char))) 
        if key.char=='w':
           clear()
           up(tyles)
           fill(tyles)
           custom_print(tyles)
           print(' ')
        elif key.char=='a':
           clear()
           left(tyles)
           fill(tyles)
           custom_print(tyles)
           print(' ')
        elif key.char=='s':
        	clear()
        	fill(tyles)
        	down(tyles)
        	custom_print(tyles)
        	print(' ')

        elif key.char=='d':
        	clear()
        	fill(tyles)
        	right(tyles)
        	custom_print(tyles)
        	print(' ')
        else:
        	print("Invalid input")
        win_flag=win(tyles=tyles, win_no=win_no)
        if win_flag==1:
        	print("!!!You won!!!")
        	Key.esc
        end_flag=end(tyles)
        if end_flag==1:
        	print("!!!You Lost!!!")
        	Key.esc

    except AttributeError: 
        print('special key {0} pressed'.format(key)) 



def on_release(key): 

    if key == Key.esc: 

        # Stop listener 
        return False



with Listener(on_press = on_press, 
            on_release = on_release) as listener: 

    listener.join()