from fastapi import FastAPI
import subprocess
import threading

app = FastAPI()

is_running = False  # ป้องกันรันซ้ำ

def run_script():
    global is_running
    is_running = True
    try:
        subprocess.run(["python3", "/home/rwb/code/controller.py"])
    finally:
        is_running = False

@app.get("/run")
def run_controller():
    global is_running
    if is_running:
        return {"status": "running", "message": "🚧 กำลังทำงานอยู่แล้ว"}
    else:
        thread = threading.Thread(target=run_script)
        thread.start()
        return {"status": "started", "message": "▶️ เริ่มรัน controller.py แล้ว"}
