from datetime import datetime

# Testing purpose
def test_datetime_parsing():
    date_str = "2024-06-15 14:30:00"
    expected_datetime = datetime(2024, 6, 15, 14, 30, 0)
    parsed_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    assert parsed_datetime == expected_datetime, f"Expected {expected_datetime}, got {parsed_datetime}" 
    print("Datetime parsing test passed.")  

if __name__ == "__main__":
    test_datetime_parsing() 

