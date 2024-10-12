# Python script to create HTML files named Lesson 1 to Lesson 10

for i in range(10, 70):
    filename = f"Lesson {i}.html"
    # HTML content template
    html_content = f""""""
    # Writing to the file
    with open(filename, "w") as file:
        file.write(html_content)

print("HTML files Lesson 1 to Lesson 10 have been created.")
