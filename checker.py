import json
import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python checker.py endpoints.json")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as file:
    endpoints = json.load(file)

online = 0
failed = 0

print("API Status Checker")
print("------------------")
print()

for endpoint in endpoints:
    name = endpoint["name"]
    url = endpoint["url"]

    try:
        response = requests.get(url, timeout=5)

        status_code = response.status_code
        response_time = response.elapsed.total_seconds() * 1000

        if 200 <= status_code <= 399:
            status = "OK"
            online += 1
        else:
            status = "FAILED"
            failed += 1
        print(f"{name:<20} {status_code:<4} {status:<8} {response_time:.0f} ms")

    except requests.exceptions.Timeout:
        failed += 1
        print(f"{name:<20} {'---':<4} {'TIMEOUT':<8}")

    except requests.exceptions.ConnectionError:
        failed += 1
        print(f"{name:<20} {'---':<4} {'CONNECTION ERROR'}")


print()
print(f"Checked: {len(endpoints)}")
print(f"Online: {online}")
print(f"Failed: {failed}")
