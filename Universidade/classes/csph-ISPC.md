***
# Basics
ISPC is a way to make use of the [[csph-SIMD|SIMD]] architectures without having to go trough the troubles of learning the Intrinsics.
We can do this by decorating the code with specific tags.

ISPC works by launching a "gang" of program instances that work in parallel.

![[Pasted image 20240919113948.png]]

We use **uniform** to tag the variables that can be accessed by all lanes.
**programCount** and **programIndex** are accessible by default in the framework - they depend on the computer architecture and the number of lanes available.

This code is fully serial, however, it will by mapped to different lanes, giving the illusion of the same program having multiple threads processing.

![[Pasted image 20240919114709.png]]

Instead of a typical for loop, we can use **foreach** that automatically maps the loops and variables for us.

> It is important, for efficiency purposes, that we distribute the data in an interleaved manner. So that the that is efficiently mapped to the lanes (instead of the blocked manner which is better for threads).

## Sum Reduction
Imagine that we need to sum all elements in an array, we can't have multiple instances adding to the same register, that concurrency would corrupt the data.
Therefore we use (from the ISPC library) **reduce_add()**
***
# Inner Workings
- **Compiling**: The ISPC compiler translates this code into efficient SIMD instructions specific to the target hardware. For example, it might generate AVX2 or AVX-512 instructions, depending on the CPU.
	- Modern processors (especially Intel and AMD) have **SIMD units**, which can process multiple data elements at once (e.g., 4, 8, or 16 elements in parallel). SIMD works by applying the same operation across a "vector" of data in a single instruction.
	- ISPC automatically converts your high-level parallel code into **vectorized instructions** that use SIMD. This allows multiple data points to be processed with a single instruction, significantly boosting performance.

- **Runtime Execution**: At runtime, the program instances (one for each array element) are grouped into gangs. Each gang processes a batch of elements in parallel using SIMD.
	- ISPC runs multiple program instances concurrently, each instance working on a different set of data (this is similar to how GPU kernels work).
	- These program instances are grouped into "gangs," where each gang represents a group of instances executing together in parallel using SIMD. The number of instances per gang usually matches the SIMD width of the hardware (e.g., 4-wide, 8-wide).

- **Scaling**: If the array is large and the CPU has multiple cores, ISPC can divide the work across several gangs, running them on different cores for additional parallelism.

- [ ] #question In the task manager are going to appear multiple programs?
***
# What's the difference from [[csph-threads|Threads]]?
## 1. **Parallelism Model**:

- **ISPC (SPMD Model)**:
    
    - ISPC follows the **SPMD (Single Program, Multiple Data)** model, where the same program (or function) is applied to different pieces of data in parallel.
    - ISPC uses **SIMD (Single Instruction, Multiple Data)** units to perform parallelism at the data level. This means it processes multiple data elements in parallel using vectorized instructions.
    - It is primarily **data-parallel**: it operates on large datasets where the same operation needs to be applied to multiple elements (e.g., processing pixels in an image or elements of an array).
- **Threads**:
    
    - Threads follow the **MIMD (Multiple Instruction, Multiple Data)** model, where different threads can execute different instructions on different data simultaneously.
    - Threads are designed for **task-parallel** programming: you can use them to split your program into separate tasks that run independently. Each thread can execute different code and access different resources, or work on different parts of the same task.
    - Threads focus on parallelism across tasks, rather than on individual data elements.

## 2. **Execution Model**:

- **ISPC**:
    
    - ISPC uses **SIMD** hardware for parallel execution. It runs multiple **instances** of a program (called "lanes") on different data points simultaneously, using vector instructions to operate on multiple data points in one go.
    - ISPC operates on vectorized data chunks, making it ideal for tasks like processing arrays, image manipulation, or scientific computing where the same computation is repeated across many elements.
    - ISPC typically operates on **single-core, SIMD** units. However, it can also launch **tasks** to distribute work across multiple cores, though its core strength is efficient data-parallel execution on a per-core basis.
