# import hanlp
from hanlp_restful import HanLPClient

# HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH)
HanLP = HanLPClient('https://www.hanlp.com/api', auth='MTczNEBiYnMuaGFubHAuY29tOm9Xb3JpR094cWV0ZEZ5Rzg=', language='zh')

# extracting text from file
# with open('./data/news_test.txt', encoding='UTF-8') as f:
#     s = f.read()

# doc = HanLP(s, tasks='srl')
doc = HanLP('2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。', tasks='srl')

doc.pretty_print()

for i, pas in enumerate(doc['srl'][0]):
    print(f'第{i+1}个谓词论元结构：')
    for form, role, begin, end in pas:
        print(f'{form} = {role} at [{begin}, {end}]')

HanLP(tokens=[
    ["HanLP", "为", "生产", "环境", "带来", "次世代", "最", "先进", "的", "多语种", "NLP", "技术", "。"],
    ["我", "的", "希望", "是", "希望", "张晚霞", "的", "背影", "被", "晚霞", "映红", "。"]
  ], tasks='srl', skip_tasks='tok*').pretty_print()

print(doc)
