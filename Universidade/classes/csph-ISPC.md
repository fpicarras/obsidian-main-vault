***
ISPC is a way to make use of the SIMD architectures without having to go trough the troubles of learning the [[Intrinsics]].
We can do this by decorating the code with specific tags.

ISPC works by lauching a "gand" of program instances that work in parallell.

![[Pasted image 20240919113948.png]]

We use **uniform** to tag the variables that 