from ctypes import *


class Vector2(Structure):
	"""Vector2, 2 components"""
	@property
	def x(self) -> float:
		pass

	@x.setter
	def x(self, i: float) -> None:
		pass

	@property
	def y(self) -> float:
		pass

	@y.setter
	def y(self, i: float) -> None:
		pass


class Vector3(Structure):
	"""Vector3, 3 components"""
	@property
	def x(self) -> float:
		pass

	@x.setter
	def x(self, i: float) -> None:
		pass

	@property
	def y(self) -> float:
		pass

	@y.setter
	def y(self, i: float) -> None:
		pass

	@property
	def z(self) -> float:
		pass

	@z.setter
	def z(self, i: float) -> None:
		pass


class Vector4(Structure):
	"""Vector4, 4 components"""
	@property
	def x(self) -> float:
		pass

	@x.setter
	def x(self, i: float) -> None:
		pass

	@property
	def y(self) -> float:
		pass

	@y.setter
	def y(self, i: float) -> None:
		pass

	@property
	def z(self) -> float:
		pass

	@z.setter
	def z(self, i: float) -> None:
		pass

	@property
	def w(self) -> float:
		pass

	@w.setter
	def w(self, i: float) -> None:
		pass


class Quaternion(Structure):
	"""Quaternion, 4 components (Vector4 alias)"""
	@property
	def x(self) -> float:
		pass

	@x.setter
	def x(self, i: float) -> None:
		pass

	@property
	def y(self) -> float:
		pass

	@y.setter
	def y(self, i: float) -> None:
		pass

	@property
	def z(self) -> float:
		pass

	@z.setter
	def z(self, i: float) -> None:
		pass

	@property
	def w(self) -> float:
		pass

	@w.setter
	def w(self, i: float) -> None:
		pass


class Matrix(Structure):
	"""Matrix, 4x4 components, column major, OpenGL style, right handed"""
	@property
	def m0(self) -> float:
		pass

	@m0.setter
	def m0(self, i: float) -> None:
		pass

	@property
	def m4(self) -> float:
		pass

	@m4.setter
	def m4(self, i: float) -> None:
		pass

	@property
	def m8(self) -> float:
		pass

	@m8.setter
	def m8(self, i: float) -> None:
		pass

	@property
	def m12(self) -> float:
		pass

	@m12.setter
	def m12(self, i: float) -> None:
		pass

	@property
	def m1(self) -> float:
		pass

	@m1.setter
	def m1(self, i: float) -> None:
		pass

	@property
	def m5(self) -> float:
		pass

	@m5.setter
	def m5(self, i: float) -> None:
		pass

	@property
	def m9(self) -> float:
		pass

	@m9.setter
	def m9(self, i: float) -> None:
		pass

	@property
	def m13(self) -> float:
		pass

	@m13.setter
	def m13(self, i: float) -> None:
		pass

	@property
	def m2(self) -> float:
		pass

	@m2.setter
	def m2(self, i: float) -> None:
		pass

	@property
	def m6(self) -> float:
		pass

	@m6.setter
	def m6(self, i: float) -> None:
		pass

	@property
	def m10(self) -> float:
		pass

	@m10.setter
	def m10(self, i: float) -> None:
		pass

	@property
	def m14(self) -> float:
		pass

	@m14.setter
	def m14(self, i: float) -> None:
		pass

	@property
	def m3(self) -> float:
		pass

	@m3.setter
	def m3(self, i: float) -> None:
		pass

	@property
	def m7(self) -> float:
		pass

	@m7.setter
	def m7(self, i: float) -> None:
		pass

	@property
	def m11(self) -> float:
		pass

	@m11.setter
	def m11(self, i: float) -> None:
		pass

	@property
	def m15(self) -> float:
		pass

	@m15.setter
	def m15(self, i: float) -> None:
		pass


class Color(Structure):
	"""Color, 4 components, R8G8B8A8 (32bit)"""
	@property
	def r(self) -> int:
		pass

	@r.setter
	def r(self, i: int) -> None:
		pass

	@property
	def g(self) -> int:
		pass

	@g.setter
	def g(self, i: int) -> None:
		pass

	@property
	def b(self) -> int:
		pass

	@b.setter
	def b(self, i: int) -> None:
		pass

	@property
	def a(self) -> int:
		pass

	@a.setter
	def a(self, i: int) -> None:
		pass


