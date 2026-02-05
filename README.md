# 🏷️ Discount Calculator

![Python Banner](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📋 Project Overview

This is a simple Python script designed to calculate the final price of an item after applying a discount. It includes a specific condition: **the discount is only applied if it is 20% or higher**. If the discount is less than 20%, the original price is returned.

---

## 🚀 Features

* **Conditional Discounting:** Automatically checks if the discount meets the minimum threshold (20%).
* **User Input:** Prompts the user to enter the original price and discount percentage.
* **Input Validation:** Includes error handling for non-numeric inputs.
* **Formatted Output:** Displays the final price formatted to two decimal places.

---

## 🛠️ How It Works

1. The user enters the **Original Price**.
2. The user enters the **Discount Percentage**.
3. The program checks the condition:
   * **If Discount >= 20%**: The discount is subtracted from the original price.
   * **If Discount < 20%**: No changes are made; the original price remains.
4. The final result is printed to the screen.

---

## 🏃‍♂️ How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Cynthia-M-M/Discount-Calculator.git](https://github.com/Cynthia-M-M/Discount-Calculator.git)
   Here is the **rest of the README** to complete your Discount Calculator project.

I have fixed the `git clone` command (removing the brackets) and added the **Usage Examples** so users can clearly see how the 20% rule works.

### **Copy this block and paste it to finish your file:**

```markdown
   git clone https://github.com/Cynthia-M-M/Discount-Calculator.git

```

### 2. Navigate to the Folder

```bash
cd Discount-Calculator

```

### 3. Run the Program

```bash
python discount_calculator.py

```

---

## 💻 Usage Examples

Here is how the program behaves in two different scenarios:

### Scenario A: High Discount (Applied)

* **Original Price:** 1000
* **Discount:** 25%
* **Result:** Discount is applied.

```text
Enter the original price of the item: 1000
Enter the discount percentage: 25
The final price is: 750.00

```

### Scenario B: Low Discount (Not Applied)

* **Original Price:** 1000
* **Discount:** 10%
* **Result:** Discount is ignored (less than 20%).

```text
Enter the original price of the item: 1000
Enter the discount percentage: 10
No discount applied. The original price is: 1000.00

```

---

## 📂 Project Structure

```text
Discount-Calculator/
│
├── discount_calculator.py   # Main script logic
└── README.md                # Project documentation

```

---

## 🧠 Code Logic

The core logic relies on a simple function that decides whether to apply the math or return the original value:

```python
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

```

---

## 📄 License

This project is open-source and created for educational purposes.

```

```
