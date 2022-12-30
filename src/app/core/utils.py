import functools


def sub_test(param_list):
    """Decorates a unittest test case to run it as a set of subtests."""

    # original post: https://stackoverflow.com/a/62476654/11882892

    def decorator(f):
        @functools.wraps(f)
        def wrapped(self):
            for param in param_list:
                with self.subTest(**param):
                    f(self, **param)

        return wrapped

    return decorator
