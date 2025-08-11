import sqlite3
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = sqlite3.connect('nba_stats.db')
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    """Initialize the database schema"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Create tables for different stats
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS stat_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stat_type TEXT NOT NULL,
            player_name TEXT NOT NULL,
            value REAL NOT NULL,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Create table for thresholds
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS stat_thresholds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stat_type TEXT UNIQUE NOT NULL,
            min_threshold REAL,
            max_threshold REAL
        )
        ''')
        
        conn.commit()

def set_threshold(stat_type, min_threshold=None, max_threshold=None):
    """Set or update thresholds for a specific stat type"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO stat_thresholds (stat_type, min_threshold, max_threshold)
            VALUES (?, ?, ?)
            ON CONFLICT(stat_type) DO UPDATE SET
                min_threshold = excluded.min_threshold,
                max_threshold = excluded.max_threshold
        ''', (stat_type, min_threshold, max_threshold))
        conn.commit()

def save_stat(stat_type, player_name, value):
    """Save a new stat record to the database"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO stat_records (stat_type, player_name, value)
            VALUES (?, ?, ?)
        ''', (stat_type, player_name, value))
        conn.commit()
        return cursor.lastrowid

def get_thresholds(stat_type):
    """Get the current thresholds for a stat type"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT min_threshold, max_threshold 
            FROM stat_thresholds 
            WHERE stat_type = ?
        ''', (stat_type,))
        return cursor.fetchone()

def send_email_notification(subject, body, to_email):
    """Send an email notification"""
    # Replace these with your email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your-email@gmail.com"  # Replace with your email
    sender_password = "your-app-password"   # Replace with your app password
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    
    message.attach(MIMEText(body, "plain"))
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

def check_and_notify(stat_type, player_name, value):
    """Check if a value crosses any thresholds and send notifications if needed"""
    thresholds = get_thresholds(stat_type)
    if thresholds:
        min_val, max_val = thresholds
        if min_val and value <= min_val:
            send_email_notification(
                f"Low {stat_type} Alert",
                f"{player_name} has reached a low of {value} in {stat_type}",
                "your-email@example.com"  # Replace with your email
            )
        elif max_val and value >= max_val:
            send_email_notification(
                f"High {stat_type} Alert",
                f"{player_name} has reached a high of {value} in {stat_type}",
                "your-email@example.com"  # Replace with your email
            )
