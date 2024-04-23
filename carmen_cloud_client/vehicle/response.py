# generated by datamodel-codegen:
#   filename:  response.schema.json
#   timestamp: 2024-04-23T13:27:50+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, conint


class BottomLeft(BaseModel):
    x: Optional[int] = Field(None, description='x coordinate')
    y: Optional[int] = Field(None, description='y coordinate')


class BottomRight(BaseModel):
    x: Optional[int] = Field(None, description='x coordinate')
    y: Optional[int] = Field(None, description='y coordinate')


class TopLeft(BaseModel):
    x: Optional[int] = Field(None, description='x coordinate')
    y: Optional[int] = Field(None, description='y coordinate')


class TopRight(BaseModel):
    x: Optional[int] = Field(None, description='x coordinate')
    y: Optional[int] = Field(None, description='y coordinate')


class ExtendedPlateFrame(BaseModel):
    bottomLeft: Optional[BottomLeft] = Field(
        None, description='The bottom left corner of the rectangle.'
    )
    bottomRight: Optional[BottomRight] = Field(
        None, description='The bottom right corner of the rectangle.'
    )
    topLeft: Optional[TopLeft] = Field(
        None, description='The top left corner of the rectangle.'
    )
    topRight: Optional[TopRight] = Field(
        None, description='The top right corner of the rectangle.'
    )


class VehicleFrame(BaseModel):
    bottomLeft: Optional[BottomLeft] = Field(
        None, description='The bottom left corner of the rectangle.'
    )
    bottomRight: Optional[BottomRight] = Field(
        None, description='The bottom right corner of the rectangle.'
    )
    topLeft: Optional[TopLeft] = Field(
        None, description='The top left corner of the rectangle.'
    )
    topRight: Optional[TopRight] = Field(
        None, description='The top right corner of the rectangle.'
    )


class Bounds(BaseModel):
    extendedPlateFrame: Optional[ExtendedPlateFrame] = Field(
        None,
        description='The coordinates of the license plate extension, on the basis of which the vehicle type can be determined.',
    )
    vehicleFrame: Optional[VehicleFrame] = Field(
        None,
        description='The coordinates of the vehicle if provided by the MMR engine.',
    )


class Color(BaseModel):
    b: Optional[conint(ge=0, le=255)] = Field(
        None, description='the blue component of the color'
    )
    g: Optional[conint(ge=0, le=255)] = Field(
        None, description='the green component of the color'
    )
    r: Optional[conint(ge=0, le=255)] = Field(
        None, description='the red component of the color'
    )


class Mmr(BaseModel):
    found: Optional[bool] = Field(
        None,
        description='True if an MMR engine found mmr information in the image, otherwise false. (*Available since version 1.2.*)',
    )
    engine: Optional[str] = Field(
        None,
        description='The name of the MMR engine that successfully processed this vehicle. (*Available since version 1.3.*)',
    )
    category: Optional[str] = Field(None, description='The vehicle’s category.')
    categoryConfidence: Optional[conint(ge=0, le=100)] = Field(
        None, description='The confidence level of the vehicle category recognition.'
    )
    heading: Optional[str] = Field(
        None,
        description='**DEPRECATED:** The vehicle’s view (frontal or rear). (*Available since version 1.2.*)',
    )
    headingConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='**DEPRECATED:** The confidence level of the view recognition. (*Available since version 1.2.*)',
    )
    color: Optional[Color] = Field(None, description='The vehicle’s color.')
    colorConfidence: Optional[conint(ge=0, le=100)] = Field(
        None, description='The confidence level of the vehicle color recognition.'
    )
    colorName: Optional[str] = Field(
        None,
        description="The vehicle’s color as a string. The value is 'GRAYSCALE' for grayscale input images.",
    )
    make: Optional[str] = Field(None, description='The make/brand of the vehicle.')
    makeConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='The confidence level of  vehicle make recognition. (*Available since version 1.2.*)',
    )
    model: Optional[str] = Field(None, description='The model type of a vehicle.')
    modelConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='The confidence level of the vehicle model recognition. (*Available since version 1.2.*)',
    )
    field_makeAndModelConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        alias='*makeAndModelConfidence',
        description='The confidence level of the vehicle make and model recognition. (*Removed since version 1.2.*)',
    )
    field_submodel: Optional[str] = Field(
        None,
        alias='*submodel',
        description='The submodel type of a vehicle. (*Removed since version 1.2.*)',
    )
    proctime: Optional[int] = Field(
        None, description='The running time of the engine in milliseconds.'
    )
    bodyType: Optional[str] = Field(
        None,
        description="The body type of the vehicle. E.g. 'sedan', 'SUV', 'hatchback', etc. (*Available since version 1.4.*)",
    )
    bodyTypeConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='The confidence level of the body type recognition. (*Available since version 1.4.*)',
    )
    viewPoint: Optional[str] = Field(
        None,
        description='The orientation of the vehicle in the image. Available values: `rear`, `front`, `rear_side`, `front_side`, `side`. (*Available since version 1.4.*)',
    )
    viewPointConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='The confidence level of the view point recognition. (*Available since version 1.4.*)',
    )
    imageTooltips: Optional[List[str]] = Field(
        None,
        description='A list of hints that help improve recognition accuracy. (*Available since version 1.4.*)',
    )
    frameTooltips: Optional[List[str]] = Field(
        None,
        description='A list of hints that help improve recognition accuracy. (*Available since version 1.4.*)',
    )


