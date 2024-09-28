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

