#Currently using Jake's Token#s
APItoken = '778ffa03964d8181be69c33e7daccc3b3fbd3ed1ef610a5244d2c31f62bdc3685e5a7267e6db2ddd0902e6d994493aa9c7b37431842b090d6e1e660fb0ad1ac0'
config = {'url': 'https://quantumexperience.ng.bluemix.net/api'}

if 'APItoken' not in locals():
     raise Exception('Please set up your access token. See Qconfig.py.')