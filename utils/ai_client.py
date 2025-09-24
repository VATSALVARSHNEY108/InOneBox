import os
import json
import streamlit as st
from typing import Optional, Dict, Any, List
import requests
import base64
import tempfile

# Gemini integration for multimodal AI - using google-genai SDK
try:
    import google as genai
    from google.genai import types
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


# OpenAI integration for image generation - using openai SDK
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIClient:
    """Unified AI client using direct API calls"""

    def __init__(self):
        pass

    def _init_clients(self):
        """No initialization needed for direct API calls"""
        pass

    def _has_gemini(self) -> bool:
        """Check if Gemini API key is available"""
        # Check environment variables first
        key = os.environ.get('GEMINI_API_KEY')
        if key and key.strip():
            return True

        # Check Streamlit secrets
        try:
            if hasattr(st, 'secrets') and 'GEMINI_API_KEY' in st.secrets:
                key = st.secrets['GEMINI_API_KEY']
                if key and key.strip():
                    return True
        except Exception:
            pass

        return False

    def _get_gemini_key(self) -> Optional[str]:
        """Get Google Gemini API key from environment variables or Streamlit secrets"""
        # Check environment variables first
        key = os.environ.get('GEMINI_API_KEY')
        if key and key.strip():
            return key.strip()

        # Check Streamlit secrets
        try:
            if hasattr(st, 'secrets') and 'GEMINI_API_KEY' in st.secrets:
                key = st.secrets['GEMINI_API_KEY']
                if key and key.strip():
                    return key.strip()
        except Exception:
            pass

        return None

    def _has_openai(self) -> bool:
        """Check if OpenAI API key is available"""
        key = os.environ.get('OPENAI_API_KEY')
        if key:
            return True

        # Check Streamlit secrets
        try:
            key = st.secrets.get("OPENAI_API_KEY")
            if key:
                return True
        except:
            pass

        return False

    def _get_openai_key(self) -> Optional[str]:
        """Get OpenAI API key from environment variables or Streamlit secrets"""
        # Check environment variables
        key = os.environ.get('OPENAI_API_KEY')
        if key:
            return key

        # Check Streamlit secrets
        try:
            key = st.secrets.get("OPENAI_API_KEY")
            if key:
                return key
        except:
            pass

        return None

    def _generate_text_direct(self, prompt: str, model: str = "gemini-2.5-flash") -> str:
        """Generate text using Gemini API directly"""
        api_key = self._get_gemini_key()
        if not api_key:
            return "Gemini API not available."

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

        headers = {
            'Content-Type': 'application/json',
        }

        data = {
            'contents': [{
                'parts': [{
                    'text': prompt
                }]
            }]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()

            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                return result['candidates'][0]['content']['parts'][0]['text']
            else:
                return "No response generated"

        except Exception as e:
            return f"Error generating text: {str(e)}"

    def generate_text(self, prompt: str, model: str = "gemini", max_tokens: int = 1000) -> str:
        """Generate text using direct Gemini API"""
        try:
            # Adjust prompt based on requested "model" style
            if model == "openai":
                enhanced_prompt = f"Act like GPT/OpenAI model. {prompt}"
            elif model == "anthropic":
                enhanced_prompt = f"Act like Claude/Anthropic model. {prompt}"
            else:
                enhanced_prompt = prompt

            # Use direct Gemini API call
            return self._generate_text_direct(enhanced_prompt)

        except Exception as e:
            return f"Error generating text: {str(e)}"

    def analyze_image(self, image_data: bytes, prompt: str = "Analyze this image", model: str = "gemini") -> str:
        """Analyze image using direct Gemini API"""
        try:
            return "Image analysis feature requires library integration. Please use text generation tools."
        except Exception as e:
            return f"Error analyzing image: {str(e)}"

    def generate_image(self, prompt: str, provider: str = "gemini", model: str = "gemini", size: str = "1024x1024") -> Optional[bytes]:
        """Generate image using Gemini - simple and efficient"""

        # Debug: Check what's available
        api_key = self._get_gemini_key()
        has_key = self._has_gemini()

        if not GEMINI_AVAILABLE:
            st.error("⚠️ Google genai library is not available. Please check installation.")
            return None

        if not has_key:
            st.error("⚠️ Gemini API key not found. Please check your GEMINI_API_KEY environment variable or secrets.")
            return None

        if not api_key:
            st.error("⚠️ Could not retrieve Gemini API key.")
            return None

        # Use Gemini for image generation
        try:
            return self._generate_image_gemini(prompt, size)
        except Exception as e:
            st.error(f"Image generation failed: {str(e)}")
            return None

    def _generate_image_gemini(self, prompt: str, size: str = "1024x1024") -> Optional[bytes]:
        """Generate image using Gemini"""
        try:
            # Re-import to ensure availability
            from google import genai
            from google.genai import types

            # Get Gemini API key from environment
            gemini_api_key = self._get_gemini_key()
            if not gemini_api_key:
                raise Exception("Gemini API key not found in environment")

            # Initialize Gemini client
            client = genai.Client(api_key=gemini_api_key)

            # Generate image using Gemini
            # Note: Gemini doesn't support custom sizes like OpenAI, it generates standard sizes
            response = client.models.generate_content(
                # IMPORTANT: only this gemini model supports image generation
                model="gemini-2.0-flash-preview-image-generation",
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )

            if not response.candidates:
                raise Exception("No response candidates from Gemini")

            content = response.candidates[0].content
            if not content or not content.parts:
                raise Exception("No content parts in Gemini response")

            # Extract image data from response
            for part in content.parts:
                if part.inline_data and part.inline_data.data:
                    # Handle both bytes and base64 encoded data
                    data = part.inline_data.data
                    if isinstance(data, str):
                        # If data is base64 string, decode it
                        import base64
                        return base64.b64decode(data)
                    else:
                        # If data is already bytes, return as-is
                        return data

            raise Exception("No image data found in Gemini response")

        except Exception as e:
            raise Exception(f"Gemini image generation failed: {str(e)}")

    def analyze_sentiment(self, text: str, model: str = "gemini") -> Dict[str, Any]:
        """Analyze sentiment using direct Gemini API"""
        try:
            # Adjust prompt based on requested "model" style
            base_prompt = f"""
            Analyze the sentiment of the following text and provide:
            1. Overall sentiment (positive/negative/neutral)
            2. Confidence score (0-1)
            3. Key emotional indicators
            4. Brief explanation

            Text: {text}

            Respond in JSON format.
            """

            if model == "openai":
                prompt = f"Act like GPT/OpenAI sentiment analysis model. {base_prompt}"
            elif model == "anthropic":
                prompt = f"Act like Claude sentiment analysis model. {base_prompt}"
            else:
                prompt = base_prompt

            # Use direct API call
            response_text = self._generate_text_direct(prompt)

            try:
                return json.loads(response_text)
            except json.JSONDecodeError:
                return {"error": "Invalid JSON response from API"}

        except Exception as e:
            return {"error": f"Sentiment analysis failed: {str(e)}"}

    def translate_text(self, text: str, target_language: str, model: str = "gemini") -> str:
        """Translate text to target language"""
        try:
            prompt = f"Translate the following text to {target_language}: {text}"
            return self.generate_text(prompt, model=model)
        except Exception as e:
            return f"Translation failed: {str(e)}"

    def summarize_text(self, text: str, max_sentences: int = 3, model: str = "gemini") -> str:
        """Summarize text to specified number of sentences"""
        try:
            prompt = f"Summarize the following text in {max_sentences} sentences: {text}"
            return self.generate_text(prompt, model=model)
        except Exception as e:
            return f"Summarization failed: {str(e)}"

    def detect_language(self, text: str, detection_mode: str = "Quick Detection", include_confidence: bool = True) -> Dict[str, Any]:
        """Detect language of text using AI"""
        try:
            # Create language detection prompt based on mode
            if detection_mode == "Quick Detection":
                prompt = f"""Detect the language of the following text. Respond with JSON format:
                {{"detected_language": "language name", "language_code": "ISO code", "confidence": 0.95}}

                Text: {text[:1000]}"""  # Limit text length for API efficiency

            elif detection_mode == "Detailed Analysis":
                prompt = f"""Analyze the language of the following text in detail. Respond with JSON format:
                {{
                    "detected_language": "language name",
                    "language_code": "ISO code", 
                    "confidence": 0.95,
                    "language_info": {{
                        "native_name": "native language name",
                        "family": "language family",
                        "script": "writing system",
                        "speakers": "number of speakers"
                    }}
                }}

                Text: {text[:1000]}"""

            elif detection_mode == "Multi-Language Detection":
                prompt = f"""Detect all languages present in the following text. Respond with JSON format:
                {{
                    "detected_language": "primary language",
                    "language_code": "primary ISO code",
                    "confidence": 0.95,
                    "alternative_languages": [
                        {{"language": "secondary language", "confidence": 0.15}},
                        {{"language": "tertiary language", "confidence": 0.05}}
                    ]
                }}

                Text: {text[:1000]}"""

            else:  # Confidence Analysis
                prompt = f"""Detect the language with detailed confidence analysis. Respond with JSON format:
                {{
                    "detected_language": "language name",
                    "language_code": "ISO code",
                    "confidence": 0.95,
                    "confidence_details": "explanation of confidence level"
                }}

                Text: {text[:1000]}"""

            # Get AI response
            response_text = self._generate_text_direct(prompt)

            try:
                # Parse JSON response
                result = json.loads(response_text)

                # Ensure required fields exist
                if 'detected_language' not in result:
                    # Fallback to simple detection
                    return self._fallback_language_detection(text)

                return result

            except json.JSONDecodeError:
                # If JSON parsing fails, try to extract language from text response
                return self._parse_text_language_response(response_text, text)

        except Exception as e:
            return {"error": f"Language detection failed: {str(e)}"}

    def _fallback_language_detection(self, text: str) -> Dict[str, Any]:
        """Simple fallback language detection"""
        # Basic language detection based on character patterns
        text_lower = text.lower()

        # Common language indicators
        if any(word in text_lower for word in ['the', 'and', 'that', 'have', 'for', 'not', 'you', 'are']):
            return {
                "detected_language": "English",
                "language_code": "en",
                "confidence": 0.8,
                "method": "fallback"
            }
        elif any(word in text_lower for word in ['el', 'la', 'de', 'que', 'es', 'en', 'un', 'se']):
            return {
                "detected_language": "Spanish",
                "language_code": "es",
                "confidence": 0.7,
                "method": "fallback"
            }
        elif any(word in text_lower for word in ['le', 'de', 'et', 'à', 'un', 'il', 'être', 'avoir']):
            return {
                "detected_language": "French",
                "language_code": "fr",
                "confidence": 0.7,
                "method": "fallback"
            }
        elif any(word in text_lower for word in ['der', 'die', 'und', 'in', 'den', 'von', 'zu', 'das']):
            return {
                "detected_language": "German",
                "language_code": "de",
                "confidence": 0.7,
                "method": "fallback"
            }
        else:
            return {
                "detected_language": "Unknown",
                "language_code": "unknown",
                "confidence": 0.3,
                "method": "fallback"
            }

    def _parse_text_language_response(self, response: str, original_text: str) -> Dict[str, Any]:
        """Parse text response to extract language information"""
        response_lower = response.lower()

        # Common languages to look for in response
        languages = {
            'english': {'name': 'English', 'code': 'en'},
            'spanish': {'name': 'Spanish', 'code': 'es'},
            'french': {'name': 'French', 'code': 'fr'},
            'german': {'name': 'German', 'code': 'de'},
            'italian': {'name': 'Italian', 'code': 'it'},
            'portuguese': {'name': 'Portuguese', 'code': 'pt'},
            'chinese': {'name': 'Chinese', 'code': 'zh'},
            'japanese': {'name': 'Japanese', 'code': 'ja'},
            'korean': {'name': 'Korean', 'code': 'ko'},
            'russian': {'name': 'Russian', 'code': 'ru'},
            'arabic': {'name': 'Arabic', 'code': 'ar'},
            'hindi': {'name': 'Hindi', 'code': 'hi'}
        }

        for lang_key, lang_info in languages.items():
            if lang_key in response_lower:
                return {
                    "detected_language": lang_info['name'],
                    "language_code": lang_info['code'],
                    "confidence": 0.8,
                    "method": "text_parsing"
                }

        # If no language found in response, use fallback
        return self._fallback_language_detection(original_text)

    def get_available_models(self) -> List[str]:
        """Get list of available AI models - All powered by single Gemini API"""
        # All models use the same Gemini API - just different prompting styles
        return ["gemini"] if self._has_gemini() else []


# Global AI client instance
ai_client = AIClient()
