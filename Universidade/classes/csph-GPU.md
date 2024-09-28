***
# How GPUs Work: Hardware vs. Software

GPUs (Graphics Processing Units) are specialized hardware designed for parallel computing, especially efficient in tasks like rendering graphics and performing matrix calculations in scientific computing, machine learning, and data analysis. Let's explore both the **hardware** aspects of a GPU and the **CUDA software programming model** that leverages its architecture.

---

# Hardware Overview of GPUs

GPUs differ from CPUs in their architecture, focusing on high-throughput parallelism rather than single-threaded performance. GPUs are composed of many **cores** that can execute thousands of threads simultaneously. This structure makes them ideal for **data-parallel tasks** where the same operation is applied to multiple data elements in parallel.

## Key Hardware Features
- **SIMD Execution (Single Instruction, Multiple Data)**: GPUs use SIMD execution, where a single instruction operates on multiple data elements at once. Each core can process multiple data streams concurrently.
- **Multi-Threaded Execution**: Each core in a GPU is multi-threaded, meaning it can execute multiple threads at the same time. GPUs are designed to handle hundreds of thousands of threads efficiently.
- **Memory Hierarchy**:
  - **Global Memory**: Accessible by all threads but relatively slow.
  - **Shared Memory**: Faster, low-latency memory shared between threads within the same block, allowing for cooperative computation.
  - **Private/Local Memory**: Each thread has its own private memory for storing temporary variables.
  
High-end GPUs, such as those used in **NVIDIA's Tesla or RTX** series, have impressive memory bandwidths (e.g., **GDDR6X memory** with up to 504.2 GB/sec, as shown in the slides【17†source】). The memory system is structured to support the needs of highly parallel workloads.

---

# Evolution of GPU Architecture

GPUs initially evolved for rendering 3D graphics in gaming. Over time, they have transitioned into general-purpose computing platforms due to their ability to handle parallel tasks efficiently. In 2007, NVIDIA introduced the **Tesla architecture** and the **CUDA programming model**, which made it possible to use GPUs for non-graphics tasks like scientific computing and machine learning.

- **Graphics Pipeline**: The traditional role of GPUs was limited to the graphics pipeline—transforming 3D geometry into 2D images (rasterization). However, modern GPUs also support general-purpose computing (GPGPU) for scientific computations, data analysis, and machine learning.

- **Tesla and Beyond**: NVIDIA's Tesla architecture was a game-changer, allowing programmers to run general-purpose tasks on GPUs. Tesla introduced a programmable core with a **compute mode** interface, simplifying the execution of non-graphics tasks like parallel data processing.

---

# CUDA Programming Model

CUDA (**Compute Unified Device Architecture**) is a parallel computing platform and programming model developed by NVIDIA. It allows developers to write programs that run on the GPU for general-purpose computing tasks. CUDA is similar to **C** and provides abstractions that map closely to GPU hardware.

#### **Basic Concepts in CUDA**:
- **Host vs. Device**: The CPU is the **host**, and the GPU is the **device**. Programs are divided between the host (CPU) and the device (GPU), with data being passed between the two.
- **Kernels**: In CUDA, the function that runs on the GPU is called a **kernel**. A kernel is launched by the host and executed by the GPU across many threads simultaneously.
  
  ```cpp
  __global__ void matrixAdd(float* A, float* B, float* C, int N) {
      int i = blockIdx.x * blockDim.x + threadIdx.x;
      if (i < N) C[i] = A[i] + B[i];
  }
  ```

- **Threads and Blocks**: Threads in CUDA are organized into **blocks**, and blocks are grouped into a **grid**. This hierarchical structure allows for efficient parallel execution:
  - Each thread has its own **thread ID**.
  - A **block** is a group of threads that can share data using **shared memory**.
  - A **grid** contains multiple blocks that execute the same kernel【17†source】.

- **Thread Scheduling**: Threads are scheduled in **warps**, where 32 threads execute the same instruction at a time. GPUs are efficient in executing multiple warps simultaneously, allowing for **massive parallelism**.
## CUDA Memory Model

CUDA has a hierarchical memory structure designed to optimize access times and parallelism:

- **Global Memory**: Accessible by all threads but has higher latency. This is the main memory for storing large data sets.
  
