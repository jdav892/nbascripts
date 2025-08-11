from decorators import db_reader
from database import set_threshold
import pandas as pd
from datetime import datetime, timedelta

# Set your thresholds for different stats
def configure_thresholds():
    # Steals per game thresholds
    set_threshold("steals_per_game", min_threshold=1.5, max_threshold=3.0)
    
    # Blocks per game thresholds
    set_threshold("blocks_per_game", min_threshold=1.8, max_threshold=3.5)
    
    # Points per game thresholds
    set_threshold("points_per_game", min_threshold=20.0, max_threshold=35.0)
    
    # Rebounds per game thresholds
    set_threshold("rebounds_per_game", min_threshold=8.0, max_threshold=15.0)
    
    # Assists per game thresholds
    set_threshold("assists_per_game", min_threshold=6.0, max_threshold=12.0)

# Analysis functions for each stat type
@db_reader("steals_per_game")
def analyze_steals(df):
    """Analyze steals per game trends"""
    if df.empty:
        return "No steals data available"
    
    latest = df.iloc[0]
    week_ago = datetime.now() - timedelta(days=7)
    weekly_data = df[pd.to_datetime(df['recorded_at']) >= week_ago]
    
    analysis = {
        'current_leader': latest['player_name'],
        'current_spg': latest['value'],
        'weekly_avg': weekly_data['value'].mean() if not weekly_data.empty else None,
        'weekly_trend': 'UP' if not weekly_data.empty and latest['value'] > weekly_data['value'].mean() else 'DOWN'
    }
    return analysis

@db_reader("blocks_per_game")
def analyze_blocks(df):
    """Analyze blocks per game trends"""
    if df.empty:
        return "No blocks data available"
    
    latest = df.iloc[0]
    week_ago = datetime.now() - timedelta(days=7)
    weekly_data = df[pd.to_datetime(df['recorded_at']) >= week_ago]
    
    analysis = {
        'current_leader': latest['player_name'],
        'current_bpg': latest['value'],
        'weekly_avg': weekly_data['value'].mean() if not weekly_data.empty else None,
        'weekly_trend': 'UP' if not weekly_data.empty and latest['value'] > weekly_data['value'].mean() else 'DOWN'
    }
    return analysis

@db_reader("points_per_game")
def analyze_points(df):
    """Analyze points per game trends"""
    if df.empty:
        return "No points data available"
    
    latest = df.iloc[0]
    week_ago = datetime.now() - timedelta(days=7)
    weekly_data = df[pd.to_datetime(df['recorded_at']) >= week_ago]
    
    analysis = {
        'current_leader': latest['player_name'],
        'current_ppg': latest['value'],
        'weekly_avg': weekly_data['value'].mean() if not weekly_data.empty else None,
        'weekly_trend': 'UP' if not weekly_data.empty and latest['value'] > weekly_data['value'].mean() else 'DOWN'
    }
    return analysis

@db_reader("rebounds_per_game")
def analyze_rebounds(df):
    """Analyze rebounds per game trends"""
    if df.empty:
        return "No rebounds data available"
    
    latest = df.iloc[0]
    week_ago = datetime.now() - timedelta(days=7)
    weekly_data = df[pd.to_datetime(df['recorded_at']) >= week_ago]
    
    analysis = {
        'current_leader': latest['player_name'],
        'current_rpg': latest['value'],
        'weekly_avg': weekly_data['value'].mean() if not weekly_data.empty else None,
        'weekly_trend': 'UP' if not weekly_data.empty and latest['value'] > weekly_data['value'].mean() else 'DOWN'
    }
    return analysis

@db_reader("assists_per_game")
def analyze_assists(df):
    """Analyze assists per game trends"""
    if df.empty:
        return "No assists data available"
    
    latest = df.iloc[0]
    week_ago = datetime.now() - timedelta(days=7)
    weekly_data = df[pd.to_datetime(df['recorded_at']) >= week_ago]
    
    analysis = {
        'current_leader': latest['player_name'],
        'current_apg': latest['value'],
        'weekly_avg': weekly_data['value'].mean() if not weekly_data.empty else None,
        'weekly_trend': 'UP' if not weekly_data.empty and latest['value'] > weekly_data['value'].mean() else 'DOWN'
    }
    return analysis

def run_all_analysis():
    """Run analysis for all stat categories"""
    # Configure thresholds (adjust these values based on your preferences)
    configure_thresholds()
    
    # Run all analyses
    analyses = {
        'steals': analyze_steals(),
        'blocks': analyze_blocks(),
        'points': analyze_points(),
        'rebounds': analyze_rebounds(),
        'assists': analyze_assists()
    }
    
    # Print results
    for stat_type, analysis in analyses.items():
        if isinstance(analysis, str):
            print(f"\n{stat_type.upper()}: {analysis}")
        else:
            print(f"\n{stat_type.upper()} Analysis:")
            print(f"Current Leader: {analysis['current_leader']}")
            print(f"Current Value: {analysis['current_' + stat_type[0] + 'pg']:.2f}")
            if analysis['weekly_avg']:
                print(f"Weekly Average: {analysis['weekly_avg']:.2f}")
                print(f"Trend: {analysis['weekly_trend']}")

if __name__ == "__main__":
    run_all_analysis()