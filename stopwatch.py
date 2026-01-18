import time

print("Stopwatch started. Press Ctrl+C to stop.")

start_time = time.time()

try:
    while True:
        elapsed_time = int(time.time() - start_time)
        mins, secs = divmod(elapsed_time, 60)
        print(f"\r ⏳ Elapsed time: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopwatch stopped. at {min:.02d}:{sec:02d} seconds.".format(min=mins, sec=secs))   