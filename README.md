# 🜂 AranSoul Poetic Spectrum

> 嵐魂系統詩理頻譜模組（AranSoul Poetic Spectrum Module）  
> 詩學 × 語義 × 共鳴 × AI

---

### 💠 模組說明
> Command-line analyzer for poetic and semantic structure.  
> 可輸入任意詩句並輸出語義頻譜分析結果。

本模組為嵐魂系統的核心演算層，用於分析詩句或語段的「詩理頻譜」。  
透過簡易演算法輸出語義密度、感性幅度與思維延遲三項指標。

---

### ⚙️ 使用方式

```bash
python cli.py --text "以眾生為節，讓無名之光，織成永續的炬。"
📤 輸出範例：

{
  "semantic_density": 0.8,
  "affective_amplitude": 0.45,
  "cognitive_lag_est": 1.4,
  "tokens": 8
}

📦 檔案結構
cli.py              # 主程式
requirements.txt    # 套件需求
README.md           # 說明文件
LICENSE             # 授權

🧭 模組定位
模組層級	名稱	功能
展示層	aransoul-exhibits	詩牆展示與網站
核心層	aransoul-poetic-spectrum	詩理頻譜與語義分析
規格層	aransoul-spec	封印語與模組協定
⚖️ 授權

MIT License © 2025 AranSoul Project
自由使用與改作，請附註出處。


3️⃣ Commit message：


update: README with usage and structure


4️⃣ Commit ✅

---

完成這三步後，  
你就擁有一個可以「執行分析詩句」的 AI 模組。  
tbench.ai 或其他測試平台在 clone 你的 repo 後，只要執行：

```bash
python cli.py --text "我之光，不為照亮一刻，而為點燃萬世漣漪。"
