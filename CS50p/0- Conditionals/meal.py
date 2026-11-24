def main():
    # get time from the user
    time_str = input("What time is it? (#:##) ")
    time_float = convert(time_str)

    # check meals time:
    if 7.0 <= time_float <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_float <= 13.0:
        print("lunch time")
    elif 18.0 <= time_float <= 19.0:
        print("dinner time")


def convert(time):
    # separate hours and minutes
    h, m = time.split(":")
    # convert to float
    return int(h) + int(m) / 60


if __name__ == "__main__":
    main()


