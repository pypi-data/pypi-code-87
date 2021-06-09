from pmfp.utils.endpoint import EndPoint
from ..core import grpc


class Query(EndPoint):
    """请求指定grpc的服务.

    需要本地有`grpcurl`,可以在`https://github.com/fullstorydev/grpcurl/releases`下载安装
    """
    argparse_noflag = "url"
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": ["url", "method", "payload", "service"],
        "properties": {
            "url": {
                "type": "string",
                "description": "grpc的服务位置.",
            },
            "service": {
                "type": "string",
                "title": "s",
                "description": "指定grpc提供的service使用.",
            },
            "method": {
                "type": "string",
                "title": "m",
                "description": "请求grpc的方法.",
            },
            "payload": {
                "type": "string",
                "title": "d",
                "description": "请求grpc的负载.需要是一个json文件的地址",
                "default": "query.json"
            },
            "cwd": {
                "type": "string",
                "description": "执行操作时的操作目录.",
                "default": "."
            },
            "plaintext": {
                "type": "boolean",
                "title": "p",
                "description": "是否不使用TLS加密传输.",
                "default": False
            },
            "insecure": {
                "type": "boolean",
                "title": "i",
                "description": "跳过服务器证书和域验证.",
                "default": False
            },
            "cacert": {
                "type": "string",
                "title": "a",
                "description": "根证书位置."
            },
            "cert": {
                "type": "string",
                "title": "e",
                "description": "服务证书位置."
            },
            "key": {
                "type": "string",
                "title": "k",
                "description": "服务证书对应的私钥位置."
            },
        }
    }


grpc_query = grpc.regist_sub(Query)
