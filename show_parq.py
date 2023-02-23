import sys
from tkinter import *
from pandastable import Table
import pandas as pd
from pathlib import Path


class TestApp(Frame):
    """show table"""

    def __init__(self, df, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        # self.main.geometry("600x400+200+100")
        self.main.title("Table app")
        f = Frame(self.main)
        f.pack(fill=BOTH, expand=1)
        self.table = pt = Table(f, dataframe=df, showtoolbar=True, showstatusbar=True)
        pt.show()
        return


def main():
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
        df = pd.read_parquet(p)
        app = TestApp(df)
        # launch the app
        app.mainloop()


if __name__ == "__main__":
    main()
