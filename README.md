# Collecting NASA Globe Cloud Data using Cloud Vision APIs

## Overview

NASA runs a citizen science project named Globe. This project consists of collecting data on Cloud and Land cover classification and mosquito habitats. 

My children participate in the cloud cover program. As part of the program, participants would need to find satellite overpass times for their home/school location and at a specific time take a picture of the sky and horizon, classify the cloud types given a few reference images, input additional data such as ground/sky conditions, if its raining/snowing and submit the data.

## Problem

The satellite overpass times happen at a few odd times during the day and night. NASA does mention that data can be submitted within 15 minutes of overpass time. However my children have missed data collection quite a few times. 

## Solution

The solution was born out of a question from my 13 year old daughter: If "the cloud" can identify a cat or dog, can it identify a cloud type by its shape?. Her observation was triggered by seeing a few AWS DeepLens demo videos. To answer that question, together we set out on a journey to see how the different cloud provider vision algorithms can identify the cloud cover (no pun intended). 

This led me down a path to learn machine learning and computer vision. In this repo, you would see the same problem solved by using three leading cloud providers. 

### Data

The images are collected from Creative Commons Media search to ensure I use images free from any licensing restrictions even though this data is being used to help advance science. 

### Process

Data from image search is not perfect. Some images may have people or landmarks. In order to get quality images for training the models, manual processing is required. As per a few experts in this field, I was told to collect images that take a human a couple of seconds to identify the cloud type correctly. This rule-of-thumb could help in designing the human-in-the-loop workflow to collect other pieces of data.

Each cloud provider could train the model differently. The provider specific configuration, tuning or details can be found in the provider specific folders in this project.

### Results

## Conclusion


> Disclaimer: This project is a personal project to learn and use the knowledge to advance science in a way that helps me and children make a small contribution. I do not directly or indirectly endorsing a given cloud provider. I'm not comparing/contrasting the features or recommending one provider over the other. Opinions expressed in this project are my own. Please feel free to use any or all of this project at your own risk.
 