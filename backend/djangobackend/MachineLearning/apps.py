from django.apps import AppConfig
from transformers import BertTokenizer, BertForSequenceClassification
import html 
import pathlib
import os
import pandas as pd
import torch

class MachinelearningConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MachineLearning'

