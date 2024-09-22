***
> Threads are software units of process that run instruction streams, in parallel. They are managed by the operating system

For example, an array that has N elements, instead of being processed in Serial, can be split for T threads and have an ideal speed-up of T.
Another useful example of threads are in user interfaces or network servers, threads can improve responsiveness by allowing background tasks to run without blocking the main thread.

# pthreads

Or POSIX threads, are the standard milti-threading in C