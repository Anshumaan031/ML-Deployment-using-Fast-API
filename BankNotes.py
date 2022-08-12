# -*- coding: utf-8 -*-

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):   #the base model inherited from pydantic hepls in validating and managing input values
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float