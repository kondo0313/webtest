import cv2
import requests
import time

# Webカメラからのキャプチャ
cap = cv2.VideoCapture(0)  # 0はデフォルトのカメラ

# Render上のFlaskサーバーのエンドポイント
server_url = "https://webtest-1.onrender.com/message"  # <your-service-name> を実際の Render サービス名に置き換えてください

while True:
    # フレームをキャプチャ
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture image")
        break
    
    # サーバーにメッセージを送信
    try:
        data = {'message': 'Frame captured'}
        
        # 送信前の時間を記録
        start_time = time.time()
        
        # サーバーにメッセージを送信
        response = requests.post(server_url, json=data, timeout=5)
        
        # 送信後の時間を記録
        end_time = time.time()
        
        # レスポンスタイムを計算
        response_time = end_time - start_time
        
        # サーバーからのレスポンスとレスポンスタイムを表示
        print(f"Response: {response.text}")
        print(f"Response time: {response_time:.4f} seconds")

    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to the server: {e}")
        continue  # エラーが発生してもループを継続

    # 画像をウィンドウに表示
    cv2.imshow('Captured Frame', frame)

    # 'q'キーが押されたらループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

# カメラをリリースしてウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()
