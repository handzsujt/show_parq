import sys
import tkinter as tk
from tkinter.messagebox import showwarning
from tkinter.filedialog import askopenfilename
from pathlib import Path

import numpy as np
import pandas as pd
from netCDF4 import Dataset
from pandastable import Table


class TestApp(tk.Frame):
    """show table"""

    def __init__(self, df, parent=None):
        self.parent = parent
        tk.Frame.__init__(self)
        self.main = self.master
        # self.main.geometry("600x400+200+100")
        self.main.title("Table app")
        f = tk.Frame(self.main)
        f.pack(fill=tk.BOTH, expand=1)
        self.table = pt = Table(f, dataframe=df, showtoolbar=True, showstatusbar=True)
        pt.show()
        return


def main():
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
    else:
        p = Path(askopenfilename())

    if p.suffix in [".parq", ".parquet"]:
        df = pd.read_parquet(p)
    elif p.suffix in [".nc", ".ncdf"]:
        dataset = Dataset(p, "r", keepweakref=True)
        d = {}
        for name, var in list(dataset.variables.items()):
            data = var[:]
            if np.ma.is_masked(data) and "float" in str(
                data.dtype
            ):  # NaNs are masked in ncdf
                d[name] = data.filled(np.NaN)
            else:
                d[name] = data
        df = pd.DataFrame(d)
    else:
        df = None

    if df is None:
        showwarning("Show Table", "File not found or file type not supported")
    else:
        app = TestApp(df)
        # launch the app
        app.mainloop()


if __name__ == "__main__":
    main()
