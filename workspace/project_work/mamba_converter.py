import torchvision.models as models
import pytorch2timeloop
from transformers import AutoTokenizer
from transformers import GPT2Tokenizer, GPT2Model
import pdb
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')
# model = GPT2Model.from_pretrained('gpt2-medium')
# text = "Replace me by any text you'd like."
# encoded_input = tokenizer(text, return_tensors='pt')
# output = model(**encoded_input)
# pdb.set_trace()


# my_embeddings = model.wte(encoded_input['input_ids'])

# model.h[0].ln_1(**encoded_input)

# Define a pytorch-based neural network model, for example, a pre-defined alexnet from torchvision.
net = models.alexnet()

import torch
import torch.nn as nn
import torch.nn.functional as F
from model import Mamba, generate

model = Mamba.from_pretrained('state-spaces/mamba-370m')
tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neox-20b')

input_shape = (10, 10)
batch_size = 1
top_dir = 'workloads'
sub_dir = 'mamba_370m'


prompt = 'I like to put pepperonis on my '
input_ids = tokenizer(prompt, return_tensors='pt').input_ids

output = generate(model, tokenizer, prompt, n_tokens_to_gen=1)
print('hello')
print(output)

# Now, convert!
pytorch2timeloop.convert_model(model, input_shape, batch_size, sub_dir, top_dir, fuse = False, convert_fc = False, sample_input = input_ids)