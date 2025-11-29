full_name = input("ФИО: ").strip()
parts = full_name.split()
full_name_no_spaces = "".join(part.strip() for part in parts)
full_name_no_spaces_len = len(full_name_no_spaces)
initials = "".join(part[0].upper() for part in parts)
length = len(full_name)
print(f"Инициалы: {initials}.")
print(
    f"Длина (символов): {full_name_no_spaces_len + 2}"
)  # +2 for the spaces between initials
