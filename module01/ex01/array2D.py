import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """This function returns a sliced list of lists (2D Lists)"""
    try:
        if not isinstance(family, list):
            raise AssertionError("family is not a list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("start or end are not integers")
        family_np = np.array(family)
        if family_np.ndim != 2:
            raise AssertionError("family present a wrong formatting")
        len_np = np.array([iter.shape[0] for iter in family_np])
        if len_np.max() != len_np.min():
            raise AssertionError("different sublength in family")
        cutted_list = family_np[start:end]
        shape0 = family_np.shape[0]
        shape1 = family_np.shape[1]
        print(f"My shape is : ({shape0}, {shape1})")
        shape0 = cutted_list.shape[0]
        shape1 = cutted_list.shape[1]
        print(f"My new shape is : ({shape0}, {shape1})")
        return cutted_list.tolist()
    except (AssertionError, TypeError, IndexError) as e:
        print(e)
        return []
