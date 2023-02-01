#!/usr/bin/env python3 

import os
import argparse 

def convert_to_vtk_42(in_vtk, out_vtk, in_dir, help=False, codes="/code") : 
    """
    Convert VTK DataFile 5.1 to 4.2

    Parameters: 
    --in-vtk  : Input
    --out-vtk : Output

    """

    if(help) : 
        print(convert_to_vtk_42.__doc__)
        return ""

    cmd  = "python3 -u "
    cmd += codes+"/convertvtk42.py" + " "

    cmd += in_dir + "/" + in_vtk + " "
    cmd += in_dir + "/" + out_vtk

    return cmd 

if __name__ == '__main__' : 
    input_parser = argparse.ArgumentParser(prog="docker run --rm --volume=/path/to/data:/data cemrg/vtk_to_42",
                                            description="CEMRG: Convert VTK legacy 5.1 to 4.2", 
                                            usage="%(prog)s [single|multiple]", 
                                            epilog="$ docker run --rm --volume=/path/to/data:/data cemrg/vtk_to_42 MODE help\n# for pecific help about MODE")
    input_parser.add_argument("operation", 
                              metavar="mode_of_operation", 
                              choices=["single", "multiple"],
                              type=str, help="Modes of operation [single|multiple]") 

    input_parser.add_argument("help", nargs='?', type=bool, default=False, help="Help page to each mode")

    input_parser.add_argument("--input-vtk", metavar="input.vtk", nargs='?', type=str)
    input_parser.add_argument("--output-vtk", metavar="output.vtk", nargs='?', type=str)

    input_parser.add_argument("--dev-base-dir", metavar="dir", nargs='?', default="/data", type=str, help="[Only DEVs] Data Path")
    input_parser.add_argument("--dev-code-dir", metavar="dir", nargs='?', default='/code', type=str, help="[Only DEVs] Code path")
    
    input_parser.add_argument("--debug", action='store_true', help="Debug only shows the command running")

    args = input_parser.parse_args()

    mode=args.operation
    myhelp=args.help 

    input_vtk=args.input_vtk 
    output_vtk=args.output_vtk

    base_dir=args.dev_base_dir 
    codes_d=args.dev_code_dir
    local=args.dev_run_local 
    debug=args.debug

    base_dir += os.sep if(base_dir[-1] is not os.sep) else "" 

    if (mode == "single") : 
        cmd = convert_to_vtk_42(input_vtk, output_vtk, base_dir, help=myhelp, codes=codes_d)

    elif (mode == "multiple") :
        if (myhelp) : 
            cmd = "" 
        else :
            new_cmd = "$HOME/.cargo/bin/rg --files-with-matches 'DataFile Version 5.1' {} > {}files.txt".format(base_dir, base_dir) 
            cmd_ret = os.system(new_cmd)
            if (cmd_ret == 0) : 
                with open(base_dir+"files.txt") as f: 
                    lines = [line.rstrip('\n') for line in f] 
                    cmd = [convert_to_vtk_42(fname, fname, base_dir, codes=codes_d) for fname in lines]

            else : 
                cmd = ""

    if (type(cmd) is list or (type(cmd) is str and cmd != "") ) : 

        ppth = "" if (local) else "/opt/conda/envs/vtk910/bin/"
        cmd = ppth + cmd 
        
        print("[INFO] Correct input. Command in container: \n {}".format(cmd))
        
        if (not debug) : 
            print('Running...')
            cmd = [cmd] if type(cmd) is str else cmd 
            for command in cmd : 
                os.system(command) 
                
