## Traits and Multiple inheritence in Scala
#### Date: Feb 15, 2016

Traits are intefaces with concrete methods. Scala deals with Diamond Problem of multiple inheritence by considering the order in which traits are inherited. If multiple traits implement a given member, the right-most member "wins".

--
