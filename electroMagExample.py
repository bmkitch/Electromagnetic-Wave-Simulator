import numpy as np
import baseSim
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import tqdm

"""
This is an example run of the electromagnetism simulation
simualtion initialization: lines 25-50
main loop: lines 58-70
plotting: lines 65-77
"""

"""
this is a field that can be added to the simulation. It represents a higher density area that will bend the light waves.
If implemented, it would replace the solid object with a hole as defined on lines 35-50. The user would have to determine
if the function modifies E (permitivity), U (permeability), O (conductivity), or some combination of the three. Of course,
new functions can be defined and used.
"""
def createField(size):
    F = np.zeros((size, size, size))

    for x in range(1, size - 2):
        for y in range(1, size - 2):
            for z in range(1, size - 2):
                F[x][y][z] = 1 / (1 + 0.01*((x - size/2)*(x - size/2) + (y-size/2)*(y-size/2) + (z-size/2)*(z-size/2)))

    return F



size = 200

E = np.full((size, size), 1)
U = np.full((size, size), 1)
O = np.zeros((size, size))

E[50:60,0:90] = 3
E[50:60,110:199] = 3
E[50:60,90] = 1.5
E[50:60,109] = 1.5


U[50:60,0:90] = 3
U[50:60,110:199] = 3
U[50:60,90] = 1.5
U[50:60,109] = 1.5


O[50:60,0:90] = 0.5
O[50:60,110:190] = 0.5
O[50:60,90] = 0.25
O[50:60,109] = 0.25

#SIMULATION INITIALIZATION
sim = baseSim.Sim2D(size, size, 1, E, U, O, 0.01)

#creating array and subplots that will store animation
fig, pic = plt.subplots()
imageArray = []

#MAIN LOOP
numOfIter = 20001
for x in tqdm.tqdm(range(numOfIter)):

    #Calculate partions must run before iterate(). This allows differential to be found for maxwell's equations
    sim.calcPartials(x)
    sim.iterate()

    if(x % 50 == 0):
        image = pic.imshow(sim.electricY, extent=(0, size-1, size-1, 0),
            interpolation='nearest', cmap=cm.gist_rainbow, vmin=-3, vmax=3)
        imageArray.append([image])


ani = animation.ArtistAnimation(fig, imageArray, interval=50, blit=True,
                                repeat_delay=1000)
plt.title("Y Component of Electric Field")
plt.ylabel("X")
plt.xlabel("Y")
plt.show()