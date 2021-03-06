# -*- coding: utf-8 -*-
from QAutoLibrary.extension import TESTDATA
import os
from selenium.webdriver.common.by import By
from QAutoLibrary.QAutoSelenium import *
from time import sleep
from common_lib import Common_lib
from pagemodel.cs_time_stamping_services_add_dlg import Cs_time_stamping_services_add_dlg
from pagemodel.cs_time_stamping_services import Cs_time_stamping_services


class Component_cs_tsp_services(CommonUtils):
    """
    Components common to central server timestamping services view

    Changelog:

    * 11.07.2017
        | Documentation updated
    """
    common_lib = Common_lib()
    cs_time_stamping_services_add_dlg = Cs_time_stamping_services_add_dlg()
    cs_time_stamping_services = Cs_time_stamping_services()

    def upload_tsa_certificate(self, section1=u'paths', section2=u'cs_url'):
        """
        Upload tsa certificate

        :param section1:  Test data section name
        :param section2:  Test data section name
        """
        sleep(2)
        type_string = os.path.join(os.getcwd(),
                                   TESTDATA[section1][u'data_folder'],
                                   TESTDATA[section2][u'tsa_cert_file_name'])
        print(type_string)
        self.common_lib.type_file_name_pyautogui(type_string)
        print("done upload")
        sleep(2)

    def add_timestamping_service_to_cs(self, section1=u'paths', section2=u'cs_url'):
        """
        Add timestamping service to central server

        :param section1:  Test data section name
        :param section2:  Test data section name
        """
        self.cs_time_stamping_services.click_button_id_tsp_add()
        self.cs_time_stamping_services_add_dlg.input_text_to_id_tsp_url(TESTDATA[section2])
        self.cs_time_stamping_services_add_dlg.click_button_upload()
        self.upload_tsa_certificate(section1, section2)
        self.cs_time_stamping_services_add_dlg.click_button_ok()
        sleep(3)