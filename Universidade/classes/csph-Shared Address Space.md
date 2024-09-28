***
# Intro

Threads communicate by reading and writing to shared memory locations. This is a straightforward extension of sequential programming but requires careful management of synchronization (locks, barriers).

**Example**:
Two threads might communicate by updating the value of a shared variable:
- **Thread 1**: Writes to a shared variable.
- **Thread 2**: Reads the value written by Thread 1.
In this way, communication between threads is implicit, as data exchange happens through the shared memory.
## Key Concepts

- **Implicit Communication**: Threads communicate implicitly through memory reads and writes, unlike message passing where communication is explicit.
- **Synchronization Primitives**: Since multiple threads access shared memory, synchronization primitives like locks, barriers, and atomic operations are necessary to avoid race conditions, ensure data consistency, and manage dependencies between threads.
- **Scalability Challenges**: The model can become inefficient as the number of processors increases because synchronization costs grow, and cache coherence protocols might struggle to keep caches consistent across multiple processors.
***
# Synchronization

Because multiple threads access the same memory locations, **synchronization** is crucial to avoid issues like race conditions. Without proper synchronization, multiple threads may simultaneously read and write to the same memory, leading to inconsistent data. The presentation outlines the following mechanisms to manage synchronization:
## **Locks**
Locks are used to enforce **mutual exclusion**, meaning only one thread can access a critical section of code or data at a time.

- **Example**: In the following pseudocode, a lock ensures that only one thread at a time increments the shared variable `x`.
```C
lock(my_lock); 
x++; 
unlock(my_lock);
```
Locks are simple and effective but can lead to performance bottlenecks if not used carefully, especially when multiple threads contend for the same lock, causing **lock contention**.
## Barriers
Barriers are synchronization points where all threads must reach before any can proceed. This is useful when threads need to complete certain phases of computation before moving on to the next step.
- **Example**: A barrier might be used to ensure that all threads have completed their tasks before continuing to the next phase:
```C
barrier(my_barrier, NUM_THREADS);
```
Barriers are a conservative mechanism to ensure all threads are synchronized, but excessive use can lead to inefficiencies if some threads finish their work much earlier than others, causing them to wait.
## Atomic Operations
In some cases, atomic operations can be used to ensure a specific operation on a shared variable is completed without interruption. These operations are typically supported by hardware and are faster than locks.
- **Example**: `atomicAdd(x, 1);` will atomically increment `x` without the need for explicit locking.
Atomic operations are essential for certain fine-grained synchronization tasks, such as counting or updating shared counters.
***
# Hardware Implementation

The hardware must support efficient memory sharing for the shared address space model to work. The presentation describes **key hardware features**:

- **Caches**: Each processor has its own local cache, which holds frequently accessed memory locations. Cache coherence protocols ensure that if one processor modifies a cached memory location, other processors' caches are updated.
    
- **Memory Interconnect**: The processors communicate via an interconnect to access shared memory. This can be implemented using a **bus**, **crossbar switch**, or **multi-stage network**.
    
- **NUMA (Non-Uniform Memory Access)**: In large systems, memory access times can vary depending on the physical location of the memory relative to the processor. This can lead to **NUMA effects**, where some memory accesses are slower because the memory is further from the processor.
***
# Challenges and Drawbacks
## **Memory Consistency Issues**:
When multiple processors or threads share memory, keeping track of which version of a memory location is the "correct" one becomes tricky. For instance:

- **Cache coherence**: Ensuring that when one thread updates a variable, the other threads see the updated value requires a cache coherence protocol (e.g., MESI protocol). However, maintaining coherence across many processors can be costly and affect performance.
## **Synchronization Overhead**:
Proper synchronization (locks, barriers, etc.) is necessary but can introduce overhead, especially when many threads need to access the same shared resources. This can lead to:
- **Lock contention**: Multiple threads waiting for a lock can cause bottlenecks.
- **False sharing**: When multiple threads access different variables that happen to be on the same cache line, updates from one thread can invalidate the cache lines of the others, leading to performance degradation.
## **Scalability**:
As the number of processors increases, maintaining efficient communication through shared memory becomes more difficult. Performance can degrade due to the overhead of synchronization, cache coherence traffic, and NUMA effects.