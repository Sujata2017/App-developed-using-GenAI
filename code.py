=== app.py ===
```python
import random
import json

class GameBoard:
    def __init__(self, size=10):
        self.size = size
        self.board = self._initialize_board()
        self.snakes = {32: 10, 62: 19, 98: 78, 95: 59, 97: 79}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84}

    def _initialize_board(self):
        return [[0 for _ in range(self.size)] for _ in range(self.size)]

    def move_player(self, player, roll):
        new_pos = player.position + roll
        new_pos = self._check_snakes_and_ladders(new_pos)
        if new_pos <= 100:
            player.position = new_pos
        else:
            player.position = 100 - (new_pos - 100)
        return player.position

    def _check_snakes_and_ladders(self, position):
        if position in self.snakes:
            return self.snakes[position]
        if position in self.ladders:
            return self.ladders[position]
        return position

class Player:
    def __init__(self, name, position=0):
        self.name = name
        self.position = position

def roll_dice():
    return random.randint(1, 6)

def main():
    game_board = GameBoard()
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    while player1.position < 100 and player2.position < 100:
        roll = roll_dice()
        new_position = game_board.move_player(player1, roll)
        print(f"{player1.name} rolled a {roll} and moved to {new_position}")
        roll = roll_dice()
        new_position = game_board.move_player(player2, roll)
        print(f"{player2.name} rolled a {roll} and moved to {new_position}")
    if player1.position == 100:
        print(f"Congratulations! {player1.name} wins!")
    else:
        print(f"Congratulations! {player2.name} wins!")

if __name__ == "__main__":
    main()
```

=== templates/index.html ===
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snake and Ladder</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <h1>Snake and Ladder Game</h1>
    <button onclick="rollDice()">Roll Dice</button>
    <div id="board"></div>
    <script>
        function rollDice() {
            // Roll dice logic here
        }
    </script>
</body>
</html>
```

=== static/styles.css ===
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    text-align: center;
}

h1 {
    color: #333;
}

button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

#board {
    margin-top: 20px;
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    gap: 5px;
    width: 500px;
    margin: auto;
    background-color: #fff;
    padding: 5px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
```

=== static/config.json ===
```json
{
  "snakes": {
    "32": 10,
    "62": 19,
    "98": 78,
    "95": 59,
    "97": 79
  },
  "ladders": {
    "1": 38,
    "4": 14,
    "9": 31,
    "21": 42,
    "28": 84
  }
}
```