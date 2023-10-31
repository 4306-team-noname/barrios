from emmett.extensions import Extension


class TestController(Extension):
    whatever: str
    namespace = "Test"
    default_config = {}

    def on_load(self):
        print("TestController loaded")
        self.app.route("/test")(test_route)


async def test_route():
    return {"message": "This actually works"}
