#!/usr/bin/env python

import os
import shutil
import subprocess
import glob
import argparse
import codecs

def get_curr_path():
    return os.path.dirname(os.path.realpath(__file__))


def which(program):
    def is_exe(cmd_path):
        return os.path.exists(cmd_path) and os.access(cmd_path, os.X_OK)

    def ext_candidates(cmd_path):
        yield cmd_path
        for ext in os.environ.get("PATHEXT", "").split(os.pathsep):
            yield cmd_path + ext

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            for candidate in ext_candidates(exe_file):
                if is_exe(candidate):
                    return candidate

    return None


def copy_all(src, dst):
    for filename in glob.glob(os.path.join(src, '*.*')):
        shutil.copy(filename, dst)


def copy_tree(src, dst):
    if os.path.isdir(src):
        from distutils.dir_util import copy_tree
        copy_tree(src, dst)
        # shutil.copytree(src, dst)
    elif os.path.exists(src):
        shutil.copy(src, dst)


def del_tree(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.remove(path)
    else:
        print 'Invalid path: ' + path

#recursively merge two folders including subfolders
def merge_tree(root_src_dir, root_dst_dir):
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                print 'remove:' + dst_file
                os.remove(dst_file)
            shutil.copy(src_file, dst_dir)

def update_version(file_path, version_num):
    fh = open(file_path, 'r')
    html_content = fh.read()

    from string import Template
    s = Template(html_content)
    replaced_content = s.substitute(sxr_version=version_num)

    fh = open(file_path, 'w')
    fh.write(replaced_content)
    fh.close()


def gen_javadoc(src_path, out_path, package_name):
    cmd = ['javadoc', '-Xdoclint:none']
    cmd.extend(['-d', out_path])
    cmd.extend(['-sourcepath', src_path])
    cmd.extend(['-subpackages', package_name])
    cmd.extend(['-encoding', 'UTF-8'])
    cmd.extend(['-charset', 'UTF-8'])
    cmd.append('-quiet')
    subprocess.call(cmd)


def update_template(out_path, version_num):
    curr_path = get_curr_path()
    full_out_path = os.path.join(curr_path, out_path)
    version_out_path = os.path.join(full_out_path, version_num)

    index2_path = os.path.join(full_out_path, 'index2.html')
    update_version(index2_path, version_num)

    java_doc_index_path = os.path.join(version_out_path, 'index.html')
    update_version(java_doc_index_path, version_num)


def gen_java_docs(base_path, out_path):
    del_tree(out_path)

    # Generate frameworks
    sub_out_path = os.path.join(out_path, 'Framework')
    src_path = os.path.join(base_path, 'SXR', 'SDK', 'sxrsdk', 'src', 'main', 'java')
    gen_javadoc(src_path, sub_out_path, 'com.samsungxr')

    # Generate DebugWebServer
    sub_out_path = os.path.join(out_path, 'DebugWebServer')
    src_path = os.path.join(base_path, 'SXR', 'Extensions', 'DebugWebServer', 'debugwebserver', 'src', 'main', 'java')
    gen_javadoc(src_path, sub_out_path, 'smcl.samsung')

    # Generate 3DCursor
    sub_out_path = os.path.join(out_path, '3DCursor')
    src_path = os.path.join(base_path, 'SXR', 'Extensions', '3DCursor', '3DCursorLibrary', 'src', 'main', 'java')
    gen_javadoc(src_path, sub_out_path, 'com.samsungxr')

    # Generate Mixed Reality
    sub_out_path = os.path.join(out_path, 'MixedReality')
    src_path = os.path.join(base_path, 'SXR', 'Extensions', 'MixedReality', 'src', 'main', 'java')
    gen_javadoc(src_path, sub_out_path, 'com.samsungxr')

    # Generate ResonanceAudio
    sub_out_path = os.path.join(out_path, 'ResonanceAudio')
    src_path = os.path.join(base_path, 'SXR', 'Extensions', 'ResonanceAudio', 'resonanceaudio', 'src', 'main', 'java')
    gen_javadoc(src_path, sub_out_path, 'com.samsungxr')

    # Generate SceneSerializer
    sub_out_path = os.path.join(out_path, 'SceneSerializer')
    src_path = os.path.join(base_path, 'SXR', 'Extensions', 'SceneSerializer', 'sceneserializer', 'src', 'main', 'java')
    gen_javadoc(src_path, sub_out_path, 'com.samsungxr')

    # Generate WidgetPlugin
    sub_out_path = os.path.join(out_path, 'WidgetPlugin')
    src_path = os.path.join(base_path, 'SXR', 'Extensions', 'widgetLib', 'src')
    gen_javadoc(src_path, sub_out_path, 'com.samsungxr')

    # Generate sxr-physics
    sub_out_path = os.path.join(out_path, 'sxr-physics')
    src_path = os.path.join(base_path, 'SXR', 'Extensions', 'sxr-physics', 'src', 'main', 'java')
    gen_javadoc(src_path, sub_out_path, 'com.samsungxr')

    # Generate particle system
    sub_out_path = os.path.join(out_path, 'sxr-particlesystem')
    src_path = os.path.join(base_path, 'SXR', 'Extensions', 'sxr-particlesystem', 'src', 'main', 'java')
    gen_javadoc(src_path, sub_out_path, 'com.samsungxr')

    # Generate Wear touchpad
    sub_out_path = os.path.join(out_path, 'WearTouchPad')
    src_path = os.path.join(base_path, 'SXR', 'Extensions', 'WearTouchPad', 'wear', 'src', 'main', 'java')
    gen_javadoc(src_path, sub_out_path, 'com.samsungxr')

def gen_all_docs(out_path, api_template_path, version_num):
    # Check required commands
    javadoc_path = which('javadoc')
    if javadoc_path is None:
        print '==> Error: Failed to find javadoc, please check your java setup'
        return

    mkdocs_path = which('mkdocs')
    if mkdocs_path is None:
        print '==> Error: Failed to find mkdocs, please follow the Readme to set it up'
        return

    del_tree(out_path)
    copy_tree(api_template_path, out_path)

    # Search for SXR folder
    # Search for SXR_SOURCE_PATH
    sxr_path = os.environ.get('SXR_SOURCE_PATH')
    curr_path = get_curr_path()
    full_out_path = os.path.join(curr_path, out_path, version_num)
    template_path = os.path.join(curr_path, api_template_path, 'template')

    print "==> Setting up environment"
    if sxr_path is None:
        # Search at the parent dir
        parent_path = os.path.dirname(curr_path)
        sxr_path = os.path.join(parent_path, 'sxrsdk')

    # Generate all java docs
    print '==> generate javadoc'
    if os.path.isdir(sxr_path):
        gen_java_docs(sxr_path, full_out_path)
    else:
        print "==> Invalid SXR path: " + sxr_path

    # copy template
    print '==> copy template'
    copy_all(template_path, full_out_path)

    # Update versions in template
    update_template(out_path, version_num)


def main():
    parser = argparse.ArgumentParser(description='Generate the documentation site for the Samsung XR SDK')
    parser.add_argument('-v', metavar='Version', dest='version', help='specify SXR SDK version', default='v5.0')
    parser.add_argument('-deploy', metavar='Deploy', dest='deploy', help='specify deploy target: github')

    args = parser.parse_args()

    if not args.version.startswith('v'):
        args.version = 'v' + args.version

    print '=> SXR SDK version: ' + args.version

    # Generate site with mkdocs
    from subprocess import call
    call(['mkdocs', 'build'])
    print '=> Generating Documentation site'

    # Generate API reference from SXR SDK source
    print '=> Generating API reference site'
    gen_all_docs('temp', 'api_reference', args.version)

    # Copy api_reference and replace the placeholder api_reference in site
    print '=> Merging API reference with documentation'
    if os.path.isdir('site'):
        print '==> Add API reference'
        copy_tree('temp', 'site/api_reference')
        print '==> Update API reference link'
        from bs4 import  BeautifulSoup
        fp = open('site/api_reference/index.html')
        soup = BeautifulSoup(fp, 'html.parser')
        article = soup.find('article')
        article.string = r'<iframe width="100%" height="800" frameBorder="0" src="index2.html"></iframe>'
        new_content = soup.prettify(formatter=None)
        fp.close()

        file = codecs.open('site/api_reference/index.html', 'w', "utf-8")
        file.write(new_content)
        file.close()
    else:
        print '=> Error: Failed to find site directory please make sure mkdocs is setup correctly'
        return

    if args.deploy == 'github':
        print '=> Deploy to github'
        from deploy import gh_deploy
        gh_deploy()


if __name__ == "__main__":
    # main()
    main()
