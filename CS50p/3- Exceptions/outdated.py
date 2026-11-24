def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()

        try:
            if "/" in date:
                month, day, year = date.split("/")
                if any(char.isalpha() for char in month):
                    continue

            # Tenta o formato de texto: Month D, Y
            elif "," in date:
                month_day, year = date.split(", ")
                month_name, day = month_day.split(" ")

                if month_name in months:
                    month = months.index(month_name) + 1
                else:
                    continue
            else:

                continue

            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