class BgColor(BaseModel):
    b: Optional[conint(ge=0, le=255)] = Field(
        None, description='the blue component of the color'
    )
    g: Optional[conint(ge=0, le=255)] = Field(
        None, description='the green component of the color'
    )
    r: Optional[conint(ge=0, le=255)] = Field(
        None, description='the red component of the color'
    )


class DaColor(BaseModel):
    b: Optional[conint(ge=0, le=255)] = Field(
        None, description='the blue component of the color'
    )
    g: Optional[conint(ge=0, le=255)] = Field(
        None, description='the green component of the color'
    )
    r: Optional[conint(ge=0, le=255)] = Field(
        None, description='the red component of the color'
    )


class PlateROI(BaseModel):
    bottomLeft: Optional[BottomLeft] = Field(
        None, description='The bottom left corner of the rectangle.'
    )
    bottomRight: Optional[BottomRight] = Field(
        None, description='The bottom right corner of the rectangle.'
    )
    topLeft: Optional[TopLeft] = Field(
        None, description='The top left corner of the rectangle.'
    )
    topRight: Optional[TopRight] = Field(
        None, description='The top right corner of the rectangle.'
    )


class CharROI(BaseModel):
    bottomLeft: Optional[BottomLeft] = Field(
        None, description='The bottom left corner of the rectangle.'
    )
    bottomRight: Optional[BottomRight] = Field(
        None, description='The bottom right corner of the rectangle.'
    )
    topLeft: Optional[TopLeft] = Field(
        None, description='The top left corner of the rectangle.'
    )
    topRight: Optional[TopRight] = Field(
        None, description='The top right corner of the rectangle.'
    )


class PlateChar(BaseModel):
    code: Optional[int] = Field(None, description='The numeric code of the character.')
    bgDark: Optional[bool] = Field(
        None,
        description='Indicates whether the character has a dark background color. Only returned if the engine does not support color analysis. (*Available since version 1.4.*)',
    )
    bgColor: Optional[BgColor] = Field(
        None, description='The background color of the character.'
    )
    color: Optional[Color] = Field(None, description='The color of the character.')
    confidence: Optional[conint(ge=0, le=100)] = Field(
        None, description="The engine's confidence for the character."
    )
    charROI: Optional[CharROI] = Field(
        None, description='The coordinates of the given character.'
    )


