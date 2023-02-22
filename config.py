DEBUG = True
debug_epochs = 1

###TRAINING
epochs = 90
print_freq = 100

###DATASET
dataset = 'cub'
download = False

###OPTIMISER
optimiser = 'adam'
grad_clip = 0.1
weight_decay = 1e-4

###SCHEDULER
scheduler = 'onecycle'
#  onecycle

###LOSS
loss_fn = 'crossentropy'
label_smoothing = 0

###MODEL
model = 'resnet18'

###TESTING
use_range = True
tau_min = 0.6
tau_max = 0.9

#  if range not used
tau = 0.85

#OUTPUT
dict_path = './output'
cloud_dict_path = '../drive/MyDrive/RP3'