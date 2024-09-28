***
# Intro

Threads communicate by reading and writing to shared memory locations. This is a straightforward extension of sequential programming but requires careful management of synchronization (locks, barriers).

**Example**:
Two threads might communicate by updating the value of a shared variable:
- **Thread 1**: Writes to a shared variable.
- **Thread 2**: Reads the value written by Thread 1.
In this way, communication between threads is implicit, as data exchange happens through the shared memory.