import json
from django.utils.deprecation import MiddlewareMixin
from django.contrib.messages import get_messages
from django.template.loader import render_to_string


class HtmxMessageMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if (
            "HX-Request" in request.headers
            and not 300 <= response.status_code < 400
            and "HX-Redirect" not in response.headers
        ):
            response.write(
                render_to_string(
                    "components/messages.html",
                    {"messages": get_messages(request)},
                )
            )
        return response
