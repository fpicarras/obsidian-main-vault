***
> Pipelining is a way to increase the throughput of a system by dividing the system into multiple sub-parts and then each set of problems is processed in a sequential form in the pipeline. Meaning there can be multiple different problems in different stages of the pipeline.

In a pipeline, the slowest stage is the one that limits the system.

In a processor, we separate the execution in different stages, allowing us to have multiple instructions at the same time in the pipeline.
A **memory bound execution** is what happens when instructions have to stop the pipeline because they are waiting for the memory (which is a very slow system in an architecture [[csph-Memmory]]).

