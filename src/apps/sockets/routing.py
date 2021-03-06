from channels.routing import route

from . import consumers


channel_routing = [
    # This makes regular HTTP requests come through our channels!!!! AH!!
    # route("http.request", "sockets.consumers.http_consumer"),

    route("websocket.connect", consumers.ws_add),
    route("websocket.receive", consumers.ws_message),
    route("websocket.receive", consumers.ws_message),
]
