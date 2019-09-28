# semantic_triples_extract
在非结构化文本中提取三元组
依赖于jieba分词，哈工大自然语言处理工具ltp
需要下载ltp模型文件放到./model文件夹里面
http://ltp.ai/download.html  选择 ltp_data_v3.4.0.zip

1.	将需要提取的句子放入input_text.txt文件中
2.	运行extract_demo.py
3.	将input_text.txt中句子提取出的三元组输出到knowledge_triple.json中
4.  insert_to_neo4j.py 将三元组存入知识库



