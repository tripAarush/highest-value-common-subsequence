import os
import time
import matplotlib.pyplot as plt
from hvlcs_sol import read_input_file, solve_hvlcs

# keeping track of the runtimes
def benchmark_folder(test_folder: str):
    files = sorted([f for f in os.listdir(test_folder) if f.endswith(".txt")])
    results = []

    for filename in files:
        path = os.path.join(test_folder, filename)
        values, a, b = read_input_file(path)
        # get time
        start = time.perf_counter()
        max_value, subseq = solve_hvlcs(values, a, b)
        end = time.perf_counter()
        runtime_ms = (end - start) * 1000

        results.append({
            "file": filename,
            "max_value": max_value,
            "subsequence": subseq,
            "runtime_ms": runtime_ms
        })

    return results


def plot_results(results, output_image="runtime_graph.jpg"):
    x = [r["file"] for r in results]
    y = [r["runtime_ms"] for r in results]

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker="o")
    plt.xlabel("Input File")
    plt.ylabel("Runtime (ms)")
    plt.title("HVLCS Runtime on 10 Input Files")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_image)
    plt.show()


if __name__ == "__main__":
    test_folder = "test_files"
    results = benchmark_folder(test_folder)

    for r in results:
        print(f'File: {r["file"]}')
        print(r["max_value"])
        print(r["subsequence"])

    plot_results(results)