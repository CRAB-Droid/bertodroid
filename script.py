import os
import sys

output_txt = None

def valid_args(argc, argv):
    global output_txt 

    if argc != 5:
        return False
    if argv[1] != "-i" or argv[3] != "-o":
        return False

    output_txt = open(argv[4], "w")
    output_txt.close() # clear the file
    output_txt = open(argv[4], "a")
    return argv[2]


def analyze_manifest(manifest):
    package = None
    manifest_file = open(manifest, "r")
    for line in manifest_file:
        if "package" in line:
            start_idx = line.find("package=\"") + len("package=\"")
            end_idx = line.find("\"", start_idx)
            package = line[start_idx:end_idx]
    manifest_file.close()
    return package


def analyze_smali(path): 
    print("Path:", path)


def main():
    input_apk = valid_args(len(sys.argv), sys.argv)
    if not input_apk:
        print("Usage: python script.py -i target-app.apk -o output.txt")
        return

    # os.system("apktool d " + input_apk)

    folder = input_apk[:-4] + "/"
    print("Folder:", folder)
    manifest = folder + "AndroidManifest.xml"
    print("Manifest:", manifest)

    package = analyze_manifest(manifest)

    if not package:
        print("Package not found. Aborting...")
        return

    print("Package:", package)
    smali = folder + "smali/" + package.replace(".", "/") + "/"
    print("Smali:", smali)


    for root, dirs, files in os.walk(smali):
        for file in files:
            if file.endswith(".smali"):
                analyze_smali(os.path.join(root, file))


if __name__ == "__main__":
    main()