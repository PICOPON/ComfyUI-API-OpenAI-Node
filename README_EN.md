# ComfyUI OpenAI Node

A custom ComfyUI node that integrates OpenAI-compatible APIs for prompt generation and enhancement, specifically designed for Stable Diffusion workflows.
![微信截图_20250805130100](https://github.com/user-attachments/assets/48f8de78-fde4-4c5f-ba73-b239c3b11432)

## Features

- 🤖 **OpenAI Compatible API Integration**: Works with any OpenAI-compatible API endpoint
- 🎨 **Stable Diffusion Prompt Enhancement**: Automatically expands and improves prompts for better image generation
- 🧠 **DeepSeek R1 Support**: Pre-configured for DeepSeek-R1-Distill-Qwen-32B-910A model
- 🧹 **Clean Output**: Automatically removes thinking tags (`<think>` blocks) from responses
- ⚙️ **Flexible Configuration**: Customizable model, temperature, tokens, and API settings

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/PICOPON/ComfyUI-API-OpenAI-Node.git
   ```

3. Install required dependencies:
   ```bash
   pip install requests
   ```

4. Restart ComfyUI

## Usage

1. Add the **OpenAI Node** to your ComfyUI workflow
2. Configure the node parameters according to your needs
3. Connect the output to your desired downstream nodes

### Node Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `prompt` | STRING | "user prompts" | The input prompt to be processed |
| `system_prompt` | STRING | *Stable Diffusion prompt generator* | System instructions for the AI |
| `model` | STRING | "DeepSeek-R1-Distill-Qwen-32B" | Model name to use |
| `api_url` | STRING | "http://127.0.0.1:1935/v1" | API endpoint URL |
| `api_key` | STRING | "123" | API authentication key |
| `temperature` | FLOAT | 0.6 | Creativity level (0.0-1.0) |
| `max_tokens` | INT | 1024 | Maximum response length |

### Default System Prompt

The node comes pre-configured with a system prompt optimized for Stable Diffusion:

```
You are a prompt generation AI. Your task is to take a user input for a stable diffusion prompt and output and expand the supplied prompt in a stable diffusion format to provide better output. Do not deviate from the format. Do not output anything other than a stable diffusion prompt.
```

## Examples

### Basic Usage
1. **Input**: "a cat"
2. **Output**: "a beautiful fluffy cat, detailed fur texture, bright eyes, sitting pose, soft lighting, high quality, photorealistic, 8k resolution"

### Advanced Workflow
```
Text Input → OpenAI Node → Text Processing → Image Generation
```
### 参考流程文件AI_generated_Flux_flow.json
![微信截图_20250805131154](https://github.com/user-attachments/assets/e5e4f036-388b-42d3-91af-e2496cd2e545)

## API Compatibility

This node works with:
- ✅ OpenAI API
- ✅ DeepSeek API
- ✅ Local LLM servers (Ollama, LM Studio, etc.)
- ✅ Any OpenAI-compatible endpoint

## Configuration Examples

### Local Server (Ollama, vllm, mindie .etc.)
- **API URL**: `http://localhost:1935/v1`
- **Model**: `DeepSeek-R1-Distill-Qwen-32B` or any installed model
- **API Key**: Leave as "123" or empty

### DeepSeek API
- **API URL**: `https://api.deepseek.com/v1`
- **Model**: `deepseek-chat`
- **API Key**: Your DeepSeek API key

### OpenAI API
- **API URL**: `https://api.openai.com/v1`
- **Model**: `gpt-4` or `gpt-3.5-turbo`
- **API Key**: Your OpenAI API key

## Features in Detail

### Automatic Tag Cleaning
The node automatically removes `<think>` and `</think>` tags and their content from the AI response, ensuring clean output for downstream processing.

### Error Handling
- Network timeout protection (100 seconds)
- HTTP error status handling
- Exception catching with descriptive error messages

### Flexible API Integration
- Automatic URL completion for OpenAI-compatible endpoints
- Optional API key authentication
- Configurable model parameters

## Troubleshooting

### Common Issues

**API Connection Error**
- Check if your API URL is correct and accessible
- Verify your API key if authentication is required
- Ensure your local server is running (for local APIs)

**Model Not Found**
- Verify the model name is correct for your API provider
- Check if the model is available in your account/server

**Timeout Issues**
- Increase timeout value in the code if needed
- Check your internet connection
- Verify API server status

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the GNU-3.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- ComfyUI team for the excellent framework
- OpenAI for the API standard
- DeepSeek for their powerful models

## Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/comfyui-openai-node/issues) page
2. Create a new issue with detailed information
3. Include your ComfyUI version and error logs

---

⭐ If this node helps your workflow, please consider giving it a star!
