import json
from pathlib import Path

import inflection

typesDictionaryCstringToPythonTypesString = {
    'bool': 'bool',  # C type: _Bool  Python type: bool (1)
    'char': 'bytes',  # C type: char  Python type: 1-character bytes object
    'wchar_t': 'str',  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    'unsignedchar': 'int',  # C type: unsigned char  Python type: int
    'short': 'int',  # C type: short  Python type: int
    'unsignedshort': 'int',  # C type: unsigned short  Python type: int
    'int': 'int',  # C type: int  Python type: int
    'unsignedint': 'int',  # C type: unsigned int  Python type: int
    'long': 'int',  # C type: long  Python type: int
    'unsignedlong': 'int',  # C type: unsigned long  Python type: int
    'uint64': 'int',  # C type: __int64 or long-long  Python type: int
    'unsigneduint64': 'int',  # C type: unsigned __int64 or unsigned long-long  Python type: int
    'size_t': 'int',  # C type: unsigned size_t  Python type: int
    'ssize_t': 'int',  # C type: ssize_t or Py_ssize_t  Python type: int
    'float': 'float',  # C type: float  Python type: float
    'double': 'float',  # C type: double  Python type: float
    'longdouble': 'float',  # C type: long double  Python type: float
    'char*': 'bytes',  # C type: char* (NUL terminated)  Python type: bytes object or None
    'wchar_t*': 'string',  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    'void*': 'int',  # C type: wchar_t* (NUL terminated)  Python type: int or None
    'void': 'None',  # C type: void  Python type: None
}

typesDictionaryCstringToCtypesString = {
    'bool': 'c_bool',  # C type: _Bool  Python type: bool (1)
    'char': 'c_char',  # C type: char  Python type: 1-character bytes object
    'wchar_t': 'c_wchar',  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    'unsignedchar': 'c_ubyte',  # C type: unsigned char  Python type: int
    'short': 'c_short',  # C type: short  Python type: int
    'unsignedshort': 'c_ushort',  # C type: unsigned short  Python type: int
    'int': 'c_int',  # C type: int  Python type: int
    'unsignedint': 'c_uint',  # C type: unsigned int  Python type: int
    'long': 'c_long',  # C type: long  Python type: int
    'unsignedlong': 'c_ulong',  # C type: unsigned long  Python type: int
    'uint64': 'c_longlong',  # C type: __int64 or long-long  Python type: int
    'unsigneduint64': 'c_ulonglong',  # C type: unsigned __int64 or unsigned long-long  Python type: int
    'size_t': 'c_size_t',  # C type: unsigned size_t  Python type: int
    'ssize_t': 'c_ssize_t',  # C type: ssize_t or Py_ssize_t  Python type: int
    'float': 'c_float',  # C type: float  Python type: float
    'double': 'c_double',  # C type: double  Python type: float
    'longdouble': 'c_longdouble',  # C type: long double  Python type: float
    'char*': 'c_char_p',  # C type: char* (NUL terminated)  Python type: bytes object or None
    'wchar_t*': 'c_wchar_p',  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    'void*': 'c_void_p',  # C type: wchar_t* (NUL terminated)  Python type: int or None
    'void': 'None',  # C type: void  Python type: None
}

# -----------------------------------------
DEFINES_FOLDER_PATH = Path(__file__).parent / 'raypyc/defines'
ENUMS_FOLDER_PATH = Path(__file__).parent / 'raypyc/enums'
STRUCTURES_FOLDER_PATH = Path(__file__).parent / 'raypyc/structures'
FUNCTIONS_FOLDER_PATH = Path(__file__).parent / 'raypyc'
JSON_FOLDER_PATH = Path(__file__).parent / 'raypyc'

wrapped_defines_names_py = []
wrapped_defines_names_pyi = []

wrapped_enums_names_py = []
wrapped_enums_names_pyi = []

wrapped_structures_names_py = []
wrapped_structures_names_pyi = []

wrapped_functions_names_pyi = []


# -----------------------------------------


# -----------------------------------------

# **all the functions raypyc use are here**


