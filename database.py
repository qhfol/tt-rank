import sqlite3

# Kết nối đến database
conn = sqlite3.connect("players.db")
cursor = conn.cursor()

# Tạo bảng nếu chưa tồn tại
cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        score INTEGER,
        rank TEXT
    )
''')

# Hàm xếp hạng theo điểm số
def get_rank(score):
    if 1500 <= score <= 1599:
        return "E"
    elif 1600 <= score <= 1699:
        return "D"
    elif 1700 <= score <= 1799:
        return "C"
    elif 1800 <= score <= 1899:
        return "B"
    elif score >= 1900:
        return "A"
    return "Chưa xếp hạng"

# Thêm vận động viên vào database
def add_player(name, score):
    rank = get_rank(score)
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO players (name, score, rank) VALUES (?, ?, ?) ON CONFLICT(name) DO UPDATE SET score=excluded.score, rank=excluded.rank", (name, score, rank))
    conn.commit()
    conn.close()

# Lấy danh sách vận động viên
def get_players():
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, score, rank FROM players ORDER BY score DESC")
    players = cursor.fetchall()
    conn.close()
    return players

if __name__ == "__main__":
    players = [
        ("Nguyễn Văn A", 1550),
        ("Trần Thị B", 1620),
        ("Lê Văn C", 1750),
        ("Phạm Minh D", 1850),
        ("Hoàng Tuấn E", 1950),
        ("Vũ Chí Cường", 2000)
    ]
    for name, score in players:
        add_player(name, score)
    print("Dữ liệu đã được khởi tạo.")
