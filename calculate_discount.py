def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount and return the final price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied, return the original price
        return price

# Prompt the user for the original price and discount percentage
def main():
    try:
        original_price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate the final price
        final_price = calculate_discount(original_price, discount_percent)
        
        # Print the final price or the original price
        if final_price != original_price:
            print(f"The final price after applying the discount is: ${final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: ${original_price:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for both price and discount.")

if __name__ == "__main__":
    main()
