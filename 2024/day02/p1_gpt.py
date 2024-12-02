def is_safe(report):
    """Check if a report is safe based on the given rules."""
    # Check if all adjacent differences are between 1 and 3
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False

    # Check if the report is strictly increasing or strictly decreasing
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    return is_increasing or is_decreasing

def count_safe_reports(file_path):
    """Count the number of safe reports from a file."""
    safe_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report):
                safe_count += 1
    
    return safe_count

if __name__ == "__main__":
    # Input file containing reports
    input_file = "input.txt"
    
    # Count safe reports
    safe_reports_count = count_safe_reports(input_file)
    
    # Output the result
    print("Number of safe reports:", safe_reports_count)
