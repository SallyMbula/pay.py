#getting the gross pay
def get_input(prompt, error_message):
  while True:
    try:
      value = float(input(prompt))
      if value >= 0:
        return value
      else:
        print(error_message)
    except ValueError:
      print(error_message)


def calculate_gross_pay(hours, rate):
  return hours * rate


def main():
  hours_worked = get_input("Enter hours worked: ",
                           "Invalid input. Please enter a number.")
  rate_per_hour = get_input("Enter rate per hour: ",
                            "Invalid input. Please enter a number.")

  gross_pay = calculate_gross_pay(hours_worked, rate_per_hour)
  print(f"Gross pay: ${gross_pay:.2f}")


if __name__ == "__main__":
  main()
