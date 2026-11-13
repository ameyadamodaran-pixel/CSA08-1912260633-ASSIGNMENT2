# Q4 - Building Long Text: + or join?
import time
import statistics

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    return ";".join(parts) + ";"

def build_fstring(parts):
    lines = []
    for p in parts:
        lines.append(f"{p};")
    return "".join(lines)

def measure(function, parts, repeats=3):
    samples = []
    result = None
    for _ in range(repeats):
        start = time.perf_counter()
        result = function(parts)
        samples.append(time.perf_counter() - start)
    return result, samples, statistics.mean(samples)

if __name__ == "__main__":
    plus_text, plus_times, plus_avg = measure(build_plus, items)
    join_text, join_times, join_avg = measure(build_join, items)
    f_text, f_times, f_avg = measure(build_fstring, items)
    print("Same output:", plus_text == join_text == f_text)
    print("Output length:", len(join_text))
    print("Repeated += times:", [round(x, 6) for x in plus_times])
    print("join times:", [round(x, 6) for x in join_times])
    print("f-string/list times:", [round(x, 6) for x in f_times])
    print("Average +=:", round(plus_avg, 6), "seconds")
    print("Average join:", round(join_avg, 6), "seconds")
    print("Average f-string/list:", round(f_avg, 6), "seconds")
