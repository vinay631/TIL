## Currying
#### Date Feb 21, 2016

Currying is a technique in functional programming language to decompose a function that takes multiple arguments into multiple functions that take single arguments.

Currying in Scala:

<pre><code>
def add(x:Int)(y:Int) = x + y
add(3)(4)
</code></pre>

Or:

<pre><code>
def add(x:Int, y:Int) = x + y

def curriedAdd = Function.curried(add _)

add(3, 4)
curriedAdd(3)(4)
</code></pre>

--
