from datetime import datetime as dt
from database import save_stat, init_db

def db_writer(stat_type):
    def decorator(function):
        def wrapper():
            # Initialize database if not exists
            init_db()
            
            # Get player name and value from the scraper
            player_data = function()
            if isinstance(player_data, str):
                # Parse the string format "(name, value)"
                player_data = eval(player_data)
            
            player_name, value = player_data
            # Convert value to float if it's a string
            value = float(value)
            
            # Save to database
            save_stat(stat_type, player_name, value)
        return wrapper
    return decorator

def db_reader(stat_type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            from database import get_db_connection
            import pandas as pd
            
            with get_db_connection() as conn:
                # Query the database and convert to DataFrame
                df = pd.read_sql_query('''
                    SELECT player_name, value, recorded_at
                    FROM stat_records
                    WHERE stat_type = ?
                    ORDER BY recorded_at DESC
                ''', conn, params=(stat_type,))
                
            return function(df, *args, **kwargs)
        return wrapper 
    return decorator