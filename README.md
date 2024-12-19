This is a simple, Maxwell's Equations based simulation of light waves. All derivatives are calculated through numpy and the third dimension has a size of one allowing for fast computation. Since the third dimension does still exist, Maxwell's equations could be implemented without needing significant modification. The simulation also uses permittivity, permeability, and conductivity data. Here is the form of Maxwell's Equations that is used:

![alt text](https://www.maxwells-equations.com/EH-maxwells.gif)

There are four main parts to running the simulation:
  1. The permittivity (E), permeability (U), and conductivity (O) data must be defined. The 2d array sizes for the data must be the same as the grid size used in the simulation
  2. The simulation must be initialized with all of the defined data from above (e.g. sim = baseSim.Sim2D(X_Size, Y_Size, gridlenth, E, U, O, timestep)
  3. A loop must be made that first runs Sim2d.calcPartials(time) and then runs Sim2d.iterate(). The time parameter is used to calculated the initial condition that forms the light waves at the top (x = 0) part of the simulation. iterate() updates the values of the simulation.
  4. The numpy arrays storing data in the simulation get updated with each iteration. Thus, any information that needs to be saved while the simulation is running must be saved to a user added data structure before iterate() is called again. In the example file electroMagExample.py, information is saved into a matplotlib image every 50 iterations. These images are then placed into an animation which is shown at the end of the script.