class Plate(BaseModel):
    found: Optional[bool] = Field(
        None,
        description='True if an ANPR engine found plate information in the image, otherwise false. (*Available since version 1.2.*)',
    )
    engine: Optional[str] = Field(
        None,
        description='The name of the ANPR engine that successfully processed this vehicle. (*Available since version 1.3.*)',
    )
    bgDark: Optional[bool] = Field(
        None,
        description='Indicates whether the license plate has a dark background color. Only returned if the engine does not support color analysis. (*Available since version 1.4.*)',
    )
    bgColor: Optional[BgColor] = Field(
        None,
        description='The color of the license plate background if provided by the ANPR engine, can be white or black. This also means that the engine does not give yellow to taxis and green to electric cars, but white. The color is specified by an RGB (red-green-blue) code which properties (r, g, and b respectively) are integer numbers between 0 and 255.',
    )
    daColor: Optional[DaColor] = Field(
        None,
        description='The dedicated area color if provided by the ANPR engine. (*Available since version 1.2.*)',
    )
    color: Optional[Color] = Field(
        None,
        description='The color of the license plate foreground if provided by the ANPR engine.',
    )
    plateHeight: Optional[float] = Field(
        None,
        description='The estimated height (in millimeters) of the license plate. (*Available since version 1.4.*)',
    )
    plateWidth: Optional[float] = Field(
        None,
        description='The estimated width (in millimeters) of the license plate. (*Available since version 1.4.*)',
    )
    confidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='Overall confidence of the license plate calculated from plate type, position, and character confidence values (plateTypeConfidence * positionConfidence * average of characterConfidences). If you need more fine-grained confidence data, use the other plate or character-level confidence properties.',
    )
    textConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='Confidence of license plate text recognition. (*Available since version 1.4.*)',
    )
    normalizedConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='Combined confidence of licese plate text, country, and state recognition. (*Available since version 1.4.*)',
    )
    plateTypeConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='Confidence of the license plate type. (*Available since version 1.1.*)',
    )
    positionConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='Confidence of the license plate position. (*Available since version 1.1.*)',
    )
    proctime: Optional[int] = Field(
        None, description='The running time of the engine in milliseconds.'
    )
    category: Optional[str] = Field(
        None,
        description='The category of the license plate. (*Available since version 1.1.*) For the list of possible values please refer to the [Carmen ANPR Reference Manual](https://adaptiverecognition.com/app/uploads/DOC/Software/Carmen/ANPR/carmen_anpr_reference_manual.pdf)',
    )
    country: Optional[str] = Field(
        None,
        description='The nationality of the license plate. For a list of possible values please refer to [this table](/docs/content/references/countries).',
    )
    state: Optional[str] = Field(
        None,
        description='Where it makes sense, the code of the state, county or region.',
    )
    plateType: Optional[int] = Field(
        None,
        description='The Adaptive Recognition type code of the table. For a list of possible values please refer to the [Carmen ANPR Reference Manual](https://adaptiverecognition.com/app/uploads/DOC/Software/Carmen/ANPR/carmen_anpr_reference_manual.pdf).',
    )
    plateSizeSource: Optional[str] = Field(
        None,
        description='If present, indicates whether the plate size has been determined based on the plate type (`database`) or using a statistical estimation (`statistical`). If a plate size has not been returned, this property is missing.',
    )
    separatedText: Optional[str] = Field(
        None,
        description='The recognized text of the license plate with gap symbols as it is visible on the plate (<b>*</b> for crest, **¶** for new row, **space** for space, **|** for vertical line, **-** for hyphen, and **(** **)** for begin end symbol of small characters. *Available since version 1.3.*)',
    )
    unicodeText: Optional[str] = Field(
        None, description='The recognized text of the license plate.'
    )
    plateROI: Optional[PlateROI] = Field(
        None, description='The coordinates of the license plate found.'
    )
    plateChars: Optional[List[PlateChar]] = Field(
        None, description='An array of read characters, including character structures.'
    )


class PlateROI1(BaseModel):
    bottomLeft: Optional[BottomLeft] = Field(
        None, description='The bottom left corner of the rectangle.'
    )
    bottomRight: Optional[BottomRight] = Field(
        None, description='The bottom right corner of the rectangle.'
    )
    topLeft: Optional[TopLeft] = Field(
        None, description='The top left corner of the rectangle.'
    )
    topRight: Optional[TopRight] = Field(
        None, description='The top right corner of the rectangle.'
    )


class CharROI1(BaseModel):
    bottomLeft: Optional[BottomLeft] = Field(
        None, description='The bottom left corner of the rectangle.'
    )
    bottomRight: Optional[BottomRight] = Field(
        None, description='The bottom right corner of the rectangle.'
    )
    topLeft: Optional[TopLeft] = Field(
        None, description='The top left corner of the rectangle.'
    )
    topRight: Optional[TopRight] = Field(
        None, description='The top right corner of the rectangle.'
    )


