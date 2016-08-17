import json

# load the conversations into a list
def load_conversations(training_filename):
	with open(training_filename) as input_file:
		data = json.load(input_file)
	conversations = []
	for d in data['Issues']:
		for m in d['Messages']:
			conversations.append(m['Text'].encode('utf-8'))
	return conversations

for d in load_conversations('sample_conversations.json'):
	print d

# intructions to train with torch-rnn:

# 1. pipe to file: python train_model.py > conversations.txt

# 2. process using torch-rnn
# python scripts/preprocess.py \
#  --input_txt conversations.txt \
#  --output_h5 my_data.h5 \
#  --output_json my_data.json

# 3. train using torch-rnn
# th train.lua -input_h5 my_data.h5 -input_json my_data.json -gpu -1 -batch_size 1 -seq_length 50