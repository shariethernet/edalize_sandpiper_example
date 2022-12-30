from edalize import *
import os
work_root = 'build_tlv5'

files = [
    {'name':os.path.relpath('1_adder.tlv',work_root),'file_type':'TLverilogSource'}
]

tool_options = {
		"sandpipersaas": {
			"sandpiper_saas": [
				"--bestsv"
			],
            "output_file":"1_adder_rtl.sv",
            "output_dir":"out1"
		}
	}
tool = 'sandpipersaas'
parameters = {}
edam = {
    'files':files,
    'name':'build_tlv1',
    'parameters':parameters,
    'tool_options':tool_options
}

backend = get_edatool(tool)(edam=edam, work_root=work_root)

os.makedirs(work_root)
backend.configure()
backend.build()
backend.run()
