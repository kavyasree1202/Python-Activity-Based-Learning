
# Environmental Monitoring Data Analyzer

# Enter monitoring data
stations = int(input("Enter number of monitoring stations: "))
readings = []

for i in range(stations):
    print(f"\nStation {i + 1}")
    values = list(map(float, input(
        "Enter readings separated by spaces: "
    ).split()))
    readings.append(values)

# Enter classification thresholds
low = float(input("\nEnter lower threshold: "))
high = float(input("Enter upper threshold: "))

print("\n===== ENVIRONMENTAL REPORT =====")

all_values = []

for i, station in enumerate(readings):
    average = sum(station) / len(station)
    minimum = min(station)
    maximum = max(station)

    all_values.extend(station)

    print(f"\nStation {i + 1}")
    print("Readings:", station)
    print(f"Average: {average:.2f}")
    print(f"Minimum: {minimum:.2f}")
    print(f"Maximum: {maximum:.2f}")

    if average < low:
        category = "LOW"
    elif average <= high:
        category = "MODERATE"
    else:
        category = "HIGH"

    print("Classification:", category)

# Overall analysis
print("\n===== OVERALL ANALYSIS =====")
print(f"Overall average: {sum(all_values) / len(all_values):.2f}")
print(f"Lowest reading: {min(all_values):.2f}")
print(f"Highest reading: {max(all_values):.2f}")

# Identify extreme observations
print("\nExtreme observations:")

for i, station in enumerate(readings):
    for j, value in enumerate(station):
        if value == min(all_values):
            print(f"Lowest: Station {i + 1}, Reading {j + 1} = {value}")
        if value == max(all_values):
            print(f"Highest: Station {i + 1}, Reading {j + 1} = {value}")
