***
> A very big problem with memory (RAM) is the time it takes to access the data, there are three common solutions:

- [[Cache]] - which approximate the data from the cores.

- Compiler optimizations - the compiler attempts to optimize fetch instructions and stores in parts of the code that are not dependant.

- Multi-threading - With hide the latency to access the memory by using the stall intervals to run other threads/processes in the same core.
# Compiler Optimizations

All modern CPUs have logic for prefetching data into caches - Dynamically analyse program’s access pattern, predict what it will access soon.
Note: Prefetching can also reduce performance if the guess is wrong (hogs bandwidth, pollutes caches).
# Multi-Threading

Idea: interleave processing of multiple threads on the same core to hide stalls.
Each core can run 1 thread at a time, but, we can use the stall times to run other processes. This is done by having bigger register banks (**Execution Context**) - this concept is called **Hyper-Threading**

![[hardware-threads.png|center]]

We don't fix the latency issue, however, by using the stall time to run another hardware thread we increase the throughput of the CPU.
## Limitations

Notice that these threads are not running in parallel, in fact, they are concurring for the core's resources.
The potential of this hardware threads is limited by the size of their *Executions Context* (Register banks). We can have a processor with a lot of register banks (allowing for high latency hiding ability/multiple hardware threads) but we would be limited by capacity.

## Implementation

Core manages Execution contexts for multiple threads:
- Runs instructions from runnable threads (processor makes decision about which thread to run each clock, not the operating system).
- Core still has the same number of ALU resources: multi-threading only helps use them more efficiently in the face of high-latency operations like memory access.

Interleaved multi-threading:
- What we described on the previous slides: each clock, the core chooses a thread, and runs an instruction from the thread on the ALUs.

Simultaneous multi-threading (SMT):
- Each clock, core chooses instructions from multiple threads to run on ALUs.
- Extension of superscalar CPU design.
- Example: Intel Hyper-threading (2 threads per core).
# Bandwidth

> Te rate at which the memory system can provide data to a processor, example: 20GB/s.

**Latency** is the amount of time it takes to for the first set of data to arrive.
We can use data pipelining ([[cpsh-Pipeline]])to increase bandwidth.

### GPU's
GPU's have lower memory capacities but they have way better memory-cores interfaces, allowing for bigger bandwidths. This happens because they invest way more on communication.
There is a lot of switching between warps in a GPU so having a huge bandwidth is a must!!