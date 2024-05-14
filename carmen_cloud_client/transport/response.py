# generated by datamodel-codegen:
#   filename:  response.schema.json
#   timestamp: 2024-05-10T13:30:44+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, conint


class BgColor(BaseModel):
    b: Optional[conint(ge=0, le=255)] = Field(
        None, description='The blue component of the color, 0-255.', title='Blue'
    )
    g: Optional[conint(ge=0, le=255)] = Field(
        None, description='The green component of the color, 0-255.', title='Green'
    )
    r: Optional[conint(ge=0, le=255)] = Field(
        None, description='The red component of the color, 0-255.', title='Red'
    )


class Color(BaseModel):
    b: Optional[conint(ge=0, le=255)] = Field(
        None, description='The blue component of the color, 0-255.', title='Blue'
    )
    g: Optional[conint(ge=0, le=255)] = Field(
        None, description='The green component of the color, 0-255.', title='Green'
    )
    r: Optional[conint(ge=0, le=255)] = Field(
        None, description='The red component of the color, 0-255.', title='Red'
    )


class BottomLeft(BaseModel):
    x: Optional[int] = Field(
        None, description='The X coordinate of the corner.', title='X coordinate'
    )
    y: Optional[int] = Field(
        None, description='The Y coordinate of the corner.', title='Y coordinate'
    )


class BottomRight(BaseModel):
    x: Optional[int] = Field(
        None, description='The X coordinate of the corner.', title='X coordinate'
    )
    y: Optional[int] = Field(
        None, description='The Y coordinate of the corner.', title='Y coordinate'
    )


class TopLeft(BaseModel):
    x: Optional[int] = Field(
        None, description='The X coordinate of the corner.', title='X coordinate'
    )
    y: Optional[int] = Field(
        None, description='The Y coordinate of the corner.', title='Y coordinate'
    )


class TopRight(BaseModel):
    x: Optional[int] = Field(
        None, description='The X coordinate of the corner.', title='X coordinate'
    )
    y: Optional[int] = Field(
        None, description='The Y coordinate of the corner.', title='Y coordinate'
    )


class CharROI(BaseModel):
    bottomLeft: Optional[BottomLeft] = Field(
        None,
        description='Coordinates of the bottom left corner of the region in the uploaded image.',
        title='Bottom Left',
    )
    bottomRight: Optional[BottomRight] = Field(
        None,
        description='Coordinates of the bottom right corner of the region in the uploaded image.',
        title='Bottom Right',
    )
    topLeft: Optional[TopLeft] = Field(
        None,
        description='Coordinates of the top left corner of the region in the uploaded image.',
        title='Top Left',
    )
    topRight: Optional[TopRight] = Field(
        None,
        description='Coordinates of the top right corner of the region in the uploaded image.',
        title='Top Right',
    )


class Character(BaseModel):
    code: Optional[int] = Field(
        None, description='The numeric code of the character.', title='Code'
    )
    bgDark: Optional[bool] = Field(
        None,
        description='A boolean indicating whether the background is darker than the character found.',
        title='Dark Background',
    )
    bgColor: Optional[BgColor] = Field(
        None,
        description='The color of the background of the character.',
        title='Background Color',
    )
    color: Optional[Color] = Field(
        None, description='The color of the character.', title='Text Color'
    )
    confidence: Optional[int] = Field(
        None,
        description='The estimated probability of the recognized character being correct as a percentage between 0 and 100.',
        title='Confidence',
    )
    charROI: Optional[CharROI] = Field(
        None,
        description='The quadrangle (not necessarily a rectangle) where the character has been found.',
        title='Character Region of Interest',
    )


class ImageResult(BaseModel):
    found: Optional[bool] = Field(
        None,
        description='A boolean indicating whether a code has been found on the image.',
        title='Found',
    )
    text: Optional[str] = Field(
        None, description='The code found on the image as a string.', title='Text'
    )
    confidence: Optional[int] = Field(
        None,
        description='The estimated probability of the recognized code being correct as a percentage between 0 and 100.',
        title='Confidence',
    )
    characters: Optional[List[Character]] = Field(
        None,
        description='An array of objects which describe each character of the recognized code.',
        title='Characters',
    )


class Code(BaseModel):
    code: Optional[str] = Field(None, description='The code as a string.', title='Code')
    confidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='The estimated probability of the recognized code being correct as a percentage between 0 and 100.',
        title='Confidence',
    )
    imageResults: Optional[List[ImageResult]] = Field(
        None,
        description='An array in which each item corresponds to one image uploaded. The items are objects that describe the recognition results found on their respective input images.',
        title='Image Results',
    )


class Data(BaseModel):
    codes: Optional[List[Code]] = Field(
        None,
        description='An array containing all codes recognized on the images uploaded.',
        title='Codes',
    )


class TransportationCargoApiResponse(BaseModel):
    nodename: Optional[str] = Field(
        None,
        description='Name of the worker node that generated the response.',
        title='Node Name',
    )
    nodetime: Optional[float] = Field(
        None,
        description='The time, in milliseconds, it took to generate the response.',
        title='Node Time',
    )
    version: Optional[str] = Field(
        None,
        description='The version of the API that returned the response.',
        title='API version',
    )
    data: Optional[Data] = Field(
        None,
        description='An object containing the results of the OCR operation.',
        title='Image Recognition Result',
    )