class Rectangle(Structure):
	"""Rectangle, 4 components"""
	@property
	def x(self) -> float:
		pass

	@x.setter
	def x(self, i: float) -> None:
		pass

	@property
	def y(self) -> float:
		pass

	@y.setter
	def y(self, i: float) -> None:
		pass

	@property
	def width(self) -> float:
		pass

	@width.setter
	def width(self, i: float) -> None:
		pass

	@property
	def height(self) -> float:
		pass

	@height.setter
	def height(self, i: float) -> None:
		pass


class Image(Structure):
	"""Image, pixel data stored in CPU memory (RAM)"""
	@property
	def data(self) -> int:
		pass

	@data.setter
	def data(self, i: int) -> None:
		pass

	@property
	def width(self) -> int:
		pass

	@width.setter
	def width(self, i: int) -> None:
		pass

	@property
	def height(self) -> int:
		pass

	@height.setter
	def height(self, i: int) -> None:
		pass

	@property
	def mipmaps(self) -> int:
		pass

	@mipmaps.setter
	def mipmaps(self, i: int) -> None:
		pass

	@property
	def format(self) -> int:
		pass

	@format.setter
	def format(self, i: int) -> None:
		pass


class Texture(Structure):
	"""Texture, tex data stored in GPU memory (VRAM)"""
	@property
	def id(self) -> int:
		pass

	@id.setter
	def id(self, i: int) -> None:
		pass

	@property
	def width(self) -> int:
		pass

	@width.setter
	def width(self, i: int) -> None:
		pass

	@property
	def height(self) -> int:
		pass

	@height.setter
	def height(self, i: int) -> None:
		pass

	@property
	def mipmaps(self) -> int:
		pass

	@mipmaps.setter
	def mipmaps(self, i: int) -> None:
		pass

	@property
	def format(self) -> int:
		pass

	@format.setter
	def format(self, i: int) -> None:
		pass


class Texture2D(Structure):
	"""Texture2D, same as Texture"""
	@property
	def id(self) -> int:
		pass

	@id.setter
	def id(self, i: int) -> None:
		pass

	@property
	def width(self) -> int:
		pass

	@width.setter
	def width(self, i: int) -> None:
		pass

	@property
	def height(self) -> int:
		pass

	@height.setter
	def height(self, i: int) -> None:
		pass

	@property
	def mipmaps(self) -> int:
		pass

	@mipmaps.setter
	def mipmaps(self, i: int) -> None:
		pass

	@property
	def format(self) -> int:
		pass

	@format.setter
	def format(self, i: int) -> None:
		pass


class TextureCubemap(Structure):
	"""TextureCubemap, same as Texture"""
	@property
	def id(self) -> int:
		pass

	@id.setter
	def id(self, i: int) -> None:
		pass

	@property
	def width(self) -> int:
		pass

	@width.setter
	def width(self, i: int) -> None:
		pass

	@property
	def height(self) -> int:
		pass

	@height.setter
	def height(self, i: int) -> None:
		pass

	@property
	def mipmaps(self) -> int:
		pass

	@mipmaps.setter
	def mipmaps(self, i: int) -> None:
		pass

	@property
	def format(self) -> int:
		pass

	@format.setter
	def format(self, i: int) -> None:
		pass


class RenderTexture(Structure):
	"""RenderTexture, fbo for texture rendering"""
	@property
	def id(self) -> int:
		pass

	@id.setter
	def id(self, i: int) -> None:
		pass

	@property
	def texture(self) -> Texture:
		pass

	@texture.setter
	def texture(self, i: Texture) -> None:
		pass

	@property
	def depth(self) -> Texture:
		pass

	@depth.setter
	def depth(self, i: Texture) -> None:
		pass


class RenderTexture2D(Structure):
	"""RenderTexture2D, same as RenderTexture"""
	@property
	def id(self) -> int:
		pass

	@id.setter
	def id(self, i: int) -> None:
		pass

	@property
	def texture(self) -> Texture:
		pass

	@texture.setter
	def texture(self, i: Texture) -> None:
		pass

	@property
	def depth(self) -> Texture:
		pass

	@depth.setter
	def depth(self, i: Texture) -> None:
		pass


