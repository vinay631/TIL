## Amdahl's law 

Amdahl's law or Amdahl's argument is used to find out the maximum expected improvement in a system when only a part of it is improved. It is used in parallel computing to calculate the maximum theoritical speedup using multiple processors.

A program has a part which cannot be serialized and the other that can be serialized. Speedups can be achieved by splitting up the latter and distributing those across multiple processors. The speedup can be represented as:
S = T/T(N) where, 
T = B + P
and, 
T(N) = B + P/N

B is the serial part, P is the part that can be parallelized and N is the number of processor.
