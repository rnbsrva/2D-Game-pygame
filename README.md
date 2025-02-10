# **2D Game Development Project**

This project is a 2D game developed using the **Pygame** library in Python. The game features engaging mechanics and showcases essential elements of game development, including player movement, collision detection, scoring, and multiple levels.

---

## **Game Description**

The game is a 2D game where the player controls a character to collect coins, avoid enemies, and complete levels. The game includes two levels with varying difficulty, a camera system that follows the player, and win/lose mechanics. The player must collect a specific number of coins to complete each level while avoiding enemies and their attacks.

---

## **Key Features**

1. **Player Movement**:
   - The player can move in four directions (up, down, left, right) using the arrow keys.
   - Collision detection prevents the player from passing through walls.

2. **Camera System**:
   - The camera follows the player and restricts movement to the level boundaries.

3. **Collectible Items**:
   - The player can collect coins to increase their score.
   - Completing a level requires collecting a specific number of coins.

4. **Enemies**:
   - Enemies move randomly around the level and can damage the player on contact.
   - The player loses health when colliding with enemie's bullets.

5. **Multiple Levels**:
   - The game includes two levels with varying difficulty:
     - **Level 1 (Easy)**: Fewer enemies and more coins.
     - **Level 2 (Hard)**: More enemies, fewer coins, and faster enemy movement.

6. **Win/Lose Mechanics**:
   - The player wins by completing both levels and collecting 20 coins.
   - The player loses if their health reaches zero.

7. **Sound Effects**:
   - Background music plays continuously during gameplay.
   - Sound effects are included for collecting coins and colliding with enemies.

8. **Text Interface**:
   - The current score, player health, and level are displayed on the screen.
   - Messages like "Level Completed" and "Game Over" are displayed at key moments.

---

## **Screenshots**

Here are some screenshots of key moments in the game:

### **Level 1**
![Level 1 Screenshot](screenshots/level-1.png)
- The player starts in Level 1, where they must collect coins, avoid enemies and enemie's bullets.

### **Level 2**
![Level 2 Screenshot](screenshots/level-2.png)
- In Level 2, the difficulty increases with more enemies and fewer coins.

### **Game Over**
![Game Over Screenshot](screenshots/game-over.png)
- The "Game Over" screen is displayed when the player loses all their health.

### **Level Completed**
![Level Completed Screenshot](screenshots/level-completed.png)
- The "Level Completed" screen is displayed when the player finishes a level.

---

## **Installation and Launch Instructions**

Follow these steps to run the game on your local machine:

### **Prerequisites**
- **Python 3.x**: Make sure Python is installed on your system.
- **Pygame**: Install the Pygame library using pip.

### **Steps**
1. **Clone the Repository**:
   ```bash
   git clone URL
   cd your-repo-name
   ```

2. **Install Dependencies**:
   Install the required Pygame library:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   Execute the main Python script to start the game:
   ```bash
   python main.py
   ```

4. **Controls**:
   - Use the **arrow keys** to move the player.
   - Collect coins to increase your score.
   - Avoid enemies and their bullets to survive.

---

## **Implementation Details**

### **Main Mechanics**
1. **Player Movement**:
   - The player's position is updated based on keyboard input.
   - Collision detection ensures the player cannot pass through walls.

2. **Camera System**:
   - The camera follows the player and is restricted to the level boundaries.

3. **Enemy Movement**:
   - Enemies move randomly and shoot bullets at the player.
   - The player loses health upon collision with enemies or their bullets.

4. **Scoring and Win/Lose Conditions**:
   - The player's score increases when they collect coins.
   - The game ends when the player completes both levels or loses all their health.

5. **Sound Effects**:
   - Background music and sound effects are implemented using the Pygame mixer.

6. **Text Interface**:
   - The current score, player health, and level are displayed using Pygame's font rendering.

---

## **Conclusion**

This project demonstrates the implementation of a 2D game using Pygame. It includes all the required features, such as player movement, collision detection, scoring, and multiple levels. The game is optimized for performance and provides an enjoyable gaming experience.

---

Assem Zhakanova 😊#   2 D - G a m e - p y g a m e  
 