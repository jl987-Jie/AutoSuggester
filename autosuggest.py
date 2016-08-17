import json
import cherrypy
import PyTorch
import PyTorchHelpers
# need to nltk.download('punkt')
import nltk.data 

class AutoSuggestEngine():
	exposed = True

	# load tokenizer from nltk
	def __init__(self):
		self.tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	# generate suggestions based on a prefix
	def generate_suggestions(self, prefix):
		unicode_prefix = unicode(prefix, "utf-8")
		list_of_responses = []
		# return 5 results from model (configurable)
		for x in range(0, 5):
			response = self.sample_from_model(prefix)
			list_of_responses.append(self.tokenizer.tokenize(response)[0])
		result = {"Suggestions": list_of_responses}
		return result

	# sample from LSTM model trained by Torch-rnn.
	def sample_from_model(self, prefix):
		# make sure to have 'VanillaRNN.lua' and 'LSTM.lua' in home directory's '.luarocks/share/lua/5.1/'
		RunModel = PyTorchHelpers.load_lua_class('RunModel.lua', 'RunModel')
		runModel = RunModel()
		result = runModel.sample(prefix, len(prefix))
		return result

	# return a list of suggestions
	@cherrypy.tools.json_out()
	def GET(self, prefix=None):
		if prefix == None:
			# return no suggestions if prefix is empty
			return {"Suggestions": []}
		else:
			return self.generate_suggestions(prefix)
