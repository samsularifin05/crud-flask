from flask import make_response


class BaseResponse:

    @staticmethod
    def serialize_error(code, message):
        return make_response({"code": code, "messages": message}, code)

    @staticmethod
    def serialize_object(code, message, data):
        return make_response({"code": code, "messages": message, "data": data}, code)

    @staticmethod
    def serialize_list(code, message, data):
        return make_response(
            {
                "code": code,
                "messages": message,
                "data": data,
            },
            code,
        )
