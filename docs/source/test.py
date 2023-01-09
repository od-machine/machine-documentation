def foo(x) -> int:
    """
    This is a docstring.

    :param bar: This is a parameter.
    :type x: int
    :return: This is a return value.
    :rtype: int
    """
    print('foo')

def some_func(foo, bar, baz):
    """Does some stuff

    Parameters
    ----------
    foo : int, float, str, or tf.Tensor
    The foo to bar, which has a really really, reeeeeeeeeeeeeeeeally
    unnecessarily long multiline description.
    bar : str
    Bar to use on foo
    baz : float
    Baz to frobnicate

    Returns
    -------
    float
    The frobnicated baz
    """