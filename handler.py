import runpod
from transformers import pipeline

# Model loads automatically from Hugging Face
model = pipeline("image-classification", "JeffreyXiang/TRELLIS-image-large")

def handler(job):
  """ Input: {'image': URL_OR_BASE64} """
  return model(job["input"]["image"])

runpod.serverless.start({"handler": handler})