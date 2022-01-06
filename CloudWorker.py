import asyncio
from pyzeebe import ZeebeWorker, create_camunda_cloud_channel
from Task import router

async def main():
    channel = create_camunda_cloud_channel("4ye8lbCADxGYT2LIWh~ZM2xHOEAm1Gd2", "X9LOUH17KvUIMIyd-8Vfqs94M4ALjc2yA6IeaAbYIXXWDKExSYBOY634qO0vcjUs", "f8e9dd9a-7b25-40b0-b852-13223df7f2e9")
    worker = ZeebeWorker(channel)
    worker.include_router(router)
    await worker.work()

asyncio.run(main())