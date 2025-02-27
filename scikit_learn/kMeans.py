import numpy as np


class KMeans:
    """使用python语言实现聚类算法"""

    def __init__(self, k, times):
        """初始化方法

        Parameters
        -----
        k : int
            聚类的个数

        times : int
            聚类迭代的次数
        """

        self.labels_ = None
        self.cluster_centers_ = None
        self.k = k
        self.times = times

    def fit(self, X):
        """根据提供的训练数据，对模型进行训练。

        Parameters
        ------
        X : 类数组类型，形状为：[样本数量，特征数量]
            待训练的样本特征属性。
        """

        X = np.asarray(X)
        # 设置随机种子，以便于可以产生相同的随机序列。（随机的结果可以重现。）
        np.random.seed(0)
        # 从随机数组中随机选择k个点作为初始聚类中心。
        self.cluster_centers_ = X[np.random.randint(0, len(X), self.k)]
        # 用来存放每个点所处的组或簇
        self.labels_ = np.zeros(len(X))

        for i in range(self.times):
            for index, x in enumerate(X):
                # 计算每个样本与聚类中心的距离，采用欧式距离
                dis = np.sqrt(np.sum((x - self.cluster_centers_) ** 2, axis=1))
                # 将最小的索引赋值给标签数组。索引的值是当前点所属的簇。范围为[0, k - 1]
                self.labels_[index] = dis.argmin()
            # 循环遍历每一个簇
            for i in range(self.k):
                # 计算每个簇内所有点的均值，更新聚类中心
                self.cluster_centers_[i] = np.mean(X[self.labels_ == i], axis=0)

    def predict(self, X):
        """根据参数传递的样本，对样本数据进行预测。（预测样本属于哪一个簇中）

        Parameters
        -----
        X : 类数组类型。形状为：[样本数量，特征数量]
            待预测的特征属性。

        Returns
        -----
        result : 数组类型
            预测的结果。每一个X所属的簇。
        """

        X = np.asarray(X)
        result = np.zeros(len(X))
        for index, x in enumerate(X):
            # 计算样本到每个聚类中心的距离
            dis = np.sqrt(np.sum((x - self.cluster_centers_) ** 2, axis=1))
            # 找到距离最近的聚类中心，划分类别。
            result[index] = dis.argmin()
        return result
