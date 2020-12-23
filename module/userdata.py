import json
from ansible.module_utils.basic import  AnsibleModule
import sys

def main():
    module=AnsibleModule(
        argument_spec=dict(
            name= dict(required=True, type='str'),
            code=dict(required=True, type='int')
        )
    )

    name=module.params['name']
    code=module.params['code']

    data=dict(output='Data has been stored by module')
    try:
        file=open("/tmp/userdata.txt","w")
        file.write("Name: {}, Code: {}".format(name,code))
        module.exit_json(changed=True,success=data,msg=data)
    except Exception as e:
        module.fail_json(msg="Some error occured")


if __name__ == "__main__":
    main()