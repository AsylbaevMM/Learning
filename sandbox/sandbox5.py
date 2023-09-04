import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 2

async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x+2

async def recharge_portal(x):
    print(f"Подзарядка портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x*3

async def check_portal_stability(x):
    print(f"Проверка стабильности портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 4

async def restore_portal(x):
    print(f"Восстановление портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x*5

async def close_portal(x):
    print(f"Закрытие портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x - 1

async def portal_operator():
    tasks = []
    for task, value in zip([activate_portal, 
                            perform_teleportation, 
                            recharge_portal, 
                            check_portal_stability, 
                            restore_portal, 
                            close_portal], [i for i in range(2, 10)]):
        tasks.append(asyncio.ensure_future(task(value)))
    result = await asyncio.gather(*tasks)
    
    print(f"""Результат активации портала: {result[0]} единиц энергии
Результат телепортации: {result[1]} единиц времени
Результат подзарядки портала: {result[2]} единиц энергии
Результат проверки стабильности: {result[3]} единиц времени
Результат восстановления портала: {result[4]} единиц энергии
Результат закрытия портала: {result[5]} единиц времени""")
    
asyncio.run(portal_operator())