import requests
import json
import re

class OpenAINode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "user prompts"
                }),
                "system_prompt": ("STRING", {
                    "multiline": True,
                    "default": "You are a prompt generation AI. your task is to take a user input for a stable difusion prompt and output and expand the supplied prompt in a stable difusion format to provide better output. Do not deviate from the format. Do not output anything other than a stable diffusion prompt.Output English whatever the input language is."
                }),
                "model": ("STRING", {
                    "multiline": True,
                    "default": "DeepSeek-R1-Distill-Qwen-32B"
                }),
                "api_url": ("STRING", {
                    "multiline": False,
                    "default": "http://127.0.0.1:1935/v1"
                }),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": "123"
                }),
                "temperature": ("FLOAT", {
                    "default": 0.6,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"
                }),
                "max_tokens": ("INT", {
                        "default": 1024,
                        "min": 1, 
                        "max": 2048,
                        "display": "number"
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_completion"
    CATEGORY = "OpenAIapi"
    
    def remove_think_tags(self, text):
        """
        移除文本中的 <think> 和 </think> 标签及其之间的内容
        """
        # 使用正则表达式匹配 <think> 到 </think> 之间的所有内容（包括标签本身）
        # re.DOTALL 使 . 匹配包括换行符在内的任何字符
        pattern = r'<think>.*?</think>'
        cleaned_text = re.sub(pattern, '', text, flags=re.DOTALL | re.IGNORECASE)
        
        # 清理多余的空行和空白字符
        cleaned_text = re.sub(r'\n\s*\n', '\n', cleaned_text.strip())
        
        return cleaned_text
    
    def get_completion(self, prompt, api_url, temperature, max_tokens, model, system_prompt, api_key):
        try:
            # 确保API URL格式正确
            if not api_url.endswith('/chat/completions'):
                if api_url.endswith('/v1'):
                    api_url += '/chat/completions'
                else:
                    api_url += '/v1/chat/completions'
            
            headers = {
                "Content-Type": "application/json"
            }
            
            # 如果提供了有效的API密钥，添加认证头
            if api_key and api_key != "123":
                headers["Authorization"] = f"Bearer {api_key}"
            
            payload = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": max_tokens,
                "temperature": temperature,
                "model": model,
                "top_p": 0.95,
                "top_k": 20,
                "repetition_penalty": 1.1
            }
            
            response = requests.post(api_url, headers=headers, data=json.dumps(payload), timeout=100000)
            
            if response.status_code == 200:
                data = response.json()
                # 兼容返回结构
                if "choices" in data and len(data["choices"]) > 0:
                    content = data["choices"][0]["message"]["content"]
                    # 移除 think 标签内容
                    cleaned_content = self.remove_think_tags(content)
                    return (cleaned_content,)
                else:
                    return ("No choices found in response.",)
            else:
                return (f"Error: HTTP {response.status_code} - {response.text}",)
                
        except Exception as e:
            return (f"Exception: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "OpenAINode": OpenAINode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenAINode": "OpenAI Node"
}
