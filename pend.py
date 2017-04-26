#########################################################################################
#	Computational Physics HW6 Problem 1
#	
#	This program uses various numerical methods to solve for the motion of a non-linear 
# 	pendulum 
#
#	Units: 
#	Acceleration due to gravity (g) : m/s 
#	Length of pendulum (l) : m
#	Intial displacement angle (theta) : degrees (converted to radians later in code)
#	Initial angular velocity (omega) : rad/s
#
#	Written by Jacqueline Antwi-Danso 04/17
#########################################################################################
import pylab
import numpy as np 
import matplotlib.pyplot as p
import matplotlib.animation as animation

method = ['4ORunge-Kutta', 'Leap Frog']
theta0 = [-174.0, 87.0]
color = ['blue', 'black']

for i, solve in enumerate(method):

	#initial conditions and constants
	g = 9.8
	l = 0.18
	omega0 = -(g/l)*np.sin(theta0[i]*np.pi/180)

	#differential equations to be solved 
	def f(r,t):
		theta = r[0]
		omega = r[1]
		ftheta = omega 
		fomega = -(g/l)*np.sin(theta*np.pi/180)
		return np.array([ftheta,fomega],float) 

	a, b, N = 0.0, 100.0, 2300 #large N because Leap Frog is less accurate 
	h = (b-a)/N
	time = np.arange(a,b,h)
	angle = []
	r = np.array([theta0[i], omega0], float)

	
	for t in time:
		angle.append(r[0])
		k1 = h*f(r,t)
		k2 = h*f(r+0.5*k1,t+0.5*h)
		if solve == '4ORunge-Kutta':
			k3 = h*f(r+0.5*k2,t+0.5*h)
			k4 = h*f(r+k3,t+h)
			r += (k1+2*k2+2*k3+k4)/6
		else:
			k3 = (0.5*k1) + h*f(r+k2,t+h)
			r += k3

	#plots
	p.plot(time, angle, label=solve, color=color[i])
	legend = pylab.legend(loc='upper right', fontsize=7)
	p.title('Angular displacement of non-linear pendulum over time')
	p.xlabel('Time (s)')
	p.ylabel('$\\theta$ ($^\circ$)')

	#animation
	fig = p.figure()
	fig.set_size_inches(6.5, 6.5, forward=False) #make grids square so pendulum length does not appear to change
	ax = fig.add_subplot(111, autoscale_on=False, xlim=(-l-0.1, l+0.1), 
		ylim=(-l-0.1, l+0.1))
	ax.grid()
	line, = ax.plot([], [], 'o-', lw=2, ms=15)
	#display time passage at top of animation
	time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
	time_template = 'time = %.1fs'

	def init():
		line.set_data([], [])
		time_text.set_text('')
		return line, time_text

	def animate(j):
		#convert to cartesian coordinates
		x = [0, -l*np.cos(angle[j]*np.pi/180)]
		y = [0,	l*np.sin(angle[j]*np.pi/180)]
		line.set_data(y, x) #flipped to simulate reality
		time_text.set_text(time_template % (j*h))
		return line, time_text

	ani = animation.FuncAnimation(fig, animate, np.arange(0, len(time),1),
                              interval=25, blit=False, init_func=init)
	
	p.show()

	#note : to display subsequent plots/animations, just clost current window. 







