import xlwings as xw
import pandas as pd
import os

def main():
    wb = xw.Book.caller()

    #path to working dir : os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.dirname(os.path.realpath(__file__))+"\\data\\iris.csv")
    df['total_length'] =  df['sepal_length'] + df['petal_length']
    wb.sheets[0].range('A1').value = df

@xw.func
def hello(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    xw.Book("IntroXlwings.xlsm").set_mock_caller()
    main()
