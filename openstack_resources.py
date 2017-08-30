from openstack import connection
from openstack import profile

def create_cloud_conn():
    prof = profile.Profile()
    prof.set_region(profile.Profile.ALL, "nova")

    domain_name = "default"
    if domain_name == '':
        # Empty domain is useless, but may cause problems if v2.0 is used
        domain_name = None

    return connection.Connection(
        profile=prof,
        auth_url="www.openstack.com:5000/v3",
        username="autouser",
        password="WvU",
        project_id="24dd47df604b44bd8bbd7ce0fb2b6cc3",
        verify=False,
        user_domain_name=domain_name,
        project_domain_name=domain_name,
    )


conn = create_cloud_conn()
conn.authorize()

def get_networks():
    networks = conn.network.networks()
    for net in networks:
        print net, net.is_router_external


def get_subnets():
    subnets = conn.network.subnets()
    for sub in subnets:
        print sub

def get_security_groups():
    security_groups = conn.network.security_groups()
    for sc in security_groups:
        print sc


def get_images():
    images = conn.image.images(project_id="24dd47df604b44bd8bbd7ce0fb2b6cc3")
    for image in images:
        print image.name


def get_flavors():
    flavors = conn.compute.flavors()
    for flavor in flavors:
        print flavor

get_images()
