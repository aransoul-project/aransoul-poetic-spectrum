# cli.py
import argparse
import json

def poetic_spectrum(text: str) -> dict:
    """
    詩理頻譜計算模組（簡版）
    以文字內容分析語義密度、感性幅度與思維延遲。
    """
    words = [w for w in text.replace("，", " ").replace("。", " ").split() if w]
    unique = len(set(words)) or 1
    total = len(words) or 1

    # 三個基本指標（簡易計算範例）
    semantic_density = round(min(1.0, unique / total), 2)
    affective_amplitude = round(0.3 + text.count("！") * 0.2 + text.count("。") * 0.05, 2)
    cognitive_lag_est = round(max(0.4, 3.0 - semantic_density * 2), 2)

    return {
        "semantic_density": semantic_density,
        "affective_amplitude": affective_amplitude,
        "cognitive_lag_est": cognitive_lag_est,
        "tokens": total,
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AranSoul Poetic Spectrum Analyzer")
    parser.add_argument("--text", required=True, help="輸入詩句或文本")
    args = parser.parse_args()

    result = poetic_spectrum(args.text)
    print(json.dumps(result, ensure_ascii=False))
