***
> The main ideia for SIMD - **Single Instruction Multiple Data** - is that most of the time we process data with the same instructions, so we modify the hardware so that with a single instruction stream, we can operate in multiple positions of an array at a time - allowing for effective parallelization of an array processing on a hardware level.

Of coarse we need to modify the code in order to support **SIMD**, because this process requires specific instructions.
![[simd-example.png|center]]
## Conditional Execution

It's all fun and games when we run the same operations on all the elements, but what if those operations are conditional? For example if an element is bigger than 100 do nothing on it...

This is where **lane masking** comes into play: we stop the executions of specific lanes that do not satisfy a condition and the other lanes continue with the execution stream.
*What does this mean?*

In assembly the code is sequential, when we do not satisfy an *if* we jump over to where the *else* condition is defined. Here we can not change the program counter - we can not branch. Hence if we not not want, for example, to operate on lanes which input is bigger than 100, we stop this lanes and only operate on the others.

## Coherent Execution

> Same instruction sequence applies to all elements operated upon simultaneously. Coherent execution is necessary for efficient use of SIMD processing resources.

Coherent execution is not necessary for efficient parallelization across cores, since each core is capable of fetching/decoding different instruction streams.
*Divergent Execution* is what we call when different lanes are never operating simultaneously.

In the worst case, poorly written code might execute at 1/L the peak capability of the machine, where L is the number of lanes.

## Execution... On modern CPU's
### Instructions
#SSE - 128-bit: 4x32 bits or 2x64 bits (4-wide vectors)
#AVX2 - 256-bit: 8x32 bits or 4x64 bits (8-wide vectors)
#AVX512 - 512-bit: 16x32 bits or 8x64 bits (16-wide vectors)

In modern GPU's lanes have ranges from 8 to 32.
### Generation
This instructions can be generated on compile time or by explicit request via *intrinsics*. 

***
# Why not Threads?

[[csph-threads|Threads]] are software concepts, they require multiple core to operate properly, *SIMD* are physical processing lanes that a processor has that allow for multiple data to have the same process applied to it in the same core in a single clock.
***
# How to code?

Intel created a package called **intrinsics** that allows for C programmers to make use of *SIMD*, however...
```C
#include <immintrin.h>

void sinx(int N, int terms, float* x, float* result){
	float three_fact = 6; // 3!
	for (int i=0; i<N; i+=8){
		__m256 origx = _mm256_load_ps(&x[i]);
		__m256 value = origx;
		__m256 numer = _mm256_mul_ps(origx, _mm256_mul_ps(origx, origx));
		__m256 denom = _mm256_broadcast_ss(&three_fact);
		int sign = -1;
			for (int j=1; j<=terms; j++){
			// value += sign * numer / denom;
			__m256 tmp = _mm256_div_ps(_mm256_mul_ps(_mm256_broadcast_ss(sign),numer),denom);
			value = _mm256_add_ps(value, tmp);
			numer = _mm256_mul_ps(numer, _mm256_mul_ps(origx, origx));
			denom = _mm256_mul_ps(denom, _mm256_broadcast_ss((2*j+2) * (2*j+3)));
			sign *= -1;
			}
			_mm256_store_ps(&result[i], value);
	}
}
```
The code is way too complicated, even though is just a simple translation.
Notice how we now increment the outer loop iterator in batches of 8, from this code we can determine that it was done for a CPU with 8 SIMD lanes.

## "Fake" Intrinsics

To simplify the programming of code that makes use of SIMD processing, we created *"Fake" intrincis*. Therefore we don't need to know how many lanes we have, or what operations are supported, we just have abstract operations.
### Data Types
- **__vint** - Instance of an INT array.
- **__vfloat** - Instance of a Float array.
- **__vbool** - Instance of a Boolean array.
### Data movement
- **vVar = \_vload(\*mem_addr)** - Loads L elements from the address given.
- **\_vstore(\*mem_addr, vVar)** - Stores L elements (from vVar) to the address given.
- **vDst = \_vcopy(vDst, vSrc)** - Copies what is vSrc to vDst.
### Operations
- **vR = \_vadd(v1, v2)** - Adds v1 and v2.
- **vR = \_vsub(v1, v2)** - Subtracts v1 from v1.
- **vR = \_vmul(v1, v2)** - multiplies v1 by v2.
### Logic Operations
- **vbR = \_vnot(vBool)** - Inverts the boolean values 