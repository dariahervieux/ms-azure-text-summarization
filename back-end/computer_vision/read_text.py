import json
import os
import sys
import requests
import time

class ReadText:
	READ_API = "vision/v3.0/read/analyze"

	def __init__(self):
		missing_env = False
		# Add your Computer Vision subscription key and endpoint to your environment variables.
		if 'COMPUTER_VISION_ENDPOINT' in os.environ:
			self.text_recognition_url = os.environ['COMPUTER_VISION_ENDPOINT'] + self.READ_API
		else:
			print("From Azure Cognitive Service, retrieve your endpoint and subscription key.")
			print("\nSet the COMPUTER_VISION_ENDPOINT environment variable, such as \"https://westus2.api.cognitive.microsoft.com\".\n")
			missing_env = True

		if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
			self.subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
		else:
			print("From Azure Cognitive Service, retrieve your endpoint and subscription key.")
			print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable, such as \"1234567890abcdef1234567890abcdef\".\n")
			missing_env = True

		if missing_env:
			print("**Please configure your application.**")
			sys.exit()

	""" Initiate image reading process.
	    Returns URL to retrieve the status of processing and eventually the result. 
	"""
	def _start_read(self, image_path):
		# Read the image into a byte array
		image_data = open(image_path, "rb").read()

		headers = {'Ocp-Apim-Subscription-Key': self.subscription_key,
               'Content-Type': 'application/octet-stream'}

		response = requests.post(self.text_recognition_url, headers=headers, data=image_data)
		response.raise_for_status()

		# 'Operation-Location' holds the URI used to retrieve the recognized text.
		retrieve_text_url = response.headers["Operation-Location"]
		print(f'retrieved URL: {retrieve_text_url}')
		return retrieve_text_url

		# Extracting text requires two API calls: One call to submit the
		# image for processing, the other to retrieve the text found in the image.

	def read(self, image_path):
		retrieve_text_url = self._start_read(image_path)
		# The recognized text isn't immediately available, so poll to wait for completion.
		analysis = {}
		poll = True
		headers = {'Ocp-Apim-Subscription-Key': self.subscription_key,
		           'Content-Type': 'application/octet-stream'}
		while (poll):
			response_final = requests.get(retrieve_text_url, headers=headers)
			analysis = response_final.json()
			
			#print(json.dumps(analysis, indent=4))

			time.sleep(1)
			if ("analyzeResult" in analysis):
				poll = False
			if ("status" in analysis and analysis['status'] == 'failed'):
				poll = False

		text = []
		if ("analyzeResult" in analysis):
			# Extract the recognized text, with bounding boxes.
			text = [(line["text"])
						for line in analysis["analyzeResult"]["readResults"][0]["lines"]]
		print(f'text: {text}')
		return ' '.join(text)

