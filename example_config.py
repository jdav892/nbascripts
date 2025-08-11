"""
Example script showing how to use the configuration system
"""
from utils.config import get_config
from db.database import init_db, set_threshold
from scrapers.spg import scrape_steals
from analyzers.mvps import analyze_mvp_candidates

def setup_thresholds():
    """Set up statistical thresholds from configuration"""
    config = get_config()
    thresholds = config.get('thresholds', {})
    
    for stat_type, values in thresholds.items():
        set_threshold(
            stat_type,
            min_threshold=values.get('min'),
            max_threshold=values.get('max')
        )

def main():
    # Initialize the database
    init_db()
    
    # Set up thresholds from configuration
    setup_thresholds()
    
    # Run a sample scrape
    scrape_steals()
    
    # Run MVP analysis
    mvp_candidates = analyze_mvp_candidates()
    
    # Print configuration info
    config = get_config()
    print("\nCurrent Configuration:")
    print(f"Environment: {config.get('env', default='development')}")
    print(f"Database Path: {config.get('database', 'path')}")
    print(f"Logging Level: {config.get('logging', 'level')}")
    
    if mvp_candidates:
        print("\nMVP Candidates found!")
        for player, categories in mvp_candidates.items():
            print(f"\n{player} is leading in {len(categories)} categories:")
            for cat in categories:
                print(f"- {cat['stat_type']}: {cat['value']:.2f}")

if __name__ == "__main__":
    main()