- **Shared Memory**: Each thread block has its own **shared memory**, which is faster and allows for communication between threads in the same block. For example, in a matrix multiplication, blocks can load a portion of the matrix into shared memory, reducing the need for repeated accesses to global memory.

- **Private/Local Memory**: Used for storing temporary data for each thread, like loop counters or intermediate values.

An example from the slides shows how **shared memory** can improve performance by reducing redundant global memory accesses. The CUDA kernel stores input values in **shared memory** before performing computations【17†source】:

```cpp
__shared__ float support[THREADS_PER_BLK + 2];
support[threadIdx.x] = input[index];
```

This type of memory optimization is critical for achieving high performance on GPUs.

## CUDA Execution Model

The **CUDA execution model** follows the **Single Program, Multiple Data (SPMD)** paradigm, where the same program (kernel) is executed by multiple threads in parallel. Here’s how it works:

1. **Kernel Launch**: The CPU (host) launches a kernel on the GPU (device) with a specified grid and block size. For example, if you're adding two arrays, each thread can compute the sum of corresponding elements from both arrays.

2. **Thread Execution**: Each thread calculates its unique index within the grid using the built-in variables `threadIdx`, `blockIdx`, `blockDim`, etc. Threads can operate independently or cooperatively by using **synchronization primitives** like `__syncthreads()`.

3. **Synchronization and Atomic Operations**: Threads in the same block can synchronize using `__syncthreads()`, ensuring that all threads in the block have completed their tasks before proceeding to the next step. CUDA also supports **atomic operations** to ensure safe updates to shared or global memory by multiple threads【17†source】.

4. **Memory Transfers**: Data is transferred between the host and device using `cudaMemcpy()`. Since the host and device have separate memory spaces, explicit copying is required:
  
  ```cpp
  cudaMemcpy(deviceA, hostA, size, cudaMemcpyHostToDevice);
  ```

This distinction between **host memory** and **device memory** is crucial for efficient data management in CUDA programs.
## Examples
### Matrix Multiplication
Consider a program that multiplies each element of $A$ to it's corresponding in $B$ and stores it in $C$.
Let's say that that matrix is $6\times12$. First we need to create an application thread running on the *host* the configures the *device*, saying how many blocks we want and how many threads per block.
```Cpp
const int Nx = 12;
const int Ny = 6;

dim3 threadsPerBlock(4, 3, 1); 
dim3 numBlocks( Nx/threadsPerBlock.x, Ny/threadsPerBlock.y, 1); 
// assume A, B, C are allocated Nx x Ny float arrays 
// this call will launch 72 CUDA threads: 
// 6 thread blocks of 12 threads each 
matrixAdd<<numBlocks, threadsPerBlock>>(A,B,C);
```
What this will do is map the matrixes to the grid we want to create, resulting in the following disposition:
![[Pasted image 20240928200104.png|center]]
Finally `matrixAdd<<numBlocks, threadsPerBlock>>(A,B,C);` bulk launches many CUDA threads, this call returns when all threads have finished.
Now, we need to create the *kernel*:
```Cpp
// kernel definition (runs on GPU) 
__global__ void matrixAdd(float A[Ny][Nx], float B[Ny][Nx], float C[Ny][Nx]) {
	int i = blockIdx.x * blockDim.x + threadIdx.x;
	int j = blockIdx.y * blockDim.y + threadIdx.y;

	C[j][i] = A[j][i] + B[j][i]; 
}
```
As you can see, each thread needs to identify it's corresponding matrix coordinates. Since we mapped the grid to equal the matrix, we just need to use the thread/block information to be able to map: each block as an id (`blockIdx` - 2D), a size (`blockDim` - 2D) and each thread an id (`threadIdx` - 2D). So to get the matrix index (on each dimension) we have to jump `blockIdx` blocks of size `blockDim` and then, inside the target block, get to the target thread, by skipping `threadIdx`. 
What if the matrix size if not a multiple of `threadsPerBlock`?
```Cpp
/* Host */
const int Nx = 11; // not a multiple of threadsPerBlock.x
const int Ny = 5;  // not a multiple of threadsPerBlock.y

dim3 threadsPerBlock(4, 3, 1); 
dim3 numBlocks( Nx/threadsPerBlock.x, Ny/threadsPerBlock.y, 1); 
// assume A, B, C are allocated Nx x Ny float arrays 
// this call will launch 72 CUDA threads: 
// 6 thread blocks of 12 threads each 
matrixAdd<<numBlocks, threadsPerBlock>>(A,B,C);
```

