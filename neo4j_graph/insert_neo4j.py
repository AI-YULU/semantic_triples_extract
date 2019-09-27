from neo4j import GraphDatabase
import json

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "Nic180319"))

def add_node(tx, name1, relation,name2):

    tx.run("MERGE (a:Node {name: $name1}) "
        "MERGE (b:Node {name: $name2}) "
           "MERGE (a)-[:"+relation+"]-> (b)",
           name1=name1,name2=name2)



with driver.session() as session:
    lines=open('../data/knowledge_triple.json','r',encoding='utf-8').readlines()
    print(len(lines))
    pattern=''
    for i,line in enumerate(lines):
        line = json.loads(line)
        arrays=line['知识']
        name1=arrays[0]
        relation=arrays[1].replace('：','').replace(':','').replace('　','').replace(' ','').replace('【','').replace('】','')
        name2=arrays[2]
        print(str(i))
        try:
            session.write_transaction(add_node,name1, relation,name2)
        except Exception as e:
            print( name1, relation,name2,str(e))
