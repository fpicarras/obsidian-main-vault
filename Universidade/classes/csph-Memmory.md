***
> A very big problem with memory (RAM) is the time it takes to access the data, there are three common solutions:

- [[Cache]] - which approximate the data from the cores.

- Compiler optimizations - the compiler attempts to optimize fetch instructions and stores in parts of the code that are not dependant.

- Multi-threading - With hide the latency to access the memory by using the stall intervals to run other threads/processes in the same core.
# Compiler Optimizations

# Multi-Threading

Each core can run 1 thread at a time, but, we can use the stall times to run other processes. This is done by having bigger register banks (**Execution Context**)

## Bandwidth

> Te rate at which the memory system can provide data to a processor, example: 20GB/s.

**Latency** is the amount of time it takes to for the first set of data to arrive.
We can use data pipelining ([[cpsh-Pipeline]])to increase bandwidth.

### GPU's
GPU's have lower memory capacities but they have way better memory-cores interfaces, allowing for bigger bandwidths. This happens because they invest way more on communication.
There is a lot of switching between warps in a GPU so having a huge bandwidth is a must!!