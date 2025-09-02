# Sin Value Calculator with Python

A simple Python script that calculates the sine of a given angle in degrees.

##  Features

- Ask user to how many times they want to calculate sine values.
- Takes user input for an angle in degrees
- Converts the input to radians
- Calculates the sine value using Python’s built-in `math.sin`
- Displays the result with clear formatting
- Supports multiple calculations in a single run.
- Rounds results to **4 decimal places** for readability.

##  Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/0PKunal/Sin-Value-Calculator-with-Python.git


2. Navigate to the project directory:

   ```bash
   cd Sin-Value-Calculator-with-Python
   ```

### Usage

Run the script using:

```bash
python sin_value_calculator.py
```

You’ll be prompted to enter an angle in degrees. Once entered, the script will output the sine of that angle.

## Example

```bash
How many times to calculate: 3

Set 1
Enter the angel: 30
The Sin value of 30.0° is 0.5000

Set 2
Enter the angel: 45
The Sin value of 45.0° is 0.7071

Set 3
Enter the angel: 60
The Sin value of 60.0° is 0.8660
```

## Expected Input & Output

| Input (degrees) | Output (sine value) |
| --------------- | ------------------- |
| 0               | 0.0                 |
| 90              | 1.0                 |
| 180             | 0.0                 |
| 270             | -1.0                |
| 360             | 0.0                 |

*(Results may vary slightly due to floating-point precision.)*

## How It Works

The script:
1. Prompts the user to enters how many times they want to calculate sine values.
2. Prompts the user for an angle in degrees
3. Converts it to radians using `math.radians`
4. Calculates the sine using `math.sin`
5. Prints the result

## Requirements

* Python 3.x (3.13.5 Recomended)
* Standard library only (`math` module)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Optional Enhancements

If you’d like to extend this project, consider adding:

* Support for radians input as an alternative
* A graphical user interface (GUI) using Tkinter
* Additional trigonometric functions (cos, tan, etc.)
* Command-line arguments using `argparse` for automation
---
<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/0PKunal">0PKunal</a></p>
  <p>If this project helped you, please give it a ⭐️</p>
</div>
