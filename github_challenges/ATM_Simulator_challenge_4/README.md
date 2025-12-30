<div align="center">

# 🏧 CLI ATM System

A secure, interactive command-line interface (CLI) ATM simulator. 
Built with Python, this tool features a stylish menu-driven interface, secure PIN masking, and real-time transaction processing with color-coded feedback.

</div>

## 📸 Demo Preview

![Terminal Preview](atm-demo.gif)

## Features

- **Interactive Menu System** - Navigate options using arrow keys via `questionary`
- **Secure Authentication** - PIN inputs are masked (hidden) for security
- **Transaction Handling** - Supports Deposits, Withdrawals, and Balance inquiries
- **Input Validation** - robust error handling for invalid PINs, negative amounts, or insufficient funds
- **Visual Feedback** - Color-coded outputs (Green for success, Red for errors) using `colorama`
- **Account Management** - Includes functionality to safely change your 4-digit PIN

## Getting Started

### Prerequisites
Ensure you have Python installed. You will also need to install the required libraries found in `requirements.txt`.

```bash
pip install -r requirements.txt

```

### How to Run

1. Download the script (`main.py`) to your local machine.
2. Open your terminal or command prompt.
3. Run the script:
```bash
python main.py

```

4. **Setup Phase**: Enter your Name, create a 4-digit PIN, and set an opening balance.
5. **Operation Phase**: Use the arrow keys to select an action from the menu.

## System Logic & Rules

The system mimics real-world banking constraints:

* **Authentication**: You must re-enter your PIN for **every** transaction to ensure security.
* **PIN Requirements**: A PIN must be exactly **4 digits**.
* **Withdrawals**: You cannot withdraw more money than your current balance (No Overdraft).
* **Deposits/Withdrawals**: Amounts must be positive values.
* **Data Persistence**: The account data persists as long as the script is running. Exiting clears the session.

## Technologies Used

* **Python 3.13** - Core programming language
* **Questionary** - For the interactive CLI menus and arrow-key navigation
* **Colorama** - For cross-platform colored terminal text

**Enjoy the banking experience!** 💳 If you found this project helpful, please consider giving it a ⭐

<p align="center">
  Made with ❤️ by im-junaid
</p>
