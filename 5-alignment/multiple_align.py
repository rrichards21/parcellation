import subprocess as sp
import sys
import os
import shutil

if len(sys.argv) < 2:
    print("Usage: python multiple_transform.py ../subjects_dir/")
    sys.exit(1)
clean = input("Clean not aligned files? (y/n): ").capitalize()
subjs_dir = sys.argv[1]
subs = len(os.listdir(subjs_dir))
for sub in os.listdir(subjs_dir):
    print("Aligning subject "+sub)
    sub_dir = subjs_dir+"/"+sub+"/segmented_T1/"
    aligned_out = subjs_dir+"/"+sub+"/aligned_T1"
    sp.call(['python3', 'align_bundles.py', sub_dir, aligned_out])
    
    if clean[0] == 'Y':
        shutil.rmtree(sub_dir)