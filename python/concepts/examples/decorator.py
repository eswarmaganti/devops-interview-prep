import time


def timer(func):
  def wrapper(*args, **kwargs):
    print(f"Started {func.__name__} Execution")
    start_time = time.perf_counter()
    # execute the passed function
    value = func(*args,**kwargs)

    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Finished {func.__name__} in {run_time} secs")
    return value
  return wrapper

@timer
def perform_operation():
  print("Operation Started")
  time.sleep(10)
  print("Operation Completed")


if __name__ == "__main__":
  perform_operation()