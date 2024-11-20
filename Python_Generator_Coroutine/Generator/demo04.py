import asyncio

async def work(x):
    print("当前接收的参数是: ", x)
    await asyncio.sleep(x)
    return f"当前任务的返回值是 {x}"


async def main():
    tasks = [asyncio.create_task(work(i)) for i in range(1, 11)]

    done, pending = await asyncio.wait(tasks)

    # print(done)
    # print(pending)

    res = await asyncio.gather(*tasks)
    print(res)  # 有序的返回结果

    for item in done:
        print(item.result())  # 无顺序的返回结果


asyncio.run(main())