本次推荐系统实践主要集中在 对效用矩阵的处理上。
占内存和 吃时间的运算 相似度矩阵一个， 评估RMSE函数一个
稀疏矩阵的选择和操作
使用git的必要性，不用每次改完文件都改不回去


scipy.sparse 构建

三元组构建， 给出行列data三个array ， 

    testrow, testcol = np.array([]) , np.array([])
    data = np.ones(len(testrow))
    mit_test = csr_matrix((data, (testrow, testcol)), dtype=float)
   
几个矩阵可以相互转化， csr， csc 分别是按照行和列保存， 可以直接用下标获取data

重要函数：
  itemlist = mit_test.getrow(user).indices
  可以获得user行所有非零的列， 作为ndarray可以直接切片矩阵
  
        s = self.effect_matrix.nonzero()
        row = s[0]
        col = s[1]
        获得非零的行和列，然后可以mit[row[i], col[i] ] 获得对于data
        
      save_npz(path, mit) 
      load_npz  
      可以直接保存和读取稀疏矩阵
      
 scipy  sklearn  numpy 相互支持的性能非常好
 
 
 numpy 重要函数
 argsort， 获得的是排序后， 该位置该放源数组的哪一个位置的数
 
 a = np.argsort(array)
 b = np.sort(array)
 b == array[a]
 
 numpy可以直接用ndarray数组切片，极其好用。
 
 sklearn  
 
 pairwise_distances函数接受稀疏矩阵和一般矩阵， 
 返回基于行计算的相似度矩阵， 距离计算函数可以选择， 相似度= 1 - 距离
 
 划分函数
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
 对稀疏矩阵这么划分能返回稀疏矩阵， 但是一是划分似乎是随机挑出几行作为测试集，
 二是 划分完之后， 原来 第50 行， 划分之后会变成第46行（比如说）
 不保证行号和原来一直， 并不是基于稀疏矩阵的记录数划分的， 没有找到基于稀疏矩阵的记录数据随机划分的函数
