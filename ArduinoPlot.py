import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import math
import serial

arduino = serial.Serial('/dev/cu.wchusbserial1420', 9600)
fig, ax = plt.subplots(figsize=(19,7))
x, y = [],[] #initial of plot 
sc = ax.scatter(x,y)
plt.xlim(0,5)
plt.ylim(-60,60)

#plt.xlim(-np.pi * 4,np.pi * 4)
#plt.xlim(-1,1)
#plt.ylim(-2,2)


def animate(i):
	num = arduino.readline()
	num = num.decode('utf-8')
	a,b = num.split(',') #compatible with only np cython?
	#x.append(np.float(np.random.rand(1)*10))
	#y.append(np.float(np.random.rand(1)*10)) #using np cython string/int to float
	#x.append(np.float(np.cos(i * 4) * 100/10)) # possible to do translations
	#y.append(np.float(np.sin(i* 8) * 10/10)) #dividing can help decrease the distance between points i is an increment unit 
	x.append(np.float(a))
	y.append(np.float(b))
	sc.set_offsets(np.c_[x,y])
	#sc.set_offsets(np.c_[[1],[1]]) ##offsets updates points
	#>>> np.c_[np.array([1,2,3]), np.array([4,5,6])] forms array pairs 
#array([[1, 4],
       #[2, 5],
       #[3, 6]])

ani = matplotlib.animation.FuncAnimation(fig, animate, 
                frames=500, interval=50, repeat=True)
                
                #frames addsmore frames steps, but strangely works without it in python when using arduino like it runs out at one but still goes
                #interval is time each frame
                 
plt.show()

arduino.close()

#x.append(np.float(np.cos(i)*4/10)) # possible to do translations
#	y.append(np.float(np.sin(i)*8/10)) #dividing can help decrease the distance between points i is an increment unit 
#makes circle 
