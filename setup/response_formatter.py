from rest_framework.renderers import JSONRenderer

from setup.async_task import add_cloudwatch_log


class ApiRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        HTTP_MESSAGES = {
            'INFO': 'INFO',
            'WARNING': 'WARNING',
            'ERROR': 'ERROR',
            'CRITICAL': 'CRITICAL',
            'SUCCESS': 'SUCCESS'
        }

        value_http_message = HTTP_MESSAGES.get(data['http_message'], 'ERROR')

        response = {
            "status": value_http_message,
            "code": status_code,
            "data": data
        }

        # Error formatting
        if not str(status_code).startswith('2'):
            response["code"] = status_code
            response["context"] = {}
            del response["data"]
            try:
                response["message"] = data['data']['respEstado']['msgeRespuesta']
                response["context"] = {
                    "response": data["data"]
                }
            except:
                response["context"] = {
                    **response["context"],
                    "error_context": data
                }

            response["context"] = {
                **response["context"],
                "token_provided": renderer_context['request'].headers.get('Token'),
            }

        add_cloudwatch_log.delay(response, value_http_message)
        return super(ApiRenderer, self).render(data, accepted_media_type, renderer_context)
