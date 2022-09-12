import asyncio
import monitors

async def main():
    task_mem = asyncio.create_task(monitors.get_mem_usage())
    task_cpu = asyncio.create_task(monitors.get_cpu_usage())
    task_temp = asyncio.create_task(monitors.get_temp())
    await task_mem
    await task_cpu
    await task_temp

if __name__ == "__main__":
    asyncio.run(main())