import os
import codecs
import  re



class Configuration(object):
    def __init__(self):
        self.config_list = []

    def search(self, root, target):
        """找到目录下的config.xml文件
            return 路径列表
        """
        items = os.listdir(root)
        for item in items:
            path = os.path.join(root, item)
            if os.path.isdir(path):
                self.search(path, target)
            elif path.split('\\')[-1] == target:
                path = eval(repr(path).replace('\\', '/')).replace('//','/')
                print(type(path),path)
                self.config_list.append(path)
            else:
                continue
        return self.config_list
    
    def extractConfiguration(self, configPath):
        """提取配置文件内容函数 
        configPaht: 提供配置文件的路径
        return 返回字典 key路径，val是提取的字典{command OR env:val}
        """
        result = {}
        with codecs.open(configPath, 'r',encoding='utf-8') as f:
            jk_Conf = f.read()
            #关键字<execCommand> 提取启动命令
            c1 = '<execCommand>'
            c2 = '</execCommand>'
            command_pat = re. compile (c1 + '(.*?)' + c2,re.S)
            command_result = ":".join(command_pat.findall(jk_Conf))
            result.update({"command":command_result})

            #关键字<envVariableString> 提取变量
            e1 = '<envVariableString>'
            e2 = '</envVariableString>'
            env_pat = re. compile (e1 + '(.*?)' + e2,re.S)
            env_result = ":".join(env_pat.findall(jk_Conf))
            result.update({"env":env_result})

        # 返回字典 key路径，val是提取的值
        return {configPath:result}

    def replaceConfiguration(self, tagConfigPath, source_val, tag_val):
        """替换函数
        tagConfigPath：目标config.xml路径
        source_val： 源文件值
        tag_val：目标值
        """
        configFile = open(tagConfigPath, 'r+',encoding='utf-8')
        configFile_text = configFile.read()
        # 先把变量用冒号替换成一行
        """</envVariableString>
    </org.jenkinsci.plugins.envpropagator.EnvPropagatorBuilder>
    <org.jenkinsci.plugins.envpropagator.EnvPropagatorBuilder plugin="build-env-propagator@1.0">
      <envVariableString>"""
        replaceEnvXml = """</envVariableString>
    </org.jenkinsci.plugins.envpropagator.EnvPropagatorBuilder>
    <org.jenkinsci.plugins.envpropagator.EnvPropagatorBuilder plugin="build-env-propagator@1.0">
      <envVariableString>"""
        configFile_text = re.sub(replaceEnvXml, ":", configFile_text)

        print(tag_val, source_val, configFile_text)
        configFile_text = re.sub(tag_val, source_val, configFile_text)

        configFile.seek(0)
        configFile.write(configFile_text)
        configFile.close()



cf = Configuration()
source_config_res = cf.search("./zw5-jenkins/feature",'config.xml')
# print(config_res)
for source_config in source_config_res:
    source_res = cf.extractConfiguration(source_config)
    # print(source_res)

    for config_source_path in source_res:
        tag_config_path = re.sub('feature', 'zw5', config_source_path)
        tag_res =  cf.extractConfiguration(tag_config_path)
        # print(tag_res)

    #     # 调用替换函数
        source_command_val = source_res[source_config]["command"]
        source_env_val = source_res[source_config]["env"]
        tag_command_val = tag_res[tag_config_path]["command"]
        tag_env_val = tag_res[tag_config_path]["env"]
        cf.replaceConfiguration(tag_config_path, source_val=source_env_val, tag_val=tag_env_val)

# extractConfiguration(config_list)