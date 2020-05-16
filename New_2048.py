import pynput 
import optparse
import random

parser=optparse.OptionParser()
parser.add_option("-n","--number",dest="n",help="number of rows and columns")
parser.add_option("-w","--win",dest="win_no",help="Exponent of 2 greater than two reaching which you win")
(values,arguments)=parser.parse_args()


n=values.n
win_no=values.win_no

if type(n)=='str':
	n=int(n)
else: 
    n=5


if type(win_no)=='str':
	win_no=int(win_no)
else: 
	win_no=2048


tyles= [[0]*n for x in range(n)]


def win(tyles=tyles, win_no=2048):
	flag=0
	for i in tyles:
		if win_no in i:
			flag=1
			break
	return flag

def custom_print(tyles):
	for i in tyles:
		print(i)

     

#def up(tyles):
#	for i in range(n):
 #   	for t in range(n-1):
  # 			if tyles[t][i]==tyles[t+1][i] and tyles[t][i]!=0:
   #     		tyles[t][i]+=tyles[t+1][i]
   	#   			for x in range(t+1,n-1):
    #				tyles[x][i]=tyles[x+1][i]
    #			tyles[n-1][i]=0
    #		elif tyles[t][i]==0:
    #			for x in range(t,n-1):
    #				tyles[x][i]=tyles[x+1][i]
    #			tyles[n-1][i]=0

def up(tyles):
	for c in range(n):
		d=[]
		#final=[]
		for i in tyles:
			if i[c]!=0:
				d.append(i[c])
		q=len(d)
		for x in range(q-1):
			if d[x]==d[x+1]:
				d[x]+=d[x+1]
				for k in range(x+1,q-1):
					d[k]=d[k+1]
				d[q-1]=0
				#d[x]+=d[x+1]
				##d.pop(x+1)  for k i
				#final.append(d[x]+d[x+1])
		for p in range(len(d)):
			tyles[p][c]=d[p]
		for y in range(len(d),n):
			tyles[y][c]=0


def down(tyles):
	for c in range(n):
		d=[]
		#final=[]
		for i in range(n-1,-1,-1):
			if tyles[i][c]!=0:
				d.append(tyles[i][c])
		q=len(d)
		for x in range(q-1):
			if d[x]==d[x+1]:
				d[x]+=d[x+1]
				for k in range(x+1,q-1):
					d[k]=d[k+1]
				d[q-1]=0
				#d[x]+=d[x+1]
				##d.pop(x+1)  for k i
				#final.append(d[x]+d[x+1])
		for p in range(len(d)):
			tyles[n-p-1][c]=d[p]
		for y in range(n-len(d)):
			tyles[y][c]=0


def left(tyles):
		for c in range(n):
			d=[]
			#final=[]
			for i in range(n):
				if tyles[c][i]!=0:
					d.append(tyles[c][i])
			q=len(d)
			for x in range(q-1):
				if d[x]==d[x+1]:
					d[x]+=d[x+1]
					for k in range(x+1,q-1):
						d[k]=d[k+1]
					d[q-1]=0
					#d[x]+=d[x+1]
					##d.pop(x+1)  for k i
					#final.append(d[x]+d[x+1])
			for p in range(len(d)):
				tyles[c][p]=d[p]
			for y in range(len(d),n):
				tyles[c][y]=0

def right(tyles):
		for c in range(n):
			d=[]
			#final=[]
			for i in range(n-1,-1,-1):
				if tyles[c][i]!=0:
					d.append(tyles[c][i])
			q=len(d)
			for x in range(q-1):
				if d[x]==d[x+1]:
					d[x]+=d[x+1]
					for k in range(x+1,q-1):
						d[k]=d[k+1]
					d[q-1]=0
					#d[x]+=d[x+1]
					##d.pop(x+1)  for k i
					#final.append(d[x]+d[x+1])
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
           up(tyles)
           custom_print(tyles)
           print(' ')
        elif key.char=='a':
           left(tyles)
           custom_print(tyles)
           print(' ')
        elif key.char=='s':
            down(tyles)
            custom_print(tyles)
            print(' ')
        elif key.char=='d':
            right(tyles)
            custom_print(tyles)
            print(' ')
        
    except AttributeError: 
        print('special key {0} pressed'.format(key)) 
        
            
def on_release(key): 
                    
    if key == Key.esc: 
        # Stop listener 
        return False

    fill(tyles)
    custom_print(tyles)
    print(' ')


with Listener(on_press = on_press, 
            on_release = on_release) as listener: 
                    
    listener.join() 