# ExtendClass

A metaclass that allows to extend a class with methods from another.

## Example
```python
from django.contrib.auth.models import User

class UserExtension(object):

    __metaclass__ = ExtendClass(User)

    @property
    def profile(self):
        return self.get_profile()

    def in_group(self, name):
        return self.groups.filter(name=name).count() > 0

# >>> u = User.objects.all()[0]
# >>> assert u.profile == u.get_profile()
# >>> assert u.in_group("crazy_group") == False
```

## TODO

The real reason for this metaclass is to detect if we are overriding something.

1. Warn if something is being overriden
2. Optionally force override
3. Friendly interface, something like "class UserExtension(User,Extension): ... "

