import uuid, yaml, json, sys, os, unittest, logging
from k8svimdriver.service.infrastructure import InfrastructureService
from k8svimdriver.toscak8s.translator import ToscaK8sTranslator
from k8svimdriver.k8s.environment import K8sDeploymentLocationTranslator
from tests.unit.testutils.constants import TOSCA_TEMPLATES_PATH, TOSCA_HELLO_WORLD_FILE

logging.basicConfig(level=logging.DEBUG)

tosca_templates_dir = os.path.join(os.path.dirname(__file__), TOSCA_TEMPLATES_PATH)
hello_world_tosca_file = os.path.join(tosca_templates_dir, TOSCA_HELLO_WORLD_FILE)

class TestK8s(unittest.TestCase):

    def test_create(self):
        dl_translator = K8sDeploymentLocationTranslator()
        tosca_translator = ToscaK8sTranslator()

        service = InfrastructureService(dl_translator, tosca_translator)

        inputs = {
            'name': 'helloworld',
            'image': 'accanto/osslm-ansible-rm:1.3.4',
            'container_port': 8080,
            'storage_size': 2,
            'storage_class': 'hostpath',
            'storage_hostpath': '/tmp/a'
        }
        deployment_location = {
            'name': 'default',
            'properties': {
                'k8s-server': 'https://10.220.217.113:6443',
                # 'token': 'ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklpSjkuZXlKcGMzTWlPaUpyZFdKbGNtNWxkR1Z6TDNObGNuWnBZMlZoWTJOdmRXNTBJaXdpYTNWaVpYSnVaWFJsY3k1cGJ5OXpaWEoyYVdObFlXTmpiM1Z1ZEM5dVlXMWxjM0JoWTJVaU9pSmtaV1poZFd4MElpd2lhM1ZpWlhKdVpYUmxjeTVwYnk5elpYSjJhV05sWVdOamIzVnVkQzl6WldOeVpYUXVibUZ0WlNJNkltUmxabUYxYkhRdGRHOXJaVzR0Tm10eFpIWWlMQ0pyZFdKbGNtNWxkR1Z6TG1sdkwzTmxjblpwWTJWaFkyTnZkVzUwTDNObGNuWnBZMlV0WVdOamIzVnVkQzV1WVcxbElqb2laR1ZtWVhWc2RDSXNJbXQxWW1WeWJtVjBaWE11YVc4dmMyVnlkbWxqWldGalkyOTFiblF2YzJWeWRtbGpaUzFoWTJOdmRXNTBMblZwWkNJNkltVTJNREEwWmpFMExUYzNZbVV0TVRGbE9TMWhOR1E0TFRBd05UQTFOamsxTldVd1ppSXNJbk4xWWlJNkluTjVjM1JsYlRwelpYSjJhV05sWVdOamIzVnVkRHBrWldaaGRXeDBPbVJsWm1GMWJIUWlmUS5nNUo4N2NBVzZZZW9uZE15WVNWbDdCbnpWNmJzNnZtdlFKT2E1bEREeE1NbFV1SGJqV3oxYm9EM0dNS2xTVVFyeVMwVVRrUnFpYUhpemlDYmlncXByamMwT1pSLUVtLXFmWU5uQ29oNnl1RnZOYkdMcUVLcEE1bWVQYzl6TWd3WUcxMlNPNE1CQ2pjVGpwUHhSQWs0YzdrM1BOc1hwb1E0eE1EajVpSWNVZVUtWUJrdFo2d3dWRDEwTzlQcDNvUUliaTdwMlBGbzZya2ZuR2pxVG1JVXBpbm1UOTBGLTBkRFNCV19GOWZJd0Q2dGQ5VlZHSzV1Y3F2aDB6Tzk4RXJxeE91NHF3eEM3MW93T2JxNHhWdFlyM2xoUGM0dGx3M0xnRERMR1NodGIyY2daRnBnT3dqNE9nendta3htOVBvVEhURDQ5R0ZDQ2NsZ29hNDV2RHlSSmc=',
                'certificate-authority-data': 'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRFNU1EVXhOakE1TkRFeU1Gb1hEVEk1TURVeE16QTVOREV5TUZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTlpnClorUTNrcFE4bFh4NTJGVzkzVVdXSkJYK0VpMm51UVFqOXJ4anZua1kwSWpMUmp1RUlNMzFrWVlQZmRXd0E5Z3AKR0oxWm50R1hGeEN0aFpuYk1wd0x0UHcyMUh4TkNBQTVlWWdtQmQzYWVXR1VtQmZIczM1WDRmaGhzWC9BbVd4ZQpvU0NWKzJqeVZwOEQzdjkycFpMSENGSTF3N1RNNVcrTHFKUWJGRUtIeldKeGx2d1RzRVR4d1NLeGxMeHVkWlZFCm8zaW5hWmRXL0ZKTVNSNXdSU3pHZnYwMEFHbGNRcXRoaXpXcC9HOGh6aHlaNWdKM1g3STh6SWQzR2tPNnhJNk0KcnUvOTJMZVFEcXJXWEZtWkIyeWxwc2tjRFFsenRBZUpRMnFIU2RsZ0RkM1JoVkdFU0NTUnQ3b3UvZ1VFTjJkRQpMc0EwRy91VVZtMDlXbDFLV2tNQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFIQ2hiZVRYeWg0TC9wTCtlVW5paWZINHhqV1kKMGgyK2xxL1JzS0FSNlFpNDh0MEdiRzI4UDY1LzRjMG0xaUFPUFErWHRydCtmME5VSXN3anoxU01xYzlrVFhHMApNOUV2NlN5eWJrdGttTXhVV3U4SzhTcGdYZkEyMnNzajBHM29mNHh1VldXZTY2Q1RKeXZub3YzbDFrVGU4TUJYClRENGF2WFNuWG5UcVhpeXNucEV3ZlhjZkdha2ZOTllZVjk2T0xTM001V1Z4S2ZYd3F4UzN5Tmtia2Z5dVFwUDEKbExnT09CT254UWJxQW5ORjB3M1g4MHo4cGVXQ2w5Y2VqRUVscVY4NkVUMnNNOWVnTjVkR2pEMmxMQ2NiK3E0bApsbnRYc2h4cGxWWEkvNC80T0JGcGZrcGJXNzlYZXNoR21LSTljZzFvSGFPTEloQlVYWjlCZkRoRUQ2RT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=',
                'client-certificate-data': 'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM4akNDQWRxZ0F3SUJBZ0lJY3dFL0dXZTRSVUV3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB4T1RBMU1UWXdPVFF4TWpCYUZ3MHlNREExTVRVd09UUXhNalphTURReApGekFWQmdOVkJBb1REbk41YzNSbGJUcHRZWE4wWlhKek1Sa3dGd1lEVlFRREV4QnJkV0psY201bGRHVnpMV0ZrCmJXbHVNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXYvbkp3ZnhRUzJJNGdkODAKWGNHNU5FNUVEeC9Ba3VBSzdTSndUSnZkb2pFeTFrL0xLcno2TlNBay9NSDdLcy9XQjhISlpNbDVtS1V2bTJXTApnNHVyNG9ldWdCamVYOGxvanhKV3dhUzVEeTh5ZE9BcWRvV002dWdtZEp0STVUR21KNjIycTR3K1JwbXdKYTlWCkdGTDRKbkIrQUxuMGNPZU9hbm5tVC9iMTFtekhMZHQwYnA0NmVETy9XMm9tUEh1VGVrbmw2dFdGZVRHZ1EwUTkKOTdkZUxhaDJQZXRPNDdLanhuQTZSMmlOZkI5dExVK1d3QUVoTzgzZVg2Q0tKSFBjN3Y2T3pCd2lIL2RpcDdxTApYYkM5cXJlbUs4ZmdteVZxNVV3YXJZQmZxTEx1akEwY25WNWZTazlXR2ovMEo5dk5iem0yL0VUUkE4aFIxMzM2CkNaWkhqUUlEQVFBQm95Y3dKVEFPQmdOVkhROEJBZjhFQkFNQ0JhQXdFd1lEVlIwbEJBd3dDZ1lJS3dZQkJRVUgKQXdJd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFJUFNJU1JVVXBpa0thWFcrYnlLTlNIL1VvcTNjWW1WU0Q3MgpoVlRRNzZ3aU0yU1RzM09sdjRJWUQ1d0dJVkdEcHFIK2loSSt3N3N2azhxemhBQjNTUmhJT2xVQVV0RVA1MndECnI2ZDIzYXZmS0lnbWtGZ2NRYmp6QVhvTzU0VnZaKzhMOWplOEpKWWVGNktBa3l5S0V4a3hmcW9YaEw1RmZLZ2oKeGtMS3BOQmpIR1kzOXY4aElZZ0w0U3dwRkpQYmFQZ3FoVlpZT1owR2NpZzVBWmZSQWVWTUxheGxjN3ZEeGJDQQpISVJubkFVWnZCQ0NwQ3NiVEJId1hkeHZ2RVhIOHVDVWpaRUNOT2JZTmZWalpZamRmZFRFT01BTzNsbVMxaEJ6ClBxMkxxQmhLOEhzMWwrbkc3MTJPd3RHK1NOZDZWdmpTWmpwNTJydEpHQnB4MVJmTTRNUT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=',
                'client-key-data': 'LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb2dJQkFBS0NBUUVBdi9uSndmeFFTMkk0Z2Q4MFhjRzVORTVFRHgvQWt1QUs3U0p3VEp2ZG9qRXkxay9MCktyejZOU0FrL01IN0tzL1dCOEhKWk1sNW1LVXZtMldMZzR1cjRvZXVnQmplWDhsb2p4Sld3YVM1RHk4eWRPQXEKZG9XTTZ1Z21kSnRJNVRHbUo2MjJxNHcrUnBtd0phOVZHRkw0Sm5CK0FMbjBjT2VPYW5ubVQvYjExbXpITGR0MApicDQ2ZURPL1cyb21QSHVUZWtubDZ0V0ZlVEdnUTBROTk3ZGVMYWgyUGV0TzQ3S2p4bkE2UjJpTmZCOXRMVStXCndBRWhPODNlWDZDS0pIUGM3djZPekJ3aUgvZGlwN3FMWGJDOXFyZW1LOGZnbXlWcTVVd2FyWUJmcUxMdWpBMGMKblY1ZlNrOVdHai8wSjl2TmJ6bTIvRVRSQThoUjEzMzZDWlpIalFJREFRQUJBb0lCQUFiWlFHdGROdmdaZnU2VApLZWtXV2ljVmk3UUdhL1pSYTlKZDRpZTVmOFNqZ0s3SWxmVG1YUDY4TU5XYmpmeFBBZEd4QmlCRVY4UXNVSEI0CnhPdGlkalZVcGRNSUVCYld0cFkwRDBoRk9oemlrQ2cvUHdTUGF5R09PcUQ2VVRWcitnTjhYUUh0dE9NTDVJN1QKbkhPTHNqS2MzTUhsNEdTT3ZqUHFPVjhzN2tSQitWMm93KzBpMEovOEQyYXNVeCtLWmw3ZXFnOEZXMEhleTRHRApXV1FyOG9jd3VZMVNpeGs2eDNKSVdVQkpKbVNubHRSZ2ZZMm83Z2FjbFI4a1d4cXpna0Jva3libk9HYWlJbkNvCjBxbldieXBXa29LWXoxWFJGSHlaZ1hKMm9BWkNtS2w5d01qM1dvcjg1TTI5NnpCZEMzcVlNdGJnN2QwTUxWWVUKU29IbEZrRUNnWUVBMXBOU3NxOElROEpWMVoxMTZTVjdwWGY0bW12L3UrMXpmSHhVdUVjZG44VzlZU2pwRjdDUQpyNWFYaWZFT3luQjdwSHFJcUR2R2syRytHQWNEUlY5UXBReTBYV0xlalcxVktxODFVbHhwbUE3aVROeXNKd2thCmdYajBjSGM1Y0tXNVZUVVIwQW5pQy9jSFduSFNSQzVTU0toUUxDczA3cnJTaGpIRDMybi9ib2tDZ1lFQTVRbU0KVGxua200WFZPSCtTWDBSaURCYzZNd0RDdEdOeFY2VG1BYkRrVjhzejdNaFovQmpkL2lUcldxUjhnYzdESi9hRgpCZTZhOGNNQVFYTHpUaEludG5nMU45R29oa0tydkplV21ObTlTc0NuRElqRys2TVVFNEVsdXR2VGVPRDJwckJJCnlxTE12N0F4NDBmR1J0UVFieUxzYzN4V2lXQ2JUM09lY21zVGIrVUNnWUFla2dTeE1tQ3lEcWpkOHo0T1JtblUKVEVCZDk4OEtmaXo2NmxmRG5WWXFJaWoyQTdjWnllMERKeWhWM2NNbXNsbmJPQjNxSWdJTGsxeGEzZnpvVUVrVQpDcmhUcWJkZFhOdEtab1hwUXdORVI3S1VFc2h3RTByMGNVQWFHZEpVS3pnNVhJTTZLWDVNQ0JqREdQNUUrbmg4Cm80WXdsTU5JMDlNVWpWaURwdjFlU1FLQmdIYXpQUmo2TTZWNmRlZkREZXY3dDhqR1hPNUQ3YVNwaVB0QVJjZ0kKa2o4QjNCWlNPM2lRdHJSWkUvUzFIS1gxcjJUTnVXRTZxT2kxQkRQblREdGc0MTRJN0tQU0w4SHRXYTN5N2lTbgpiQmdLd2tpWHRuQ0Jzd3pzdU00ZjBYaHJOc2xxd1Q3cm9xdVJ1RGt2WUk0aXA2WEJkc1BmWThYczRIRUwzY2swCnZ5MFZBb0dBTzZNUmRwU1dkS1dSWUFDUUZMdE80QTMycTFkbDkreHFzWEc4ckg5RDkzUFdQNCtDS3J1bmRsMTcKZks5UHhnYzhROGpoWGRpbWZtbHplT0F1NFFreHdpNlIwSU1xTGVPbUJVYnRXenl2c3ZzcHRCTUFIZW9rZEY3VApPSkZJbzdhUTdYYmo4SFpsSjFjYjhNdnRUU3kvcThpR0ZVbzlKdklPTjR5cEswaUhrNEU9Ci0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0tCg=='
            }
        }

        with open(hello_world_tosca_file, 'r') as tosca_reader:
            tosca_template = tosca_reader.read()

        print(str(service.create_infrastructure(tosca_template, inputs, deployment_location)))


