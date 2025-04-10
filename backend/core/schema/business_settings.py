from pydantic import BaseModel


class BusinessSettingsSchema(BaseModel):
    name: str
    value: str


class BusinessSettingsCreateSchema(BusinessSettingsSchema):
    ...


class BusinessSettingsUpdateSchema(BusinessSettingsSchema):
    ...


class BusinessSettingsReadSchema(BusinessSettingsSchema):
    ...
