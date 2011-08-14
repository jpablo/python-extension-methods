__author__ = 'jpablo'


def ExtendClass(extend_class):
    """
    Mimics extension methods in c#
    """

    class ExtensionMetaclass(type):
        def __new__(mcs, name,bases,dct):
#            extend_class = dct.pop('extend_class')
            public_attrs = filter(lambda a: not a.startswith("__") ,dct)
            for attr_name in public_attrs:
                setattr(extend_class,attr_name, dct[attr_name])
            return super(ExtensionMetaclass,mcs).__new__(mcs,name,bases,{})

    return ExtensionMetaclass