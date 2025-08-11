import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scrapers.database import get_db_connection, send_email_notification
from collections import defaultdict
import pandas as pd

def get_current_leaders():
    """Get the current leaders from all stat categories"""
    with get_db_connection() as conn:
        # Query to get the most recent leader for each stat type
        query = """
        WITH RankedStats AS (
            SELECT 
                stat_type,
                player_name,
                value,
                recorded_at,
                ROW_NUMBER() OVER (PARTITION BY stat_type ORDER BY recorded_at DESC) as rn
            FROM stat_records
        )
        SELECT stat_type, player_name, value, recorded_at
        FROM RankedStats
        WHERE rn = 1
        """
        
        # Read into a pandas DataFrame
        return pd.read_sql_query(query, conn)

def analyze_mvp_candidates():
    """
    Analyze players leading in multiple statistical categories
    and send notifications for potential MVP candidates
    """
    # Get current leaders
    leaders_df = get_current_leaders()
    
    # Count categories led by each player
    player_categories = defaultdict(list)
    for _, row in leaders_df.iterrows():
        player_categories[row['player_name']].append({
            'stat_type': row['stat_type'],
            'value': row['value']
        })
    
    # Check for players leading multiple categories
    mvp_candidates = {
        player: categories 
        for player, categories in player_categories.items() 
        if len(categories) >= 2  # Player leads in 2 or more categories
    }
    
    # If we found any MVP candidates, send notifications
    if mvp_candidates:
        for player, categories in mvp_candidates.items():
            # Create detailed message about the player's achievements
            category_details = "\n".join([
                f"- {cat['stat_type']}: {cat['value']:.2f}"
                for cat in categories
            ])
            
            subject = f"MVP Alert: {player} Leading Multiple Categories"
            body = f"""
{player} is currently leading in {len(categories)} statistical categories:

{category_details}

This level of performance across multiple categories suggests MVP-caliber play.
"""
            send_email_notification(subject, body, "your-email@example.com")
            
            # Also print to console
            print(f"\nMVP Alert: {player}")
            print(category_details)
    
    return mvp_candidates

def print_all_leaders():
    """Print current leaders in all categories"""
    leaders_df = get_current_leaders()
    
    print("\nCurrent Statistical Leaders:")
    print("-" * 50)
    
    for _, row in leaders_df.iterrows():
        print(f"{row['stat_type']:20} {row['player_name']:25} {row['value']:.2f}")

if __name__ == "__main__":
    print_all_leaders()
    mvp_candidates = analyze_mvp_candidates()
    
    if not mvp_candidates:
        print("\nNo players currently leading in multiple categories.")
