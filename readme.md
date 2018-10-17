# Analysis of Graph's generated from Quantum Lattice

Starting from a toy-hamiltonian model, we generate hoppig amplitudes from lattice sites i to j (currently for a one-dimensional system). 

Using the inverse amplitudes as weights, we create a fully connected graph with each eash lattice site serving as a node. 

Various network algorithms are run on the generated graph. 

## To-Do
- Ramp up Node count t oget ride of finite size effects
- Currently only focusing one 1-d chain. Start looking into 2-d and 3-d models and the possible representations
- Prootyped using python and networkx. Future iterations will require more parallelism so will look into c++ implementations if results look promising
- Add small-worldedness, clustering classification 
- Some new data
