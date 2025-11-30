rows = int(input("Please enter the amount of rows: "))
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(' ', end='')
    for k in range(1, i + 1):
        print('*', end='')
    print()
print("REMINDER: This was made by the help of Google Gemini")