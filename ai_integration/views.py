from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai
import os

# Load OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@csrf_exempt
def generate_blog(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            topic = data.get("topic", "Artificial Intelligence")
            category = data.get("category", "Technology")

            prompt = f"Write a detailed blog post on the topic '{topic}' under the category '{category}'. The article should be informative, engaging, and well-structured."

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert blog writer."},
                    {"role": "user", "content": prompt}
                ]
            )

            blog_content = response["choices"][0]["message"]["content"]
            return JsonResponse({"blog": blog_content}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
