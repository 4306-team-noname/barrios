from emmett import Pipe, current, request, response
import json


class HTMXMessagePipe(Pipe):
    async def open(self):
        pass

    async def close(self):
        # print(current.response.alerts())
        if "HX-Request" in request.headers:
            response.headers.__setitem__(
                "HX-Trigger",
                json.dumps(
                    {
                        "alerts": [
                            {"alert": alert[1], "category": alert[0]}
                            for alert in current.response.alerts(with_categories=True)
                        ]
                    }
                ),
            )
            # print(response.headers)
        return response

    async def pipe(self, next_pipe, **kwargs):
        return await next_pipe(**kwargs)

    async def on_pipe_success(self):
        pass

    async def on_pipe_failure(self):
        pass
