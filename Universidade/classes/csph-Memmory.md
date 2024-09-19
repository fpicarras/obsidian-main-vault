***
> A very big problem with memory (RAM) is the time it takes to access the data, there are three common solutions:

- Caches - which approximate the data from the cores.

- Compiler optimizations - the compiler attempts to optimize fetch instructions and stores in parts of the code that are not dependant.

- Multi-threading - With hide the latency to access the memory by using the stall intervals to run other threads/processes in the same core.

# Caches

# Compiler Optimizations

# Memory

Each core can run 1 thread at a time, but, we can use the stall times to run other processes. This is done by having bigger register banks (**Execution Context**)