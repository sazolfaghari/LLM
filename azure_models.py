import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(""),
        UserMessage("""Explain this joke: I was going to fly to visit my family on May 3rd. 
                          My mom said "Oh great, your dad's poetry reading is that night!" 
                          So now I'm flying in on May 4th."""),
    ],
    temperature=1,
    top_p=1,
    model=model
)

print(response.choices[0].message.content)

