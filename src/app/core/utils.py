import functools
from collections.abc import Callable
from typing import Any, ParamSpec, TypeVar

RT = TypeVar("RT")  # Return Type
PT = ParamSpec("PT")  # Param Type


def sub_test(params: list[dict[str, Any]]) -> Callable[[Callable[PT, RT]], Callable[[Any], None]]:
    """Decorates a unittest test case to run it as a set of subtests."""

    # original post: https://stackoverflow.com/a/62476654/11882892

    def decorator(f: Callable[PT, RT]) -> Callable[[Any], None]:
        @functools.wraps(f)
        def wrapped(self: Any) -> None:
            for param in params:
                with self.subTest(**param):
                    f(self, **param)

        return wrapped

    return decorator
