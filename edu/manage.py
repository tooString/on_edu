# -*- coding: utf-8 -*-

from edu.app import create_app

# 使用开发环境配置
app = create_app('development')

if __name__ == '__main__':
    # 使用 gevent 提供的 WSGI 服务器，并启用 WebSocket 支持
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    # 创建一个 WSGIServer ，包含 app 和 gevent 的 WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
