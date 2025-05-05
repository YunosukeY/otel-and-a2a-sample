from common.client import A2AClient
import asyncio
from uuid import uuid4

client = A2AClient(url="http://localhost:10002")
res = asyncio.run(client.send_task({
    "id": str(uuid4()),
    "message": {
        "role": "user",
        "parts": [
            {
                "type": "text",
                "text": "Hello world"
            }
        ]
    },
}))
print(res.result)
