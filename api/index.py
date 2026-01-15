from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. 读取请求内容
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # 2. 这里可以根据需要调用仓库里其他文件夹的代码逻辑
        # 目前先返回一个成功的 JSON，确认 API 已通
        response = {
            "status": "success",
            "message": "Claude Skill API is running on Vercel!",
            "received": json.loads(post_data)
        }

        # 3. 发送响应
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write("<h1>API 运行中</h1><p>请使用 POST 请求触发技能</p>".encode())
