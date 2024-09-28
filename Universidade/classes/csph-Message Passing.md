***
# Intro

The **message passing model** is a parallel programming paradigm where threads or processes do not share memory but instead communicate by sending and receiving messages. This model is commonly used in distributed systems, where each processor has its own private memory space, and communication happens explicitly through message exchanges. Here’s a more in-depth exploration of the message passing model based on the presentation.

**Example**:
Two threads, Thread 1 and Thread 2, want to exchange data:
- **Thread 1**: Sends a message containing variable `X` to Thread 2.
- **Thread 2**: Receives the message from Thread 1 and stores the value of `X`.
In contrast to the shared address space model, where threads communicate via shared memory, message passing requires explicit actions to communicate.
## Key Concept

- **Explicit Communication**: All communication is explicit in the form of sending and receiving messages. Unlike the shared address space model, where memory access is implicit, the message passing model forces the programmer to manage communication.
- **Synchronization through Messages**: Sending and receiving messages can serve as both communication and synchronization mechanisms. For example, a process must wait to receive a message before proceeding, thus synchronizing with the sender.
- **Private Memory Spaces**: Each thread or process has its own private memory. The only way to exchange data between processes is by sending and receiving messages.
***
# Message Passing Operations
> In this model, communication occurs via two fundamental operations: **send** and **receive**.
## Send
The `send` operation transmits data from one process to another. A message contains the data to be transmitted and metadata like the destination process and an optional tag to identify the message.
```C
send(X, destination, tag);
```
This sends the variable `X` to the `destination` process and attaches a `tag` to the message.
## Recieve
The `receive` operation allows a process to receive a message from another process. The receiving process specifies which sender it expects the message from and the tag associated with the message.