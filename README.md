# Classifying Cloud Shapes for NASA Globe project

## Overview

NASA runs a citizen science project named [Globe](https://www.globe.gov). This project consists of collecting data on Cloud and Land cover classification and mosquito habitats. Several schools and individuals participate in this program.

My children participate in the cloud cover program. As part of the program, participants would need to find satellite overpass times for their home/school location and at a specific time take a picture of the sky and horizon, classify the cloud types given a few reference images, input additional data such as ground/sky conditions, if its raining/snowing and submit the data.

## Problem

The satellite overpass times happen at a few odd times during the day and night. NASA does mention that data can be submitted within 15 minutes of satellite overpass time. However my children have missed data collection quite a few times. In addition, classifying cloud shapes is an interesting computer vision problem, quite different from common objects such as people, cars, cats and dogs. My motivation was to find a reliable way to classify the cloud shapes using different cloud vision APIs, open source tools and mobile AI APIs. In the process, learn and share the knowledge with others in the field.

## Solution

The solution consists of 4 parts. First two parts are common for all providers/APIs. The last two steps might vary based on provider/tool.

- Collecting data to train a model with each provider.
- Capturing images using RaspberryPi/Camera based on satellite overpass times.
- Classifying the realtime images using the trained model.
- Implement a human-in-the-loop workflow to retrain the models based on accuracy of the predictions.  

### Data collection for model training

In order to compare and contrast different Vision APIs, the dataset would need to be same. Images are collected from Creative Commons Media search API to ensure images are free from any licensing restrictions. 

Use ```get-images.py``` to get images from CreativeCommons. However for the initial use, you would need to get ```client_id```, ```client_secret``` and ```name``` and save it in ```secrets.json```.  

### Field image collection

Images from the field (ground truth) are collected from using a Raspberry Pi with a Camera. [Satellite overpass times](https://scool.larc.nasa.gov/GLOBE/globe_overpass-en.html) are provided by NASA manually by filling a form. I wrote a python script to capture the same data programmatically such that this data can be converted into a cronjob template and image capture can be triggered by a cronjob.

### Predictions
> TODO

### Human-in-the-loop
> TODO

## Conclusion
>TODO

### Disclaimer

This project is a personal project to learn and use the knowledge to advance science in a way that helps me and children make a small contribution. I'm not directly or indirectly endorsing a given cloud provider. I'm not comparing/contrasting the features or recommending one provider over the other. Opinions expressed in this project are my own. Please feel free to use any or all of this project at your own risk.
 
