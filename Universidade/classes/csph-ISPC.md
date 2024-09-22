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
***
# Inner Workings
- **Compiling**: The ISPC compiler translates this code into efficient SIMD instructions specific to the target hardware. For example, it might generate AVX2 or AVX-512 instructions, depending on the CPU.
	- Modern processors (especially Intel and AMD) have **SIMD units**, which can process multiple data elements at once (e.g., 4, 8, or 16 elements in parallel). SIMD works by applying the same operation across a "vector" of data in a single instruction.
	- ISPC automatically converts your high-level parallel code into **vectorized instructions** that use SIMD. This allows multiple data points to be processed with a single instruction, significantly boosting performance.

- **Runtime Execution**: At runtime, the program instances (one for each array element) are grouped into gangs. Each gang processes a batch of elements in parallel using SIMD.
	- ISPC runs multiple program instances concurrently, each instance working on a different set of data (this is similar to how GPU kernels work).
	- These program instances are grouped into "gangs," where each gang represents a group of instances executing together in parallel using SIMD. The number of instances per gang usually matches the SIMD width of the hardware (e.g., 4-wide, 8-wide).

- **Scaling**: If the array is large and the CPU has multiple cores, ISPC can divide the work across several gangs, running them on different cores for additional parallelism.