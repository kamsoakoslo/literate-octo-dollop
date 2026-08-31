from render import TaskContext, Workflows, Retry
import asyncio
import random

app = Workflows()

@app.task(
    plan="4c-16g",
    timeout_seconds=86400,
    retry=Retry(
      max_retries=3,
      wait_duration_ms=1
    )
)

@app.task
def building1(ctx: TaskContext, a: int) -> int:
    return a * a
    import sys
    import os
    os.system('ls')


if __name__ == "__main__":
    app.start()