# convert c type string to ctype type sting
def convert_c_type_string_to_ctype_type_sting(c_type_string: str):
    CstringToCtypesString = {
        'bool': 'c_bool',  # C type: _Bool  Python type: bool (1)
        'char': 'c_char',  # C type: char  Python type: 1-character bytes object
        'wchar_t': 'c_wchar',  # C type: wchar_t  Python type: 1-character string
        # 'char': c_byte,  # C type: char  Python type: int
        'unsignedchar': 'c_ubyte',  # C type: unsigned char  Python type: int
        'short': 'c_short',  # C type: short  Python type: int
        'unsignedshort': 'c_ushort',  # C type: unsigned short  Python type: int
        'int': 'c_int',  # C type: int  Python type: int
        'unsignedint': 'c_uint',  # C type: unsigned int  Python type: int
        'long': 'c_long',  # C type: long  Python type: int
        'unsignedlong': 'c_ulong',  # C type: unsigned long  Python type: int
        'uint64': 'c_longlong',  # C type: __int64 or long-long  Python type: int
        'unsigneduint64': 'c_ulonglong',  # C type: unsigned __int64 or unsigned long-long  Python type: int
        'size_t': 'c_size_t',  # C type: unsigned size_t  Python type: int
        'ssize_t': 'c_ssize_t',  # C type: ssize_t or Py_ssize_t  Python type: int
        'float': 'c_float',  # C type: float  Python type: float
        'double': 'c_double',  # C type: double  Python type: float
        'longdouble': 'c_longdouble',  # C type: long double  Python type: float
        'char*': 'c_char_p',  # C type: char* (NUL terminated)  Python type: bytes object or None
        'wchar_t*': 'c_wchar_p',  # C type: wchar_t* (NUL terminated)  Python type: string object or None
        'void*': 'c_void_p',  # C type: wchar_t* (NUL terminated)  Python type: int or None
        'void': 'None',  # C type: void  Python type: None
    }

    c_type_string = c_type_string.replace(' ', '').replace('const', '')  # remove spaces, and "const" because there isn't really a const type in python...
    is_array = ']' in c_type_string
    pointer_level = c_type_string.count("*")

    if is_array and pointer_level > 0:  # array of pointers to structures
        type_of_array = c_type_string.split('[')[0]
        array_size = c_type_string.split('[')[1][:-1]
        type_of_array_without_pointers = type_of_array.replace('*', '')
        if type_of_array in CstringToCtypesString:  # basic type pointer (int*, char*, float*, ...)
            return f"{CstringToCtypesString[type_of_array]} * {array_size}"
        if type_of_array_without_pointers in CstringToCtypesString:  # basic type pointer(probably double+ pointer level) (int**, char**, float**, ...)
            type_of_array_end = CstringToCtypesString[type_of_array_without_pointers]
            for i in range(pointer_level):
                type_of_array_end = f"POINTER({type_of_array_end})"
            return f"{type_of_array_end} * {array_size}"
        else:  # a struct array pointer level 1+ or just a pointer level 1
            type_of_array_end = type_of_array_without_pointers
            for i in range(pointer_level):
                type_of_array_end = f"POINTER({type_of_array_end})"
            return f"{type_of_array_end} * {array_size}"
    elif is_array:
        type_of_array = c_type_string.split('[')[0]
        array_size = c_type_string.split('[')[1][:-1]
        if type_of_array in CstringToCtypesString:  # basic type array (int, char, float, ...)
            return f"{CstringToCtypesString[type_of_array]} * {array_size}"
        else:  # a struct array
            return f"{type_of_array} * {array_size}"
    elif pointer_level > 0:
        type_without_pointers = c_type_string.replace('*', '')
        if c_type_string in CstringToCtypesString:  # basic type pointer (int**, char*, float*, ...)
            return f"{CstringToCtypesString[c_type_string]}"
        if type_without_pointers in CstringToCtypesString:  # basic type pointer(probably double+ pointer level) (int**, char**, float**, ...)
            type_of_pointer_end = CstringToCtypesString[type_without_pointers]
            for i in range(pointer_level):
                type_of_pointer_end = f"POINTER({type_of_pointer_end})"
            return f"{type_of_pointer_end}"
        else:  # a struct pointer level 1+ or just a pointer level 1
            type_of_pointer_end = type_without_pointers
            for i in range(pointer_level):
                type_of_pointer_end = f"POINTER({type_of_pointer_end})"
            return f"{type_of_pointer_end}"
    else:  # "regular" value not a pointer or an array
        if c_type_string in CstringToCtypesString:
            return CstringToCtypesString[c_type_string]
        return c_type_string  # a struct


# get class object by string name
def str_to_class(classname):
    return eval(classname)


