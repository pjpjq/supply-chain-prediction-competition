# supply-chain-prediction-competition

Competition: https://www.datafountain.cn/competitions/313/details/rule.

## Objective

-   运用最近1年多的商品数据预测45天后5周每周 (week1-5) 的销量. 

(具体为: 2017年3月1日至2018年3月16日数据 -> 预测2018年5月1日，5月8日，5月15日，5月22日，5月29日起5周的销量)

-   Evaluation: RMS Error (评测的 score = 1/(1+rmse)), 做实验 loss 用 l2 loss 就好了

## Resources

-   Kaggle 学习资料
    -    https://github.com/apachecn/kaggle
-   需求预测: https://en.wikipedia.org/wiki/Demand_forecasting.
-   Time series 分析 (里面链接有点太多了挑些看): https://www.kaggle.com/c/demand-forecasting-kernels-only/discussion/63568
-   类似的比赛 (搜 online + sales/demand + prediction/forcasting + competition/challenge):
    -   https://www.kaggle.com/c/demand-forecasting-kernels-only
    -   https://semantive.com/long-term-demand-forecasting/ 博客

## Additional Info (optional)

-   可能有用的外部信息
    -   [ ] 特殊节日: 类似双十一的促销节或者滞销时期, 好像促销很关键, 所以 
    -   [ ] 查下5月的促销节
    -   [ ] 气候
    -   [ ] 宗教, 比如有什么节是不能买东西的
    -   [ ] 跟中国的政治关系变化 (对外贸易的政策变化)
    -   [ ] 执御在沙特主要销售什么产品? 什么特点? 跟沙特人民的喜好关系?
        -   和网红合作 (有什么用?)
-   


## Understanding Datasets

-   [ ] 数据集各列的意义

    具体不懂有没有用的搜下研究下

    其他基本的看比赛网站的数据说明, 一些特殊的需要注释一下:

    -   sku_id: 单品 
    -   goods_id: 商品, 一个可以有多个sku (款式)
    -   [ ] 点击次数 加购次数和收藏次数==>可以合成一个特征: 商品流行度/用户兴趣

-   [ ] 数据集大小

## Data Preprocessing 洗数据 分数据

-   [ ] 补缺失值 (好像没什么要补的?)
-   [ ] 清异常值 (可以利用到相关性, 比如相同品牌/商品可以做一个平均基准)
-   [ ] 

-   [ ] 分割训练测试集 (怎么分?)
-   [ ] 调整权重

## Feature Engineering

- New Features:
    -   

## Model Training

找各种模型 + 调参

### NN

GPU 上 train, 用 fast.ai 技巧如 https://blog.floydhub.com/ten-techniques-from-fast-ai/

-   [ ] LSTM
-   [ ] 普通全连接 MLP

### RF

### SVR

其他时序模型

## Ensemble

融合

-   [ ] XGBoost (是什么?)
-   [ ] lightGBM (what?)

## Misc

-   [ ] EDA 是什么????????? 好多用了 EDA, eg https://www.kaggle.com/harshpan/store-item-eda-lightgbm
-   [ ] sklearn 的模型怎么调参? 有什么好方法, fast.ai有讲吗?


