cdef extern from "config.h":
    cdef int SUPPORT_MODULE_RSHAPES = 1
    cdef int SUPPORT_MODULE_RTEXTURES = 1
    cdef int SUPPORT_MODULE_RTEXT = 1  # WARNING: It requires SUPPORT_MODULE_RTEXTURES to load sprite font textures
    cdef int SUPPORT_MODULE_RMODELS = 1
    cdef int SUPPORT_MODULE_RAUDIO = 1
    cdef int SUPPORT_CAMERA_SYSTEM = 1
    cdef int SUPPORT_GESTURES_SYSTEM = 1
    cdef int SUPPORT_MOUSE_GESTURES = 1
    cdef int SUPPORT_SSH_KEYBOARD_RPI = 1
    cdef int SUPPORT_WINMM_HIGHRES_TIMER = 1
    cdef int SUPPORT_SCREEN_CAPTURE = 1
    cdef int SUPPORT_GIF_RECORDING = 1
    cdef int SUPPORT_COMPRESSION_API = 1
    cdef int MAX_FILEPATH_CAPACITY = 8192  # Maximum file paths capacity
    cdef int MAX_FILEPATH_LENGTH = 4096  # Maximum length for filepaths (Linux PATH_MAX default value)
    cdef int MAX_KEYBOARD_KEYS = 512  # Maximum number of keyboard keys supported
    cdef int MAX_MOUSE_BUTTONS = 8  # Maximum number of mouse buttons supported
    cdef int MAX_GAMEPADS = 4  # Maximum number of gamepads supported
    cdef int MAX_GAMEPAD_AXIS = 8  # Maximum number of axis supported (per gamepad)
    cdef int MAX_GAMEPAD_BUTTONS = 32  # Maximum number of buttons supported (per gamepad)
    cdef int MAX_TOUCH_POINTS = 8  # Maximum number of touch points supported
    cdef int MAX_KEY_PRESSED_QUEUE = 16  # Maximum number of keys in the key input queue
    cdef int MAX_CHAR_PRESSED_QUEUE = 16  # Maximum number of characters in the char input queue
    cdef int MAX_DECOMPRESSION_SIZE = 64  # Max size allocated for decompression in MB
    cdef int RL_DEFAULT_BATCH_BUFFERS = 1  # Default number of batch buffers (multi-buffering)
    cdef int RL_DEFAULT_BATCH_DRAWCALLS = 256  # Default number of batch draw calls (by state changes: mode, texture)
    cdef int RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS = 4  # Maximum number of textures units that can be activated on batch drawing (SetShaderValueTexture())
    cdef int RL_MAX_MATRIX_STACK_SIZE = 32  # Maximum size of internal Matrix stack
    cdef int RL_MAX_SHADER_LOCATIONS = 32  # Maximum number of shader locations supported
    cdef float RL_CULL_DISTANCE_NEAR = 0.01  # Default projection matrix near cull distance
    cdef float RL_CULL_DISTANCE_FAR = 1000.0  # Default projection matrix far cull distance
    cdef char* RL_DEFAULT_SHADER_ATTRIB_NAME_POSITION = "vertexPosition"  # Binded by default to shader location: 0
    cdef char* RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD = "vertexTexCoord"  # Binded by default to shader location: 1
    cdef char* RL_DEFAULT_SHADER_ATTRIB_NAME_NORMAL = "vertexNormal"  # Binded by default to shader location: 2
    cdef char* RL_DEFAULT_SHADER_ATTRIB_NAME_COLOR = "vertexColor"  # Binded by default to shader location: 3
    cdef char* RL_DEFAULT_SHADER_ATTRIB_NAME_TANGENT = "vertexTangent"  # Binded by default to shader location: 4
    cdef char* RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD2 = "vertexTexCoord2"  # Binded by default to shader location: 5
    cdef char* RL_DEFAULT_SHADER_UNIFORM_NAME_MVP = "mvp"  # model-view-projection matrix
    cdef char* RL_DEFAULT_SHADER_UNIFORM_NAME_VIEW = "matView"  # view matrix
    cdef char* RL_DEFAULT_SHADER_UNIFORM_NAME_PROJECTION = "matProjection"  # projection matrix
    cdef char* RL_DEFAULT_SHADER_UNIFORM_NAME_MODEL = "matModel"  # model matrix
    cdef char* RL_DEFAULT_SHADER_UNIFORM_NAME_NORMAL = "matNormal"  # normal matrix (transpose(inverse(matModelView))
    cdef char* RL_DEFAULT_SHADER_UNIFORM_NAME_COLOR = "colDiffuse"  # color diffuse (base tint color, multiplied by texture color)
    cdef char* RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE0 = "texture0"  # texture0 (texture slot active 0)
    cdef char* RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE1 = "texture1"  # texture1 (texture slot active 1)
    cdef char* RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE2 = "texture2"  # texture2 (texture slot active 2)
    cdef int SUPPORT_QUADS_DRAW_MODE = 1
    cdef int SUPPORT_FILEFORMAT_PNG = 1
    cdef int SUPPORT_FILEFORMAT_GIF = 1
    cdef int SUPPORT_FILEFORMAT_QOI = 1
    cdef int SUPPORT_FILEFORMAT_DDS = 1
    cdef int SUPPORT_FILEFORMAT_HDR = 1
    cdef int SUPPORT_IMAGE_EXPORT = 1
    cdef int SUPPORT_IMAGE_GENERATION = 1
    cdef int SUPPORT_IMAGE_MANIPULATION = 1
    cdef int SUPPORT_DEFAULT_FONT = 1
    cdef int SUPPORT_FILEFORMAT_FNT = 1
    cdef int SUPPORT_FILEFORMAT_TTF = 1
    cdef int SUPPORT_TEXT_MANIPULATION = 1
    cdef int MAX_TEXT_BUFFER_LENGTH = 1024  # Size of internal static buffers used on some functions:
    cdef int MAX_TEXTSPLIT_COUNT = 128  # Maximum number of substrings to split: TextSplit()
    cdef int SUPPORT_FILEFORMAT_OBJ = 1
    cdef int SUPPORT_FILEFORMAT_MTL = 1
    cdef int SUPPORT_FILEFORMAT_IQM = 1
    cdef int SUPPORT_FILEFORMAT_GLTF = 1
    cdef int SUPPORT_FILEFORMAT_VOX = 1
    cdef int SUPPORT_MESH_GENERATION = 1
    cdef int MAX_MATERIAL_MAPS = 12  # Maximum number of shader maps supported
    cdef int MAX_MESH_VERTEX_BUFFERS = 7  # Maximum vertex buffers (VBO) per mesh
    cdef int SUPPORT_FILEFORMAT_WAV = 1
    cdef int SUPPORT_FILEFORMAT_OGG = 1
    cdef int SUPPORT_FILEFORMAT_XM = 1
    cdef int SUPPORT_FILEFORMAT_MOD = 1
    cdef int SUPPORT_FILEFORMAT_MP3 = 1
    cdef int AUDIO_DEVICE_CHANNELS = 2  # Device output channels: stereo
    cdef int AUDIO_DEVICE_SAMPLE_RATE = 0  # Device sample rate (device default)
    cdef int MAX_AUDIO_BUFFER_POOL_CHANNELS = 16  # Maximum number of audio pool channels
    cdef int SUPPORT_TRACELOG = 1
    cdef int MAX_TRACELOG_MSG_LENGTH = 128  # Max length of one trace-log message


