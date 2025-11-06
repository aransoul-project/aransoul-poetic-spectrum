# app.py
import gradio as gr
from cli import poetic_spectrum

def analyze_text_ui(text):
    """
    介面函式：接收文字輸入並回傳詩理頻譜分析結果。
    """
    if not text.strip():
        return {"error": "請輸入文字"}

    try:
        result = poetic_spectrum(text)
        return result
    except Exception as e:
        return {"error": str(e)}

demo = gr.Interface(
    fn=analyze_text_ui,
    inputs=gr.Textbox(lines=3, label="輸入詩句或語段"),
    outputs="json",
    title="🜂 AranSoul Poetic Spectrum",
    description="嵐魂系統詩理頻譜模組 · 輸入詩句後可獲得語義密度、感性幅度與思維延遲估計。"
)

if __name__ == "__main__":
    demo.launch()
