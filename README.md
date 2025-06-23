# 📘 Python 小說爬蟲與 PDF 自動轉檔工具

這是一個使用 Python 製作的小說爬蟲工具，能自動抓取小說網站的章節內容，儲存為 `.txt` 檔案，並可轉換成格式良好的 `.pdf`，方便離線閱讀。本專案參考公開資源與教學影片製作，並結合 ChatGPT 協助與個人邏輯整合完成，適合自學者練習 Python 爬蟲、文字處理與專案實作能力。

---

## 🔧 使用技術與工具

| 技術/套件              | 用途                   |
|------------------------|------------------------|
| Python 3.x             | 主程式語言              |
| requests               | HTTP 請求              |
| BeautifulSoup4         | HTML 分析與內容擷取     |
| re / os / time         | 系統操作與正規表達式處理 |
| fpdf                   | 將 TXT 轉換為 PDF       |
| Noto Sans TC 字型      | 支援繁體中文顯示         |
| ChatGPT                | 協助除錯與功能優化       |

---

## 📌 專案功能

- 🕸️ 爬取小說網站（如 linovelib.com）之章節內容
- 📄 儲存每章為 `.txt` 檔案，並支援章節排序與重新命名
- 🖼️ 抓取內文圖片並本地儲存
- 🧾 將 `.txt` 自動轉換成格式清晰的 `.pdf` 檔案
- ⏱️ 每爬取固定次數自動休息，降低被網站封鎖風險

---

## 📂 專案資料夾結構

```plaintext
project_root/
│
├── main.py                      # 主程式
├── font/                        # 字型資料夾（需手動放入 .ttf 字型）
│   └── NotoSansTC-Regular.ttf
├── content/
│   └── 小說名稱/
│       ├── txt/                # 每章節的文字檔
│       ├── img/                # 圖片下載
│       └── pdf/                # 輸出 PDF
└── README.md                    # 說明文件（本檔案）
```

---

## 🚀 如何使用

1. 安裝必要套件：

```bash
pip install requests beautifulsoup4 fpdf
```

2. 放入字型（建議使用 [Noto Sans TC](https://fonts.google.com/specimen/Noto+Sans+TC)）至 `font/` 資料夾。

3. 修改 `main.py` 中的小說起始網址與小說名稱。

4. 執行程式：

```bash
python main.py
```

5. 範例轉檔使用方式：

```python
txt_to_pdf('content/小說名稱/txt/001.txt', 'content/小說名稱/pdf/001.pdf')
```

---

## 🙋‍♂️ 個人貢獻與開發心得

- 結合開源影片與教學資源，實作出符合自己需求的完整工具。
- 善用 ChatGPT 幫助除錯與程式邏輯設計，並將功能模組化。
- 更加熟悉 HTML 結構、爬蟲 headers 設定、資料儲存與文字編碼處理。

---

## 📚 資料來源與參考

- 🎥 [YouTube 教學影片：20分鐘內教你如何爬取嗶哩輕小說](https://www.youtube.com/watch?v=IJXvcU63nvA&t=564s)
- 🤖 [ChatGPT](https://chat.openai.com/) — 協助理解與改寫部分程式邏輯
- 🤖 [Microsoft Copilot](https://copilot.microsoft.com) — 協助理解與改寫部分程式邏輯
- 🐍 [Python 官方網站](https://www.python.org/) — 程式語言與模組查詢
- 🎓 [STEAM 教育學習網](https://steam.oxxostudio.tw) — 基礎 Python 與爬蟲參考學習資源

---

## 📄 授權條款

本專案僅供學習與研究用途，請勿用於商業行為，並請遵守原網站（如小說來源）的使用規範。  
程式碼部分採用 MIT License 授權。
