import pandas as pd
import os
from apyori import apriori


sample = [['말','사자'],
          ['호랑이,사자'],
          ['곰','사자']
          ]

aa = list(apriori(sample,
                  max_length=2,
                  min_confidence=0.5))

print(aa)