class NPatchInfo(Structure):
	"""NPatchInfo, n-patch layout info"""
	@property
	def source(self) -> Rectangle:
		pass

	@source.setter
	def source(self, i: Rectangle) -> None:
		pass

	@property
	def left(self) -> int:
		pass

	@left.setter
	def left(self, i: int) -> None:
		pass

	@property
	def top(self) -> int:
		pass

	@top.setter
	def top(self, i: int) -> None:
		pass

	@property
	def right(self) -> int:
		pass

	@right.setter
	def right(self, i: int) -> None:
		pass

	@property
	def bottom(self) -> int:
		pass

	@bottom.setter
	def bottom(self, i: int) -> None:
		pass

	@property
	def layout(self) -> int:
		pass

	@layout.setter
	def layout(self, i: int) -> None:
		pass


class GlyphInfo(Structure):
	"""GlyphInfo, font characters glyphs info"""
	@property
	def value(self) -> int:
		pass

	@value.setter
	def value(self, i: int) -> None:
		pass

	@property
	def offsetX(self) -> int:
		pass

	@offsetX.setter
	def offsetX(self, i: int) -> None:
		pass

	@property
	def offsetY(self) -> int:
		pass

	@offsetY.setter
	def offsetY(self, i: int) -> None:
		pass

	@property
	def advanceX(self) -> int:
		pass

	@advanceX.setter
	def advanceX(self, i: int) -> None:
		pass

	@property
	def image(self) -> Image:
		pass

	@image.setter
	def image(self, i: Image) -> None:
		pass


class Font(Structure):
	"""Font, font texture and GlyphInfo array data"""
	@property
	def baseSize(self) -> int:
		pass

	@baseSize.setter
	def baseSize(self, i: int) -> None:
		pass

	@property
	def glyphCount(self) -> int:
		pass

	@glyphCount.setter
	def glyphCount(self, i: int) -> None:
		pass

	@property
	def glyphPadding(self) -> int:
		pass

	@glyphPadding.setter
	def glyphPadding(self, i: int) -> None:
		pass

	@property
	def texture(self) -> Texture2D:
		pass

	@texture.setter
	def texture(self, i: Texture2D) -> None:
		pass

	@property
	def recs(self) -> POINTER(Rectangle):
		pass

	@recs.setter
	def recs(self, i: POINTER(Rectangle)) -> None:
		pass

	@property
	def glyphs(self) -> POINTER(GlyphInfo):
		pass

	@glyphs.setter
	def glyphs(self, i: POINTER(GlyphInfo)) -> None:
		pass


class Camera3D(Structure):
	"""Camera, defines position/orientation in 3d space"""
	@property
	def position(self) -> Vector3:
		pass

	@position.setter
	def position(self, i: Vector3) -> None:
		pass

	@property
	def target(self) -> Vector3:
		pass

	@target.setter
	def target(self, i: Vector3) -> None:
		pass

	@property
	def up(self) -> Vector3:
		pass

	@up.setter
	def up(self, i: Vector3) -> None:
		pass

	@property
	def fovy(self) -> float:
		pass

	@fovy.setter
	def fovy(self, i: float) -> None:
		pass

	@property
	def projection(self) -> int:
		pass

	@projection.setter
	def projection(self, i: int) -> None:
		pass


class Camera(Structure):
	"""Camera type fallback, defaults to Camera3D"""
	@property
	def position(self) -> Vector3:
		pass

	@position.setter
	def position(self, i: Vector3) -> None:
		pass

	@property
	def target(self) -> Vector3:
		pass

	@target.setter
	def target(self, i: Vector3) -> None:
		pass

	@property
	def up(self) -> Vector3:
		pass

	@up.setter
	def up(self, i: Vector3) -> None:
		pass

	@property
	def fovy(self) -> float:
		pass

	@fovy.setter
	def fovy(self, i: float) -> None:
		pass

	@property
	def projection(self) -> int:
		pass

	@projection.setter
	def projection(self, i: int) -> None:
		pass


