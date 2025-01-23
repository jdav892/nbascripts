from datetime import datetime as dt
import pandas 

today = dt.today()

def writer(file_name):
    def decorator(function):
        def file_entry():
            output = function()
            with open(file_name, 'a', encoding="utf-8") as f:
                f.write(f"{output}, {today}\n")
        return file_entry
    return decorator

def reader(file_name):
    def decorator(function):
        def wrapper(*args, **kwargs):
            df = pandas.read_csv(file_name, usecols=[0, 1, 2])
            return function(df, *args, **kwargs)
        return wrapper 
    return decorator