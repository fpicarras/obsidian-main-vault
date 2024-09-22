***
> The main ideia for SIMD - **Single Instruction Multiple Data** - is that most of the time we process data with the same instructions, so we modify the hardware so that with a single instruction stream, we can operate in multiple positions of an array at a time - allowing for effective parallelization of an array processing on a hardware level.

Of coarse we need to modify the code in order to support **SIMD**, because this process requires specific instructions.
![[simd-example.png|center]]
# Why not Threads?

[[csph-threads|Threads]] are software concepts, they require multiple core to operate properly, *SIMD* are physical processing lanes that a processor has that allow for multiple data to have the same process applied to it in the same core in a single clock.

# How to code?

Intel created a package called **intrinsics** that allows for C programmers to make use of *SIMD*, however...
???