import numpy as np


def give_bmi(heigth: list[int | float], weigth: list[int | float])\
      -> list[int | float]:
    """This function returns a list of bmi calculated for each user
represented by a list of heigths and a list of weigths"""
    try:
        heigth_np = np.array(heigth)
        weigth_np = np.array(weigth)
        if heigth_np.shape[0] != weigth_np.shape[0]:
            raise AssertionError("List have different sizes")
        if heigth_np.shape[0] == 0:
            raise AssertionError("The lists are empty")
        try:
            decoy_boolean = np.any(heigth_np <= 0) or np.any(weigth_np <= 0)
        except TypeError:
            raise AssertionError("List contains a string")
        if decoy_boolean:
            raise AssertionError("List contains negative numbers or zero")
        if heigth_np.ndim > 1 or weigth_np.ndim > 1:
            raise AssertionError("List contain sublist in it")
        result_np = (weigth_np / (heigth_np**2))
        result = result_np.tolist()
        return result
    except (TypeError, AssertionError, OverflowError) as e:
        print(e)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """This function returns a list of booleans that represent if the user
is over a limit of bmi value or not"""
    try:
        bmi_np = np.array(bmi)
        if bmi_np.shape[0] == 0:
            raise AssertionError("List passed as argument is empty")
        if limit < 0:
            raise AssertionError("Limit is a negative number")
        result_np = bmi_np > limit
        result = result_np.tolist()
        return result
    except (AssertionError, TypeError) as e:
        print(e)
        return []
