import os
import spacy
import shutil

model_version = '2.2.5'
previous_version = '2.2.0'

model_name = 'en_core_web_lg'
SPACY_MODEL_PATH = '/home/jovyan/work/shared/'+model_name+'-'+model_version
SPACY_MODEL_FILE = '/home/jovyan/work/shared/'+model_name+'-'+model_version+'/'+model_name+'-'+model_version+'.tar.gz'

if os.path.exists(SPACY_MODEL_FILE):
    model_size = os.path.getsize(SPACY_MODEL_FILE)
    print(SPACY_MODEL_FILE+' exists. Model size is '+str(model_size)+' bytes')
else:
    print(SPACY_MODEL_FILE+' does not exist.')
    if not os.path.exists(SPACY_MODEL_PATH):
        os.makedirs(SPACY_MODEL_PATH)
        print('created '+SPACY_MODEL_PATH)
    print('Downloading model...')
    os.system('wget https://github.com/explosion/spacy-models/releases/download/'+model_name+'-'+model_version+'/'+model_name+'-'+model_version+'.tar.gz -O /home/jovyan/work/shared/'+model_name+'-'+model_version+'/'+model_name+'-'+model_version+'.tar.gz')
    if os.path.exists(SPACY_MODEL_FILE):
        model_size = os.path.getsize(SPACY_MODEL_FILE)
        print('Download complete. Model size = '+str(model_size)+' bytes')
    #!wget https://github.com/explosion/spacy-models/releases/download/en_vectors_web_lg-2.1.0/en_vectors_web_lg-2.1.0.tar.gz -O /home/jovyan/work/shared/en_vectors_web_lg-2.1.0/en_vectors_web_lg-2.1.0.tar.gz

print('Installing model '+model_name+' ...')
os.system('python -m pip install --no-cache-dir /home/jovyan/work/shared/'+model_name+'-'+model_version+'/'+model_name+'-'+model_version+'.tar.gz')
try:
    import en_core_web_lg
    print('Install successful, model '+model_name+'.')
except ImportError:
    print('install failed, failed import for '+model_name+'. ')

if model_version != previous_version:
    if os.path.exists('/home/jovyan/work/shared/'+model_name+'-'+previous_version+'/'+model_name+'-'+previous_version+'.tar.gz'):
        os.remove('/home/jovyan/work/shared/'+model_name+'-'+previous_version+'/'+model_name+'-'+previous_version+'.tar.gz')
        shutil.rmtree('/home/jovyan/work/shared/'+model_name+'-'+previous_version)
        print('previous version '+model_name+', '+previous_version+' removed')
