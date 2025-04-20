# # chained_comparisons.py

# def check_x_range(x: int):
#     if 10 < x < 20:
#         print(f"{x} is between 10 and 20")
#     else:
#         print(f"{x} is NOT between 10 and 20")

# def check_multiple_ranges(x: int, y: int):
#     if 1 < x < 5 < y < 10:
#         print(f"x = {x} is between 1 and 5, and y = {y} is between 5 and 10")
#     else:
#         print(f"x = {x} and y = {y} do NOT meet the condition")

# # Run demo
# if __name__ == "__main__":
#     print("🔎 Chained Comparison Demo in Python")

#     x = int(input("Enter value for x: "))
#     check_x_range(x)

#     print("\n🔁 Let's try multiple comparisons:")
#     x = int(input("Enter value for x (between 1 and 5): "))
#     y = int(input("Enter value for y (between 5 and 10): "))
#     check_multiple_ranges(x, y)






x = int(input("Enter a number: "))
# if 10 < x and x < 20
if 10 < x < 20:
    print("x is between 10 and 20")
else:
    print("x is NOT between 10 and 20")
