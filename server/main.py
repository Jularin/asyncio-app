import asyncio

from tasks import char_multiple, string_permutation, reverse_string


tasks_types = {
    1: reverse_string,
    2: string_permutation,
    3: char_multiple
}

tasks = {}


async def new_task(task_type: str, data: str):
    task = tasks_types.get(int(task_type))
    t = task.delay(data)
    tasks[t.task_id] = t
    return t.task_id


async def get_status(task_id):
    t = tasks.get(task_id)
    return t.status


async def get_result(task_id):
    t = tasks.get(task_id)
    if t.result is None:
        return "Task is pending"
    else:
        return t.result


commands = {
    "create": new_task,
    "get_status": get_status,
    "get_result": get_result
}


async def handle_command(reader, writer):
    request = None
    while request != "quit\n" and request != "":
        request = (await reader.read(255)).decode('utf8')
        args = request.split()
        if not args:
            break
        if args[0] not in commands.keys():
            break
        command = commands[args[0]]
        response = await command(*args[1:])
        writer.write(response.encode('utf8'))
        await writer.drain()
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_command, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
