searched_book = input()
count_book = int(input())

counter = 0
is_found = False

while counter < count_book:
    current_book = input()

    if searched_book == current_book:
        is_found = True
        break

    counter += 1
    if counter == current_book:
        break


if is_found:
    print(f"You checked {count_book} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {count_book} books.")

