#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 

Argument parser for the function

@author: nicolas
"""

import argparse

def get_parser_args():
	"""
	Parser of the argument of the program
	"""
	desc = "TensorFlow implementation of 'A Neural Algorithm for Artisitc Style'"  
	parser = argparse.ArgumentParser(description=desc)

	# Verbose argument
	parser.add_argument('--verbose',action="store_true",
		help='Boolean flag indicating if statements should be printed to the console.')
		
	# Name of the Images
	parser.add_argument('--output_img_name', type=str, 
		default='Pastiche',help='Filename of the output image.')

	parser.add_argument('--style_img_name',  type=str,default='StarryNight',
		help='Filename of the style image (example: StarryNight). It must be a .jpg image otherwise change the img_ext.')
  
	parser.add_argument('--content_img_name', type=str,default='Louvre',
		help='Filename of the content image (example: Louvre). It must be a .jpg image otherwise change the img_ext.')
		
	# Name of the folders 
	parser.add_argument('--img_folder',  type=str,default='images/',
		help='Name of the images folder')
  
	parser.add_argument('--data_folder', type=str,default='data/',
		help='Name of the data folder')
	
	# Extension of the image
	parser.add_argument('--img_ext',  type=str,default='.jpg',
		help='Extension of the image')
		
	# Infomartion about the optimization
	parser.add_argument('--optimizer',  type=str,default='lbfgs',
		choices=['lbfgs', 'adam'],
		help='Loss minimization optimizer. (default|recommended: %(default)s)')
	
	parser.add_argument('--max_iter',  type=int,default=10,
		help='Number of Iteration Maximum. (default %(default)s)')
	
	parser.add_argument('--print_iter',  type=int,default=1,
		help='Number of iteration between each checkpoint. (default %(default)s)')
		
	parser.add_argument('--learning_rate',  type=float,default=10.,
		help='Learning rate only for adam method. (default %(default)s)')	
		
	# Profiling Tensorflow
	parser.add_argument('--tf_profiler',action='store_false',
		help='Profiling Tensorflow operation available only for adam.')
		
	# Info on the style transfer
	parser.add_argument('--content_strengh',  type=float,default=0.001,
		help='Importance give to the content : alpha/beta ratio. (default %(default)s)')
	
	parser.add_argument('--init_noise_ratio',type=float,default=0.9,
		help='Propostion of the initialization image that is noise. (default %(default)s)')
		
	parser.add_argument('--start_from_noise',type=int,default=0,choices=[0,1],
		help='Start compulsory from the content image noised if = 1 or from the former image with the output name if = 0. (default %(default)s)')
	
	# VGG 19 info
	parser.add_argument('--pooling_type', type=str,default='avg',
    choices=['avg', 'max'],help='Type of pooling in convolutional neural network. (default: %(default)s)')
	
	return(parser)
