import numpy as np


def make_json_serializable(data: dict) -> dict:
    """
    Convert NumPy values into native
    Python types for Qdrant payloads.
    """

    output = {}

    for key, value in data.items():

        if isinstance(value, np.ndarray):
            output[key] = value.tolist()

        elif isinstance(value, np.generic):
            output[key] = value.item()

        else:
            output[key] = value

    return output