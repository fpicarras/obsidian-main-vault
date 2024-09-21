***
# Concepts
[[csph-ILP]]

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