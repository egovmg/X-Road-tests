# coding=utf-8
import unittest

from helpers import xroad
from main.maincontroller import MainController
from tests.xroad_configure_service_222 import configure_edit_wsdl


class XroadEditAddressWSDL(unittest.TestCase):
    """
    SERVICE_09 Edit the Address of a WSDL
    RIA URL: https://jira.ria.ee/browse/XT-266, https://jira.ria.ee/browse/XTKB-23
    Depends on finishing other test(s):
    Requires helper scenarios:
    X-Road version: 6.16.0
    """
    def __init__(self, methodName='test_xroad_configure_service'):
        unittest.TestCase.__init__(self, methodName)

    def test_xroad_configure_service(self):
        main = MainController(self)

        # Set test name and number
        main.test_number = 'SERVICE_08'
        main.test_name = self.__class__.__name__

        ss_host = main.config.get('ss2.host')
        ss_user = main.config.get('ss2.user')
        ss_pass = main.config.get('ss2.pass')

        client = xroad.split_xroad_id(main.config.get('ss2.client_id'))
        requester = xroad.split_xroad_id(main.config.get('ss1.client_id'))

        wsdl_url = main.config.get('wsdl.remote_path').format(main.config.get('wsdl.service_wsdl'))

        service_name = main.config.get('services.test_service')  # xroadGetRandom
        service_url = main.config.get('services.test_service_url')
        service_2_name = main.config.get('services.test_service_2')  # bodyMassIndex
        service_2_url = main.config.get('services.test_service_2_url')


        # Configure the service
        test_configure_service = configure_edit_wsdl.test_configure_service(case=main, client=client,
                                                                                check_add_errors=True,
                                                                                check_edit_errors=True,
                                                                                check_parameter_errors=True,
                                                                                service_name=service_name,
                                                                                service_url=service_url,
                                                                                service_2_name=service_2_name,
                                                                                service_2_url=service_2_url, wsdl_url=wsdl_url)




        try:
            # Open webdriver
            main.reload_webdriver(url=ss_host, username=ss_user, password=ss_pass)

            # Add WSDL and configure service
            test_configure_service()

        except:

            main.log('XroadConfigureService: Failed to configure service')

            main.save_exception_data()

        finally:


            main.save_exception_data()

            # Test teardown

            main.tearDown()
