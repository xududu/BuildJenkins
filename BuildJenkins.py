import jenkins
import getopt
import sys

'''buildJenkins的脚本，
启动命令：python BuildJenkins.py -g <group> -i <images:version>
可选参数：-g 可选参数：单个group，zs=正式，all=所有组
        -i 可选参数： 一个或多个镜像和版本号的字典，某个model=domain,subs,....，all=所有镜像
'''
server = jenkins.Jenkins('http://192.168.0.202:48080/', username='admin', password='admin')
ZS_Group_list = ['dongbei', 'shandong', 'zw4', 'zw5']
model_list = ['all', 'subs', 'webapi', 'domain', 'dc', 'sync', 'website']
jk_view_name = 'stable'
# 镜像和Jenkins项目名对应关系的字典,key:镜像名，value:job_name
imgCorrespondenceJK = {'aicard': 'stable_aicard_website',
                                'authoritydomainserver': 'stable_AuthorityDomainServer_domain',
                                'syncauthorityserver': 'stable_authority_sync', 'hexbeike': 'stable_beike_website',
                                'bianji': 'stable_bianji_website',
                                'buryingpointdomainserver': 'stable_buryingpoint_domain',
                                'buryingpointwebapiserver': 'stable_buryingpoint_webapi',
                                'classnumberserver': 'stable_classnumberserver_domain',
                                'classroomrecorddomainserver': 'stable_classroomrecord_domain',
                                'classroomrecordwebapiserver': 'stable_classroomrecord_webapi',
                                'cmswebapiserver': 'stable_cmswebapiserver_webapi',
                                'coursedomainserver': 'stable_course_domain',
                                'coursesubsreport': 'stable_coursesubsreport_subs',
                                'courseware2': 'stable_courseware2_website',
                                'coursewaredomainserver': 'stable_courseware_domain',
                                'coursewaresubsserver': 'stable_courseware_subs',
                                'coursewarewebapiserver': 'stable_courseware_webapi',
                                'courseware': 'stable_courseware_website', 'coursewebapiserver': 'stable_course_webapi',
                                'datacollectionwebapiserver': 'stable_datacollection_webapi',
                                'dccoursereceiveserver': 'stable_DCCourseReceiveServer_dc',
                                'dccoursesendserver': 'stable_DCCourseSendServer_dc',
                                'dccoursewarereceiveserver': 'stable_DCCoursewareReceiveServer_dc',
                                'dccoursewaresendserver': 'stable_DCCoursewareSendServer_dc',
                                'dcebookreceiveserver': 'stable_DCEbookReceiveServer_dc',
                                'dcebooksendserver': 'stable_DCEbookSendServer_dc',
                                'dcexercisereceiveserver': 'stable_DCExerciseReceiveServer_dc',
                                'dcexercisesendserver': 'stable_DCExerciseSendServer_dc',
                                'dclicensereceiveserver': 'stable_DCLicenseReceiveServer_dc',
                                'dclicensesendserver': 'stable_DCLicenseSendServer_dc',
                                'dcuserreceiveserver': 'stable_DCUserReceiveServer_dc',
                                'dcusersendserver': 'stable_DCUserSendServer_dc',
                                'dohtesubsreportserver': 'stable_dohtesubsreport_subs',
                                'ebookdomainserver': 'stable_ebook_domain', 'ebookwebapiserver': 'stable_ebook_webapi',
                                'enotesubshexcubeserver': 'stable_enotesubshexcube_subs',
                                'exercisedomainserver': 'stable_exercise_domain',
                                'exercisesubexercisebook': 'stable_exercisesubexercisebook_subs',
                                'exercisesubredis': 'stable_exercisesubredis_subs',
                                'exercisesubsreportkeypointserver': 'stable_exercisesubsreportkeypoint_subs',
                                'exercisesubusecount': 'stable_exercisesubusecount_subs',
                                'exercisev2': 'stable_exercisev2_website',
                                'exercisewebapiserver': 'stable_exercise_webapi', 'hexpaper': 'stable_exercise_website',
                                'hexburyingpoint': 'stable_hexburyingpoint_website',
                                'hexcuberedisservicetodb': 'stable_HexCubeRedisServiceToDB_subs',
                                'hexoffice': 'stable_hexoffice_website',
                                'hexresource': 'stable_hexresource_website', 'hexschool': 'stable_hexschool_website',
                                'hexstatistics': 'stable_hexstatistics_website',
                                'hteclassstatisticssubserver': 'stable_hteclassstatisticssubserver_subs',
                                'htedomainserver': 'stable_hte_domain',
                                'hteonlysubsreportserver': 'stable_hteonlysubsreport_subs',
                                'htepapersub21exerciserelation': 'stable_htepapersub21exerciserelation_subs',
                                'htepapersub21exercise': 'stable_htepapersub21exercise_subs',
                                'htepapersubhte': 'stable_htepapersubhte_subs',
                                'htepapersubredis': 'stable_htepapersubredis_subs',
                                'htepapertimersubredis': 'stable_HTEPaperSubTimerRedis_subs',
                                'htestatic': 'stable_htestatic_website',
                                'htesub21centerexercise': 'stable_htesub21centerexercise_subs',
                                'htesub21exerciserelation': 'stable_htesub21exerciserelation_subs',
                                'htesub21exercise': 'stable_htesub21exercise_subs',
                                'htesubintowrongnote': 'stable_htesubintowrongnote_subs',
                                'htesubsreportserver': 'stable_htesubsreport_subs',
                                'htewebapiserver': 'stable_htewebapiserver_webapi',
                                'imdomainserver': 'stable_im_domain', 'syncimserver': 'stable_im_sync',
                                'imwebapiserver': 'stable_im_webapi', 'hexinclass': 'stable_inclass_website',
                                'inithtesubscribeserver': 'stable_inithtesubscribeserve_subs',
                                'intowrongnote': 'stable_intowrongnote_subs', 'jiaowu': 'stable_jiaowu_website',
                                'jidi': 'stable_jidi_website', 'lessondomainserver': 'stable_lesson_domain',
                                'lessonwebapiserver': 'stable_lesson_webapi',
                                'licensedomainserver': 'stable_license_domain',
                                'licensewebapiserver': 'stable_license_webapi',
                                'miscwebapiserver': 'stable_misc_webapi',
                                'mobileexercise': 'stable_mobileexercise_website',
                                'mvcwebapiserver': 'stable_mvc_webapi',
                                'oauthwebapiserver': 'stable_oauthwebapiserver_webapi',
                                'onetoonedomainserver': 'stable_onetoone_domain',
                                'onetoonesubschatrecordserver': 'stable_onetoonesubschatrecord_subs',
                                'onetoonesubscourseserver': 'stable_onetoonesubscourse_subs',
                                'onetoonetimerserver': 'stable_OneToOneTimerServer_subs',
                                'onetoonewebapiserver': 'stable_onetoone_webapi',
                                'powerdomainserver': 'stable_power_domain', 'powerwebapiserver': 'stable_power_webapi',
                                'productsubresource': 'stable_productsubresource_subs',
                                'qrlogin': 'stable_qrlogin_website', 'reportdomainserver': 'stable_report_domain',
                                'reporthtestatisticsserver': 'stable_ReportHTEStatisticsServer_subs',
                                'reportkeypointdomainserver': 'stable_reportkeypointdomainserver_domain',
                                'reportsubspushserver': 'stable_reportsubspush_subs',
                                'reportwebapiserver': 'stable_report_webapi',
                                'rmswebapiserver': 'stable_rmswebapiserver_webapi',
                                'sharehtesub': 'stable_sharehtesub_subs',
                                'solrralationdomainserver': 'stable_solrralation_domain',
                                'solrsubsaexercisenoteserver': 'stable_solrsubsaexercisenote_subs',
                                'solrsubsexerciseserver': 'stable_solrsubsexercise_subs',
                                'solrsubsexercisetimerserver': 'stable_solrsubsexercisetimerserver_subs',
                                'solrsubsonetooneserver': 'stable_solrsubsonetoone_subs',
                                'solrsubsremoveenoteserver': 'stable_solrsubsremoveenote_subs',
                                'solrsubswexercisenoteserver': 'stable_SolrSubsWExerciseNoteServer_subs',
                                'statistics': 'stable_statistics_website',
                                'synccourseserver': 'stable_SyncCourseServer_sync',
                                'synccoursewareserver': 'stable_SyncCoursewareServer_sync',
                                'syncebookserver': 'stable_SyncEbookServer_sync',
                                'syncexerciseserver': 'stable_SyncExerciseServer_sync',
                                'synchteserver': 'stable_SyncHTEServer_sync',
                                'synclicenseserver': 'stable_SyncLicenseServer_sync',
                                'synconetooneserver': 'stable_SyncOneToOneServer_sync',
                                'syncpowerserver': 'stable_syncPowerServer_sync',
                                'syncwenoteserver': 'stable_SyncWENoteServer_sync',
                                'typesetserver2': 'stable_typesetserver2_website',
                                'typesetserver': 'stable_typesetserver_website',
                                'userdomainserver': 'stable_user_domain',
                                'userdomainsubhte': 'stable_userdomainsubhte_subs',
                                'userwebapiserver': 'stable_user_webapi',
                                'varexercisedomainserver': 'stable_varexercise_domain',
                                'warehousereportdomainserver': 'stable_warehousereport_domain',
                                'warehousereportwebapiserver': 'stable_warehousereport_webapi',
                                'wrongexercisenotedomainserver': 'stable_wrongexercisenote_domain',
                                'wrongexercisenotewebapiserver': 'stable_wrongexercisenote_webapi'}


