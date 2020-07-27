import rpc
import time

print("Demo for python-discord-rpc")
client_id = '727996514936291362' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = time.time()
while True:
    activity = {
            "state": "Active on: iMac Pro",
            "details": "Designing Logo",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "zero",
                "small_image": "zero",
                "large_text": "one",
                "large_image": "one"
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(30)