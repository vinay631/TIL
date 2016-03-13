## Mixin

Mixin is a way to compose classes without using multiple inheritence. Its useful when you need to provide a lots of optional features to a class or when you want to use same features in different classes.

<pre><code>rom werkzeug import BaseRequest, AcceptMixin

class Request(BaseRequest, AcceptMixin):
    pass
    
</code></pre>

--
