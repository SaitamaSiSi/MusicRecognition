# Python结合Pandas、NumPy、Scikit-learn
# 用户行为预测系统

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from scikit_learn.kMeans import KMeans


# 生成推荐
def recommend(user_id, user_similarity, user_item_matrix):
    user_index = user_id - 1  # 用户索引
    similar_users = user_similarity[user_index]
    similar_users_indices = np.argsort(-similar_users)[1:]  # 排序相似用户

    # 查找相似用户喜欢但当前用户未评分的项目
    recommended_items = []
    for similar_user_index in similar_users_indices:
        similar_user_ratings = user_item_matrix.iloc[similar_user_index]
        user_ratings = user_item_matrix.iloc[user_index]
        items_to_recommend = similar_user_ratings[(similar_user_ratings > 0) & (user_ratings == 0)]
        recommended_items.extend(items_to_recommend.index.tolist())

    return set(recommended_items)


def example():
    # 构造用户-项目评分矩阵
    data = {'user_id': [1, 1, 1, 2, 2, 3, 3, 4],
            'item_id': [101, 102, 103, 101, 103, 102, 104, 101],
            'rating': [5, 3, 4, 4, 5, 5, 2, 3]}

    df = pd.DataFrame(data)

    # 将数据转换为用户-项目矩阵
    user_item_matrix = df.pivot_table(index='user_id', columns='item_id', values='rating').fillna(0)

    # 计算用户之间的余弦相似度
    user_similarity = cosine_similarity(user_item_matrix)

    # 测试推荐系统
    user_id = 1
    recommended_items = recommend(user_id, user_similarity, user_item_matrix)
    print(f"为用户 {user_id} 推荐的项目: {recommended_items}")


def test():
    # 加载数据

    # 自定义用户花费数据集 spend.csv
    data = pd.read_csv("./scikit_learn/spend.csv", parse_dates=["日期"])
    data = data.sort_values(by="日期")  # 按日期排序
    # 可以在已有数据的基础上进行数据扩展
    data['星期'] = data['日期'].dt.dayofweek
    data['是否周末'] = data['星期'].isin([5, 6]).astype(int)
    data['月份'] = data['日期'].dt.month
    data['前一天花费'] = data['当日花费'].shift(1)
    data['前一周平均花费'] = data['当日花费'].rolling(window=7).mean()
    data['前一周总花费'] = data['当日花费'].rolling(window=7).sum()
    data['目标'] = data['当日花费'].shift(-1)

    print(data.head())

    # 删除缺失值
    data = data.dropna().reset_index(drop=True)

    # 选择特征和目标
    features = ['星期', '是否周末', '前一天花费', '前一周平均花费', '前一周总花费']
    x = data[features]
    y = data['目标']

    # 划分训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)

    # 训练模型
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)

    # 预测
    y_predict = model.predict(x_test)

    # 评估模型
    mse = mean_squared_error(y_test, y_predict)
    print(f"Mean Squared Error: {mse}")

    # 假设最新的前一天数据
    latest_data = pd.DataFrame({
        '星期': [5],  # 假设今天是周五
        '是否周末': [1],  # 是周末
        '前一天花费': [24],  # 假设前一天花费为24元
        '前一周平均花费': [20],  # 假设前一周平均花费为20元
        '前一周总花费': [140]  # 假设前一周总花费为140元
    })

    # 预测下一天的花费
    predicted_spending = model.predict(latest_data)
    print(f"预测下一天的花费: {predicted_spending[0]:.2f}元")


def test2():
    # 加载数据

    # 顾客购物订单数据集 order.csv
    data = pd.read_csv("./scikit_learn/order.csv")
    # 选取每个顾客所购买各个商品所占的比重信息来进行聚类
    t = data.iloc[:, -8:]
    print(t)

    kmeans = KMeans(3, 50)
    kmeans.fit(t)
    print(kmeans.cluster_centers_)
    # 查看某个簇的所有样本数据。
    print(t[kmeans.labels_ == 0])

    # 简单进行预测
    kmeans.predict([[30, 30, 40, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 30, 30, 40], [30, 30, 0, 0, 0, 0, 20, 20]])

    t2 = data.loc[:, "Food%":"Fresh%"]
    kmeans = KMeans(3, 50)
    kmeans.fit(t2)

    # 如果想显示中文的话，可以看这一段，默认情况下，matplotlib不支持中文显示，进行以下设置
    # 设置字体为黑体，以支持中文显示
    mpl.rcParams['font.family'] = 'SimHei'
    # 设置在中文字体时，能够正常的显示负号（-）
    mpl.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(10, 10))
    # 绘制每个类别的散点图
    plt.scatter(t2[kmeans.labels_ == 0].iloc[:, 0], t2[kmeans.labels_ == 0].iloc[:, 1], label='Category 1')
    plt.scatter(t2[kmeans.labels_ == 1].iloc[:, 0], t2[kmeans.labels_ == 1].iloc[:, 1], label='Category 2')
    plt.scatter(t2[kmeans.labels_ == 2].iloc[:, 0], t2[kmeans.labels_ == 2].iloc[:, 1], label='Category 3')
    # 绘制聚类中心
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='+', s=300)
    plt.title('Cluster analysis of food and meat purchases')
    plt.xlabel('food')
    plt.ylabel('meat')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # example()
    test()
