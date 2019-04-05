from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint
from pathlib import Path

class Configuration(object):

    NODE_ID = '0xf6140a03926b0801cd891d2d128ebd8dffbda252'

def test_docker():
    d = gu_rest_api.Driver()

    with d.session(name="test", tags=[]) as session:

        print("peers=", d.peers)
        print("session id=", session.id)
        print("session info=", session.info)

        peer_session_spec = gu_rest_api.DeploymentSpec(env_type='docker',
            image=gu_rest_api.DeploymentSpecImage(hash='sha256:644fcb1a676b5165371437feaa922943aaf7afcfa8bfee4472f6860aad1ef2a0',
            url='alpine'),
            name='docker test', tags=['test'], options=gu_rest_api.DockerCreateOptions(volumes=[]))

        peer = session.peer(Configuration.NODE_ID)
        print("peer=", peer.info)

        gu_test = peer.new_deployment(peer_session_spec)
        
        print("deployment=", gu_test.info)

        print("r=", gu_test.begin().do_open().do_exec('find', '/').do_close().send())



if __name__ == '__main__':
    test_docker()

