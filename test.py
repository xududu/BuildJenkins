import jenkins

server = jenkins.Jenkins('http://192.168.0.202:48080/', username='admin', password='admin')
# jobs = server.get_jobs(view_name='modle')

job_info = server.get_job_info('model_DC_send')
server.get_queue_info()
# print(server.get_queue_info())
aa = 'sdf'
bb = 'asdf'
print('sfs %s %s' % (aa, bb))
# print(job_info)
# 获取下一个构建编号：
# build_number = server.get_job_info('stable_DCCourseSendServer_dc')['nextBuildNumber']
# 开始构建
''''''

# 获取构建信息：
# build_info = server.get_build_info('stable_DCCourseSendServer_dc', 47)
# 获取构建状态：
# print(build_info)
# is_building = build_info['building'] # True是正在构建—>如果这个值存在，则说明在构建，如果不存在则说明已经构建完成了，通过build_info[“result”]获取构建成功还是构建失败！
# print(is_building)

# 获取下级项目是否构建成功
# job_info = server.get_job_info('stable_DCCourseSendServer_dc')
# print(job_info['downstreamProjects'][0]['color']) #状态
# print(job_info['downstreamProjects'][0]['name'])  #名字

# 最后一次构建是否成功
# build_info = server.get_build_info('model_DC_receive', 266)
# print(build_info['result'])
# print(build_info.build_info['building'])
# print(jobs)
