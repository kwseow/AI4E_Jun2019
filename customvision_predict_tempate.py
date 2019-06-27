from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

ENDPOINT = "https://southeastasia.api.cognitive.microsoft.com"

# Replace with a valid key
training_key = "<your_training_key>"
prediction_key = "<your_training_key>"
prediction_resource_id = "<your_prediction_resource_id>"
project_id = "your_project_id"
publish_iteration_name = "<your_publish_iteration_name>"



# Now there is a trained endpoint that can be used to make a prediction
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

with open("test_image.jpg", "rb") as image_contents:
    results = predictor.classify_image(project_id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print ("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))
