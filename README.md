# caffe-load-same-weight-in-different-branch
when I try to reproduce the paper:Learning Discriminative Features with Multiple Granularities for Person Re-Identification in caffe. I find that initialize different branch with same pre-trained weights is a problem. Because the different branchs has different name.

you can edit the layer name in caffemodel, and load three pretraind models to MGN.

train -solver=/xiaoyu/mgn_caffe/solver.prototxt -weights=ResNet-50-model-1.caffemodel,ResNet-50-model2.caffemodel,/xiaoyu/mgn_caffe/resnet50/ResNet-50-model-3.caffemodel
