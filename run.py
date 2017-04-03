import src.nntrain as nntrain
import src.nnplot as nnplot
import src.nnload as nnload
import numpy as np

# Define preprocessor
x_ppi = {'name': 'StandardScaler', 'method': 'qTindividually'}
y_ppi = {'name': 'SimpleY', 'method': 'qTindividually'}



# Run an example with many neurons in first layer, but not many in second layer
nntrain.TrainNNwrapper(1, 51, x_ppi, y_ppi, minlev=0.2,
                 n_iter=3000, rainonly=False, weight_decay=1e-6,
                 N_trn_exs=50, weight_precip=False,
                 weight_shallow=False, convcond=False,
                 cirrusflag=True)

num_layers = [1, 2]
num_neurons = [100, 50, 10]  # [10, 50, 100]
num_trains = [400000]  # [1000, 5000, 10000, 100000]
cvcdbool = [False]  # , True]
regs = [1e-6]  # 1e-5 1e-6

# for cvcd in cvcdbool:
#     for reg in regs:
#         for num_layer in num_layers:
#             for num_train in num_trains:
#                 for num_neuron in num_neurons:
#                     nntrain.train_nn_wrapper(num_layer, num_neuron, x_ppi, y_ppi, minlev=0.2,
#                                          n_iter=10000, rainonly=False, weight_decay=reg,
#                                          N_trn_exs=num_train, weight_precip=False,
#                                          weight_shallow=False, convcond=cvcd,
#                                          cirrusflag=True)


# n_samps = [1000,5000,10000,50000]
# # n_samps=[1001]
# #hid_neur = [10,20,40,60,100,150,225,300,450,600,800,1000]
# # hid_neur = [5,15,30,50,80]
# # nntrain.train_nn_wrapper(2, 61, x_ppi, y_ppi, n_iter=10000, minlev=0.25, noshallow=True)
# for n_samp in n_samps:
#     nntrain.train_nn_wrapper(2, 60, x_ppi, y_ppi, minlev=0.1, n_iter=10000,
#                         rainonly=False, weight_decay=1e-4,
#                         N_trn_exs=n_samp, weight_precip=False, weight_shallow=False)
# for n_samp in n_samps:
#     nntrain.train_nn_wrapper(2, 60, x_ppi, y_ppi, minlev=0.1, n_iter=10000,
#                         rainonly=False, weight_decay=1e-4,
#                         N_trn_exs=n_samp, weight_precip=False, weight_shallow=False,
#                         convcond=True)
