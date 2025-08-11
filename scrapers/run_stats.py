from spg import steal_leader
from bpg import block_leader
from ppg import scoring_leader
from rbpg import rebound_leader
from apg import assist_leader
from analysis import run_all_analysis

def collect_and_analyze():
    """Collect new data and run analysis"""
    print("Scraping in progress")
    
    # Collect all stats
    steal_leader()
    block_leader()
    scoring_leader()
    rebound_leader()
    assist_leader()
    
    print("\nScraping Complete")
    run_all_analysis()

if __name__ == "__main__":
    collect_and_analyze()