class Camera2D(Structure):
	"""Camera2D, defines position/orientation in 2d space"""
	@property
	def offset(self) -> Vector2:
		pass

	@offset.setter
	def offset(self, i: Vector2) -> None:
		pass

	@property
	def target(self) -> Vector2:
		pass

	@target.setter
	def target(self, i: Vector2) -> None:
		pass

	@property
	def rotation(self) -> float:
		pass

	@rotation.setter
	def rotation(self, i: float) -> None:
		pass

	@property
	def zoom(self) -> float:
		pass

	@zoom.setter
	def zoom(self, i: float) -> None:
		pass


class Mesh(Structure):
	"""Mesh, vertex data and vao/vbo"""
	@property
	def vertexCount(self) -> int:
		pass

	@vertexCount.setter
	def vertexCount(self, i: int) -> None:
		pass

	@property
	def triangleCount(self) -> int:
		pass

	@triangleCount.setter
	def triangleCount(self, i: int) -> None:
		pass

	@property
	def vertices(self) -> POINTER(c_float):
		pass

	@vertices.setter
	def vertices(self, i: POINTER(c_float)) -> None:
		pass

	@property
	def texcoords(self) -> POINTER(c_float):
		pass

	@texcoords.setter
	def texcoords(self, i: POINTER(c_float)) -> None:
		pass

	@property
	def texcoords2(self) -> POINTER(c_float):
		pass

	@texcoords2.setter
	def texcoords2(self, i: POINTER(c_float)) -> None:
		pass

	@property
	def normals(self) -> POINTER(c_float):
		pass

	@normals.setter
	def normals(self, i: POINTER(c_float)) -> None:
		pass

	@property
	def tangents(self) -> POINTER(c_float):
		pass

	@tangents.setter
	def tangents(self, i: POINTER(c_float)) -> None:
		pass

	@property
	def colors(self) -> POINTER(c_ubyte):
		pass

	@colors.setter
	def colors(self, i: POINTER(c_ubyte)) -> None:
		pass

	@property
	def indices(self) -> POINTER(c_ushort):
		pass

	@indices.setter
	def indices(self, i: POINTER(c_ushort)) -> None:
		pass

	@property
	def animVertices(self) -> POINTER(c_float):
		pass

	@animVertices.setter
	def animVertices(self, i: POINTER(c_float)) -> None:
		pass

	@property
	def animNormals(self) -> POINTER(c_float):
		pass

	@animNormals.setter
	def animNormals(self, i: POINTER(c_float)) -> None:
		pass

	@property
	def boneIds(self) -> POINTER(c_ubyte):
		pass

	@boneIds.setter
	def boneIds(self, i: POINTER(c_ubyte)) -> None:
		pass

	@property
	def boneWeights(self) -> POINTER(c_float):
		pass

	@boneWeights.setter
	def boneWeights(self, i: POINTER(c_float)) -> None:
		pass

	@property
	def vaoId(self) -> int:
		pass

	@vaoId.setter
	def vaoId(self, i: int) -> None:
		pass

	@property
	def vboId(self) -> POINTER(c_uint):
		pass

	@vboId.setter
	def vboId(self, i: POINTER(c_uint)) -> None:
		pass


class Shader(Structure):
	"""Shader"""
	@property
	def id(self) -> int:
		pass

	@id.setter
	def id(self, i: int) -> None:
		pass

	@property
	def locs(self) -> POINTER(c_int):
		pass

	@locs.setter
	def locs(self, i: POINTER(c_int)) -> None:
		pass


class MaterialMap(Structure):
	"""MaterialMap"""
	@property
	def texture(self) -> Texture2D:
		pass

	@texture.setter
	def texture(self, i: Texture2D) -> None:
		pass

	@property
	def color(self) -> Color:
		pass

	@color.setter
	def color(self, i: Color) -> None:
		pass

	@property
	def value(self) -> float:
		pass

	@value.setter
	def value(self, i: float) -> None:
		pass


class Material(Structure):
	"""Material, includes shader and maps"""
	@property
	def shader(self) -> Shader:
		pass

	@shader.setter
	def shader(self, i: Shader) -> None:
		pass

	@property
	def maps(self) -> POINTER(MaterialMap):
		pass

	@maps.setter
	def maps(self, i: POINTER(MaterialMap)) -> None:
		pass

	@property
	def params(self) -> c_float * 4:
		pass

	@params.setter
	def params(self, i: c_float * 4) -> None:
		pass


