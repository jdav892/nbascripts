from datetime import datetime as dt

today = dt.today()

def writer(file_name):
    def decorator(function):
        def file_entry():
            output = function()
            with open(file_name, 'a') as f:
                f.write(f"{output}, {today}\n")
        return file_entry
    return decorator