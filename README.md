# HelmetDetection

### This is E2E machine learning classification project to detect the helmet in images. 

Goal of the project was to generate and deploy machine learning model on the scrapped images of internet. This project gives hands-on experience 
of Roboflow, Hugging face and Flask.

## Step1: Generate dataset

We have used serpapi of googlesearch module to scrap the images from internet. 
Script has been written in python language - Image_scrap.py
You can replace the api_key with your account's token. 

This script will download images in SerpApi_images folder.

documentation: https://serpapi.com/blog/scrape-google-images-with-python/

## Step2: Labelling Dataset

1047 images were downloaded using scrapping script and manually labeled using Roboflow.

Roboflow is useful for labelling the dataset: https://app.roboflow.com/aicamp-7rst6/ai-camp-mtn7c/2

![Screen Shot 2023-03-30 at 3 51 58 PM](https://user-images.githubusercontent.com/28559153/228982158-202ad89f-d961-40ac-810c-3358fc41a4bb.png)

## Step3: Pre-processing of Dataset

We divided dataset into train-val-test split using 70-20-10 ratio, Resized into 224x224 dimension. 

Augmentation has been also applied to generalize the model.

## Step4: Uploading the dataset into Hugging Face.

Helmet_model.ipynb file has been used to upload the Roboflow dataset into the HuggingFace dataset.

HuggingFace dataset can be found - https://huggingface.co/datasets/pzalavad/HelmetDataset 

## Step5: Training

We used ViTForImageClassification of transformers module to train the model for classification, after training we were able to obtain 95% training accuracy with 0.25 validation loss.

## Step6: Deployment

Model has been deployed in Hugging face - https://huggingface.co/pzalavad/AiCampHelmet using Helmet_model.ipynb for consuming into various platforms. 

## Step7: Create simple website and consume model using Flask

Checkout simple website explaining whole project and detecting helmets of picture. Some screenshots are provided below,
Repl: https://computer-vision-module-priyanshzalavad.2023-instructor-crash-course.repl.co/
![Screen Shot 2023-04-13 at 11 07 53 PM](https://user-images.githubusercontent.com/28559153/231955700-e230fef7-30cd-4809-b054-d9fb5c068df0.png)
![Screen Shot 2023-04-13 at 11 08 23 PM](https://user-images.githubusercontent.com/28559153/231955718-47df8f27-4630-4605-9aaa-97638ff1edf0.png)
![Screen Shot 2023-04-13 at 11 08 44 PM](https://user-images.githubusercontent.com/28559153/231955732-6d253103-65ff-47cb-9c3f-176b9c38e670.png)