class PlateChar1(BaseModel):
    code: Optional[int] = Field(None, description='The numeric code of the character.')
    bgColor: Optional[BgColor] = Field(
        None, description='The background color of the character.'
    )
    color: Optional[Color] = Field(None, description='The color of the character.')
    confidence: Optional[conint(ge=0, le=100)] = Field(
        None, description="The engine's confidence for the character."
    )
    charROI: Optional[CharROI1] = Field(
        None, description='The coordinates of the given character.'
    )


class Marking(BaseModel):
    engine: Optional[str] = Field(
        None,
        description='The name of the ANPR engine that successfully processed this marking.',
    )
    confidence: Optional[conint(ge=0, le=100)] = Field(
        None, description='Overall confidence of the plate.'
    )
    plateTypeConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='Confidence of the plate type. (*Not provided for eADR and A plates*)',
    )
    positionConfidence: Optional[conint(ge=0, le=100)] = Field(
        None,
        description='Confidence of the plate position. (*Not provided for eADR and A plates*)',
    )
    proctime: Optional[int] = Field(
        None, description='The running time of the engine in milliseconds.'
    )
    plateType: Optional[int] = Field(
        None,
        description='The Adaptive Recognition type code of the table. For a list of possible values please refer to the [Carmen ANPR Reference Manual](https://adaptiverecognition.com/app/uploads/DOC/Software/Carmen/ANPR/carmen_anpr_reference_manual.pdf).',
    )
    type: Optional[str] = Field(
        None,
        description='The type of the table. **ADR** for ADR plates, **E** for empty ADR plates, **AP** for A plates, and **IMO** for IMO plates',
    )
    unicodeText: Optional[str] = Field(
        None,
        description='The recognized text of the ADR plate or a textual representation of the IMO plate.',
    )
    plateROI: Optional[PlateROI1] = Field(
        None, description='The coordinates of the plate found.'
    )
    plateChars: Optional[List[PlateChar1]] = Field(
        None,
        description='An array of read characters, including character structures. (*Not provided for IMO, eADR and A plates*)',
    )


class Vehicle(BaseModel):
    bounds: Optional[Bounds] = Field(
        None, description='The bounds of the vehicle. (*Available since version 1.3.*)'
    )
    mmr: Optional[Mmr] = Field(
        None, description='The make, model and color of the vehicle.'
    )
    plate: Optional[Plate] = Field(None, description='The recognized license plate.')
    markings: Optional[List[Marking]] = Field(
        None,
        description='The markings found on the vehicle. (*Available since version 1.3.*)',
    )


class Data(BaseModel):
    vehicles: Optional[List[Vehicle]] = Field(
        None,
        description='The recognition results returned by each recognition service specified for the vehicles detected in the image (**plate** for *anpr*, **mmr** for *mmr*, and **markings** for *adr* service).',
    )


class VehicleApiResponse(BaseModel):
    field_engines: Optional[List[str]] = Field(
        None,
        alias='*engines',
        description='Includes the names of the recognition engines that successfully processed the request. (*Removed since version 1.3.*)',
    )
    nodename: Optional[str] = Field(
        None,
        description='The name of the node this request has been processed by. This is diagnostic information to be included in error reports.',
    )
    nodetime: Optional[float] = Field(
        None,
        description='Total processing time spent on the worker node (includes processing, image loading and latency). (*Available since version 1.4.*)',
    )
    startuptime: Optional[float] = Field(
        None,
        description='Startup time of the node processing the request. This can be greater in case of a cold start. (*Available since version 1.4.*)',
    )
    recognitiontime: Optional[float] = Field(
        None,
        description='Net processing time spent on recognizing the already loaded image. Use this number if you want to make an objective comparison between the difficulty of different images. (*Available since version 1.4*)',
    )
    version: Optional[str] = Field(
        None,
        description='The version of the API that returned the response. Incremented each time the response structure changes.',
    )
    data: Optional[Data] = Field(None, description='The recognition results.')
