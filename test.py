# from bs4 import BeautifulSoup
# 'G:\Vscode-python\zw5-jenkins\zw5\zw5_AuthorityDomainServer_publish\config.xml'
#
#
# soup = BeautifulSoup(open('G:\Vscode-python\zw5-jenkins\zw5\zw5_AuthorityDomainServer_publish\config.xml',encoding='UTF-8'),'lxml')
# soup=soup.body
# print(soup)
# command_str = soup.project.builders.execcommand.string
# print(command_str)
# for child in soup.children:#遍历子节点，并存在List中，用来排序
#
#     print(child)
a = {'a': 1}
b = a.keys()
print(list(b))
