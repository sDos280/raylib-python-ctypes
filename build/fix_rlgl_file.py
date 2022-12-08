import os

# fix rlgl file
rlgl_to_replace = b"""#if defined(GRAPHICS_API_OPENGL_11) || defined(GRAPHICS_API_OPENGL_33)\r\n    unsigned int *indices;      // Vertex indices (in case vertex data comes indexed) (6 indices per quad)\r\n#endif\r\n#if defined(GRAPHICS_API_OPENGL_ES2)\r\n    unsigned short *indices;    // Vertex indices (in case vertex data comes indexed) (6 indices per quad)\r\n#endif\r\n"""

rlgl_replace_with = b"""    unsigned int *indices;      // Vertex indices (in case vertex data comes indexed) (6 indices per quad)\r\n"""

with open('raylib/src/rlgl.h', 'rb') as read_file:
    rlgl_text = read_file.read()
try:
    os.remove('raylib/src/rlgl_old.h')
except Exception as e:
    print(e)

with open('raylib/src/rlgl_old.h', 'x') as create_file:
    pass
with open('raylib/src/rlgl_old.h', 'wb') as write_file:
    write_file.write(rlgl_text)

rlgl_text = rlgl_text.replace(rlgl_to_replace, rlgl_replace_with)

with open('raylib/src/rlgl.h', 'wb') as write_file:
    write_file.write(rlgl_text)
