# A module for writing code to a source file and executing it.
# Supports: c, cpp, py, pl, rb
import sys
import re
import tempfile
import shutil
from subprocess import Popen, PIPE

def writeSource(source, ext):
    tempfile.tempdir = tempfile.mkdtemp()
    fn = "{0}/source.{1}".format(tempfile.tempdir, ext)

    with open(fn, 'w') as f:
        f.write(source)

    return fn

def compileSource(compiler, source, ext):
    fn = writeSource(source, ext)

    compLine = "{0} {1} -o {1}.exe".format(compiler, fn)
    proc = Popen(compLine.split(' '), stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()

    if err:
        raise Exception("{}".format(str(err)))

    return "{0}.exe".format(fn)

def c_run(exe):
    proc = Popen(exe, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()

    if err:
        raise Exception("{}".format(err))

    # Delete tmp dir and reset tempfile's tempdir to None
    shutil.rmtree(tempfile.tempdir)
    tempfile.tempdir = None
    return out

def c_compile(source):
    exe = compileSource('clang', source, 'c')
    return c_run(exe)

def cpp_compile(source):
    exe = compileSource('clang++ -std=c++11', source, 'cpp')
    return c_run(exe)

def py_run(source, interp = "python"):
    exe = writeSource(source, 'py')
    return c_run([interp, exe])

def pl_run(source):
    exe = writeSource(source, 'pl')
    return c_run(["perl", exe])

def rb_run(source):
    exe = writeSource(source, 'rb')
    return c_run(["ruby", exe])

''' {0} == source file '''

command = {
    'c': c_compile,
    'cpp': cpp_compile,
    'py': py_run,
    'pl': pl_run,
    'rb': rb_run
}

def escapeNewlines(code):
    replace = lambda x: x.group(0).replace('\n', '\\n')
    return re.sub(r'"[^"]*"', replace, code)

def run(code, codeType):
    code = escapeNewlines(code)
    return command[codeType](code)

def tests():
    out = run('''
print('Yo')

def yo():
    print('Yo!')

yo()
    ''', 'py')
    print(out)

    out = run('''
    print 'Hello!';
    ''', 'rb')

    print(out)

    out = run('''
    print 'Perl!';
    ''', 'pl')

    print(out)

