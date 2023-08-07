import numpy as np

from radtools.numerical import compare_numerically
import radtools.crystal.cell as Cell
from radtools.crystal.constants import (
    TRANSFORM_TO_CONVENTIONAL,
    REL_TOL,
    ABS_TOL_ANGLE,
    ABS_TOL,
)

__all__ = [
    "standardize_cell",
    "CUB_standardize_cell",
    "FCC_standardize_cell",
    "BCC_standardize_cell",
    "TET_standardize_cell",
    "BCT_standardize_cell",
    "ORC_standardize_cell",
    "ORCF_standardize_cell",
    "ORCI_standardize_cell",
    "ORCC_standardize_cell",
    "HEX_standardize_cell",
    "RHL_standardize_cell",
    "MCL_standardize_cell",
    "MCLC_standardize_cell",
    "TRI_standardize_cell",
]


# Main routine, serves as interface to all of them
def standardize_cell(cell, correct_lattice_type, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine it
    if required to ensure the unique choice of lattice vectors.

    See :ref:`lattice-standardization` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.
    correct_lattice_type : str
        Correct lattice type.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """

    cell = np.array(cell)
    functions = {
        "CUB": CUB_standardize_cell,
        "FCC": FCC_standardize_cell,
        "BCC": BCC_standardize_cell,
        "TET": TET_standardize_cell,
        "BCT": BCT_standardize_cell,
        "ORC": ORC_standardize_cell,
        "ORCF": ORCF_standardize_cell,
        "ORCI": ORCI_standardize_cell,
        "ORCC": ORCC_standardize_cell,
        "HEX": HEX_standardize_cell,
        "RHL": RHL_standardize_cell,
        "MCL": MCL_standardize_cell,
        "MCLC": MCLC_standardize_cell,
        "TRI": TRI_standardize_cell,
    }

    return functions[correct_lattice_type](cell, rtol=rtol, atol=atol)


def CUB_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the CUB lattice conditions.

    See :ref:`guide_cub` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
        Ignored here, but preserved for the unification of input.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.
        Ignored here, but preserved for the unification of input.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """

    return np.array(cell)


def FCC_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the FCC lattice conditions.

    See :ref:`guide_fcc` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
        Ignored here, but preserved for the unification of input.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.
        Ignored here, but preserved for the unification of input.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """

    return np.array(cell)


def BCC_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the BCC lattice conditions.

    See :ref:`guide_bcc` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
        Ignored here, but preserved for the unification of input.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.
        Ignored here, but preserved for the unification of input.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """

    return np.array(cell)


def TET_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the TET lattice conditions.

    See :ref:`guide_tet` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """

    cell = np.array(cell)

    a, b, c, alpha, beta, gamma = Cell.params(cell)

    if compare_numerically(a, "==", c, rtol=rtol, atol=atol):
        cell = [cell[2], cell[0], cell[1]]
    elif compare_numerically(b, "==", c, rtol=rtol, atol=atol):
        cell = [cell[1], cell[2], cell[0]]

    return cell


def BCT_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the BCT lattice conditions.

    See :ref:`guide_bct` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """
    cell = np.array(cell)

    a, b, c, alpha, beta, gamma = Cell.params(TRANSFORM_TO_CONVENTIONAL["BCT"] @ cell)

    if compare_numerically(a, "==", c, rtol=rtol, atol=atol):
        cell = [cell[2], cell[0], cell[1]]
    elif compare_numerically(b, "==", c, rtol=rtol, atol=atol):
        cell = [cell[1], cell[2], cell[0]]

    return cell


def ORC_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the ORC lattice conditions.

    See :ref:`guide_orc` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """
    cell = np.array(cell)

    a, b, c, alpha, beta, gamma = Cell.params(cell)

    if compare_numerically(a, ">", b, rtol=rtol, atol=atol):
        # minus preserves right-hand order
        cell = [cell[1], cell[0], -cell[2]]
        a, b = b, a
    if compare_numerically(a, ">", c, rtol=rtol, atol=atol):
        cell = [cell[2], cell[0], cell[1]]
    elif compare_numerically(b, ">", c, rtol=rtol, atol=atol):
        # minus preserves right-hand order
        cell = [cell[0], cell[2], -cell[1]]

    return cell


def ORCF_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the ORCF lattice conditions.

    See :ref:`guide_orcf` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """
    cell = np.array(cell)
    a, b, c, alpha, beta, gamma = Cell.params(cell)

    if compare_numerically(a, "<", b, rtol=rtol, atol=atol):
        # minus preserves right-hand order
        # abc - > bca
        cell = [cell[1], cell[2], cell[0]]
        if compare_numerically(b, "<", c, rtol=rtol, atol=atol):
            # minus preserves right-hand order
            # bca -> -cba
            cell = [-cell[1], cell[0], cell[2]]
        elif compare_numerically(c, "<", a, rtol=rtol, atol=atol):
            # minus preserves right-hand order
            # bca -> b-ac
            cell = [cell[0], -cell[2], cell[1]]
    elif compare_numerically(a, "<", c, rtol=rtol, atol=atol):
        # abc -> cab
        cell = [cell[2], cell[0], cell[1]]
    elif compare_numerically(b, "<", c, rtol=rtol, atol=atol):
        # minus preserves right-hand order
        # abc -> a-cb
        cell = [cell[0], -cell[2], cell[1]]

    return cell


def ORCI_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the ORCI lattice conditions.

    See :ref:`guide_orci` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitiv4e unit cell.
    """

    cell = np.array(cell)

    a, b, c, alpha, beta, gamma = Cell.params(TRANSFORM_TO_CONVENTIONAL["ORCI"] @ cell)

    if compare_numerically(a, ">", b, rtol=rtol, atol=atol):
        # minus preserves right-hand order
        # abc - > bca
        cell = [cell[1], cell[2], cell[0]]
        if compare_numerically(b, ">", c, rtol=rtol, atol=atol):
            # minus preserves right-hand order
            # bca -> -cba
            cell = [-cell[1], cell[0], cell[2]]
        elif compare_numerically(c, ">", a, rtol=rtol, atol=atol):
            # minus preserves right-hand order
            # bca -> b-ac
            cell = [cell[0], -cell[2], cell[1]]
    elif compare_numerically(a, ">", c, rtol=rtol, atol=atol):
        # abc -> cab
        cell = [cell[2], cell[0], cell[1]]
    elif compare_numerically(b, ">", c, rtol=rtol, atol=atol):
        # minus preserves right-hand order
        # abc -> a-cb
        cell = [cell[0], -cell[2], cell[1]]

    return cell


def ORCC_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the ORCC lattice conditions.

    See :ref:`guide_orcc` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """

    a, b, c, alpha, beta, gamma = Cell.params(cell)

    # a == c
    if compare_numerically(a, "==", c, rtol=rtol, atol=atol):
        cell = [cell[2], cell[0], cell[1]]
    # b = c
    elif compare_numerically(b, "==", c, rtol=rtol, atol=atol):
        cell = [cell[1], cell[2], cell[0]]

    a, b, c, alpha, beta, gamma = Cell.params(cell)

    cell = np.array(cell)

    a, b, c, alpha, beta, gamma = Cell.params(TRANSFORM_TO_CONVENTIONAL["ORCC"] @ cell)

    if compare_numerically(a, ">", b, rtol=rtol, atol=atol):
        # minus preserves right-hand order
        cell = [-cell[1], cell[0], cell[2]]

    return cell


def HEX_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the HEX lattice conditions.

    See :ref:`guide_hex` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
        Ignored here, but preserved for the unification of input.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.
        Ignored here, but preserved for the unification of input.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """
    cell = np.array(cell)
    a, b, c, alpha, beta, gamma = Cell.params(cell)

    # a == c
    if compare_numerically(beta, "==", 120.0, eps=ABS_TOL_ANGLE):
        cell = [cell[2], cell[0], cell[1]]
    # b = c
    elif compare_numerically(alpha, "==", 120.0, eps=ABS_TOL_ANGLE):
        cell = [cell[1], cell[2], cell[0]]

    return cell


def RHL_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the RHL lattice conditions.

    See :ref:`guide_rhl` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
        Ignored here, but preserved for the unification of input.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.
        Ignored here, but preserved for the unification of input.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """

    return np.array(cell)


def MCL_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the MCL lattice conditions.

    See :ref:`guide_mcl` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """

    cell = np.array(cell)
    a, b, c, alpha, beta, gamma = Cell.params(cell)

    # beta != 90
    if compare_numerically(beta, "!=", 90.0, eps=ABS_TOL_ANGLE):
        cell = [cell[1], cell[2], cell[0]]
    # gamma != 90
    elif compare_numerically(gamma, "!=", 90.0, eps=ABS_TOL_ANGLE):
        cell = [cell[2], cell[0], cell[1]]

    a, b, c, alpha, beta, gamma = Cell.params(cell)

    # alpha > 90
    if compare_numerically(alpha, ">", 90.0, eps=ABS_TOL_ANGLE):
        cell = [cell[0], cell[2], -cell[1]]

    a, b, c, alpha, beta, gamma = Cell.params(cell)

    # b > c
    if compare_numerically(b, ">", c, rtol=rtol, atol=atol):
        cell = [-cell[0], cell[2], cell[1]]

    return cell


def MCLC_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the MCLC lattice conditions.

    See :ref:`guide_mclc` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """

    a, b, c, alpha, beta, gamma = Cell.params(cell)

    # a == c
    if compare_numerically(a, "==", c, rtol=rtol, atol=atol):
        cell = [cell[2], cell[0], cell[1]]
    # b == c
    elif compare_numerically(b, "==", c, rtol=rtol, atol=atol):
        cell = [cell[1], cell[2], cell[0]]

    cell = np.array(cell)
    a, b, c, alpha, beta, gamma = Cell.params(TRANSFORM_TO_CONVENTIONAL["MCLC"] @ cell)

    # alpha > 90
    if compare_numerically(alpha, ">", 90.0, eps=ABS_TOL_ANGLE):
        cell = [cell[0], cell[2], -cell[1]]

    cell = np.array(cell)
    a, b, c, alpha, beta, gamma = Cell.params(TRANSFORM_TO_CONVENTIONAL["MCLC"] @ cell)

    # b > c
    if compare_numerically(b, ">", c, rtol=rtol, atol=atol):
        cell = [-cell[0], cell[2], cell[1]]

    return cell


# TODO
def TRI_standardize_cell(cell, rtol=REL_TOL, atol=ABS_TOL, resiprocal=False):
    r"""
    Analyse arbitrary cell and redefine vectors if required to satisfy the TRI lattice conditions.

    See :ref:`guide_tri` for the details.

    Parameters
    ----------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    rtol : float, default ``REL_TOL``
        Relative tolerance for numerical comparison.
    atol : float, default ``ABS_TOL``
        Absolute tolerance for numerical comparison.
    resiprocal : bool, default False
        Whether to interpret input as reciprocal cell.

    Returns
    -------
    cell : (3,3) :numpy:`ndarray`
        Primitive unit cell.
    """

    return np.array(cell)