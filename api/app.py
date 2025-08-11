from flask import Flask, jsonify
from flask_cors import CORS
from db.database import get_db_connection
from datetime import datetime
import os

HOST = os.getenv('API_HOST', '0.0.0.0')
PORT = int(os.getenv('API_PORT', '5000'))
DEBUG = os.getenv('API_DEBUG', 'False').lower() == 'true'

app = Flask(__name__)
CORS(app)

@app.route('/api/stats/current', methods=['GET'])
def get_current_stats():
    """Get the most recent stats for all categories"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    stats = {}
    categories = ['ppg', 'rpg', 'apg', 'spg', 'bpg']
    
    for category in categories:
        cursor.execute(f'''
            SELECT player, team, stat_value, date_recorded 
            FROM stats 
            WHERE stat_type = ? 
            ORDER BY date_recorded DESC 
            LIMIT 1
        ''', (category,))
        result = cursor.fetchone()
        
        if result:
            stats[category] = {
                'player': result[0],
                'team': result[1],
                'value': result[2],
                'last_updated': result[3]
            }
    
    conn.close()
    return jsonify(stats)

@app.route('/api/stats/historical/<category>', methods=['GET'])
def get_historical_stats(category):
    """Get historical stats for a specific category"""
    if category not in ['ppg', 'rpg', 'apg', 'spg', 'bpg']:
        return jsonify({'error': 'Invalid category'}), 400
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT player, team, stat_value, date_recorded 
        FROM stats 
        WHERE stat_type = ? 
        ORDER BY date_recorded DESC 
        LIMIT 10
    ''', (category,))
    
    results = cursor.fetchall()
    historical_data = [{
        'player': row[0],
        'team': row[1],
        'value': row[2],
        'date': row[3]
    } for row in results]
    
    conn.close()
    return jsonify(historical_data)

@app.route('/api/stats/analysis', methods=['GET'])
def get_analysis():
    """Get the latest analysis results"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT analysis_type, result, date_analyzed
        FROM analysis_results
        ORDER BY date_analyzed DESC
    ''')
    
    results = cursor.fetchall()
    analysis_data = [{
        'type': row[0],
        'result': row[1],
        'date': row[2]
    } for row in results]
    
    conn.close()
    return jsonify(analysis_data)

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
