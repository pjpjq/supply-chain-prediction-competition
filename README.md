# supply-chain-prediction-competition

Competition: https://www.datafountain.cn/competitions/313/details/rule.

## Objective

-   运用最近1年多的商品数据预测45天后5周每周 (week1-5) 的销量. 

(具体为: 2017年3月1日至2018年3月16日数据 -> 预测2018年5月1日，5月8日，5月15日，5月22日，5月29日起5周的销量)

-   Evaluation: RMS Error (评测的 score = 1/(1+rmse)), 做实验 loss 用 l2 loss 就好了

## Resources

-   Kaggle 学习
    -    https://github.com/apachecn/kaggle
-   需求预测: https://en.wikipedia.org/wiki/Demand_forecasting.
-   Time series 分析 (里面链接有点太多了找些看): https://www.kaggle.com/c/demand-forecasting-kernels-only/discussion/63568
-   类似的比赛 (搜 online + sales/demand + prediction/forcasting + competition/challenge):
    -   https://www.kaggle.com/c/demand-forecasting-kernels-only
    -   https://semantive.com/long-term-demand-forecasting/ 博客

## Additional Info (optional)

-   可能有用的外部信息
    -   [ ] 特殊节日: 类似双十一的促销节或者滞销时期
    -   [ ] 气候
    -   [ ] 宗教
    -   [ ] 执御在沙特主要销售什么产品? 什么特点? 
        -   和网红合作 (有什么用?)
-   


## Understanding Datasets

-   [ ] 数据集各列的意义

    具体不懂有没有大用的搜下研究下, 比如:点击次数, 加购次数, 有什么用?

    其他基本的看比赛网站的数据说明, 一些特殊的需要注释一下:

    -   sku_id: 单品 
    -   goods_id: 商品, 一个可以对应多个sku (款式)

-   [ ] 数据集大小

## Data Preprocessing 洗数据 分数据

-   [ ] 补缺失值
-   [ ] 清异常值
-   [ ] 

-   [ ] 分割训练测试集
-   [ ] 调整权重

## Feature Engineering

-   New Features:
    -   

## Model Training

找各种模型, 调参

### NN

-   [ ] LSTM
-   [ ] 普通全连接

### RF

### SVR



## Emsemble

融合

-   [ ] XGboost 等等 (是什么?)

## Misc

-   [ ] EDA 是什么????????? 好多用了 EDA, eg https://www.kaggle.com/harshpan/store-item-eda-lightgbm


