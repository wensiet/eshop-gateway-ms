from pydantic import BaseModel
from typing import Type


def make_model(proto_message) -> Type[BaseModel]:
    fields = {}

    descriptor = proto_message.DESCRIPTOR
    for field in descriptor.fields:
        field_name = field.name
        field_type = None

        if field.cpp_type == 1:  # CPPTYPE_INT32
            field_type = int
        elif field.cpp_type == 3:  # CPPTYPE_UINT32
            field_type = int
        elif field.cpp_type == 2:  # CPPTYPE_INT64
            field_type = int
        elif field.cpp_type == 4:  # CPPTYPE_UINT64
            field_type = int
        elif field.cpp_type == 5:  # CPPTYPE_DOUBLE
            field_type = float
        elif field.cpp_type == 6:  # CPPTYPE_FLOAT
            field_type = float
        elif field.cpp_type == 9:  # CPPTYPE_STRING
            field_type = str
        elif field.cpp_type == 11:  # CPPTYPE_BOOL
            field_type = bool

        if field_type is not None:
            fields[field_name] = field_type
        else:
            fields[field_name] = None

        # Create a Pydantic model dynamically
        pydantic_model = type(
            f"{proto_message.__name__}Pydantic",
            (BaseModel,),
            {'__annotations__': fields, '__module__': __name__}
        )
    return pydantic_model


def convert_to_proto(proto_message, pydantic_instance: BaseModel):
    proto_instance = proto_message()

    for field_name, value in pydantic_instance.dict().items():
        if value is not None:
            setattr(proto_instance, field_name, value)

    return proto_instance


def convert_from_proto(proto_instance, pydantic_model=None) -> BaseModel:
    if pydantic_model is None:
        pydantic_model = make_model(type(proto_instance))
    pydantic_instance_data = {}

    for field in proto_instance.DESCRIPTOR.fields:
        field_name = field.name
        field_value = getattr(proto_instance, field_name)
        pydantic_instance_data[field_name] = field_value

    return pydantic_model(**pydantic_instance_data)
