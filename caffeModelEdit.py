#! python
#coding=utf-8



import os,sys
caffe_root = '/data/darwin-caffe-base/'# caffe的根目录
os.chdir(caffe_root)  #os.chdir()用于改变当前工作目录到指定的路径
sys.path.insert(0,caffe_root+'python')

from caffe import Net,TEST
import caffe



n_orig = Net('/data/mgn_caffe/resnet50/ResNet-50-deploy.prototxt', '/data/mgn_caffe/resnet50/ResNet-50-model.caffemodel', 0)
n_new = Net('/data/mgn_caffe/resnet50/ResNet-50-deploy-2.prototxt', '/data/mgn_caffe/resnet50/ResNet-50-model.caffemodel',0)

for orig_name in n_orig.params:
    for new_name in n_new.params:
	    if (new_name == orig_name+'_2'):		 
             n_new.params[new_name] = n_orig.params[orig_name]
             print(new_name)

n_new.save('/data/mgn_caffe/resnet50/ResNet-50-model-2.caffemodel')
