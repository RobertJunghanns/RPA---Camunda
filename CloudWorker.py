import asyncio
from pyzeebe import ZeebeWorker, create_camunda_cloud_channel
from Task import router

async def main():
    channel = create_camunda_cloud_channel("J7.i-DNCUeO4bWKE8swQXsJQ62C9yUsS", "2rXd645bmYnWu4ks4rHIjPuZ5NJu7RTEBK922.dmOUovN~_KnH31wKfEaUKbX18x", "c0557209-b1e9-4502-9dcf-975c1d35ae46")
    worker = ZeebeWorker(channel)
    worker.include_router(router)
    await worker.work()

asyncio.run(main())