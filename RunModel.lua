require 'torch'
require 'nn'

require 'LanguageModel'

local RunModel = torch.class('RunModel')

function RunModel:sample(start_text, length_of_start_text)
  opt = {checkpoint = "cv/checkpoint_72000.t7", length = length_of_start_text + 50, start_text = start_text, sample = 1, temperature = 0.5, gpu = -1, gpu_backend = "cuda", verbose = 0}
  local checkpoint = torch.load(opt.checkpoint)
  local model = checkpoint.model
  model:evaluate()
  local sample = model:sample(opt)
  return sample
end