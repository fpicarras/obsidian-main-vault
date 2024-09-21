***
> Instruction Level Parallelism (ILP) - Independent instructions can be simultaneously executed by a processor without impacting program correctness.

**Super Scalar Execution** - processor dynamically finds independent instructions in an instruction sequence and executes them in parallel.

However, to benefit from this we would have to be pulling multiple instructions per clock cycle, and on top of that those instructions have to be independent, which is checked via hardware. The result is a costly operation that is most of the times program dependent.

In order to have a processor with ILP, we need to draw 2 instruction streams a