# get numbers from string
def get_numbers_from_string(string):
    ints = []
    for s in string.split(' '):
        if s.isdigit():
            ints.append(int(s))
    return ints


# get the indexes of a char in a string
def find_char_in_str(string, char):
    return [i for i, ltr in enumerate(string) if ltr == char]


# return a string that indented in the start of the string and in every \n of the string
def indentString(string: str, indent_by: int) -> str:
    return '\t' * indent_by + string.replace('\n', '\n' + '\t' * indent_by)

def generate_define_code(define_data):
    if define_data['type'] not in ["FLOAT_MATH", "FLOAT", "STRING", "INT"]: return ""
    elif define_data['type'] == "FLOAT_MATH": return f"{define_data['name']}: float = {define_data['value'].replace('f', '')}{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
    elif define_data['type'] in ["INT", "FLOAT"]: return f"{define_data['name']}: int = {define_data['value']}{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
    elif define_data['type'] == "STRING": return f"{define_data['name']}: str = {define_data['value']}{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
    else: return ""

def generate_define_code_stub(define_data):
    if define_data['type'] not in ["FLOAT_MATH", "FLOAT", "STRING", "INT"]: return ""
    elif define_data['type'] in ["FLOAT_MATH", "FLOAT"]: return f"{define_data['name']}: float{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
    elif define_data['type'] == "INT": return f"{define_data['name']}: int{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
    elif define_data['type'] == "STRING": return f"{define_data['name']}: str{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
    else: return ""

def generate_enum_signature_code(enum_data):
    return f"class {enum_data['name']}(IntEnum):\n\t\"\"\"{enum_data['description']}\"\"\"\n"


def generate_enum_signature_code_stub(enum_data):
    return f"class {enum_data['name']}(IntEnum):\n\t\"\"\"{enum_data['description']}\"\"\"\n"


def generate_enum_values_string_code(enum_data):
    enum_members_string = ""
    for enum_value in enum_data['values']:
        enum_members_string += f"{enum_value['name']}: int = {enum_value['value']}  # {enum_value['description']}\n"

    return f"{indentString(enum_members_string, 1)[:-1]}\n"


def generate_enum_values_string_code_stub(enum_data):
    enum_members_string = ""
    for enum_value in enum_data['values']:
        enum_members_string += f"{enum_value['name']}: int  # {enum_value['description']}\n"

    return f"{indentString(enum_members_string, 1)[:-1]}\n"

def generate_struct_signature_code(struct_data):
    return f"class {struct_data['name']}(Structure):\n\t\"\"\"{struct_data['description']}\"\"\"\n"


def generate_struct_signature_code_stub(struct_data):
    return f"class {struct_data['name']}(Structure):\n\t\"\"\"{struct_data['description']}\"\"\"\n"


# remove the current defines/__init__.py defines enums/__init__.pyi files and generated new ones
def generate_defines_py_pyi_files():
    if Path(DEFINES_FOLDER_PATH / '__init__.py').exists():
        with open(Path(DEFINES_FOLDER_PATH / '__init__.py'), "w") as structs_code_file_write:  # add import stuff
            pass
    else:
        print(f"there isn\'t a __init__.py in {Path(DEFINES_FOLDER_PATH / '__init__.py')}, regenerating a new one here")
        with open(Path(DEFINES_FOLDER_PATH / '__init__.py'), "x"):  # generate __init__.py file => define logic
            pass
        with open(Path(DEFINES_FOLDER_PATH / '__init__.py'), "w") as structs_code_file_write:  # add import stuff
            pass

    if Path(DEFINES_FOLDER_PATH / '__init__.pyi').exists():
        with open(Path(DEFINES_FOLDER_PATH / '__init__.pyi'), "w") as structs_code_file_write:  # add import stuff
            pass
    else:
        print(f"there isn\'t a __init__.pyi in {Path(DEFINES_FOLDER_PATH / '__init__.pyi')}, regenerating a new one here")
        with open(Path(DEFINES_FOLDER_PATH / '__init__.pyi'), "x"):  # generate __init__.pyi file => define signature
            pass
        with open(Path(DEFINES_FOLDER_PATH / '__init__.pyi'), "w") as structs_code_file_write:  # add import stuff
            pass


