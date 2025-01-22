# Coffee Machine Project

Welcome to the **Coffee Machine** project! This Python program simulates a coffee vending machine, allowing users to purchase coffee, view the machine's resources, and enjoy a visually enhanced experience with ASCII art.

---

## Features

- **Menu Options**: Offers three coffee choices: `Espresso`, `Latte`, and `Cappuccino`.
- **Resource Tracking**: Tracks water, milk, and coffee availability.
- **Coin Processing**: Accepts coins (quarters, dimes, nickels, and pennies) to calculate payment.
- **Transaction Management**: Ensures sufficient payment and provides change.
- **Visually Enhanced Output**: Engages users with ASCII art for the coffee types and messages.

---

## Requirements

- Python 3.x

---

## How to Run

1. Clone the repository or download the script.
2. Open the terminal or command prompt and navigate to the script's directory.
3. Run the program using the command:

   ```bash
   python main.py
   ```

4. Follow the on-screen instructions to interact with the coffee machine.

---

## ASCII Art Example

### Welcome Screen
```
   __  __       _         __  __             _     
  |  \/  |     (_)       |  \/  |           | |    
  | \  / | __ _ _ _ __   | \  / | ___  _ __ | | __
  | |\/| |/ _` | | '_ \  | |\/| |/ _ \| '_ \| |/ /
  | |  | | (_| | | | | | | |  | | (_) | | | |   <  
  |_|  |_|\__,_|_|_| |_| |_|  |_|\___/|_| |_|_|\_\

```

### Coffee Art
#### Latte:
```
      ( (   
       ) )  
    ........
    |      |]
    \      /
     `----'
```
#### Espresso:
```
    {   }
     }_{ __{
    .-{   }-.
   (   }   { )
   |`-..-'|
   `-'||`-'
```
#### Cappuccino:
```
   (  )   (   )  )
    ) (   )  (  (
    ( )  (    ) )
    _____________
   <_____________> ___
   |             |/ _ \
   |               | | |
   |               |_| |
   |             |\___/
   |_____________|
```
---

## Sample Output

### Menu
```
What would you like? (espresso/latte/cappuccino):
```

### Successful Purchase
```
Here is your latte ☕. Enjoy!
```

### Insufficient Resources
```
Sorry, there is not enough water.
```

### Insufficient Payment
```
Sorry that's not enough money. Money refunded.
```

---

## Code Structure

### Functions
1. **`is_resource_sufficient(order_ingredients)`**
   - Checks if the resources are sufficient for the requested coffee.

2. **`process_coins()`**
   - Processes user inputs for coins and calculates the total amount.

3. **`is_transaction_successful(money_received, drink_cost)`**
   - Verifies payment sufficiency and updates profit.

4. **`make_coffee(drink_name, order_ingredients)`**
   - Prepares the coffee and deducts resources.

### Main Loop
- Continuously prompts the user for actions (`espresso`, `latte`, `cappuccino`, `report`, `off`).

---
