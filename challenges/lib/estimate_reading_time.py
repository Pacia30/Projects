def estimate_reading_time(text):
    words = text.split()
    length = len(words)
    estimate_read_time = (length/200)
    return (f"The estimate reading time for this text is {estimate_read_time} minutes.")

