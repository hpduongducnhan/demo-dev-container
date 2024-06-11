import subprocess
import json

def inspect_container(container_id):
    result = subprocess.run(['docker', 'inspect', container_id], stdout=subprocess.PIPE)
    container_info = json.loads(result.stdout)[0]
    memory_limit = container_info['HostConfig']['Memory']
    cpu_limit = container_info['HostConfig']['NanoCpus']
    return memory_limit, cpu_limit

container_id = 'strange_mirzakhani'  # Replace with your container ID
memory_limit, cpu_limit = inspect_container(container_id)
print(f'Memory Limit: {memory_limit} bytes')
print(f'CPU Limit: {cpu_limit / 1e9} CPUs')  # Convert from nanoseconds to CPUs
