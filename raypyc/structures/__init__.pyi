import ctypes
from raypyc.defines import *
from typing import Type


class rAudioBuffer(ctypes.Structure):
	"""dummy structure"""
	@property
	def buffer(self) -> ctypes.c_byte * 392:
		...

	@buffer.setter
	def buffer(self, i: ctypes.c_byte * 392) -> None:
		...


class rAudioProcessor(ctypes.Structure):
	"""dummy structure"""
	@property
	def buffer(self) -> ctypes.c_byte * 24:
		...

	@buffer.setter
	def buffer(self, i: ctypes.c_byte * 24) -> None:
		...


class rlVertexBuffer(ctypes.Structure):
	"""Dynamic vertex buffers (position + texcoords + colors + indices arrays)"""
	@property
	def elementCount(self) -> ctypes.c_int:
		...

	@elementCount.setter
	def elementCount(self, i: ctypes.c_int) -> None:
		...

	@property
	def vertices(self) -> ctypes.POINTER(ctypes.c_float):
		...

	@vertices.setter
	def vertices(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
		...

	@property
	def texcoords(self) -> ctypes.POINTER(ctypes.c_float):
		...

	@texcoords.setter
	def texcoords(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
		...

	@property
	def colors(self) -> ctypes.POINTER(ctypes.c_ubyte):
		...

	@colors.setter
	def colors(self, i: ctypes.POINTER(ctypes.c_ubyte)) -> None:
		...

	@property
	def vaoId(self) -> ctypes.c_uint:
		...

	@vaoId.setter
	def vaoId(self, i: ctypes.c_uint) -> None:
		...

	@property
	def vboId(self) -> ctypes.c_uint * 4:
		...

	@vboId.setter
	def vboId(self, i: ctypes.c_uint * 4) -> None:
		...


class rlDrawCall(ctypes.Structure):
	"""of those state-change happens (this is done in core module)"""
	@property
	def mode(self) -> ctypes.c_int:
		...

	@mode.setter
	def mode(self, i: ctypes.c_int) -> None:
		...

	@property
	def vertexCount(self) -> ctypes.c_int:
		...

	@vertexCount.setter
	def vertexCount(self, i: ctypes.c_int) -> None:
		...

	@property
	def vertexAlignment(self) -> ctypes.c_int:
		...

	@vertexAlignment.setter
	def vertexAlignment(self, i: ctypes.c_int) -> None:
		...

	@property
	def textureId(self) -> ctypes.c_uint:
		...

	@textureId.setter
	def textureId(self, i: ctypes.c_uint) -> None:
		...


class rlRenderBatch(ctypes.Structure):
	"""rlRenderBatch type"""
	@property
	def bufferCount(self) -> ctypes.c_int:
		...

	@bufferCount.setter
	def bufferCount(self, i: ctypes.c_int) -> None:
		...

	@property
	def currentBuffer(self) -> ctypes.c_int:
		...

	@currentBuffer.setter
	def currentBuffer(self, i: ctypes.c_int) -> None:
		...

	@property
	def vertexBuffer(self) -> ctypes.POINTER(rlVertexBuffer):
		...

	@vertexBuffer.setter
	def vertexBuffer(self, i: ctypes.POINTER(rlVertexBuffer)) -> None:
		...

	@property
	def draws(self) -> ctypes.POINTER(rlDrawCall):
		...

	@draws.setter
	def draws(self, i: ctypes.POINTER(rlDrawCall)) -> None:
		...

	@property
	def drawCounter(self) -> ctypes.c_int:
		...

	@drawCounter.setter
	def drawCounter(self, i: ctypes.c_int) -> None:
		...

	@property
	def currentDepth(self) -> ctypes.c_float:
		...

	@currentDepth.setter
	def currentDepth(self, i: ctypes.c_float) -> None:
		...


class Vector2(ctypes.Structure):
	"""Vector2, 2 components"""
	@property
	def x(self) -> ctypes.c_float:
		...

	@x.setter
	def x(self, i: ctypes.c_float) -> None:
		...

	@property
	def y(self) -> ctypes.c_float:
		...

	@y.setter
	def y(self, i: ctypes.c_float) -> None:
		...


class Vector3(ctypes.Structure):
	"""Vector3, 3 components"""
	@property
	def x(self) -> ctypes.c_float:
		...

	@x.setter
	def x(self, i: ctypes.c_float) -> None:
		...

	@property
	def y(self) -> ctypes.c_float:
		...

	@y.setter
	def y(self, i: ctypes.c_float) -> None:
		...

	@property
	def z(self) -> ctypes.c_float:
		...

	@z.setter
	def z(self, i: ctypes.c_float) -> None:
		...


class Vector4(ctypes.Structure):
	"""Vector4, 4 components"""
	@property
	def x(self) -> ctypes.c_float:
		...

	@x.setter
	def x(self, i: ctypes.c_float) -> None:
		...

	@property
	def y(self) -> ctypes.c_float:
		...

	@y.setter
	def y(self, i: ctypes.c_float) -> None:
		...

	@property
	def z(self) -> ctypes.c_float:
		...

	@z.setter
	def z(self, i: ctypes.c_float) -> None:
		...

	@property
	def w(self) -> ctypes.c_float:
		...

	@w.setter
	def w(self, i: ctypes.c_float) -> None:
		...


Quaternion = Vector4


class Matrix(ctypes.Structure):
	"""Matrix, 4x4 components, column major, OpenGL style, right-handed"""
	@property
	def m0(self) -> ctypes.c_float:
		...

	@m0.setter
	def m0(self, i: ctypes.c_float) -> None:
		...

	@property
	def m4(self) -> ctypes.c_float:
		...

	@m4.setter
	def m4(self, i: ctypes.c_float) -> None:
		...

	@property
	def m8(self) -> ctypes.c_float:
		...

	@m8.setter
	def m8(self, i: ctypes.c_float) -> None:
		...

	@property
	def m12(self) -> ctypes.c_float:
		...

	@m12.setter
	def m12(self, i: ctypes.c_float) -> None:
		...

	@property
	def m1(self) -> ctypes.c_float:
		...

	@m1.setter
	def m1(self, i: ctypes.c_float) -> None:
		...

	@property
	def m5(self) -> ctypes.c_float:
		...

	@m5.setter
	def m5(self, i: ctypes.c_float) -> None:
		...

	@property
	def m9(self) -> ctypes.c_float:
		...

	@m9.setter
	def m9(self, i: ctypes.c_float) -> None:
		...

	@property
	def m13(self) -> ctypes.c_float:
		...

	@m13.setter
	def m13(self, i: ctypes.c_float) -> None:
		...

	@property
	def m2(self) -> ctypes.c_float:
		...

	@m2.setter
	def m2(self, i: ctypes.c_float) -> None:
		...

	@property
	def m6(self) -> ctypes.c_float:
		...

	@m6.setter
	def m6(self, i: ctypes.c_float) -> None:
		...

	@property
	def m10(self) -> ctypes.c_float:
		...

	@m10.setter
	def m10(self, i: ctypes.c_float) -> None:
		...

	@property
	def m14(self) -> ctypes.c_float:
		...

	@m14.setter
	def m14(self, i: ctypes.c_float) -> None:
		...

	@property
	def m3(self) -> ctypes.c_float:
		...

	@m3.setter
	def m3(self, i: ctypes.c_float) -> None:
		...

	@property
	def m7(self) -> ctypes.c_float:
		...

	@m7.setter
	def m7(self, i: ctypes.c_float) -> None:
		...

	@property
	def m11(self) -> ctypes.c_float:
		...

	@m11.setter
	def m11(self, i: ctypes.c_float) -> None:
		...

	@property
	def m15(self) -> ctypes.c_float:
		...

	@m15.setter
	def m15(self, i: ctypes.c_float) -> None:
		...


class Color(ctypes.Structure):
	"""Color, 4 components, R8G8B8A8 (32bit)"""
	@property
	def r(self) -> ctypes.c_ubyte:
		...

	@r.setter
	def r(self, i: ctypes.c_ubyte) -> None:
		...

	@property
	def g(self) -> ctypes.c_ubyte:
		...

	@g.setter
	def g(self, i: ctypes.c_ubyte) -> None:
		...

	@property
	def b(self) -> ctypes.c_ubyte:
		...

	@b.setter
	def b(self, i: ctypes.c_ubyte) -> None:
		...

	@property
	def a(self) -> ctypes.c_ubyte:
		...

	@a.setter
	def a(self, i: ctypes.c_ubyte) -> None:
		...


class Rectangle(ctypes.Structure):
	"""Rectangle, 4 components"""
	@property
	def x(self) -> ctypes.c_float:
		...

	@x.setter
	def x(self, i: ctypes.c_float) -> None:
		...

	@property
	def y(self) -> ctypes.c_float:
		...

	@y.setter
	def y(self, i: ctypes.c_float) -> None:
		...

	@property
	def width(self) -> ctypes.c_float:
		...

	@width.setter
	def width(self, i: ctypes.c_float) -> None:
		...

	@property
	def height(self) -> ctypes.c_float:
		...

	@height.setter
	def height(self, i: ctypes.c_float) -> None:
		...


class Image(ctypes.Structure):
	"""Image, pixel data stored in CPU memory (RAM)"""
	@property
	def data(self) -> ctypes.c_void_p:
		...

	@data.setter
	def data(self, i: ctypes.c_void_p) -> None:
		...

	@property
	def width(self) -> ctypes.c_int:
		...

	@width.setter
	def width(self, i: ctypes.c_int) -> None:
		...

	@property
	def height(self) -> ctypes.c_int:
		...

	@height.setter
	def height(self, i: ctypes.c_int) -> None:
		...

	@property
	def mipmaps(self) -> ctypes.c_int:
		...

	@mipmaps.setter
	def mipmaps(self, i: ctypes.c_int) -> None:
		...

	@property
	def format(self) -> ctypes.c_int:
		...

	@format.setter
	def format(self, i: ctypes.c_int) -> None:
		...


class Texture(ctypes.Structure):
	"""Texture, tex data stored in GPU memory (VRAM)"""
	@property
	def id(self) -> ctypes.c_uint:
		...

	@id.setter
	def id(self, i: ctypes.c_uint) -> None:
		...

	@property
	def width(self) -> ctypes.c_int:
		...

	@width.setter
	def width(self, i: ctypes.c_int) -> None:
		...

	@property
	def height(self) -> ctypes.c_int:
		...

	@height.setter
	def height(self, i: ctypes.c_int) -> None:
		...

	@property
	def mipmaps(self) -> ctypes.c_int:
		...

	@mipmaps.setter
	def mipmaps(self, i: ctypes.c_int) -> None:
		...

	@property
	def format(self) -> ctypes.c_int:
		...

	@format.setter
	def format(self, i: ctypes.c_int) -> None:
		...


Texture2D = Texture


TextureCubemap = Texture


class RenderTexture(ctypes.Structure):
	"""RenderTexture, fbo for texture rendering"""
	@property
	def id(self) -> ctypes.c_uint:
		...

	@id.setter
	def id(self, i: ctypes.c_uint) -> None:
		...

	@property
	def texture(self) -> Texture:
		...

	@texture.setter
	def texture(self, i: Texture) -> None:
		...

	@property
	def depth(self) -> Texture:
		...

	@depth.setter
	def depth(self, i: Texture) -> None:
		...


RenderTexture2D = RenderTexture


class NPatchInfo(ctypes.Structure):
	"""NPatchInfo, n-patch layout info"""
	@property
	def source(self) -> Rectangle:
		...

	@source.setter
	def source(self, i: Rectangle) -> None:
		...

	@property
	def left(self) -> ctypes.c_int:
		...

	@left.setter
	def left(self, i: ctypes.c_int) -> None:
		...

	@property
	def top(self) -> ctypes.c_int:
		...

	@top.setter
	def top(self, i: ctypes.c_int) -> None:
		...

	@property
	def right(self) -> ctypes.c_int:
		...

	@right.setter
	def right(self, i: ctypes.c_int) -> None:
		...

	@property
	def bottom(self) -> ctypes.c_int:
		...

	@bottom.setter
	def bottom(self, i: ctypes.c_int) -> None:
		...

	@property
	def layout(self) -> ctypes.c_int:
		...

	@layout.setter
	def layout(self, i: ctypes.c_int) -> None:
		...


class GlyphInfo(ctypes.Structure):
	"""GlyphInfo, font characters glyphs info"""
	@property
	def value(self) -> ctypes.c_int:
		...

	@value.setter
	def value(self, i: ctypes.c_int) -> None:
		...

	@property
	def offsetX(self) -> ctypes.c_int:
		...

	@offsetX.setter
	def offsetX(self, i: ctypes.c_int) -> None:
		...

	@property
	def offsetY(self) -> ctypes.c_int:
		...

	@offsetY.setter
	def offsetY(self, i: ctypes.c_int) -> None:
		...

	@property
	def advanceX(self) -> ctypes.c_int:
		...

	@advanceX.setter
	def advanceX(self, i: ctypes.c_int) -> None:
		...

	@property
	def image(self) -> Image:
		...

	@image.setter
	def image(self, i: Image) -> None:
		...


class Font(ctypes.Structure):
	"""Font, font texture and GlyphInfo array data"""
	@property
	def baseSize(self) -> ctypes.c_int:
		...

	@baseSize.setter
	def baseSize(self, i: ctypes.c_int) -> None:
		...

	@property
	def glyphCount(self) -> ctypes.c_int:
		...

	@glyphCount.setter
	def glyphCount(self, i: ctypes.c_int) -> None:
		...

	@property
	def glyphPadding(self) -> ctypes.c_int:
		...

	@glyphPadding.setter
	def glyphPadding(self, i: ctypes.c_int) -> None:
		...

	@property
	def texture(self) -> Texture2D:
		...

	@texture.setter
	def texture(self, i: Texture2D) -> None:
		...

	@property
	def recs(self) -> ctypes.POINTER(Rectangle):
		...

	@recs.setter
	def recs(self, i: ctypes.POINTER(Rectangle)) -> None:
		...

	@property
	def glyphs(self) -> ctypes.POINTER(GlyphInfo):
		...

	@glyphs.setter
	def glyphs(self, i: ctypes.POINTER(GlyphInfo)) -> None:
		...


class Camera3D(ctypes.Structure):
	"""Camera, defines position/orientation in 3d space"""
	@property
	def position(self) -> Vector3:
		...

	@position.setter
	def position(self, i: Vector3) -> None:
		...

	@property
	def target(self) -> Vector3:
		...

	@target.setter
	def target(self, i: Vector3) -> None:
		...

	@property
	def up(self) -> Vector3:
		...

	@up.setter
	def up(self, i: Vector3) -> None:
		...

	@property
	def fovy(self) -> ctypes.c_float:
		...

	@fovy.setter
	def fovy(self, i: ctypes.c_float) -> None:
		...

	@property
	def projection(self) -> ctypes.c_int:
		...

	@projection.setter
	def projection(self, i: ctypes.c_int) -> None:
		...


Camera = Camera3D


class Camera2D(ctypes.Structure):
	"""Camera2D, defines position/orientation in 2d space"""
	@property
	def offset(self) -> Vector2:
		...

	@offset.setter
	def offset(self, i: Vector2) -> None:
		...

	@property
	def target(self) -> Vector2:
		...

	@target.setter
	def target(self, i: Vector2) -> None:
		...

	@property
	def rotation(self) -> ctypes.c_float:
		...

	@rotation.setter
	def rotation(self, i: ctypes.c_float) -> None:
		...

	@property
	def zoom(self) -> ctypes.c_float:
		...

	@zoom.setter
	def zoom(self, i: ctypes.c_float) -> None:
		...


class Mesh(ctypes.Structure):
	"""Mesh, vertex data and vao/vbo"""
	@property
	def vertexCount(self) -> ctypes.c_int:
		...

	@vertexCount.setter
	def vertexCount(self, i: ctypes.c_int) -> None:
		...

	@property
	def triangleCount(self) -> ctypes.c_int:
		...

	@triangleCount.setter
	def triangleCount(self, i: ctypes.c_int) -> None:
		...

	@property
	def vertices(self) -> ctypes.POINTER(ctypes.c_float):
		...

	@vertices.setter
	def vertices(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
		...

	@property
	def texcoords(self) -> ctypes.POINTER(ctypes.c_float):
		...

	@texcoords.setter
	def texcoords(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
		...

	@property
	def texcoords2(self) -> ctypes.POINTER(ctypes.c_float):
		...

	@texcoords2.setter
	def texcoords2(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
		...

	@property
	def normals(self) -> ctypes.POINTER(ctypes.c_float):
		...

	@normals.setter
	def normals(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
		...

	@property
	def tangents(self) -> ctypes.POINTER(ctypes.c_float):
		...

	@tangents.setter
	def tangents(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
		...

	@property
	def colors(self) -> ctypes.POINTER(ctypes.c_ubyte):
		...

	@colors.setter
	def colors(self, i: ctypes.POINTER(ctypes.c_ubyte)) -> None:
		...

	@property
	def indices(self) -> ctypes.POINTER(ctypes.c_ushort):
		...

	@indices.setter
	def indices(self, i: ctypes.POINTER(ctypes.c_ushort)) -> None:
		...

	@property
	def animVertices(self) -> ctypes.POINTER(ctypes.c_float):
		...

	@animVertices.setter
	def animVertices(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
		...

	@property
	def animNormals(self) -> ctypes.POINTER(ctypes.c_float):
		...

	@animNormals.setter
	def animNormals(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
		...

	@property
	def boneIds(self) -> ctypes.POINTER(ctypes.c_ubyte):
		...

	@boneIds.setter
	def boneIds(self, i: ctypes.POINTER(ctypes.c_ubyte)) -> None:
		...

	@property
	def boneWeights(self) -> ctypes.POINTER(ctypes.c_float):
		...

	@boneWeights.setter
	def boneWeights(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
		...

	@property
	def vaoId(self) -> ctypes.c_uint:
		...

	@vaoId.setter
	def vaoId(self, i: ctypes.c_uint) -> None:
		...

	@property
	def vboId(self) -> ctypes.POINTER(ctypes.c_uint):
		...

	@vboId.setter
	def vboId(self, i: ctypes.POINTER(ctypes.c_uint)) -> None:
		...


class Shader(ctypes.Structure):
	"""Shader"""
	@property
	def id(self) -> ctypes.c_uint:
		...

	@id.setter
	def id(self, i: ctypes.c_uint) -> None:
		...

	@property
	def locs(self) -> ctypes.POINTER(ctypes.c_int):
		...

	@locs.setter
	def locs(self, i: ctypes.POINTER(ctypes.c_int)) -> None:
		...


class MaterialMap(ctypes.Structure):
	"""MaterialMap"""
	@property
	def texture(self) -> Texture2D:
		...

	@texture.setter
	def texture(self, i: Texture2D) -> None:
		...

	@property
	def color(self) -> Color:
		...

	@color.setter
	def color(self, i: Color) -> None:
		...

	@property
	def value(self) -> ctypes.c_float:
		...

	@value.setter
	def value(self, i: ctypes.c_float) -> None:
		...


class Material(ctypes.Structure):
	"""Material, includes shader and maps"""
	@property
	def shader(self) -> Shader:
		...

	@shader.setter
	def shader(self, i: Shader) -> None:
		...

	@property
	def maps(self) -> ctypes.POINTER(MaterialMap):
		...

	@maps.setter
	def maps(self, i: ctypes.POINTER(MaterialMap)) -> None:
		...

	@property
	def params(self) -> ctypes.c_float * 4:
		...

	@params.setter
	def params(self, i: ctypes.c_float * 4) -> None:
		...


class Transform(ctypes.Structure):
	"""Transform, vertex transformation data"""
	@property
	def translation(self) -> Vector3:
		...

	@translation.setter
	def translation(self, i: Vector3) -> None:
		...

	@property
	def rotation(self) -> Quaternion:
		...

	@rotation.setter
	def rotation(self, i: Quaternion) -> None:
		...

	@property
	def scale(self) -> Vector3:
		...

	@scale.setter
	def scale(self, i: Vector3) -> None:
		...


class BoneInfo(ctypes.Structure):
	"""Bone, skeletal animation bone"""
	@property
	def name(self) -> ctypes.c_char * 32:
		...

	@name.setter
	def name(self, i: ctypes.c_char * 32) -> None:
		...

	@property
	def parent(self) -> ctypes.c_int:
		...

	@parent.setter
	def parent(self, i: ctypes.c_int) -> None:
		...


class Model(ctypes.Structure):
	"""Model, meshes, materials and animation data"""
	@property
	def transform(self) -> Matrix:
		...

	@transform.setter
	def transform(self, i: Matrix) -> None:
		...

	@property
	def meshCount(self) -> ctypes.c_int:
		...

	@meshCount.setter
	def meshCount(self, i: ctypes.c_int) -> None:
		...

	@property
	def materialCount(self) -> ctypes.c_int:
		...

	@materialCount.setter
	def materialCount(self, i: ctypes.c_int) -> None:
		...

	@property
	def meshes(self) -> ctypes.POINTER(Mesh):
		...

	@meshes.setter
	def meshes(self, i: ctypes.POINTER(Mesh)) -> None:
		...

	@property
	def materials(self) -> ctypes.POINTER(Material):
		...

	@materials.setter
	def materials(self, i: ctypes.POINTER(Material)) -> None:
		...

	@property
	def meshMaterial(self) -> ctypes.POINTER(ctypes.c_int):
		...

	@meshMaterial.setter
	def meshMaterial(self, i: ctypes.POINTER(ctypes.c_int)) -> None:
		...

	@property
	def boneCount(self) -> ctypes.c_int:
		...

	@boneCount.setter
	def boneCount(self, i: ctypes.c_int) -> None:
		...

	@property
	def bones(self) -> ctypes.POINTER(BoneInfo):
		...

	@bones.setter
	def bones(self, i: ctypes.POINTER(BoneInfo)) -> None:
		...

	@property
	def bindPose(self) -> ctypes.POINTER(Transform):
		...

	@bindPose.setter
	def bindPose(self, i: ctypes.POINTER(Transform)) -> None:
		...


class ModelAnimation(ctypes.Structure):
	"""ModelAnimation"""
	@property
	def boneCount(self) -> ctypes.c_int:
		...

	@boneCount.setter
	def boneCount(self, i: ctypes.c_int) -> None:
		...

	@property
	def frameCount(self) -> ctypes.c_int:
		...

	@frameCount.setter
	def frameCount(self, i: ctypes.c_int) -> None:
		...

	@property
	def bones(self) -> ctypes.POINTER(BoneInfo):
		...

	@bones.setter
	def bones(self, i: ctypes.POINTER(BoneInfo)) -> None:
		...

	@property
	def framePoses(self) -> ctypes.POINTER(ctypes.POINTER(Transform)):
		...

	@framePoses.setter
	def framePoses(self, i: ctypes.POINTER(ctypes.POINTER(Transform))) -> None:
		...


class Ray(ctypes.Structure):
	"""Ray, ray for raycasting"""
	@property
	def position(self) -> Vector3:
		...

	@position.setter
	def position(self, i: Vector3) -> None:
		...

	@property
	def direction(self) -> Vector3:
		...

	@direction.setter
	def direction(self, i: Vector3) -> None:
		...


class RayCollision(ctypes.Structure):
	"""RayCollision, ray hit information"""
	@property
	def hit(self) -> ctypes.c_bool:
		...

	@hit.setter
	def hit(self, i: ctypes.c_bool) -> None:
		...

	@property
	def distance(self) -> ctypes.c_float:
		...

	@distance.setter
	def distance(self, i: ctypes.c_float) -> None:
		...

	@property
	def point(self) -> Vector3:
		...

	@point.setter
	def point(self, i: Vector3) -> None:
		...

	@property
	def normal(self) -> Vector3:
		...

	@normal.setter
	def normal(self, i: Vector3) -> None:
		...


class BoundingBox(ctypes.Structure):
	"""BoundingBox"""
	@property
	def min(self) -> Vector3:
		...

	@min.setter
	def min(self, i: Vector3) -> None:
		...

	@property
	def max(self) -> Vector3:
		...

	@max.setter
	def max(self, i: Vector3) -> None:
		...


class Wave(ctypes.Structure):
	"""Wave, audio wave data"""
	@property
	def frameCount(self) -> ctypes.c_uint:
		...

	@frameCount.setter
	def frameCount(self, i: ctypes.c_uint) -> None:
		...

	@property
	def sampleRate(self) -> ctypes.c_uint:
		...

	@sampleRate.setter
	def sampleRate(self, i: ctypes.c_uint) -> None:
		...

	@property
	def sampleSize(self) -> ctypes.c_uint:
		...

	@sampleSize.setter
	def sampleSize(self, i: ctypes.c_uint) -> None:
		...

	@property
	def channels(self) -> ctypes.c_uint:
		...

	@channels.setter
	def channels(self, i: ctypes.c_uint) -> None:
		...

	@property
	def data(self) -> ctypes.c_void_p:
		...

	@data.setter
	def data(self, i: ctypes.c_void_p) -> None:
		...


class AudioStream(ctypes.Structure):
	"""AudioStream, custom audio stream"""
	@property
	def buffer(self) -> ctypes.POINTER(rAudioBuffer):
		...

	@buffer.setter
	def buffer(self, i: ctypes.POINTER(rAudioBuffer)) -> None:
		...

	@property
	def processor(self) -> ctypes.POINTER(rAudioProcessor):
		...

	@processor.setter
	def processor(self, i: ctypes.POINTER(rAudioProcessor)) -> None:
		...

	@property
	def sampleRate(self) -> ctypes.c_uint:
		...

	@sampleRate.setter
	def sampleRate(self, i: ctypes.c_uint) -> None:
		...

	@property
	def sampleSize(self) -> ctypes.c_uint:
		...

	@sampleSize.setter
	def sampleSize(self, i: ctypes.c_uint) -> None:
		...

	@property
	def channels(self) -> ctypes.c_uint:
		...

	@channels.setter
	def channels(self, i: ctypes.c_uint) -> None:
		...


class Sound(ctypes.Structure):
	"""Sound"""
	@property
	def stream(self) -> AudioStream:
		...

	@stream.setter
	def stream(self, i: AudioStream) -> None:
		...

	@property
	def frameCount(self) -> ctypes.c_uint:
		...

	@frameCount.setter
	def frameCount(self, i: ctypes.c_uint) -> None:
		...


class Music(ctypes.Structure):
	"""Music, audio stream, anything longer than ~10 seconds should be streamed"""
	@property
	def stream(self) -> AudioStream:
		...

	@stream.setter
	def stream(self, i: AudioStream) -> None:
		...

	@property
	def frameCount(self) -> ctypes.c_uint:
		...

	@frameCount.setter
	def frameCount(self, i: ctypes.c_uint) -> None:
		...

	@property
	def looping(self) -> ctypes.c_bool:
		...

	@looping.setter
	def looping(self, i: ctypes.c_bool) -> None:
		...

	@property
	def ctxType(self) -> ctypes.c_int:
		...

	@ctxType.setter
	def ctxType(self, i: ctypes.c_int) -> None:
		...

	@property
	def ctxData(self) -> ctypes.c_void_p:
		...

	@ctxData.setter
	def ctxData(self, i: ctypes.c_void_p) -> None:
		...


class VrDeviceInfo(ctypes.Structure):
	"""VrDeviceInfo, Head-Mounted-Display device parameters"""
	@property
	def hResolution(self) -> ctypes.c_int:
		...

	@hResolution.setter
	def hResolution(self, i: ctypes.c_int) -> None:
		...

	@property
	def vResolution(self) -> ctypes.c_int:
		...

	@vResolution.setter
	def vResolution(self, i: ctypes.c_int) -> None:
		...

	@property
	def hScreenSize(self) -> ctypes.c_float:
		...

	@hScreenSize.setter
	def hScreenSize(self, i: ctypes.c_float) -> None:
		...

	@property
	def vScreenSize(self) -> ctypes.c_float:
		...

	@vScreenSize.setter
	def vScreenSize(self, i: ctypes.c_float) -> None:
		...

	@property
	def vScreenCenter(self) -> ctypes.c_float:
		...

	@vScreenCenter.setter
	def vScreenCenter(self, i: ctypes.c_float) -> None:
		...

	@property
	def eyeToScreenDistance(self) -> ctypes.c_float:
		...

	@eyeToScreenDistance.setter
	def eyeToScreenDistance(self, i: ctypes.c_float) -> None:
		...

	@property
	def lensSeparationDistance(self) -> ctypes.c_float:
		...

	@lensSeparationDistance.setter
	def lensSeparationDistance(self, i: ctypes.c_float) -> None:
		...

	@property
	def interpupillaryDistance(self) -> ctypes.c_float:
		...

	@interpupillaryDistance.setter
	def interpupillaryDistance(self, i: ctypes.c_float) -> None:
		...

	@property
	def lensDistortionValues(self) -> ctypes.c_float * 4:
		...

	@lensDistortionValues.setter
	def lensDistortionValues(self, i: ctypes.c_float * 4) -> None:
		...

	@property
	def chromaAbCorrection(self) -> ctypes.c_float * 4:
		...

	@chromaAbCorrection.setter
	def chromaAbCorrection(self, i: ctypes.c_float * 4) -> None:
		...


class VrStereoConfig(ctypes.Structure):
	"""VrStereoConfig, VR stereo rendering configuration for simulator"""
	@property
	def projection(self) -> Matrix * 2:
		...

	@projection.setter
	def projection(self, i: Matrix * 2) -> None:
		...

	@property
	def viewOffset(self) -> Matrix * 2:
		...

	@viewOffset.setter
	def viewOffset(self, i: Matrix * 2) -> None:
		...

	@property
	def leftLensCenter(self) -> ctypes.c_float * 2:
		...

	@leftLensCenter.setter
	def leftLensCenter(self, i: ctypes.c_float * 2) -> None:
		...

	@property
	def rightLensCenter(self) -> ctypes.c_float * 2:
		...

	@rightLensCenter.setter
	def rightLensCenter(self, i: ctypes.c_float * 2) -> None:
		...

	@property
	def leftScreenCenter(self) -> ctypes.c_float * 2:
		...

	@leftScreenCenter.setter
	def leftScreenCenter(self, i: ctypes.c_float * 2) -> None:
		...

	@property
	def rightScreenCenter(self) -> ctypes.c_float * 2:
		...

	@rightScreenCenter.setter
	def rightScreenCenter(self, i: ctypes.c_float * 2) -> None:
		...

	@property
	def scale(self) -> ctypes.c_float * 2:
		...

	@scale.setter
	def scale(self, i: ctypes.c_float * 2) -> None:
		...

	@property
	def scaleIn(self) -> ctypes.c_float * 2:
		...

	@scaleIn.setter
	def scaleIn(self, i: ctypes.c_float * 2) -> None:
		...


class FilePathList(ctypes.Structure):
	"""File path list"""
	@property
	def capacity(self) -> ctypes.c_uint:
		...

	@capacity.setter
	def capacity(self, i: ctypes.c_uint) -> None:
		...

	@property
	def count(self) -> ctypes.c_uint:
		...

	@count.setter
	def count(self, i: ctypes.c_uint) -> None:
		...

	@property
	def paths(self) -> ctypes.POINTER(ctypes.POINTER(ctypes.c_char)):
		...

	@paths.setter
	def paths(self, i: ctypes.POINTER(ctypes.POINTER(ctypes.c_char))) -> None:
		...


class float3(ctypes.Structure):
	"""NOTE: Helper types to be used instead of array return types for *ToFloat functions"""
	@property
	def v(self) -> ctypes.c_float * 3:
		...

	@v.setter
	def v(self, i: ctypes.c_float * 3) -> None:
		...


class float16(ctypes.Structure):
	""""""
	@property
	def v(self) -> ctypes.c_float * 16:
		...

	@v.setter
	def v(self, i: ctypes.c_float * 16) -> None:
		...


class GuiStyleProp(ctypes.Structure):
	"""Style property"""
	@property
	def controlId(self) -> ctypes.c_ushort:
		...

	@controlId.setter
	def controlId(self, i: ctypes.c_ushort) -> None:
		...

	@property
	def propertyId(self) -> ctypes.c_ushort:
		...

	@propertyId.setter
	def propertyId(self, i: ctypes.c_ushort) -> None:
		...

	@property
	def propertyValue(self) -> ctypes.c_uint:
		...

	@propertyValue.setter
	def propertyValue(self, i: ctypes.c_uint) -> None:
		...


__structs: dict[str, Type[rlVertexBuffer | rlDrawCall | rlRenderBatch | Vector2 | Vector3 | Vector4 | Quaternion | Matrix | Color | Rectangle | Image | Texture | Texture2D | TextureCubemap | RenderTexture | RenderTexture2D | NPatchInfo | GlyphInfo | Font | Camera3D | Camera | Camera2D | Mesh | Shader | MaterialMap | Material | Transform | BoneInfo | Model | ModelAnimation | Ray | RayCollision | BoundingBox | Wave | AudioStream | Sound | Music | VrDeviceInfo | VrStereoConfig | FilePathList | float3 | float16 | GuiStyleProp]] = {
	...
}