# buildJenkins调用的函数
def build_job_obj(b_group, b_img=None, img_v=None, all_img_obj=None):
    """
    build项目调用的函数
    :param b_group: 传入需要build到的组名
    :param b_img: 插入需要build的镜像名或者一个列表，如果
    :param img_v: 传入镜像版本号
    :param all_img_obj: 如果需要build所有镜像，应该把包含所有jobs的对象列表传给此参数
    :return:
    """
    if b_group == 'zs':
        group_list = ZS_Group_list
    elif b_group == 'all':
        ZS_Group_list.append('center')
        group_list = ZS_Group_list
    elif b_group in ZS_Group_list or b_group == 'center':
        group_list = b_group.split()
    else:
        print('Group Name ERROR!!!!!')
        raise IndexError
    # 如果要build所有镜像会执行此部分
    if all_img_obj:
        for job in all_img_obj:
            # 判断job的名字是否包含要启动的任务
            if job['color'] == 'disabled':
                continue
            if b_img == 'all':
                for group in group_list:
                    server.build_job(job['name'], parameters={'ms_group': group})
            # 如果只build某些model
            elif '_' + b_img in job['name']:
                for group in group_list:
                    server.build_job(job['name'], parameters={'ms_group': group})
            else:
                print('Model Name ERROR!!!!!')
                raise IndexError
        return
    else:
        # 只build一个镜像时
        job_name = imgCorrespondenceJK[b_img]
        for group in group_list:
            server.build_job(job_name, parameters={"image_tag": img_v, 'ms_group': group})
        return


