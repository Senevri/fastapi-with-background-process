from fastapi import FastAPI, BackgroundTasks
import asyncio

app = FastAPI()

# Global variable to represent the state of the continuous process

is_running = False
num_looped = 0


async def continuous_process():
    global num_looped
    while True:
        # Your continuous process logic goes here
        print("Continuous process is running...")
        num_looped += 1
        await asyncio.sleep(1)


@app.post("/start-process")
async def start_process(background_tasks: BackgroundTasks):
    global is_running
    if not is_running:
        is_running = True
        background_tasks.add_task(continuous_process)
        return {"message": "Continuous process started successfully."}
    else:
        return {"message": "Continuous process is already running."}


@app.post("/stop-process")
async def stop_process():
    global is_running
    if is_running:
        is_running = False
        return {"message": "Continuous process stopped successfully."}
    else:
        return {"message": "Continuous process is not running."}


@app.get("/get-state")
async def get_state():
    global is_running, num_looped
    return {"is_running": is_running, "num_looped": num_looped}