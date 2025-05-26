# 天気データ取得・可視化ツール（OpenWeatherMap API）

本ツールは、OpenWeatherMap API を活用して、指定都市の天気情報（気温・湿度・風速・天気概要など）を取得し、CSVファイルおよびグラフとして自動的に出力するPythonスクリプトです。

---

## ・ 機能概要

- OpenWeatherMap API による複数都市の天気情報の取得
- 天気データを一覧表形式でCSVに保存
- 都市別の気温を棒グラフで可視化（PNG画像出力）
- 出力ファイル名には実行日が自動付与され、記録として蓄積可能
- 出力対象（CSV／画像）は `output/` フォルダに整理
- 出力の例として、`sample/`フォルダを作成しています。

📊 [サンプルCSVはこちら](sample/weather_20250523.csv)  
🖼 [出力グラフはこちら](sample/weather_20250523.png)


---

## ・ 使用技術・ライブラリ

- Python 3.x
- pandas / matplotlib / requests / dotenv / pathlib
- OpenWeatherMap API（[https://openweathermap.org/api](https://openweathermap.org/api)）

---

## ・ ディレクトリ構成

```planetext
06_weather_API/
├── script/
│   └── weather_API.py           # 実行スクリプト
├── output/                      # 自動生成されるCSV／PNG
├── .env                         # APIキーを保存（非公開）
├── .gitignore                  # 不要ファイル除外設定
├── run_weather.bat             # スクリプト実行用バッチ（任意）
└── README.md                   # 本ファイル
```

---

## ・ 実行方法

### ▼ 方法①：Anaconda Promptやターミナルからの実行

```bash
python script/weather_API.py
```

※ .env にAPIキーが適切に設定されている必要があります。

### ▼ 方法②：バッチファイルからの簡易実行（Windows）
run_weather.bat をクリックすることで、Anaconda環境を経由してスクリプトを実行できます。
ご利用の環境によっては事前のパス設定などが必要になる場合があります。

---

## ・ 補足情報
都市リストはスクリプト内で自由に変更可能です。

API呼び出しは適切な待機時間（time.sleep(1)）を設けており、過剰なリクエストを避ける構成です。

スクリプトの構造はシンプルで保守性にも配慮しており、今後の拡張や再利用にも対応しやすくなっています。

---

## ・ APIキーの設定方法
プロジェクトルートに .env ファイルを作成し、以下のように記述してください：
```ini
OPENWEATHER_API_KEY=your_api_key_here
```

---

## ・ライセンス
MITライセンスのもとで公開しています。ご自由にご利用・改変いただけます。