cdef extern from "rlgl.h":
    cdef char* RLGL_VERSION = "4.0"
    cdef int RL_DEFAULT_BATCH_BUFFER_ELEMENTS = 8192
    cdef int RL_TEXTURE_WRAP_S = 10242  # GL_TEXTURE_WRAP_S
    cdef int RL_TEXTURE_WRAP_T = 10243  # GL_TEXTURE_WRAP_T
    cdef int RL_TEXTURE_MAG_FILTER = 10240  # GL_TEXTURE_MAG_FILTER
    cdef int RL_TEXTURE_MIN_FILTER = 10241  # GL_TEXTURE_MIN_FILTER
    cdef int RL_TEXTURE_FILTER_NEAREST = 9728  # GL_NEAREST
    cdef int RL_TEXTURE_FILTER_LINEAR = 9729  # GL_LINEAR
    cdef int RL_TEXTURE_FILTER_MIP_NEAREST = 9984  # GL_NEAREST_MIPMAP_NEAREST
    cdef int RL_TEXTURE_FILTER_NEAREST_MIP_LINEAR = 9986  # GL_NEAREST_MIPMAP_LINEAR
    cdef int RL_TEXTURE_FILTER_LINEAR_MIP_NEAREST = 9985  # GL_LINEAR_MIPMAP_NEAREST
    cdef int RL_TEXTURE_FILTER_MIP_LINEAR = 9987  # GL_LINEAR_MIPMAP_LINEAR
    cdef int RL_TEXTURE_FILTER_ANISOTROPIC = 12288  # Anisotropic filter (custom identifier)
    cdef int RL_TEXTURE_WRAP_REPEAT = 10497  # GL_REPEAT
    cdef int RL_TEXTURE_WRAP_CLAMP = 33071  # GL_CLAMP_TO_EDGE
    cdef int RL_TEXTURE_WRAP_MIRROR_REPEAT = 33648  # GL_MIRRORED_REPEAT
    cdef int RL_TEXTURE_WRAP_MIRROR_CLAMP = 34626  # GL_MIRROR_CLAMP_EXT
    cdef int RL_MODELVIEW = 5888  # GL_MODELVIEW
    cdef int RL_PROJECTION = 5889  # GL_PROJECTION
    cdef int RL_TEXTURE = 5890  # GL_TEXTURE
    cdef int RL_LINES = 1  # GL_LINES
    cdef int RL_TRIANGLES = 4  # GL_TRIANGLES
    cdef int RL_QUADS = 7  # GL_QUADS
    cdef int RL_UNSIGNED_BYTE = 5121  # GL_UNSIGNED_BYTE
    cdef int RL_FLOAT = 5126  # GL_FLOAT
    cdef int RL_STREAM_DRAW = 35040  # GL_STREAM_DRAW
    cdef int RL_STREAM_READ = 35041  # GL_STREAM_READ
    cdef int RL_STREAM_COPY = 35042  # GL_STREAM_COPY
    cdef int RL_STATIC_DRAW = 35044  # GL_STATIC_DRAW
    cdef int RL_STATIC_READ = 35045  # GL_STATIC_READ
    cdef int RL_STATIC_COPY = 35046  # GL_STATIC_COPY
    cdef int RL_DYNAMIC_DRAW = 35048  # GL_DYNAMIC_DRAW
    cdef int RL_DYNAMIC_READ = 35049  # GL_DYNAMIC_READ
    cdef int RL_DYNAMIC_COPY = 35050  # GL_DYNAMIC_COPY
    cdef int RL_FRAGMENT_SHADER = 35632  # GL_FRAGMENT_SHADER
    cdef int RL_VERTEX_SHADER = 35633  # GL_VERTEX_SHADER
    cdef int RL_COMPUTE_SHADER = 37305  # GL_COMPUTE_SHADER
    cdef float PI = 3.141592653589793
    cdef float DEG2RAD = (PI/180.0)
    cdef float RAD2DEG = (180.0/PI)
    cdef int GL_SHADING_LANGUAGE_VERSION = 35724
    cdef int GL_COMPRESSED_RGB_S3TC_DXT1_EXT = 33776
    cdef int GL_COMPRESSED_RGBA_S3TC_DXT1_EXT = 33777
    cdef int GL_COMPRESSED_RGBA_S3TC_DXT3_EXT = 33778
    cdef int GL_COMPRESSED_RGBA_S3TC_DXT5_EXT = 33779
    cdef int GL_ETC1_RGB8_OES = 36196
    cdef int GL_COMPRESSED_RGB8_ETC2 = 37492
    cdef int GL_COMPRESSED_RGBA8_ETC2_EAC = 37496
    cdef int GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG = 35840
    cdef int GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG = 35842
    cdef int GL_COMPRESSED_RGBA_ASTC_4x4_KHR = 37808
    cdef int GL_COMPRESSED_RGBA_ASTC_8x8_KHR = 37815
    cdef int GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT = 34047
    cdef int GL_TEXTURE_MAX_ANISOTROPY_EXT = 34046
    cdef int GL_UNSIGNED_SHORT_5_6_5 = 33635
    cdef int GL_UNSIGNED_SHORT_5_5_5_1 = 32820
    cdef int GL_UNSIGNED_SHORT_4_4_4_4 = 32819
    cdef int GL_LUMINANCE = 6409
    cdef int GL_LUMINANCE_ALPHA = 6410

    #  Dynamic vertex buffers (position + texcoords + colors + indices arrays)
    ctypedef struct rlVertexBuffer:
    	int elementCount;  # Number of elements in the buffer (QUADS)
    	float * vertices;  # Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
    	float * texcoords;  # Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
    	unsigned char * colors;  # Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
    	unsigned int * indices;  # Vertex indices (in case vertex data comes indexed) (6 indices per quad)
    	unsigned int vaoId;  # OpenGL Vertex Array Object id
    	unsigned int[4] vboId;  # OpenGL Vertex Buffer Objects id (4 types of vertex data)
    
    
    #  of those state-change happens (this is done in core module)
    ctypedef struct rlDrawCall:
    	int mode;  # Drawing mode: LINES, TRIANGLES, QUADS
    	int vertexCount;  # Number of vertex of the draw
    	int vertexAlignment;  # Number of vertex required for index alignment (LINES, TRIANGLES)
    	unsigned int textureId;  # Texture id to be used on the draw -> Use to create new draw call if changes
    
    
    #  rlRenderBatch type
    ctypedef struct rlRenderBatch:
    	int bufferCount;  # Number of vertex buffers (multi-buffering support)
    	int currentBuffer;  # Current buffer tracking in case of multi-buffering
    	rlVertexBuffer * vertexBuffer;  # Dynamic buffer(s) for vertex data
    	rlDrawCall * draws;  # Draw calls array, depends on textureId
    	int drawCounter;  # Draw calls counter
    	float currentDepth;  # Current depth value for next draw
    
    
    #  Matrix, 4x4 components, column major, OpenGL style, right handed
    ctypedef struct Matrix:
    	float m0;  # Matrix first row (4 components)
    	float m4;  # Matrix first row (4 components)
    	float m8;  # Matrix first row (4 components)
    	float m12;  # Matrix first row (4 components)
    	float m1;  # Matrix second row (4 components)
    	float m5;  # Matrix second row (4 components)
    	float m9;  # Matrix second row (4 components)
    	float m13;  # Matrix second row (4 components)
    	float m2;  # Matrix third row (4 components)
    	float m6;  # Matrix third row (4 components)
    	float m10;  # Matrix third row (4 components)
    	float m14;  # Matrix third row (4 components)
    	float m3;  # Matrix fourth row (4 components)
    	float m7;  # Matrix fourth row (4 components)
    	float m11;  # Matrix fourth row (4 components)
    	float m15;  # Matrix fourth row (4 components)
    
    
    #  
    ctypedef struct rlglData:
    	rlRenderBatch * currentBatch;  # Current render batch
    	rlRenderBatch defaultBatch;  # Default internal render batch
    	int vertexCounter;  # Current active render batch vertex counter (generic, used for all batches)
    	float texcoordx;  # Current active texture coordinate (added on glVertex*())
    	float texcoordy;  # Current active texture coordinate (added on glVertex*())
    	float normalx;  # Current active normal (added on glVertex*())
    	float normaly;  # Current active normal (added on glVertex*())
    	float normalz;  # Current active normal (added on glVertex*())
    	unsigned char colorr;  # Current active color (added on glVertex*())
    	unsigned char colorg;  # Current active color (added on glVertex*())
    	unsigned char colorb;  # Current active color (added on glVertex*())
    	unsigned char colora;  # Current active color (added on glVertex*())
    	int currentMatrixMode;  # Current matrix mode
    	Matrix * currentMatrix;  # Current matrix pointer
    	Matrix modelview;  # Default modelview matrix
    	Matrix projection;  # Default projection matrix
    	Matrix transform;  # Transform matrix to be used with rlTranslate, rlRotate, rlScale
    	bool transformRequired;  # Require transform matrix application to current draw-call vertex (if required)
    	Matrix[RL_MAX_MATRIX_STACK_SIZE] stack;  # Matrix stack for push/pop
    	int stackCounter;  # Matrix stack counter
    	unsigned int defaultTextureId;  # Default texture used on shapes/poly drawing (required by shader)
    	unsigned int[RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS] activeTextureId;  # Active texture ids to be enabled on batch drawing (0 active by default)
    	unsigned int defaultVShaderId;  # Default vertex shader id (used by default shader program)
    	unsigned int defaultFShaderId;  # Default fragment shader id (used by default shader program)
    	unsigned int defaultShaderId;  # Default shader program id, supports vertex color and diffuse texture
    	int * defaultShaderLocs;  # Default shader locations pointer to be used on rendering
    	unsigned int currentShaderId;  # Current shader id to be used on rendering (by default, defaultShaderId)
    	int * currentShaderLocs;  # Current shader locations pointer to be used on rendering (by default, defaultShaderLocs)
    	bool stereoRender;  # Stereo rendering flag
    	Matrix[2] projectionStereo;  # VR stereo rendering eyes projection matrices
    	Matrix[2] viewOffsetStereo;  # VR stereo rendering eyes view offset matrices
    	int currentBlendMode;  # Blending mode active
    	int glBlendSrcFactor;  # Blending source factor
    	int glBlendDstFactor;  # Blending destination factor
    	int glBlendEquation;  # Blending equation
    	int framebufferWidth;  # Current framebuffer width
    	int framebufferHeight;  # Current framebuffer height
    
    

