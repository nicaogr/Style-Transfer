"""
Created on  Wed 28 June

This script have the goal to generate texture with different loss function

@author: nicolas
"""

import Style_Transfer as st
from Arg_Parser import get_parser_args 
import os
import tensorflow as tf

def get_list_of_images(path_origin):
	dirs = os.listdir(path_origin)
	dirs = sorted(dirs, key=str.lower)
	return(dirs)

def do_mkdir(path):
	if not(os.path.isdir(path)):
		os.mkdir(path)
	return(0)

def generation_Texture_LossFct():
	path_origin = '/home/gonthier/Travail_Local/Texture_Style/Style_Transfer/dataImages/'
	path_origin = '/home/gonthier/Travail_Local/Texture_Style/Style_Transfer/dataImagesTest/'
	#path_origin = '/home/nicolas/random_phase_noise_v1.3/im/'
	path_output = '/home/gonthier/Travail_Local/Texture_Style/Style_Transfer/LossFct/resultsDiff_loss_functionTest/'
	#path_output = '/home/nicolas/Style-Transfer/LossFct/random_phase_noise_v1.3/'
	#path_output = '/home/nicolas/Style-Transfer/LossFct/tmp/'
	do_mkdir(path_output)
		
	parser = get_parser_args()
	max_iter = 2000
	print_iter = 500
	start_from_noise = 1
	init_noise_ratio = 1.0
	optimizer = 'lbfgs'
	init = 'Gaussian'
	init_range = 0.0
	clipping_type = 'ImageStyleBGR'
	vgg_name = 'normalizedvgg.mat'
	n_list = [1,2,4]
	p = 4
	losses_to_test = [['autocorr'],['Lp'],['fft3D'],['bizarre']]
	#losses_to_test = [['texture','HF'],['texture'],['texture','TV'],['texture','HFmany']]
	losses_to_test = [['nmoments'],['Lp'],['texture'],['PhaseAlea']]
	losses_to_test = [['autocorr_rfft'],['autocorr']]
	losses_to_test = [['texture']]
	config_layers_tab = ['PoolConfig','FirstConvs']
	config_layers_tab = ['PoolConfig']
	
	list_img = get_list_of_images(path_origin)
	
	for config_layers in config_layers_tab:
		for loss in losses_to_test:
			if loss[0] == 'nmoments':
				for n in n_list: 
					if(config_layers=='FirstConvs') and (n > 2):
						loss = ['nmoments_reduce']
					for name_img in list_img:
						tf.reset_default_graph() # Necessity to use a new graph !! 
						name_img_wt_ext,_ = name_img.split('.')
						img_folder = path_origin
						img_output_folder = path_origin
						output_img_name = name_img_wt_ext
						for loss_item in loss:
							output_img_name += '_' + loss_item + '_' + str(n)
						parser.set_defaults(verbose=True,max_iter=max_iter,print_iter=print_iter,img_folder=path_origin,
							img_output_folder=path_output,style_img_name=name_img_wt_ext,content_img_name=name_img_wt_ext,
							init_noise_ratio=init_noise_ratio,start_from_noise=start_from_noise,output_img_name=output_img_name,
							optimizer=optimizer,loss=loss,init=init,init_range=init_range,p=p,n=n,clipping_type=clipping_type,
							vgg_name=vgg_name)
						args = parser.parse_args()
						st.style_transfer(args)

			else:
				n = 4
				for name_img in list_img:
					tf.reset_default_graph() # Necessity to use a new graph !! 
					name_img_wt_ext,_ = name_img.split('.')
					img_folder = path_origin
					img_output_folder = path_origin
					output_img_name = name_img_wt_ext
					for loss_item in loss:
						output_img_name += '_' + loss_item
					parser.set_defaults(verbose=True,max_iter=max_iter,print_iter=print_iter,img_folder=path_origin,
						img_output_folder=path_output,style_img_name=name_img_wt_ext,content_img_name=name_img_wt_ext,
						init_noise_ratio=init_noise_ratio,start_from_noise=start_from_noise,output_img_name=output_img_name,
						optimizer=optimizer,loss=loss,init=init,init_range=init_range,p=p,n=n,clipping_type=clipping_type,
						vgg_name=vgg_name)
					args = parser.parse_args()
					st.style_transfer(args)

if __name__ == '__main__':
	generation_Texture_LossFct()
	# python LossFct_Test_Gen.py >> /home/nicolas/Style-Transfer/LossFct/results/output.txt
