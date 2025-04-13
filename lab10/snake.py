import psycopg2
from datetime import datetime

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="your_database_name",
    user="your_username",
    password="your_password"
)
cur = conn.cursor()

# Create tables
def create_tables():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            level INTEGER NOT NULL DEFAULT 1,
            score INTEGER NOT NULL DEFAULT 0,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()

# Get or create user
def get_or_create_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
        print("User found.")
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        print("New user created.")
    return user_id

# Get user's last saved level and score
def get_user_progress(user_id):
    cur.execute('''
        SELECT level, score FROM user_score 
        WHERE user_id = %s 
        ORDER BY saved_at DESC LIMIT 1;
    ''', (user_id,))
    result = cur.fetchone()
    if result:
        level, score = result
        print(f"Last saved level: {level}, score: {score}")
        return level, score
    else:
        print("No saved progress. Starting at level 1.")
        return 1, 0

# Save progress (e.g., on pause)
def save_progress(user_id, level, score):
    cur.execute('''
        INSERT INTO user_score (user_id, level, score, saved_at)
        VALUES (%s, %s, %s, %s);
    ''', (user_id, level, score, datetime.now()))
    conn.commit()
    print("Game progress saved.")

# Example usage (mocked for demonstration)
if __name__ == "__main__":
    create_tables()
    username = input("Enter your username: ")
    user_id = get_or_create_user(username)
    level, score = get_user_progress(user_id)

    # Here you would start your actual snake game using the level and score

    # Mock: simulate a pause and save
    pause = input("Press 'p' to pause and save game: ")
    if pause.lower() == 'p':
        save_progress(user_id, level=2, score=150)  # Example values
        print("Game paused and progress saved.")

    cur.close()
    conn.close()
