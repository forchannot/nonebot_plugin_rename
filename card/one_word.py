import httpx


async def get_one_speak() -> str:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        res = await client.get("https://tenapi.cn/v2/yiyan?format=json")
        data = res.json()["data"]["hitokoto"]
        return data[:16]