class Transform(Structure):
	"""Transform, vectex transformation data"""
	@property
	def translation(self) -> Vector3:
		pass

	@translation.setter
	def translation(self, i: Vector3) -> None:
		pass

	@property
	def rotation(self) -> Quaternion:
		pass

	@rotation.setter
	def rotation(self, i: Quaternion) -> None:
		pass

	@property
	def scale(self) -> Vector3:
		pass

	@scale.setter
	def scale(self, i: Vector3) -> None:
		pass


class BoneInfo(Structure):
	"""Bone, skeletal animation bone"""
	@property
	def name(self) -> c_char * 32:
		pass

	@name.setter
	def name(self, i: c_char * 32) -> None:
		pass

	@property
	def parent(self) -> int:
		pass

	@parent.setter
	def parent(self, i: int) -> None:
		pass


class Model(Structure):
	"""Model, meshes, materials and animation data"""
	@property
	def transform(self) -> Matrix:
		pass

	@transform.setter
	def transform(self, i: Matrix) -> None:
		pass

	@property
	def meshCount(self) -> int:
		pass

	@meshCount.setter
	def meshCount(self, i: int) -> None:
		pass

	@property
	def materialCount(self) -> int:
		pass

	@materialCount.setter
	def materialCount(self, i: int) -> None:
		pass

	@property
	def meshes(self) -> POINTER(Mesh):
		pass

	@meshes.setter
	def meshes(self, i: POINTER(Mesh)) -> None:
		pass

	@property
	def materials(self) -> POINTER(Material):
		pass

	@materials.setter
	def materials(self, i: POINTER(Material)) -> None:
		pass

	@property
	def meshMaterial(self) -> POINTER(c_int):
		pass

	@meshMaterial.setter
	def meshMaterial(self, i: POINTER(c_int)) -> None:
		pass

	@property
	def boneCount(self) -> int:
		pass

	@boneCount.setter
	def boneCount(self, i: int) -> None:
		pass

	@property
	def bones(self) -> POINTER(BoneInfo):
		pass

	@bones.setter
	def bones(self, i: POINTER(BoneInfo)) -> None:
		pass

	@property
	def bindPose(self) -> POINTER(Transform):
		pass

	@bindPose.setter
	def bindPose(self, i: POINTER(Transform)) -> None:
		pass


class ModelAnimation(Structure):
	"""ModelAnimation"""
	@property
	def boneCount(self) -> int:
		pass

	@boneCount.setter
	def boneCount(self, i: int) -> None:
		pass

	@property
	def frameCount(self) -> int:
		pass

	@frameCount.setter
	def frameCount(self, i: int) -> None:
		pass

	@property
	def bones(self) -> POINTER(BoneInfo):
		pass

	@bones.setter
	def bones(self, i: POINTER(BoneInfo)) -> None:
		pass

	@property
	def framePoses(self) -> POINTER(POINTER(Transform)):
		pass

	@framePoses.setter
	def framePoses(self, i: POINTER(POINTER(Transform))) -> None:
		pass


class Ray(Structure):
	"""Ray, ray for raycasting"""
	@property
	def position(self) -> Vector3:
		pass

	@position.setter
	def position(self, i: Vector3) -> None:
		pass

	@property
	def direction(self) -> Vector3:
		pass

	@direction.setter
	def direction(self, i: Vector3) -> None:
		pass


class RayCollision(Structure):
	"""RayCollision, ray hit information"""
	@property
	def hit(self) -> bool:
		pass

	@hit.setter
	def hit(self, i: bool) -> None:
		pass

	@property
	def distance(self) -> float:
		pass

	@distance.setter
	def distance(self, i: float) -> None:
		pass

	@property
	def point(self) -> Vector3:
		pass

	@point.setter
	def point(self, i: Vector3) -> None:
		pass

	@property
	def normal(self) -> Vector3:
		pass

	@normal.setter
	def normal(self, i: Vector3) -> None:
		pass


class BoundingBox(Structure):
	"""BoundingBox"""
	@property
	def min(self) -> Vector3:
		pass

	@min.setter
	def min(self, i: Vector3) -> None:
		pass

	@property
	def max(self) -> Vector3:
		pass

	@max.setter
	def max(self, i: Vector3) -> None:
		pass


