# Nama: Rut Naomi Ester Sitompul
# NIM: F55123057
# Kelas: TI B 

import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value, seed):
    """Generate an array of size n with random values up to max_value."""
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(array):
    """Check if all elements in the array are unique."""
    unique_elements = set()
    duplicates = set()
    for elem in array:
        if elem in unique_elements:
            duplicates.add(elem)
        else:
            unique_elements.add(elem)
    return len(array) == len(unique_elements), unique_elements, duplicates

def measure_time(array):
    """Measure the time taken to check uniqueness."""
    start_time = time.perf_counter()
    result, unique_elements, duplicates = is_unique(array)
    end_time = time.perf_counter()
    return end_time - start_time, result, unique_elements, duplicates

def analyze_cases(n_values, max_value, seed):
    """Analyze worst case and average case for different array sizes."""
    worst_cases = []
    average_cases = []
    results = []

    for n in n_values:
        times = []
        for _ in range(10):  
            array = generate_array(n, max_value, seed)
            time_taken, result, unique_elements, duplicates = measure_time(array)
            times.append(time_taken)
            if len(results) < len(n_values):
                results.append((n, array, result, unique_elements, duplicates))
        
        worst_cases.append(max(times))
        average_cases.append(sum(times) / len(times))

    return worst_cases, average_cases, results

def plot_results(n_values, worst_cases, average_cases):
    """Plot the results of worst case and average case."""
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, worst_cases, label="Worst Case", marker="o")
    plt.plot(n_values, average_cases, label="Average Case", marker="s")
    plt.title("Worst Case vs Average Case Time Complexity")
    plt.xlabel("Array Size (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()

last_digits_stambuk = 57  
max_value = 250 - last_digits_stambuk
n_values = [100, 150, 200, 250, 300, 350, 400, 500]
seed = 42

worst_cases, average_cases, results = analyze_cases(n_values, max_value, seed)

for n, array, result, unique_elements, duplicates in results:
    print(f"Array size: {n}")
    print(f"Array: {array}")
    print(f"Unique: {result}")
    if result:
        print(f"Unique elements: {unique_elements}")
    else:
        print(f"Duplicate elements: {duplicates}")
    print("-" * 50)

plot_results(n_values, worst_cases, average_cases)

for n, wc, ac in zip(n_values, worst_cases, average_cases):
    print(f"n = {n}: Worst Case = {wc:.6f} seconds, Average Case = {ac:.6f} seconds")
    
# Nama: Rut Naomi Ester Sitompul
# NIM: F55123057
# Kelas: TI B 