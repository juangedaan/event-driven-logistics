import subprocess

def run(name, command):
    print(f"\n[Launching] {name}")
    subprocess.Popen(command, shell=True)

if __name__ == "__main__":
    run("Consumer", "python3 -m app.consumer")
    run("Producer", "python3 -m app.producer")
    run("Notifier", "python3 -m app.notifier")
    run("Dashboard", "python3 -m app.dashboard.app")

    print("\n✅ All services launched. Visit http://localhost:5000 to view the dashboard.")

