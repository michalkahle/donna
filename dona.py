from collections import OrderedDict
import itertools
import numpy as np
import pandas as pd

class dframe:
    """
    Dictionary of NumPy arrays that are broadcastable together.
    """
    def __init__(self, data=None):
        self._data = OrderedDict()
        if isinstance(data, dict):
            for col in data.keys():
                if isinstance(data[col], np.ndarray):
                    self._data[col] = data[col]
                else:
                    self._data[col] = np.array(data[col])
        else:
            raise ValueError('Type %s not yet supported.' % type(data))
        if not is_broadcastable(self._data.values()):
            raise ValueError('Arrays are not broadcastable together.')

    def __repr__(self, width=80):
        col_width = []
        col_widths = np.zeros([len(self._data), 3])
        for name, arr in self._data.items():
            #max(len(name), len(str(arr.shape)), len)
            col_w = max([len(str(x)) for x in (name, arr.shape, arr.dtype)])
            #col_widths[ len(name)
            print('#', name, len(name), str(arr.shape), len(str(arr.shape)), arr.dtype)

    def __repr__(self):
        buf = StringIO("")
        max_rows = get_option("display.max_rows")
        min_rows = get_option("display.min_rows")
        max_cols = get_option("display.max_columns")
        max_colwidth = get_option("display.max_colwidth")
        show_dimensions = get_option("display.show_dimensions")
        if get_option("display.expand_frame_repr"):
            width, _ = console.get_console_size()
        else:
            width = None
        self.to_string(
            buf=buf,
            max_rows=max_rows,
            min_rows=min_rows,
            max_cols=max_cols,
            line_width=width,
            max_colwidth=max_colwidth,
            show_dimensions=show_dimensions,
        )

        return buf.getvalue()




        return str(self._data)
    # def __str__(self):
    #     return ''















def is_broadcastable(arrays):
    shapes = [x.shape[::-1] for x in arrays]
    for dim in itertools.zip_longest(*shapes):
        if len(set(dim) - {None, 1}) > 1:
            return False
    return True


if __name__ == '__main__':
    pass
