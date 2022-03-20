import asyncio
import time


async def simple_client(message):
    """Client which send simple request to server"""
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()


async def execute(task, data):
    """Execute all commands in one connection"""
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888
    )
    print("Create connection")
    writer.write(f"create {task} {data}".encode())
    await writer.drain()

    task_id = (await reader.read(100)).decode()
    print("Task id is: " + task_id)

    while 1:
        writer.write(f"get_status {task_id}".encode())
        data = (await reader.read(100)).decode()
        print("Current status of task is: " + data)
        if data == "SUCCESS":
            break
        time.sleep(.5)
    writer.write(f"get_result {task_id}".encode())
    result = (await reader.read(100)).decode()
    print("The result is: " + result)
    writer.close()
    await writer.wait_closed()
