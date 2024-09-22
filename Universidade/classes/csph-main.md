***
# Concepts
[[csph-ILP]], [[csph-threads]], [[csph-ISPC]]

***
# First Touches

For multiple years, the performance improvements we saw on computers where due to advancements done in single processors, where arquitetural upgrades and frequency increases caused the CPU's speedup to sky-rocket.

However, we start hitting a wall after a certain threshold where the frequency is so high that not only the CPU consumes a lot, but it also melts :)

Hence, we need solutions to solve big/multiple problems beyond increasing frequency. To fix this, we started adding executions units to run multiple things in parallel.

> Code now has to be prepared to be parallelised in order to increase it's computation efficiency. 
## [[csph-ILP|Instruction Level Parallelism]]

Or [[csph-ILP|ILP]], was used to attempt to speed-up code execution by parallelizing code on the hardware level. Independent instructions could be run ate the same time.
However this resulted on another wall: multiple instructions ate the same time did not prove efficient.

Before the *multi-core era* processors where "smarter", they had multiple logic units, out-of-order controls, memory pre-fetchers and higher clock frequencies.

![[pre-multi-core-cpu.png|center]]

Multi-core processors are slower at running a single instruction stream then a single-core.
But even if they are 25% slower, two cores at the same time (75% efficiency each) would be a speed-up of 150%.

## [[csph-threads|Threads]]

Thread are a mechanism used by programmers to parallelize code, they allow for the execution of multiple instruction streams in a process. However, the amount of hardware needed to run them is significant because they are not *ILP* and need multiple cores to truly run in parallel.
![[simple-dual-core.png|center]]
This is a dual core processor, able to run 2 threads in parallel and on each core 2 instruction per clock (*ILP*).
***
# SIMD - Single Instruction Multiple Data

[[csph-SIMD|SIMD]] is a hardware optimization that allows for parallel processing of consecutive elements of an array, removing the need for calling different threads (with the same function) for different chunks of said array.

![[simd-16cores.png|center]]
***
# SPMD and ISPC

> SPMD - Single Process Multiple Data.
> [[csph-ISPC|ISPC]] - Intel SPMD Program Compiler.

Since programming SIMD compatible code is boring. Intel developed a mechanism (and it's respective compiler) that takes advantage of SIMD units to speed-up performance for data-parallel tasks.
The key concept is to have the same program running on multiple data in order to make use of SIMD units.

## Whats the difference from [[csph-threads|Threads]]?

| Feature           | ISPC (SPMD+SIMD)                                            | Threads (MIMD)                                            |
| ----------------- | ----------------------------------------------------------- | --------------------------------------------------------- |
| Parallelism Model | Data-parallel, same program on multiple data elements       | Task-parallel, different tasks on different threads       |
| Execution Model   | SIMD-based, operates on vector data in parallel             | Independent thread execution across multiple cores        |
| Granularity       | Fine-grained, focused on data-parallel operations           | Coarse-grained, focused on task-level parallelism         |
| Synchronization   | Minimal need for synchronization (data usually independent) | Requires explicit synchronization (mutexes, locks)        |
| Overhead          | Low (SIMD instructions, less context switching)             | Higher (thread context switching, synchronization)        |
| Use Case          | Vectorized tasks like scientific computing, graphics        | General purpose tasks like servers, background processing |
In summary, ISPC is designed for **high-performance data-parallelism**, whereas threads provide more flexibility for **task-parallelism** across independent operations. ISPC focuses on vectorizing operations to take advantage of **SIMD** units, while threads are used for broader parallelism across multiple CPU cores.
***
# Memory

> Now that we talked about execution optimizations, let's divulge into the second key concept in computer architectures - [[csph-Memmory|Memory]]!

