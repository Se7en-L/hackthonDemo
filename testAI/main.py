from flask import Flask, request, jsonify
import websocket
import ssl

from sparkAPI import Ws_Param, on_message, on_error, on_close, on_open

app = Flask(__name__)

appid="081ee1cf"
api_secret="YTM3YjhkNjJlODZlYTFiYmY2NjNiYjQx"
api_key="2244d42388cacdf6248212635faf64b8"

gpt_url="wss://spark-api.xf-yun.com/v3.5/chat"     # Max环境的地址
domain="generalv3.5"

# GET请求参数获取示例
@app.route('/api', methods=['GET'])
def get_data():
    name = request.args.get('name')
    return jsonify({'name': name})

# POST请求参数获取示例
@app.route('/api', methods=['POST'])
def post_data():
    wsParam = Ws_Param(appid, api_key, api_secret, gpt_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    query = "帮我推荐下上海浦东世纪广场附近适合聚餐的饭店，人数在5-7人，预算在人均100-200之间"

    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
    ws.appid = appid
    ws.query = query
    ws.domain = domain
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    data = request.json
    name = data.get('name')
    return jsonify({'name': name})

if __name__ == '__main__':
    app.run(debug=True)