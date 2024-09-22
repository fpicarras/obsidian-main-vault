***
> The main ideia for SIMD - **Single Instruction Multiple Data** - is that most of the time we process data with the same instructions, so we modify the hardware so that with a single instruction stream, we can operate in multiple positions of an array at a time - allowing for effective parallelization of an array processing on a hardware level.

Of coarse we need to modify the code in order to support **SIMD**, because this process requires specific instructions.
![[simd-example.png|center]]
## Conditional Execution

It's all fun and games when we run the same operations on all the elements, but what if those operations are conditional? For example if an element is bigger than 100 do nothing on it...

This is where **lane masking** comes into play: we stop

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