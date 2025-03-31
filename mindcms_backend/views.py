import requests
import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Together AI API Configuration
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")  # Use environment variable
TOGETHER_API_URL = "https://api.together.ai/v1/chat/completions"

@csrf_exempt
def generate_blog(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            topic = data.get("topic", "").strip()
            category = data.get("category", "").strip()

            if not topic or not category:
                return JsonResponse({"error": "Both topic and category are required."}, status=400)

            # Construct the prompt
            prompt = f"Write a detailed blog post about '{topic}' in the '{category}' category."

            # Make request to Together AI
            headers = {
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                "messages": [
                    {"role": "system", "content": "You are an AI assistant that generates high-quality blog posts."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 1000,
                "temperature": 0.7
            }

            response = requests.post(TOGETHER_API_URL, headers=headers, json=payload)

            if response.status_code == 200:
                blog_text = response.json().get("choices", [{}])[0].get("message", {}).get("content", "").strip()

                if not blog_text:
                    return JsonResponse({"error": "AI response was empty. Please try again."}, status=500)

                return JsonResponse({"blog_post": blog_text})
            else:
                logger.error(f"Together AI API Error: {response.text}")
                return JsonResponse({"error": f"Together AI error: {response.text}"}, status=response.status_code)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format in request."}, status=400)
        except requests.RequestException as e:
            logger.error(f"Request to Together AI failed: {str(e)}")
            return JsonResponse({"error": "Failed to connect to Together AI. Please try again later."}, status=500)
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return JsonResponse({"error": "An unexpected error occurred."}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