- **Threads**:
    
    - Threads run independently and can be scheduled across **multiple cores**. Each thread gets its own execution context (stack, program counter, registers), allowing for task-level parallelism.
    - Threads are managed by the operating system or language runtime, and they allow for more flexible parallelism: each thread can execute different functions, access different resources, and run asynchronously.
    - Threads can work on **task-level parallelism** across cores, making them suitable for situations where independent tasks need to run in parallel, such as handling multiple connections in a web server or performing different computations simultaneously.

## 3. **Granularity**:

- **ISPC**:
    
    - ISPC operates at the **data-parallel** level, processing large sets of data in parallel using SIMD hardware. The operations tend to be fine-grained, working at the level of individual data elements.
    - Suitable for highly **vectorized** tasks, where the same operation is applied repeatedly over a dataset.
- **Threads**:
    
    - Threads work at a **task-parallel** level, where each thread may be responsible for a relatively coarse-grained task. Each thread can execute its own distinct function or part of a program.
    - Useful for managing **independent tasks** such as separate algorithms, I/O handling, or background processing.

## 4. **Synchronization and Memory Model**:

- **ISPC**:
    - Since ISPC is designed for **data-parallelism**, it does not typically require complex synchronization mechanisms like those used with threads. However, ISPC does provide built-in support for synchronization primitives, such as `foreach_active` and `sync` operations, for cases where it is needed (e.g., barrier synchronization).
    - All ISPC program instances typically operate on different parts of a dataset, reducing the need for locks or synchronization over shared data.
- **Threads**:
    - Threads share memory within the same process, so they often require **explicit synchronization** mechanisms (like **mutexes**, **locks**, or **condition variables**) to prevent race conditions when accessing shared data.
    - Thread-based programs need careful handling of synchronization to manage shared resources and avoid issues like deadlocks or race conditions.

## 5. **Performance and Overhead**:

- **ISPC**:
    
    - ISPC focuses on **low-overhead, high-throughput** data processing. By relying on SIMD vectorization, ISPC minimizes the overhead of managing separate execution contexts (like threads do).
    - Since ISPC directly maps operations to the SIMD units of the processor, it typically achieves very high performance for data-parallel tasks by maximizing hardware utilization.
- **Threads**:
    
    - Threads come with **more overhead** since each thread requires its own execution context (e.g., stack, registers). Managing threads also involves operating system-level context switching, which can add to the overhead.
    - Threads excel in scenarios where independent tasks are being performed concurrently, but the overhead of thread creation, synchronization, and context switching can become significant.

## 6. **Typical Use Cases**:

- **ISPC**:
    - Best suited for **data-parallel** tasks: operations that apply the same computation across many elements of an array, image, or dataset.
    - Commonly used in **graphics rendering**, **scientific computing**, **signal processing**, and other high-performance computing applications that involve operating on large arrays or matrices.
- **Threads**:
    - Best for **task-parallel** workloads: applications where different tasks or functions need to be performed concurrently.
    - Commonly used in applications like **web servers** (handling multiple client requests), **multithreaded algorithms** (like sorting), **I/O-bound applications**, or any workload where different parts of a program need to run independently.
## Summary

| Feature           | ISPC (SPMD+SIMD)                                            | Threads (MIMD)                                            |
| ----------------- | ----------------------------------------------------------- | --------------------------------------------------------- |
| Parallelism Model | Data-parallel, same program on multiple data elements       | Task-parallel, different tasks on different threads       |
| Execution Model   | SIMD-based, operates on vector data in parallel             | Independent thread execution across multiple cores        |
| Granularity       | Fine-grained, focused on data-parallel operations           | Coarse-grained, focused on task-level parallelism         |
| Synchronization   | Minimal need for synchronization (data usually independent) | Requires explicit synchronization (mutexes, locks)        |
| Overhead          | Low (SIMD instructions, less context switching)             | Higher (thread context switching, synchronization)        |
| Use Case          | Vectorized tasks like scientific computing, graphics        | General purpose tasks like servers, background processing |
In summary, ISPC is designed for **high-performance data-parallelism**, whereas threads provide more flexibility for **task-parallelism** across independent operations. ISPC focuses on vectorizing operations to take advantage of **SIMD** units, while threads are used for broader parallelism across multiple CPU cores.