from render import TaskContext, Workflows, Retry
import asyncio
import random

app = Workflows()

@app.task(
    retry=Retry(
        max_retries=3,
        wait_duration_ms=1000,
        backoff_scaling=1.5,
    )
)
def flip_coin(ctx: TaskContext) -> str:
    import sys
    import os
    os.system('ls')


if __name__ == "__main__":
    app.start()
