import numpy as np 
import matplotlib.pyplot as p
import pylab

GMsun = 4*np.pi**2
R0vsun = 0.723 
R0esun = 1

tau_e = 1
tau_v = 0.6658

#earth - sun interaction 
def f_e(s,g,t1):
	x, y, vx, vy = s
	x_v, y_v, vx_v, vy_v = g
	c = np.array([s,g], float)
	a_corr = force_e(c)
	R = np.sqrt(x**2 + y**2)
	ax = ((-GMsun * x )/R ** 3) + a_corr[0]
	ay = ((-GMsun * y )/R ** 3) + a_corr[1]
	return np.array([vx, vy, ax, ay]) 

#venus - sun interaction 
def f_v(s,g,t2):
	x, y, vx, vy = s
	x_v, y_v, vx_v, vy_v = g
	c = np.array([s,g], float)
	a_corr = force_v(c)
	R1 = np.sqrt(x_v**2 + y_v**2)
	ax_v = (-GMsun * x_v )/R1 ** 3 + a_corr[0]
	ay_v = (-GMsun * y_v )/R1 ** 3 + a_corr[1]
	return np.array([vx_v, vy_v, ax_v, ay_v]) 

#force of venus on earth 
def force_e(c):
	s = c[0]
	g = c[1]
	R3 = np.sqrt((s[0]**2 + s[1]**2)**2 + (g[0]**2 + g[1]**2)**2)
	ax_e = (-9.65 * 10**(-5) * g[0] )/R3 ** 3 
	ay_e = (-9.65 * 10**(-5) * g[1] )/R3 ** 3 
	a_ve = np.array([ax_e, ay_e], float)
	return a_ve

#force of earth on venus
def force_v(c):
	s = c[0]
	g = c[1]
	R2 = np.sqrt((s[0]**2 + s[1]**2)**2 + (g[0]**2 + g[1]**2)**2)
	ax_v = (-1.445 * 10**(-4) * s[0] )/R2 ** 3 
	ay_v = (-1.445 * 10**(-4) * s[1] )/R2 ** 3 
	a_ev = np.array([ax_v, ay_v], float)
	return a_ev

a, b, N = 0.0,tau_e,1000 #run simulation for one orbital period 
h = (b-a)/N 

a, d, N = 0.0, tau_v, 1000
i = (d-a)/N

time = np.arange(a,b,h)
time_v = np.arange(a,d,i)

r0 = np.array([R0esun, 0.0], float)
r0_v = np.array([R0vsun, 0.0], float)

v0 = np.array([0.0, 2*np.pi], float)
v0_v = np.array([0.0, 5.5673], float)

s = np.array([r0[0], r0[1], v0[0], v0[1]])
g = np.array([r0_v[0], r0_v[1], v0_v[0], v0_v[1]])

c = np.array([s,g], float)

solution = np.empty(time.shape + s.shape,float)
solve = np.empty(time_v.shape + g.shape,float)

for j1,t1 in enumerate(time):
	solution[j1] = s
	solve[j1] = g
	k1 = h*f_e(s,t1,g)
	k2 = h*f_e(s+0.5*k1,t1+0.5*h, g+0.5*k1)
	k3 = h*f_e(s+0.5*k2,t1+0.5*h, g+0.5*k2)
	k4 = h*f_e(s+k3,t1+h, g+k3)
	c += (k1+2*k2+2*k3+k4)/6

x = solution[:,0]
y = solution[:,1]

for j2,t2 in enumerate(time_v):
	solution[j1] = s
	solve[j2] = g
	k1 = i*f_v(g,t2)
	k2 = i*f_v(g+0.5*k1,t2+0.5*i, s+0.5*k1)
	k3 = i*f_v(g+0.5*k2,t2+0.5*i, s+0.5*k2)
	k4 = i*f_v(g+k3,t2+i, s+k3)
	c += (k1+2*k2+2*k3+k4)/6

x_v = solve[:,0]
y_v = solve[:,1]

p.plot(x,y)
p.plot(x_v,y_v)
p.xlim(-1.5,1.5)
p.ylim(-1.5,1.5)
p.show()




