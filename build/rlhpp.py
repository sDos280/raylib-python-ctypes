# https://gist.github.com/stucotso/76f602a267be052ec19686c38a783f65
# thanks https://gist.github.com/stucotso !!!

import sys
from pycparser import parse_file, c_ast

import os


class ast:
    def __init__(self, children=[], params=[], line=0):
        self.children = children
        self.params = params
        self.line = line

    def expand(self, flags, nest):
        return "".join([i.expand(flags, nest + 1) for i in self.children])

    def dump(self, nest=0):
        ret = ("\t" * nest) + self.__class__.__name__ + "\n"
        for i in self.children:
            ret += i.dump(nest + 1)
        return ret


class ifdef(ast):
    def evaluate(self, flags):
        func = self.params[0].strip()
        negate = False
        if func == "#ifndef": negate = True
        key = self.params[1].strip()
        test = key in flags.keys() and flags[key] != ""
        if negate: return not test
        return test

    def expand(self, flags, nest):
        result = ""

        if self.evaluate(flags):  #
            for i in self.children:
                child = i.expand(flags, nest + 1)
                if child.strip().split(" ")[0].strip() != "#endif":
                    result += child
        return result


class text(ast):
    def expand(self, flags, nest): return self.params[0]


class Preprocessor():
    def __init__(self, flags):
        self.index = 0
        self.flags = flags

    def preprocessLine(self, lines, parent):

        if self.index >= len(lines):
            self.index = -1
            return text(line=-1, params=[""])

        line = lines[self.index]

        directive = None
        if line.strip().startswith("#"):
            directive = line.strip().split(" ")
            if directive[0].strip() in ["#ifdef", "#ifndef", "#if"]:
                self.index += 1
                newparent = ifdef(params=directive, line=self.index, children=[])
                parent.children.append(newparent)
                self.preprocessLines(lines, newparent)
                return newparent

        self.index += 1

        result = text(line=self.index, params=[line])

        parent.children.append(result)
        return result

    def preprocessLines(self, lines, parent):
        while self.index >= 0:
            item = self.preprocessLine(lines, parent)
            if item.line == -1 or item.params[0].strip() == "#endif" or item.params[0].split(" ")[0] == "#endif":
                return

    def preprocessFile(self, f):
        print("Preproccessing file:", f)
        file = open(f, 'r')
        lines = file.readlines()
        self.index = 0
        result = ast(children=[])
        self.preprocessLines(lines, result)
        if self.index < len(lines) and self.index >= 0: raise Exception("error parsing, failed at: " + str(self.index))
        return result.expand(self.flags, 0)  # self.expand(result.children)


def printUsage():
    print("you need to use this script like that:")
    print(f"{sys.argv[0][3:]} path_to_header flag_that_you_want_to_preserve")


header = [
    sys.argv[1]
]

params = [
    f"-d {sys.argv[2] if len(sys.argv) == 3 else ''}"
]


def preprocess():
    if not os.path.exists("./tmp"):
        os.system("mkdir tmp")
    for i in header:
        fname = i.split("/")[-1]

        output = Preprocessor({}).preprocessFile(i)
        outHeader = "tmp/" + fname + ".preprocessed"
        if not os.path.exists(outHeader):
            with open(outHeader, "x"): pass
        with open(outHeader, "w") as r:
            r.write(output)


preprocess()