cdef extern from "raylib.h":
    cdef char* RAYLIB_VERSION = "4.2"

    #  Vector2, 2 components
    ctypedef struct Vector2:
    	float x;  # Vector x component
    	float y;  # Vector y component
    
    
    #  Vector3, 3 components
    ctypedef struct Vector3:
    	float x;  # Vector x component
    	float y;  # Vector y component
    	float z;  # Vector z component
    
    
    #  Vector4, 4 components
    ctypedef struct Vector4:
    	float x;  # Vector x component
    	float y;  # Vector y component
    	float z;  # Vector z component
    	float w;  # Vector w component
    
    
    #  Color, 4 components, R8G8B8A8 (32bit)
    ctypedef struct Color:
    	unsigned char r;  # Color red value
    	unsigned char g;  # Color green value
    	unsigned char b;  # Color blue value
    	unsigned char a;  # Color alpha value
    
    
    #  Rectangle, 4 components
    ctypedef struct Rectangle:
    	float x;  # Rectangle top-left corner position x
    	float y;  # Rectangle top-left corner position y
    	float width;  # Rectangle width
    	float height;  # Rectangle height
    
    
    #  Image, pixel data stored in CPU memory (RAM)
    ctypedef struct Image:
    	void * data;  # Image raw data
    	int width;  # Image base width
    	int height;  # Image base height
    	int mipmaps;  # Mipmap levels, 1 by default
    	int format;  # Data format (PixelFormat type)
    
    
    #  Texture, tex data stored in GPU memory (VRAM)
    ctypedef struct Texture:
    	unsigned int id;  # OpenGL texture id
    	int width;  # Texture base width
    	int height;  # Texture base height
    	int mipmaps;  # Mipmap levels, 1 by default
    	int format;  # Data format (PixelFormat type)
    
    
    #  RenderTexture, fbo for texture rendering
    ctypedef struct RenderTexture:
    	unsigned int id;  # OpenGL framebuffer object id
    	Texture texture;  # Color buffer attachment texture
    	Texture depth;  # Depth buffer attachment texture
    
    
    #  NPatchInfo, n-patch layout info
    ctypedef struct NPatchInfo:
    	Rectangle source;  # Texture source rectangle
    	int left;  # Left border offset
    	int top;  # Top border offset
    	int right;  # Right border offset
    	int bottom;  # Bottom border offset
    	int layout;  # Layout of the n-patch: 3x3, 1x3 or 3x1
    
    
    #  GlyphInfo, font characters glyphs info
    ctypedef struct GlyphInfo:
    	int value;  # Character value (Unicode)
    	int offsetX;  # Character offset X when drawing
    	int offsetY;  # Character offset Y when drawing
    	int advanceX;  # Character advance position X
    	Image image;  # Character image data
    
    
    #  Font, font texture and GlyphInfo array data
    ctypedef struct Font:
    	int baseSize;  # Base size (default chars height)
    	int glyphCount;  # Number of glyph characters
    	int glyphPadding;  # Padding around the glyph characters
    	Texture2D texture;  # Texture atlas containing the glyphs
    	Rectangle * recs;  # Rectangles in texture for the glyphs
    	GlyphInfo * glyphs;  # Glyphs info data
    
    
    #  Camera, defines position/orientation in 3d space
    ctypedef struct Camera3D:
    	Vector3 position;  # Camera position
    	Vector3 target;  # Camera target it looks-at
    	Vector3 up;  # Camera up vector (rotation over its axis)
    	float fovy;  # Camera field-of-view apperture in Y (degrees) in perspective, used as near plane width in orthographic
    	int projection;  # Camera projection: CAMERA_PERSPECTIVE or CAMERA_ORTHOGRAPHIC
    
    
    #  Camera2D, defines position/orientation in 2d space
    ctypedef struct Camera2D:
    	Vector2 offset;  # Camera offset (displacement from target)
    	Vector2 target;  # Camera target (rotation and zoom origin)
    	float rotation;  # Camera rotation in degrees
    	float zoom;  # Camera zoom (scaling), should be 1.0f by default
    
    
    #  Mesh, vertex data and vao/vbo
    ctypedef struct Mesh:
    	int vertexCount;  # Number of vertices stored in arrays
    	int triangleCount;  # Number of triangles stored (indexed or not)
    	float * vertices;  # Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
    	float * texcoords;  # Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
    	float * texcoords2;  # Vertex texture second coordinates (UV - 2 components per vertex) (shader-location = 5)
    	float * normals;  # Vertex normals (XYZ - 3 components per vertex) (shader-location = 2)
    	float * tangents;  # Vertex tangents (XYZW - 4 components per vertex) (shader-location = 4)
    	unsigned char * colors;  # Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
    	unsigned short * indices;  # Vertex indices (in case vertex data comes indexed)
    	float * animVertices;  # Animated vertex positions (after bones transformations)
    	float * animNormals;  # Animated normals (after bones transformations)
    	unsigned char * boneIds;  # Vertex bone ids, max 255 bone ids, up to 4 bones influence by vertex (skinning)
    	float * boneWeights;  # Vertex bone weight, up to 4 bones influence by vertex (skinning)
    	unsigned int vaoId;  # OpenGL Vertex Array Object id
    	unsigned int * vboId;  # OpenGL Vertex Buffer Objects id (default vertex data)
    
    
    #  Shader
    ctypedef struct Shader:
    	unsigned int id;  # Shader program id
    	int * locs;  # Shader locations array (RL_MAX_SHADER_LOCATIONS)
    
    
    #  MaterialMap
    ctypedef struct MaterialMap:
    	Texture2D texture;  # Material map texture
    	Color color;  # Material map color
    	float value;  # Material map value
    
    
    #  Material, includes shader and maps
    ctypedef struct Material:
    	Shader shader;  # Material shader
    	MaterialMap * maps;  # Material maps array (MAX_MATERIAL_MAPS)
    	float[4] params;  # Material generic parameters (if required)
    
    
    #  Transform, vectex transformation data
    ctypedef struct Transform:
    	Vector3 translation;  # Translation
    	Quaternion rotation;  # Rotation
    	Vector3 scale;  # Scale
    
    
    #  Bone, skeletal animation bone
    ctypedef struct BoneInfo:
    	char[32] name;  # Bone name
    	int parent;  # Bone parent
    
    
    #  Model, meshes, materials and animation data
    ctypedef struct Model:
    	Matrix transform;  # Local transform matrix
    	int meshCount;  # Number of meshes
    	int materialCount;  # Number of materials
    	Mesh * meshes;  # Meshes array
    	Material * materials;  # Materials array
    	int * meshMaterial;  # Mesh material number
    	int boneCount;  # Number of bones
    	BoneInfo * bones;  # Bones information (skeleton)
    	Transform * bindPose;  # Bones base transformation (pose)
    
    
    #  ModelAnimation
    ctypedef struct ModelAnimation:
    	int boneCount;  # Number of bones
    	int frameCount;  # Number of animation frames
    	BoneInfo * bones;  # Bones information (skeleton)
    	Transform ** framePoses;  # Poses array by frame
    
    
    #  Ray, ray for raycasting
    ctypedef struct Ray:
    	Vector3 position;  # Ray position (origin)
    	Vector3 direction;  # Ray direction
    
    
    #  RayCollision, ray hit information
    ctypedef struct RayCollision:
    	bool hit;  # Did the ray hit something?
    	float distance;  # Distance to nearest hit
    	Vector3 point;  # Point of nearest hit
    	Vector3 normal;  # Surface normal of hit
    
    
    #  BoundingBox
    ctypedef struct BoundingBox:
    	Vector3 min;  # Minimum vertex box-corner
    	Vector3 max;  # Maximum vertex box-corner
    
    
    #  Wave, audio wave data
    ctypedef struct Wave:
    	unsigned int frameCount;  # Total number of frames (considering channels)
    	unsigned int sampleRate;  # Frequency (samples per second)
    	unsigned int sampleSize;  # Bit depth (bits per sample): 8, 16, 32 (24 not supported)
    	unsigned int channels;  # Number of channels (1-mono, 2-stereo, ...)
    	void * data;  # Buffer data pointer
    
    
    #  AudioStream, custom audio stream
    ctypedef struct AudioStream:
    	rAudioBuffer * buffer;  # Pointer to internal data used by the audio system
    	rAudioProcessor * processor;  # Pointer to internal data processor, useful for audio effects
    	unsigned int sampleRate;  # Frequency (samples per second)
    	unsigned int sampleSize;  # Bit depth (bits per sample): 8, 16, 32 (24 not supported)
    	unsigned int channels;  # Number of channels (1-mono, 2-stereo, ...)
    
    
    #  Sound
    ctypedef struct Sound:
    	AudioStream stream;  # Audio stream
    	unsigned int frameCount;  # Total number of frames (considering channels)
    
    
    #  Music, audio stream, anything longer than ~10 seconds should be streamed
    ctypedef struct Music:
    	AudioStream stream;  # Audio stream
    	unsigned int frameCount;  # Total number of frames (considering channels)
    	bool looping;  # Music looping enable
    	int ctxType;  # Type of music context (audio filetype)
    	void * ctxData;  # Audio context data, depends on type
    
    
    #  VrDeviceInfo, Head-Mounted-Display device parameters
    ctypedef struct VrDeviceInfo:
    	int hResolution;  # Horizontal resolution in pixels
    	int vResolution;  # Vertical resolution in pixels
    	float hScreenSize;  # Horizontal size in meters
    	float vScreenSize;  # Vertical size in meters
    	float vScreenCenter;  # Screen center in meters
    	float eyeToScreenDistance;  # Distance between eye and display in meters
    	float lensSeparationDistance;  # Lens separation distance in meters
    	float interpupillaryDistance;  # IPD (distance between pupils) in meters
    	float[4] lensDistortionValues;  # Lens distortion constant parameters
    	float[4] chromaAbCorrection;  # Chromatic aberration correction parameters
    
    
    #  VrStereoConfig, VR stereo rendering configuration for simulator
    ctypedef struct VrStereoConfig:
    	Matrix[2] projection;  # VR projection matrices (per eye)
    	Matrix[2] viewOffset;  # VR view offset matrices (per eye)
    	float[2] leftLensCenter;  # VR left lens center
    	float[2] rightLensCenter;  # VR right lens center
    	float[2] leftScreenCenter;  # VR left screen center
    	float[2] rightScreenCenter;  # VR right screen center
    	float[2] scale;  # VR distortion scale
    	float[2] scaleIn;  # VR distortion scale in
    
    
    #  File path list
    ctypedef struct FilePathList:
    	unsigned int capacity;  # Filepaths max entries
    	unsigned int count;  # Filepaths entries count
    	char ** paths;  # Filepaths entries
    
    