```Cpp
/* kernel definition (runs on GPU) */
__global__ void matrixAdd(float A[Ny][Nx], float B[Ny][Nx], float C[Ny][Nx]) {
	int i = blockIdx.x * blockDim.x + threadIdx.x;
	int j = blockIdx.y * blockDim.y + threadIdx.y;
	// guard against out of bounds array access 
	if (i < Nx && j < Ny)
		C[j][i] = A[j][i] + B[j][i]; 
}
```
There is one thing missing... How do we get the data from the *host* to the *device*?
The solution is allocating memory in the GPU and then passing it copying the data from the *host*:
```Cpp
/* Host */
float* A = new float[N]; // allocate buffer in host memory 
// populate host address space pointer A
// ...

int bytes = sizeof(float)*N;
float *deviceA;
cudaMalloc(&deviceA, bytes);
cudaMemcpy(deviceA, A, bytes, cudaMemcpyHostToDevice);

// note: directly accessing deviceA[i] is an invalid
// operation here: cannot manipulate contents of deviceA
// directly from host (only from device code), since deviceA
// is not a pointer into the host’s memory address space
```
> There is a problem here, all the threads from all the blocks are accessing the global memory which is very slow.
### 1D Convolution
![[Pasted image 20240928210846.png|center]]
To avoid the use of global memory, let's make them all use the shared memory, of course, we would still need to load the values from the host to the global memory and then to the shared. 
```Cpp
#define THREADS_PER_BLK 128 
__global__ void convolve(int N, float* input, float* output) { 
	__shared__ float support[THREADS_PER_BLK+2]; // per-block allocation 
	int index = blockIdx.x * blockDim.x + threadIdx.x; // thread local variable
	support[threadIdx.x] = input[index]; 
	if (threadIdx.x < 2) 
		support[THREADS_PER_BLK + threadIdx.x] = input[index+THREADS_PER_BLK];
	__syncthreads(); 
	
	float result = 0.0f; // thread local variable 
	for (int i=0; i<3; i++) result += support[threadIdx.x + i]; 
	output[index] = result / 3.f; 
}
```
> `__syncthreads()` will wait for all the threads **in the same block** to finish.
***

# CUDA and GPU Architectures Working Together

GPUs are designed to handle tasks that are highly parallel, where the same operation is applied to many data elements. CUDA allows programmers to tap into the massive parallelism available in GPUs by launching thousands of threads for simple, repetitive tasks. These threads execute in **warps**, and their execution is tightly coupled with the underlying hardware for maximum efficiency.

The **hierarchical thread model** of CUDA (threads, blocks, grids) is mapped directly to the **streaming multiprocessors (SMs)** of NVIDIA GPUs. Each SM can handle multiple warps of threads concurrently, taking advantage of the high parallelism of the hardware.

For example, the **NVIDIA RTX 4070 Ti** has 60 **SM cores**, each capable of executing **up to 48 warps**, meaning thousands of threads can run simultaneously on a single GPU chip【17†source】【17†source】.

---
# Applications of GPUs and CUDA

GPUs, especially when programmed using CUDA, are used in a wide range of fields:
- **Deep Learning**: Neural networks are trained using GPUs, with frameworks like TensorFlow and PyTorch leveraging CUDA for faster matrix operations.
- **Scientific Computing**: Applications like molecular dynamics simulations, fluid simulations, and weather forecasting benefit from GPU acceleration.
- **Graphics and Gaming**: Rendering 3D scenes, ray tracing, and real-time physics simulations are handled by GPUs.
  
CUDA provides the tools to harness the computational power of GPUs for these tasks by simplifying the parallelization of code, making it accessible to a broader range of developers.

---
# Conclusion

GPUs are highly parallel processing units designed to handle large-scale, data-parallel workloads efficiently. With CUDA, programmers can exploit this parallelism for a variety of tasks, from scientific computing to machine learning. The combination of hardware capabilities (such as SIMT execution, shared memory, and fast memory bandwidth) with the flexibility of CUDA's programming model makes GPUs a cornerstone in modern computing, far beyond their original purpose of rendering graphics.