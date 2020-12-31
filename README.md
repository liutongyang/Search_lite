<!--
 * @Author: liutongyang
 * @Date: 2020-12-28 15:59:26
 * @LastEditTime: 2020-12-31 23:02:07
 * @Description: In User Settings Edit
 * @FilePath: /search_engines/sgcc_search/README.md
-->

<br />
<p align="center">

  <h1 align="center">垂直领域知识可迁移搜索项目</h1>

</p>

<!-- ABOUT THE PROJECT -->
## 项目简介

### 项目目标
垂直领域知识可迁移搜索项目，目标是通过先进的文本语义理解技术和智能检索技术，把复杂的非结构化文本建立倒排索引，提供高效、便捷、全面的垂类专业问答功能，极大提升知识检索效率，解放生产力。

### 项目功能
项目主要功能是将用户的 query 进行解析，提取 query 中的关键信息，使用该关键信息与语料库中 question 字段进行相似度匹配，相似度最高的问题为最佳匹配项，返回该问题的 anwser 作为用户 query 的回答。

### 核心模块
核心模块一共四个部分，分别是：
* 数据层
* 输入层
* 相似度计算层
* 输出层

![programming][programming]


数据层
 - 数据预处理模块
   - 将源文件转换为规定数据格式，即 question & anwser 对，分别保存至 question.txt 和 anwser.txt 文件中。
 - 数据加载模块
   - 把符合规定格式的语料库按行读入。

输入层
 - Query 清洗模块
   - 去除 query 中的乱码、非中文等特殊字符。
 - Query 特征抽取模块
   - 把 query 文本映射至高维语义空间，得到一个句向量。

相似度计算层
 - 相似度计算
   - 用户输入的 query 向量与语料库中所有 question 进行相似度计算，得到相似度匹配最高的 question 。

输出层
  - Anwser 排序模块
    - TODO
  - Query & Anwser 匹配模块
    - TODO


## 如何开始

这是一个示例，说明如何在本地设置项目。要在本地运行，请按照以下简单的示例步骤。

### 环境依赖

  * python == 3.6.5+
  * gensim == 3.8.3
  * jieba == 0.42.1
  * numpy == 1.14.3
  * scikit-learn == 0.19.1

### 一键安装依赖
```sh
  pip install -r requirements.txt
  ```

<!-- USAGE EXAMPLES -->
### 如何使用
```sh
  python main.py
  
  ...
  
  输入：油浸式变压器（电抗器）验收分类
  
  ...

  输入:验收分类
  ```

## 最终效果
![result][result]


## TODO
- 使用 flask 将算法封装接口。
- 基于 AntDesign 的清爽前端界面，提供一个算法调用服务接口。
- 数据加载模块：目前语料为手工构造，后期替换批量自动导入。
- 相似度计算模块：目前采用TFIDF进行计算两句子的相似度，后期可替换为 DSSM 语义相似度模型。
- Anwser 排序模块：将粗召回的结果进行排序。
- Query & Anwser 匹配模块：把最终的结果与用户 query 做准确性验证。


<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
[programming]: images/programming.png
[result]: images/result.jpg