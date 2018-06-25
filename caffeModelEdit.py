#! python
#coding=utf-8



import os,sys
caffe_root = '/data/darwin-caffe-base/'# caffe的根目录
os.chdir(caffe_root)  #os.chdir()用于改变当前工作目录到指定的路径
sys.path.insert(0,caffe_root+'python')

from caffe import Net,TEST
import caffe

import numpy as np

net = Net('/data/mgn_caffe/resnet50/ResNet-50-deploy.prototxt', '/data/mgn_caffe/resnet50/ResNet-50-model.caffemodel', caffe.TEST)
netNew = Net('/data/mgn_caffe/resnet50/ResNet-50-deploy-3.prototxt',caffe.TEST)

for k1, v1 in netNew.params.items():			 
    for k, v in net.params.items():
    #print (k, v[0].data.shape)
    #print np.size(net.params[k])
        for i in range(np.size(net.params[k])):
             if (k1==k+'_3'):
                  print(k1)
                  netNew.params[k1][i].data[:] = np.copy(net.params[k][i].data[:])			
        for i in range(np.size(net.params[k])):
             if (k1==k):
                  print(k1)
                  netNew.params[k][i].data[:] = np.copy(net.params[k][i].data[:])				 
netNew.save('/data/mgn_caffe/resnet50/ResNet-50-model-3.caffemodel')
			 

