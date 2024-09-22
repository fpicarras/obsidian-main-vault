***
# Basics

> On-chip storage, keeps a copy of a subset of DRAM data - If an address is stored “in the cache” (cache hit), the CPU can load/store that data more quickly than if the data resides only in DRAM

A cache is a hardware implementation detail that does not impact the output of a program, only it's performance. In fact, caches are transparent to the programmer.
When we load a value from memory we forward that request to the cache (instead of the RAM), the cache verifies that it has the value or not, if it has, returns that value with minimum latency, if it doesn't we have to forward that request to the higher levels of cache or RAM. 

To avoid having to always ask the RAM for values, we receive from the cache an array of consecutive bytes, this is called *data locality*.
## Data Locality

Is the concept of taking advantage of data being stored sequentially to minimize DRAM requests. When we ask DRAM for data, we receive an entire cache line (containing said value we requested), if this adjacent values are used in the future they will be already in cache so it's quicker to load.
### Spatial Locality
>Loading data in a cache line “preloads” the data needed for subsequent accesses to different addresses in the same line (leading to cache hits).
### Temporal Locality
>Repeated accesses to the same address result in hits.

## 3 C's of Cache misses
- *Compulsory* (cold miss) - First time data touched. Unavoidable in sequential programming.
- *Capacity miss* - Working set is larger than cache. Can be avoided/reduced by increasing cache size.
- *Conflict miss* - Miss induced by cache management policy. Can be avoided/reduced by changing cache associativity, or data access pattern in application.
***
# Policies

**Cache policies** refer to the strategies and rules that a computer system uses to manage the contents of its cache memory. Since cache is a limited, fast memory used to temporarily store frequently accessed data, efficient management is crucial for performance. Cache policies dictate how data is loaded into the cache, how long it stays there, and how it is replaced when the cache is full.

## **Cache Placement Policy**:
- Determines **where** a block of data is placed in the cache when it is loaded from main memory.
    - Types:
        - **Direct Mapping**: Each memory block is mapped to exactly one cache line. It's simple but can lead to frequent replacements if multiple memory addresses map to the same cache line.
        - **Fully Associative**: A memory block can be placed in any cache line. This offers flexibility but increases complexity.
        - **Set-Associative**: A combination of the above. The cache is divided into sets, and each memory block is mapped to a specific set but can be placed in any line within that set (e.g., 2-way, 4-way set associative).
## **Cache Replacement Policy**:
- Determines **which data is replaced** when new data needs to be loaded into a full cache.
    - Common strategies:
        - **LRU (Least Recently Used)**: The cache line that hasn't been used for the longest time is replaced. It approximates good performance since frequently accessed data tends to stay in the cache.
        - **FIFO (First-In, First-Out)**: The oldest cache line (based on insertion time) is replaced. It's simpler but may not always be optimal.
        - **Random Replacement**: A randomly chosen cache line is replaced. It's very simple but often less efficient.
        - **LFU (Least Frequently Used)**: The cache line that has been used the fewest times is replaced. It can be good for workloads with heavy repetition but is harder to implement.
## **Cache Write Policy**:    
- Determines **how data is written** to the cache and main memory when the cache is updated.
    - Types:
        - **Write-Through**: Data is written to both the cache and main memory simultaneously. This ensures data consistency but introduces more memory traffic, potentially reducing performance.
        - **Write-Back**: Data is written only to the cache at first. It is written to the main memory **later** when the cache line is replaced. This reduces memory traffic but requires more complex cache management.
        
## **Cache Write Miss Policy**:
- Determines what happens when data is **written to an address** not currently in the cache.
    - Types:
        - **Write-Allocate (Fetch on Write)**: On a write miss, the block is loaded into the cache from main memory, and the write is performed on the cache. This is commonly used with **write-back** caches.
        - **Write-No-Allocate (Write Around)**: On a write miss, the block is **directly written to main memory** without loading it into the cache. This is often used with **write-through** caches.
        
## **Cache Coherence Policies (in Multi-Core Systems)**:
- Ensures that caches across multiple processors stay **synchronized** when they share the same memory.
    - Common coherence protocols:
        - **MESI (Modified, Exclusive, Shared, Invalid)**: A common cache coherence protocol that ensures consistency between multiple cache levels in a system.
        - **MOESI**: A variation of MESI that adds an "Owned" state for more efficient cache sharing.

## Summary
| Policy Type             | Description                                                | Example Strategies               |
|-------------------------|------------------------------------------------------------|----------------------------------|
| **Placement Policy**     | Where data is placed in cache                              | Direct mapping, fully associative, set-associative |
| **Replacement Policy**   | What data to replace when the cache is full                | LRU, FIFO, Random, LFU           |
| **Write Policy**         | How data is written to cache and main memory               | Write-Through, Write-Back        |
| **Write Miss Policy**    | What happens on a cache write miss                         | Write-Allocate, Write-No-Allocate|
| **Coherence Policy**     | Keeping caches synchronized in multi-core systems          | MESI, MOESI                      |
***
# Multi-Level Caches
There is limited space in the integrated circuit near the cores, so caches can not be that big. Hence we introduce multiple levels, the closer you are to the processor cores the faster but also the smallest.
This translates to a system of successive requests (much like a DNS server) where if the data isn't in L1 we forward to L2, then to L3 then finally to the DRAM - this is called **Memory Hierarchy**.

![[cache-hierarchy.png|center]]

Accesses not satisfied in local memory cause communication with next level. So, managing locality to reduce the amount of communication performed is important at all levels!