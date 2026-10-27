import yaml
from inspect import cleandoc

class MiniMaxMusicYamlParser:
    """
    MiniMax Music3 YAML解析节点
    输入AI生成的yaml多行字符串，解析输出 caption / lyric / maxduration，直接对接MiniMax‑Music3节点
    yaml字段：caption | lyrics | maxduration
    注意：yaml内多行务必使用 | 符号保留换行；
    容错：解析异常、字段缺失会打印警告并使用兜底默认值：caption=""，lyrics=""，maxduration=120
    maxduration输出会钳位在10‑300（MiniMax Music3模型硬上限5分钟）
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "yaml_text": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "tooltip":"粘贴AI输出完整YAML文本，包含caption, lyrics, maxduration"
                }),
            }
        }
    RETURN_TYPES = ("STRING", "STRING", "INT")
    RETURN_NAMES = ("caption", "lyric", "maxduration")
    FUNCTION = "run"
    CATEGORY = "MiniMaxMusic"
    DESCRIPTION = cleandoc(__doc__)

    def run(self, yaml_text: str):
        # 兜底默认值
        caption_out = ""
        lyric_out = ""
        maxdur_out = 120

        try:
            data = yaml.safe_load(yaml_text)
            if isinstance(data, dict):
                caption_out = data.get("caption", "").strip()
                lyric_out = data.get("lyrics", "").strip()
                raw_dur = data.get("maxduration", 120)
                if isinstance(raw_dur, int):
                    maxdur_out = raw_dur
        except Exception as e:
            print(f"[WARN MiniMaxMusicYamlParser] YAML parse failed, fallback to defaults. err: {str(e)}")

        # 钳位：MiniMax Music3合法区间 [10, 300]
        maxdur_out = max(10, min(300, maxdur_out))
        print(f"[MiniMaxMusicYamlParser] parsed maxduration = {maxdur_out}")
        return (caption_out, lyric_out, maxdur_out)


NODE_CLASS_MAPPINGS = {
    "MiniMaxMusicYamlParser": MiniMaxMusicYamlParser
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MiniMaxMusicYamlParser": "MiniMax‑Music3 YAML Parser"
}
