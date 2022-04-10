# Neural-Network
Neural Networks Course Assignments
1、训练：
激活函数：第一层使用relu，第二层使用softmax

反向传播，loss以及梯度的计算：h1.0.ipynb的backward、loss函数和SGD类中

学习率下降策略：SGD类中进行了更新

L2正则化：计算损失函数时加入，h1.0.ipynb的train_reset中

优化器SGD

保存模型：保存在models文件夹中

 

2、参数查找：
学习率：[5e-3, 1e-2, 2e-2]
隐藏层大小：与训练后选择50
正则化强度：[0.001,0.01,0.1]
 

3、测试：导入模型，用经过参数查找后的模型进行测试，输出分类精度
分类精度为：0.9652

4、可视化文件保存在visual文件夹中
