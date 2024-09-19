***
ISPC is a way to make use of the SIMD architectures without having to go trough the troubles of learning the [[Intrinsics]].
We can do this by decorating the code with specific tags.

ISPC works by lauching a "gand" of program instances that work in parallell.

![[Pasted image 20240919113948.png]]

We use **uniform** to tag the variables that can be accessed by all lanes.
**programCount** and **programIndex** are accessible by default in the framework - they depend on the computer architecture and the number of lanes available.

This code is fully serial, however, it will by mapped to different lanes, giving the illusion of the same program having multiple threads processing.

![[Pasted image 20240919114709.png]]

Instead of a typical for loop, we can use **foreach** that automatically maps the loops and variables for us.

> It is important, for efficiency purposes, that we distribute the data in an interleaved manner. So that the that is efficiently mapped to the lanes (instead of the blocked manner which is better for threads).