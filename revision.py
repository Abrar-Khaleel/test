# Define the four cities
cities = ["New York", "Los Angeles", "Chicago", "Houston"]
# Initialize a list to store sales and discounts for each city
city_data = []
# Predefined sales values for each city
sales_value = {
    "New York": 12000,
    "Los Angeles": 8000,
    "Chicago": 4000,
    "Houston": 6000
}
# Input sale for each cities
for city in cities:
    sale = sales_value[city]
    # Calculate discount based on sales criteria
    if sale > 10000:
        discount = 0.10 * sale
    elif 5000 <= sale <= 10000:
        discount = 0.05 * sale
    else:
        discount = 0.02 * sale
    # Append the data as a dictionary to the list
    city_data.append({
        "City": city,
        "Sales": sale,
        "Discount": discount
})

# Display the results
print("\nCity-wise Sales and Discounts:")
for data in city_data:
    print(f"{data['City']}: Sales = {data['Sales']}, Discout = {data['Discount']}")

print("Hello")
