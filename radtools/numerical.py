r"""
Collection of small routines and constants, 
which are used across the whole package.

It's purpose is to serve as an "other" folder.
"""

from radtools.crystal.constants import ABS_TOL, REL_TOL

__all__ = [
    "compare_numerically",
]


def compare_numerically(x, condition, y, eps=None, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Compare two numbers numerically.

    Parameters
    ----------
    x : float
        First number.
    condition : str
        Condition to compare with. One of "<", ">", "<=", ">=", "==", "!=".
    y : float
        Second number.
    eps : float, optional
        Tolerance. Used for the comparison if provided. If ``None``, the computed as:

        .. code-block:: python

            eps = atol + rtol * y

    rtol : float, default 1e-04
        Relative tolerance.
    atol : float, default 1e-08
        Absolute tolerance.

    Returns
    -------
    result: bool
        Whether the condition is satisfied.
    """

    if eps is None:
        eps = atol + rtol * y

    if condition == "<":
        return x < y - eps
    if condition == ">":
        return y < x - eps
    if condition == "<=":
        return not y < x - eps
    if condition == ">=":
        return not x < y - eps
    if condition == "==":
        return not (x < y - eps or y < x - eps)
    if condition == "!=":
        return x < y - eps or y < x - eps