cdef extern from "raymath.h":
    cdef float EPSILON = 1e-06

    #  NOTE: Helper types to be used instead of array return types for *ToFloat functions
    ctypedef struct float3:
    	float[3] v;
    
    
    #  
    ctypedef struct float16:
    	float[16] v;
    
    

cdef extern from "raygui.h":
    cdef char* RAYGUI_VERSION = "3.2"
    cdef int SCROLLBAR_LEFT_SIDE = 0
    cdef int SCROLLBAR_RIGHT_SIDE = 1
    cdef int RAYGUI_ICON_SIZE = 16  # Size of icons in pixels (squared)
    cdef int RAYGUI_ICON_MAX_ICONS = 256  # Maximum number of icons
    cdef int RAYGUI_ICON_MAX_NAME_LENGTH = 32  # Maximum length of icon name id
    cdef int RAYGUI_MAX_CONTROLS = 16  # Maximum number of standard controls
    cdef int RAYGUI_MAX_PROPS_BASE = 16  # Maximum number of standard properties
    cdef int RAYGUI_MAX_PROPS_EXTENDED = 8  # Maximum number of extended properties
    cdef int KEY_RIGHT = 262
    cdef int KEY_LEFT = 263
    cdef int KEY_DOWN = 264
    cdef int KEY_UP = 265
    cdef int KEY_BACKSPACE = 259
    cdef int KEY_ENTER = 257
    cdef int RAYGUI_WINDOWBOX_STATUSBAR_HEIGHT = 24
    cdef int RAYGUI_GROUPBOX_LINE_THICK = 1
    cdef int RAYGUI_LINE_MARGIN_TEXT = 12
    cdef int RAYGUI_LINE_TEXT_PADDING = 4
    cdef int RAYGUI_PANEL_BORDER_WIDTH = 1
    cdef int RAYGUI_TOGGLEGROUP_MAX_ITEMS = 32
    cdef int RAYGUI_VALUEBOX_MAX_CHARS = 32
    cdef int RAYGUI_COLORBARALPHA_CHECKED_SIZE = 10
    cdef int RAYGUI_MESSAGEBOX_BUTTON_HEIGHT = 24
    cdef int RAYGUI_MESSAGEBOX_BUTTON_PADDING = 12
    cdef int RAYGUI_TEXTINPUTBOX_BUTTON_HEIGHT = 28
    cdef int RAYGUI_TEXTINPUTBOX_BUTTON_PADDING = 12
    cdef int RAYGUI_TEXTINPUTBOX_HEIGHT = 28
    cdef float RAYGUI_GRID_ALPHA = 0.15
    cdef int MAX_LINE_BUFFER_SIZE = 256
    cdef int ICON_TEXT_PADDING = 4
    cdef int RAYGUI_TEXTSPLIT_MAX_ITEMS = 128
    cdef int RAYGUI_TEXTSPLIT_MAX_TEXT_SIZE = 1024
    cdef int RAYGUI_TEXTFORMAT_MAX_SIZE = 256

    #  It should be redesigned to be provided by user
    ctypedef struct Texture2D:
    	unsigned int id;  # OpenGL texture id
    	int width;  # Texture base width
    	int height;  # Texture base height
    	int mipmaps;  # Mipmap levels, 1 by default
    	int format;  # Data format (PixelFormat type)
    
    
    #  Style property
    ctypedef struct GuiStyleProp:
    	unsigned short controlId;
    	unsigned short propertyId;
    	unsigned int propertyValue;
    
    

