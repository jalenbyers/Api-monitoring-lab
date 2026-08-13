import urllib.request
import urllib.error
import json
import time
import logging


logging.basicConfig(
    filename="logs/api_monitor.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def check_endpoint(endpoint):

    url = "https://jsonplaceholder.typicode.com" + endpoint

    start_time = time.time()

    try:
        response = urllib.request.urlopen(url)

        response_time = time.time() - start_time

        data = json.loads(response.read())

        logging.info(
            f"{endpoint} | {response.status} | "
            f"{response_time:.2f}s | HEALTHY"
        )

        return {
            "endpoint": endpoint,
            "status": response.status,
            "response_time": response_time,
            "healthy": True,
            "post_id": data["id"]
        }

    except urllib.error.HTTPError as error:

        response_time = time.time() - start_time

        logging.error(
            f"{endpoint} | {error.code} | "
            f"{response_time:.2f}s | FAILED"
        )

        return {
            "endpoint": endpoint,
            "status": error.code,
            "response_time": response_time,
            "healthy": False,
            "error": error.reason
        }


endpoints = [
    "/posts/1",
    "/posts/2",
    "/posts/3",
    "/posts/9999"
]


print("API HEALTH REPORT")
print("=================")

healthy_count = 0
failed_count = 0


for endpoint in endpoints:

    result = check_endpoint(endpoint)

    print()
    print(f"Endpoint: {result['endpoint']}")
    print(f"Status: {result['status']}")
    print(f"Response: {result['response_time']:.2f}s")

    if result["healthy"]:
        print("STATUS: ✅ Healthy")
        healthy_count += 1

    else:
        print("STATUS: ❌ Failed")
        print(f"Error: {result['error']}")
        failed_count += 1


print()
print("-----------------")
print(f"Healthy: {healthy_count}")
print(f"Failed: {failed_count}")