***
# Basics
Idea: interleave processing of multiple threads on the same core to hide stalls.  
Each core can run 1 thread at a time, but, we can use the stall times to run other processes. This is done by having bigger register banks (**Execution Context**) - this concept is called **Hyper-Threading**

![center](app://70fd44b442485c7eca870f09d367d1befdfe/C:/Users/fplay/OneDrive/Documentos/obsidian-main-vault/Pasted%20image%2020240922151924.png?1727014764792)

We don't fix the latency issue, however, by using the stall time to run another hardware thread we increase the throughput of the CPU.
## Limitations

Notice that these threads are not running in parallel, in fact, they are concurring for the core's resources.  
The potential of this hardware threads is limited by the size of their _Executions Context_ (Register banks). We can have a processor with a lot of register banks (allowing for high latency hiding ability/multiple hardware threads) but we would be limited by capacity.
# Implementation
## Logical vs Physical Cores

- **Physical Core**: This is the actual hardware core in a processor, capable of executing instructions, managing data flow, and handling cache.
- **Logical Core (Thread)**: When Hyper-Threading is enabled, each physical core is split into two logical cores (hardware threads). These threads share the core's resources but are presented to the operating system as separate CPU cores.
## How it works:

- **Shared Resources**: The physical core's resources (e.g., execution units, cache, memory interface) are shared between two logical cores (threads). Both threads can issue instructions to these units.
- **Thread Switching**: If one thread is stalled (e.g., waiting for data from memory), the other thread can use the core's execution resources, which increases overall utilization. The core chooses a thread, and runs an instruction from the thread on the ALUs.
- **Instruction Fetch and Decode**: Each logical core fetches and decodes its own set of instructions from memory. These instructions are then dispatched to the shared execution units of the core.
- **Execution**: Multiple threads can have instructions executed in parallel, as long as there are available execution units. If one thread doesn't need to use all the execution units, the other thread can fill the gap. Core still has the same number of ALU resources: multi-threading only helps use them more efficiently in the face of high-latency operations like memory access.

Interleaved multi-threading:
- What we described on the previous slides: each clock, t

Simultaneous multi-threading (SMT):
- Each clock, core chooses instructions from multiple threads to run on ALUs.
- Extension of superscalar CPU design.
- Example: Intel Hyper-threading (2 threads per core).