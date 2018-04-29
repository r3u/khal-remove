import subprocess


def run_sox(*arguments):
    p = subprocess.run(["sox"] + list(arguments),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.decode()
    err = p.stderr.decode()
    if p.returncode != 0:
        raise Exception("Processing failed: {0}".format(err))

def process(infile, out_prefix):
    run_sox(infile, out_prefix + "_L_fwd.wav", "remix", "1")
    run_sox(infile, out_prefix + "_R_fwd.wav", "remix", "2")
    run_sox(out_prefix + "_L_fwd.wav", out_prefix + "_L_rev.wav", "reverse")
    run_sox(out_prefix + "_R_fwd.wav", out_prefix + "_R_rev.wav", "reverse")


process("hunter.mp3", "test")