class VrDeviceInfo(Structure):
	"""VrDeviceInfo, Head-Mounted-Display device parameters"""
	@property
	def hResolution(self) -> int:
		pass

	@hResolution.setter
	def hResolution(self, i: int) -> None:
		pass

	@property
	def vResolution(self) -> int:
		pass

	@vResolution.setter
	def vResolution(self, i: int) -> None:
		pass

	@property
	def hScreenSize(self) -> float:
		pass

	@hScreenSize.setter
	def hScreenSize(self, i: float) -> None:
		pass

	@property
	def vScreenSize(self) -> float:
		pass

	@vScreenSize.setter
	def vScreenSize(self, i: float) -> None:
		pass

	@property
	def vScreenCenter(self) -> float:
		pass

	@vScreenCenter.setter
	def vScreenCenter(self, i: float) -> None:
		pass

	@property
	def eyeToScreenDistance(self) -> float:
		pass

	@eyeToScreenDistance.setter
	def eyeToScreenDistance(self, i: float) -> None:
		pass

	@property
	def lensSeparationDistance(self) -> float:
		pass

	@lensSeparationDistance.setter
	def lensSeparationDistance(self, i: float) -> None:
		pass

	@property
	def interpupillaryDistance(self) -> float:
		pass

	@interpupillaryDistance.setter
	def interpupillaryDistance(self, i: float) -> None:
		pass

	@property
	def lensDistortionValues(self) -> c_float * 4:
		pass

	@lensDistortionValues.setter
	def lensDistortionValues(self, i: c_float * 4) -> None:
		pass

	@property
	def chromaAbCorrection(self) -> c_float * 4:
		pass

	@chromaAbCorrection.setter
	def chromaAbCorrection(self, i: c_float * 4) -> None:
		pass


class VrStereoConfig(Structure):
	"""VrStereoConfig, VR stereo rendering configuration for simulator"""
	@property
	def projection(self) -> Matrix * 2:
		pass

	@projection.setter
	def projection(self, i: Matrix * 2) -> None:
		pass

	@property
	def viewOffset(self) -> Matrix * 2:
		pass

	@viewOffset.setter
	def viewOffset(self, i: Matrix * 2) -> None:
		pass

	@property
	def leftLensCenter(self) -> c_float * 2:
		pass

	@leftLensCenter.setter
	def leftLensCenter(self, i: c_float * 2) -> None:
		pass

	@property
	def rightLensCenter(self) -> c_float * 2:
		pass

	@rightLensCenter.setter
	def rightLensCenter(self, i: c_float * 2) -> None:
		pass

	@property
	def leftScreenCenter(self) -> c_float * 2:
		pass

	@leftScreenCenter.setter
	def leftScreenCenter(self, i: c_float * 2) -> None:
		pass

	@property
	def rightScreenCenter(self) -> c_float * 2:
		pass

	@rightScreenCenter.setter
	def rightScreenCenter(self, i: c_float * 2) -> None:
		pass

	@property
	def scale(self) -> c_float * 2:
		pass

	@scale.setter
	def scale(self, i: c_float * 2) -> None:
		pass

	@property
	def scaleIn(self) -> c_float * 2:
		pass

	@scaleIn.setter
	def scaleIn(self, i: c_float * 2) -> None:
		pass


class FilePathList(Structure):
	"""File path list"""
	@property
	def capacity(self) -> int:
		pass

	@capacity.setter
	def capacity(self, i: int) -> None:
		pass

	@property
	def count(self) -> int:
		pass

	@count.setter
	def count(self, i: int) -> None:
		pass

	@property
	def paths(self) -> POINTER(POINTER(c_char)):
		pass

	@paths.setter
	def paths(self, i: POINTER(POINTER(c_char))) -> None:
		pass


class float3(Structure):
	"""NOTE: Helper types to be used instead of array return types for *ToFloat functions"""
	@property
	def v(self) -> c_float * 3:
		pass

	@v.setter
	def v(self, i: c_float * 3) -> None:
		pass


class float16(Structure):
	""""""
	@property
	def v(self) -> c_float * 16:
		pass

	@v.setter
	def v(self, i: c_float * 16) -> None:
		pass


