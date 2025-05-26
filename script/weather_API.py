from dotenv import load_dotenv
import os, requests, time
from datetime import datetime
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import japanize_matplotlib


# 親フォルダ取得、出力パスを作成する関数
def prepare_directories():
    # このスクリプトの親フォルダ(=プロジェクトのルート)を取得
    base_dir = Path(__file__).resolve().parent.parent

    # 出力フォルダへの絶対パス
    output_dir = base_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True) # 念のため作成

    return base_dir, output_dir

# .envからAPI Keyを取得する関数
def load_api_key(base_dir):
    # API Keyを.envファイルから取得
    env_path = base_dir / ".env"
    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("APIキーが読み込めませんでした。")
    return api_key

# 日付文字列を作成する関数
def get_date_strings():
    #実行日の日付の文字列を取得
    today = datetime.today()
    today_formatted = today.strftime("%Y/%m/%d")

    # 保存ファイル用のフォーマット
    today_for_filename = today.strftime("%Y%m%d")
    return today_formatted, today_for_filename


# 複数の都市を対象にデータを取得し、表形式でまとめる関数
def build_weather_data_frame(api_key, today_formatted):
    # 対象都市のリストを作成
    target_cities = ["Tokyo", "Osaka", "Nagoya", "Sapporo", "Kyoto", "Fukuoka", "Yokohama",
                    "Sendai", "Chiba", "Maebashi", "Shizuoka", "Naha"]

    # 空のリスト作成
    weather_data = []

    print("天気情報の取得を開始します...")

    for city in target_cities:

        print(f"{city}の天気情報を取得中...")
        # APIエンドポイントとパラメータ
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ja"

        # APIリクエストを送信
        response = requests.get(url)

        # JSON形式で結果を受け取る
        data = response.json()

        # 各項目を辞書にまとめて、リストに追加していく
        weather_data.append({
            "日付" : today_formatted,
            "都市名" : data["name"],
            "天気" : data["weather"][0]["description"],
            "気温(℃)" : data["main"]["temp"],
            "湿度(%)" : data["main"]["humidity"],
            "風速(m/s)" : data["wind"]["speed"],
            "体感温度(℃)" : data["main"]["feels_like"],
            "最低気温(℃)" : data["main"]["temp_min"],
            "最高気温(℃)" : data["main"]["temp_max"]
        })
        # アクセスごとの間隔を開ける
        time.sleep(1)

    print("天気情報の取得が完了しました。")

    # 辞書のリストからpandasのDataFrameを作成
    df = pd.DataFrame(weather_data)

    return df

# CSVファイルに保存する関数
def save_csv_file(df, output_dir, today_for_filename):
    # 保存ファイル名
    csv_path = output_dir / f"weather_{today_for_filename}.csv"

    # 日付付ファイル名でcsv出力
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")


# グラフを作成し画像を保存する関数
def save_weather_chart(df, output_dir, today_formatted, today_for_filename):
    fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")

    # 棒グラフの描画
    ax.bar(df["都市名"], df["気温(℃)"], color='skyblue')

    # グラフタイトル・ラベルなどの設定
    ax.set_title(f"{today_formatted}の都市別気温", fontsize=14)
    ax.set_xlabel("都市名")
    ax.set_ylabel("気温(℃)")
    ax.tick_params(axis='x', rotation=45)

    # y軸スケールを固定
    ax.set_ylim(0, 40)

    # レイアウト調整
    fig.tight_layout()

    # グラフ画像を保存

    # 保存ファイル名
    img_path = output_dir / f"weather_{today_for_filename}.png"

    plt.savefig(img_path, dpi=300, bbox_inches="tight")
    plt.close()

# --- スクリプトの本体 ---
def main():
    base_dir, output_dir = prepare_directories()
    api_key = load_api_key(base_dir)
    today_formatted, today_for_filename = get_date_strings()
    df = build_weather_data_frame(api_key, today_formatted)
    save_csv_file(df, output_dir, today_for_filename)
    save_weather_chart(df, output_dir, today_formatted, today_for_filename)

# --- 実行エントリーポイント ---
if __name__ == "__main__":
    main()
