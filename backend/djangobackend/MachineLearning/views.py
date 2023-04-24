from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from transformers import BertTokenizer, BertForSequenceClassification
import html 
import pathlib
import os
import pandas as pd
import torch

#This file accesses the pretrained BERT model located at ../MLmodel/ and passes
#the URL arguments to the BERT model and returns the models response as a JSON response
#The machine learning module uses the bare minimum django resources to process responses, and does not 
#make use of models, serializers, etc.

#Replace with host server file path
input_dir = ''
loaded_model = BertForSequenceClassification.from_pretrained(input_dir)
loaded_model.eval()
loaded_tokenizer = BertTokenizer.from_pretrained(input_dir)
#Replace with host server file path
loaded_df_label = pd.read_pickle('')

def medical_symptom_detector(intent):
    pt_batch = loaded_tokenizer (
        intent,
        padding=True,
        return_tensors="pt")

    pt_outputs = loaded_model(**pt_batch)
    __, id = torch.max(pt_outputs[0], dim=1)
    prediction = loaded_df_label.iloc[[id.item()]]['intent'].item()
    print(prediction)
    return prediction

class query(APIView):

    def get(self,request):
        if request.method == 'GET':
            input = request.GET.get('query')
            output = {"output" : medical_symptom_detector(input)}
           
            return JsonResponse(output)





    