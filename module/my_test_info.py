from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=True),
    )

    result = dict(
        changed=True,
        original_message='',
        message='',
        my_useful_info={},
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

 #   if module.check_mode:
 #       module.exit_json(**result)

    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'
    result['my_useful_info'] = {
        'foo': 'bar',
        'answer': 42,
    }

    f= open("/tmp/data.txt","w")
    f.write("{}".format(module.params['name']))
    module.exit_json(output=result,data=result,msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()