def str_dict_handle(img_str: str):
    """
    字符串处理成字典
    :param img_str: {classnumberserver:1.1.1,oauthwebapiserver:1.1.2}
    :return:  {'classnumberserver': '1.1.1', 'oauthwebapiserver': '1.1.2'}--- type=dict
    """
    res_dic = {}
    han_str = img_str.strip('{}')
    han_list = han_str.split(',')
    for imgAdnVersion in han_list:
        img_name = imgAdnVersion.split(':')[0]
        img_version = imgAdnVersion.split(':')[1]
        res_dic[img_name] = img_version
    return res_dic


def main(argv):
    """
    调用的入口函数
    支持的参数： -g 组名：ms_group
                -i 镜像名：{"sharehtesub":"1.1.0"}
    :param argv:
    :return:
    """
    ms_group = ''
    img_version = ''

    try:
        opts, args = getopt.getopt(argv, "g:i:", ["ms_group", "img_version"])
    except getopt.GetoptError:
        print('BuildJenkins.py -g <ms_group> -i <img_version>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('BuildJenkins.py -g <ms_group> -i <img_version>')
            sys.exit()
        elif opt in ("-g", "--ms_group"):
            ms_group = arg
        elif opt in ("-i", "--img_version"):
            img_version = arg

    # 如果想build所有镜像执行此部分
    if img_version in model_list:
        all_jobs_name_obj = server.get_jobs(view_name=jk_view_name)
        build_job_obj(b_group=ms_group, b_img=img_version, all_img_obj=all_jobs_name_obj)
    else:
        # 如果只build某些镜像执行次部分
        img_version_dict = str_dict_handle(img_version)
        for img in img_version_dict:
            version = img_version_dict[img]
            build_job_obj(b_group=ms_group, b_img=img, img_v=version)


if __name__ == "__main__":
    main(sys.argv[1:])
