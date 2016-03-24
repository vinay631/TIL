## "__enter__" and "__exit__" magic methods in Python

"__enter__" and "__exit__" are allows the creation of objects that can be easily used with the <pre><code>with</code></pre> statement. It is useful for the code block that needs "cleandown" like closing database connections.

<pre><code>
class SomeClass:
  def __enter__(self):
    ...
    return self.db
    
  def __exit__(self):
    self.db.close()
    
with SomeClass() as someClass:
  # do something
</code></pre>