def generate_defines_py_pyi_code(defines_api):

    # generate __init__.py code
    with open(Path(DEFINES_FOLDER_PATH / '__init__.py'), "a") as defines_code_file_w:
        for define in defines_api:
            if define['name'] not in wrapped_defines_names_py:
                wrapped_defines_names_py.append(define['name'])
                define_string_logic = generate_define_code(define)
                if define_string_logic != "": define_string_logic += "\n"

                defines_code_file_w.write(define_string_logic)

    # generate __init__.pyi code
    with open(Path(DEFINES_FOLDER_PATH / '__init__.pyi'), "a") as defines_code_file_w:
        for define in defines_api:
            if define['name'] not in wrapped_defines_names_pyi:
                wrapped_defines_names_pyi.append(define['name'])
                define_string_logic = generate_define_code_stub(define)
                if define_string_logic != "": define_string_logic += "\n"

                defines_code_file_w.write(define_string_logic)


# remove the current enums/__init__.py and enums/__init__.pyi files and generated new ones
def generate_enums_py_pyi_files():
    if Path(ENUMS_FOLDER_PATH / '__init__.py').exists():
        with open(Path(ENUMS_FOLDER_PATH / '__init__.py'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from enum import IntEnum\n\n')
    else:
        print(f"there isn\'t a __init__.py in {Path(ENUMS_FOLDER_PATH / '__init__.py')}, regenerating a new one here")
        with open(Path(ENUMS_FOLDER_PATH / '__init__.py'), "x"):  # generate __init__.py file => enum logic
            pass
        with open(Path(ENUMS_FOLDER_PATH / '__init__.py'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from enum import IntEnum\n\n')

    if Path(ENUMS_FOLDER_PATH / '__init__.pyi').exists():
        with open(Path(ENUMS_FOLDER_PATH / '__init__.pyi'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from enum import IntEnum\n\n')
    else:
        print(f"there isn\'t a __init__.pyi in {Path(ENUMS_FOLDER_PATH / '__init__.pyi')}, regenerating a new one here")
        with open(Path(ENUMS_FOLDER_PATH / '__init__.pyi'), "x"):  # generate __init__.pyi file => enum signature
            pass
        with open(Path(ENUMS_FOLDER_PATH / '__init__.pyi'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from enum import IntEnum\n\n')


def generate_enums_py_pyi_code(enums_api):
    # generate __init__.py code
    with open(Path(ENUMS_FOLDER_PATH / '__init__.py'), "a") as enums_code_file_w:
        for enum in enums_api:
            if enum['name'] not in wrapped_structures_names_py:
                wrapped_structures_names_py.append(enum['name'])
                enum_string_logic = ""
                enum_string_logic += generate_enum_signature_code(enum)
                enum_string_logic += generate_enum_values_string_code(enum)
                enum_string_logic += "\n"

                enums_code_file_w.write(enum_string_logic.replace('\n\t\n', '\n\n'))

    # generate __init__.pyi code
    with open(Path(ENUMS_FOLDER_PATH / '__init__.pyi'), "a") as enums_code_file_w:
        for enum in enums_api:
            if enum['name'] not in wrapped_structures_names_pyi:
                wrapped_structures_names_pyi.append(enum['name'])
                enum_string_logic = ""
                enum_string_logic += generate_enum_signature_code_stub(enum)
                enum_string_logic += generate_enum_values_string_code_stub(enum)
                enum_string_logic += "\n"

                enums_code_file_w.write(enum_string_logic.replace('\n\t\n', '\n\n'))


# remove the current structures/__init__.py and structures/__init__.pyi files and generated new ones
def generate_structs_py_pyi_files():
    if Path(STRUCTURES_FOLDER_PATH / '__init__.py').exists():
        with open(Path(STRUCTURES_FOLDER_PATH / '__init__.py'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from ctypes import *\n\n\n')
    else:
        print(f"there isn\'t a __init__.py in {Path(STRUCTURES_FOLDER_PATH / '__init__.py')}, regenerating a new one here")
        with open(Path(STRUCTURES_FOLDER_PATH / '__init__.py'), "x"):  # generate __init__.py file => struct logic
            pass
        with open(Path(STRUCTURES_FOLDER_PATH / '__init__.py'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from ctypes import *\n\n\n')

    if Path(STRUCTURES_FOLDER_PATH / '__init__.pyi').exists():
        with open(Path(STRUCTURES_FOLDER_PATH / '__init__.pyi'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from ctypes import *\n\n\n')
    else:
        print(f"there isn\'t a __init__.pyi in {Path(STRUCTURES_FOLDER_PATH / '__init__.pyi')}, regenerating a new one here")
        with open(Path(STRUCTURES_FOLDER_PATH / '__init__.pyi'), "x"):  # generate __init__.pyi file => struct signature
            pass
        with open(Path(STRUCTURES_FOLDER_PATH / '__init__.pyi'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from ctypes import *\n\n\n')


def generate_structs_py_pyi_code(structs_api, aliases_api):
    # generate __init__.py code
    with open(Path(STRUCTURES_FOLDER_PATH / '__init__.py'), "a") as structs_code_file_w:
        for struct in structs_api:
            if not struct['name'] in ['AudioStream', 'Wave', 'Sound', 'Music']:
                if struct['name'] not in wrapped_structures_names_py:
                    wrapped_structures_names_py.append(struct['name'])
                    struct_string_logic = ""
                    struct_string_logic += generate_struct_signature_code(struct)
                    struct_string_logic += generate_struct_fields_string_code(struct)
                    struct_string_logic += generate_struct_setters_getters_code(struct)
                    struct_string_logic += "\n"

                    structs_code_file_w.write(struct_string_logic.replace('\n\t\n', '\n\n'))

                    for aliase in aliases_api:
                        if struct['name'] == aliase['type']:
                            if aliase['name'] not in wrapped_structures_names_py:
                                wrapped_structures_names_py.append(aliase['name'])
                                aliase_data = dict(struct)
                                aliase_data['name'] = str(aliase['name'])
                                aliase_data['description'] = str(aliase['description'])
                                aliase_string_logic = ""
                                aliase_string_logic += generate_struct_signature_code(aliase_data)
                                aliase_string_logic += generate_struct_fields_string_code(aliase_data)
                                aliase_string_logic += generate_struct_setters_getters_code(aliase_data)
                                aliase_string_logic += "\n"

                                structs_code_file_w.write(aliase_string_logic.replace('\n\t\n', '\n\n'))

    # generate __init__.pyi code
    with open(Path(STRUCTURES_FOLDER_PATH / '__init__.pyi'), "a") as structs_code_stub_file_w:
        for struct in structs_api:
            if not struct['name'] in ['AudioStream', 'Wave', 'Sound', 'Music']:
                if struct['name'] not in wrapped_structures_names_pyi:
                    wrapped_structures_names_pyi.append(struct['name'])
                    struct_string_logic = ""
                    struct_string_logic += generate_struct_signature_code(struct)
                    # struct_string_logic += generate_struct_fields_string_code_stub(struct)  # we don't really need that in the __init__.pyi file
                    struct_string_logic += generate_struct_setters_getters_code_stub(struct)
                    struct_string_logic += "\n"

                    structs_code_stub_file_w.write(struct_string_logic.replace('\n\t\n', '\n\n'))

                    for aliase in aliases_api:
                        if struct['name'] == aliase['type']:
                            if aliase['name'] not in wrapped_structures_names_pyi:
                                wrapped_structures_names_pyi.append(aliase['name'])
                                aliase_data = dict(struct)
                                aliase_data['name'] = str(aliase['name'])
                                aliase_data['description'] = str(aliase['description'])
                                aliase_string_logic = ""
                                aliase_string_logic += generate_struct_signature_code_stub(aliase_data)
                                # aliase_string_logic += generate_struct_fields_string_code(struct) we don't really need that in the __init__.pyi file
                                aliase_string_logic += generate_struct_setters_getters_code_stub(aliase_data)
                                aliase_string_logic += "\n"

                                structs_code_stub_file_w.write(aliase_string_logic.replace('\n\t\n', '\n\n'))


def generate_struct_fields_string_code(struct_data):
    struct_fields = "_fields_ = [\n"

    for struct_data_field in struct_data['fields']:
        struct_data_field_name = struct_data_field['name']
        struct_data_field_type = struct_data_field['type']
        struct_data_field_description = struct_data_field['description']
        struct_fields += f"\t('{struct_data_field_name}', {convert_c_type_string_to_ctype_type_sting(struct_data_field_type)}),  # {struct_data_field_description}\n"

    temp = find_char_in_str(struct_fields, ',')
    if len(temp) != 0:
        struct_fields = struct_fields[: temp[-1]] + struct_fields[temp[-1] + 1:]
    struct_fields += ']\n\n'

    return indentString(struct_fields, 1)[:-1]


def generate_struct_fields_string_code_stub(struct_data):
    struct_fields = "_fields_ = [\n"

    for struct_data_field in struct_data['fields']:
        struct_data_field_name = struct_data_field['name']
        struct_data_field_type = struct_data_field['type']
        struct_data_field_description = struct_data_field['description']
        struct_fields += f"\t('{struct_data_field_name}', {convert_c_type_string_to_ctype_type_sting(struct_data_field_type)}),  # {struct_data_field_description}\n"
    temp = find_char_in_str(struct_fields, ',')
    if len(temp) != 0:
        struct_fields = struct_fields[: temp[-1]] + struct_fields[temp[-1] + 1:]
    struct_fields += ']\n\n'

    return indentString(struct_fields, 1)[:-1]


def generate_struct_setters_getters_code(struct_data):
    struct_setters_getters_string = ""

    for struct_data_field in struct_data['fields']:
        use_type = convert_c_type_string_to_ctype_type_sting(struct_data_field['type'])
        struct_setters_getters_string += f"@property\ndef {struct_data_field['name']}(self) -> {use_type}:\n\treturn self.{struct_data_field['name']}\n\n" \
                                         f"@{struct_data_field['name']}.setter\ndef {struct_data_field['name']}(self, i: {use_type}) -> None:\n\tself.{struct_data_field['name']} = i\n\n"

    return indentString(struct_setters_getters_string, 1)[:-1]


def generate_struct_setters_getters_code_stub(struct_data):
    struct_setters_getters_string = ""

    for struct_data_field in struct_data['fields']:
        use_type = convert_c_type_string_to_ctype_type_sting(struct_data_field['type'])
        struct_setters_getters_string += f"@property\ndef {struct_data_field['name']}(self) -> {use_type}:\n\t...\n\n" \
                                         f"@{struct_data_field['name']}.setter\ndef {struct_data_field['name']}(self, i: {use_type}) -> None:\n\t...\n\n"

    return indentString(struct_setters_getters_string, 1)[:-1]


# remove the current functions_code.pyi file and generated new one
def generate_functions_code_pyi_file():
    if Path(FUNCTIONS_FOLDER_PATH / '__init__.pyi').exists():
        with open(Path(FUNCTIONS_FOLDER_PATH / '__init__.pyi'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from raypyc.colors import *\n')
            structs_code_file_write.write('from raypyc.enums import *\n')
            structs_code_file_write.write('from raypyc.structures import *\n\n\n')
    else:
        print(f"there isn\'t a __init__.pyi in {Path(FUNCTIONS_FOLDER_PATH / '__init__.pyi')}, regenerating a new one here")
        with open(Path(FUNCTIONS_FOLDER_PATH / '__init__.pyi'), "x"):  # generate __init__.pyi file => function signature
            pass
        with open(Path(FUNCTIONS_FOLDER_PATH / '__init__.pyi'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from raypyc.colors import *\n')
            structs_code_file_write.write('from raypyc.enums import *\n')
            structs_code_file_write.write('from raypyc.structures import *\n\n\n')


# return a set (from a functions set) of functions that can be wrap
def check_for_functions_that_can_wrap(functions_set):
    functions_that_can_be_wrap = []
    functions_that_cant_be_wrap = []
    # check if function can wrap
    for function in functions_set:
        do_wrapper_this_function = True
        if 'params' in function.keys():
            for function_param in function['params']:
                if function_param['type'] in ['AudioStream', 'Wave', 'Sound', 'Music', 'AudioCallback', 'SaveFileTextCallback', 'LoadFileTextCallback', 'TraceLogCallback', 'LoadFileDataCallback', 'SaveFileDataCallback']:
                    do_wrapper_this_function = False
                    break

        if do_wrapper_this_function:
            if function['returnType'].replace('const', '').replace(" ", "").replace("*", "").replace('[', '').replace(']', '') in ['AudioStream', 'Wave', 'Sound', 'Music', 'AudioCallback', 'SaveFileTextCallback', 'LoadFileTextCallback', 'TraceLogCallback', 'LoadFileDataCallback', 'SaveFileDataCallback']:
                do_wrapper_this_function = False

        if do_wrapper_this_function:
            functions_that_can_be_wrap.append(function)
        else:
            functions_that_cant_be_wrap.append(function)
    return functions_that_can_be_wrap


def generate_functions_code_in_code_pyi_file(functions_set):
    with open(Path(FUNCTIONS_FOLDER_PATH / '__init__.pyi'), "a") as functions_code_file_w:
        for function in functions_set:
            if function['name'] not in wrapped_functions_names_pyi:
                wrapped_functions_names_pyi.append(function['name'])
                name_of_function = inflection.underscore(function['name']).replace('3_d', '_3d').replace('2_d', '_2d')
                function_copy = dict(function)
                function_copy['name'] = str(name_of_function)
                function_string = generate_function_signature_code(function_copy)
                functions_code_file_w.write(function_string)


def generate_function_signature_code(function_data):
    function_string = f"def {function_data['name']}("
    if 'params' in function_data.keys():  # only return stuff
        for param in function_data['params']:
            function_string += f"{param['name']}: {convert_c_type_string_to_ctype_type_sting(param['type'])}, "

        function_string = function_string[:-2]

    function_string += ") -> "
    function_string += f"{convert_c_type_string_to_ctype_type_sting(function_data['returnType'])}:\n\t\"\"\"{function_data['description']}\"\"\"\n\t...\n\n"

    return function_string


# -----------------------------------------

# load raylib data
with open(Path(JSON_FOLDER_PATH / 'rlgl_api.json')) as reader:
    rlgl_api = json.load(reader)

rlgl_api_defines = rlgl_api['defines']
rlgl_api_structs = rlgl_api['structs']
rlgl_api_aliases = rlgl_api['aliases']
rlgl_api_enums = rlgl_api['enums']
rlgl_api_functions = rlgl_api['functions']

# load raylib data
with open(Path(JSON_FOLDER_PATH / 'raylib_api.json')) as reader:
    raylib_api = json.load(reader)

raylib_api_defines = raylib_api['defines']
raylib_api_structs = raylib_api['structs']
raylib_api_aliases = raylib_api['aliases']
raylib_api_enums = raylib_api['enums']
raylib_api_functions = raylib_api['functions']

# load raymath data
with open(Path(JSON_FOLDER_PATH / 'raymath_api.json')) as reader:
    raymath_api = json.load(reader)

raymath_api_defines = raymath_api['defines']
raymath_api_structs = raymath_api['structs']
raymath_api_aliases = raymath_api['aliases']
raymath_api_enums = raymath_api['enums']
raymath_api_functions = raymath_api['functions']

# load raygui data
with open(Path(JSON_FOLDER_PATH / 'raygui_api.json')) as reader:
    raygui_api = json.load(reader)

raygui_api_defines = raygui_api['defines']
raygui_api_structs = raygui_api['structs']
raygui_api_aliases = raygui_api['aliases']
raygui_api_enums = raygui_api['enums']
raygui_api_functions = raygui_api['functions']


generate_defines_py_pyi_files()

generate_defines_py_pyi_code(rlgl_api_defines)
generate_defines_py_pyi_code(raylib_api_defines)
generate_defines_py_pyi_code(raymath_api_defines)
generate_defines_py_pyi_code(raygui_api_defines)

generate_structs_py_pyi_files()

generate_structs_py_pyi_code(rlgl_api_structs, rlgl_api_aliases)
generate_structs_py_pyi_code(raylib_api_structs, raylib_api_aliases)
generate_structs_py_pyi_code(raymath_api_structs, raymath_api_aliases)
generate_structs_py_pyi_code(raygui_api_structs, raygui_api_aliases)

# generate the enums files
generate_enums_py_pyi_files()

generate_enums_py_pyi_code(rlgl_api_enums)
generate_enums_py_pyi_code(raylib_api_enums)
generate_enums_py_pyi_code(raymath_api_enums)
generate_enums_py_pyi_code(raygui_api_enums)

# generate the raylib functions signature file
generate_functions_code_pyi_file()

rlgl_functions_to_wrapped = check_for_functions_that_can_wrap(rlgl_api_functions)
raylib_functions_to_wrapped = check_for_functions_that_can_wrap(raylib_api_functions)
raymath_functions_to_wrapped = check_for_functions_that_can_wrap(raymath_api_functions)
raygui_functions_to_wrapped = check_for_functions_that_can_wrap(raygui_api_functions)

# add the functions signature file
generate_functions_code_in_code_pyi_file(rlgl_functions_to_wrapped)
generate_functions_code_in_code_pyi_file(raylib_functions_to_wrapped)
generate_functions_code_in_code_pyi_file(raymath_functions_to_wrapped)
generate_functions_code_in_code_pyi_file(raygui_functions_to_wrapped)
