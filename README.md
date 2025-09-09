# IPL Auction
A **Python-based auction management system** for simulating IPL auctions. It allows bidding on players, managing teams and handling players. All Players and Teams Data Handling using file operations.

## 📌 Features
- Manage the **auction process** for players.
- Manage team budgets and track spending.
- Track player status (**Available**, **Sold**, **Unsold**).
- Text files (`.txt`) included to act as a database with sample data.
- Console-based interaction for simplicity.

## 🛠️ Auction Process
1. Enter Player ID
2. Start Bidding
3. Highest Bidder Wins
4. Update Teams and Player data

## 📖 Notes
- Data Files: `availablePlayers.txt`,`soldPlayer.txt`,`Teams.txt`,`UnsoldPlayers.txt`
- `IPLauction.py` → main entry point of the project.
- `IPL` class → handles auction logic and data management.
- `File` class → handles txt files operations.
