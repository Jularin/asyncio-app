# Simple client-server application

## How to run

### 1. Run redis with docker 
```shell
docker-compose up -d --build
```

### 2. Install virtualenv with poetry
```shell
poetry install 
poetry shell
```

### 3. Run server and celery
```shell
pyton server/main.py
cd server && celery -A tasks worker -l info -c 1
```

### 4. Run commands with
```shell
python client/main.py [command type] [id]
```

## Examples
```shell
python client/main.py create --data data --task 2
Send: 'create 2 data'
Received: '007af100-da57-46d0-b724-ebca46a578a0'
Close the connection
```

```shell
python client/main.py get_result -id d925f2c2-40fb-4af0-9f0f-6b73826e803d
Send: 'get_result d925f2c2-40fb-4af0-9f0f-6b73826e803d'
Received: 'adat'
Close the connection
```

```shell
python client/main.py get_status -id d925f2c2-40fb-4af0-9f0f-6b73826e803d
Send: 'get_status d925f2c2-40fb-4af0-9f0f-6b73826e803d'
Received: 'SUCCESS'
Close the connection
```

```shell
python client/main.py execute --data data --task 1
Create connection
Task id is: eec59537-0fb5-432d-a2c8-ddd062959135
Current status of task is: PENDING
Current status of task is: PENDING
Current status of task is: PENDING
Current status of task is: PENDING
Current status of task is: SUCCESS
The result is: atad
```